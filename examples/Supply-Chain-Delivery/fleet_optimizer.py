import numpy as np
import pandas as pd
import argparse
import logging
from dual_perspective_delivery import DataHandler, StirlingOptimizer, RouteSolver

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("fleet_optimizer")

class GeneralizedFleetOptimizer:
    """
    Advanced fleet optimizer using generalized Stirling numbers with dynamic 
    affinity and barrier parameters based on payload and vehicle characteristics.
    """
    
    def __init__(self, delivery_data_path: str, fleet_data_path: str, base_params: tuple = (1.0, 1.0)):
        """
        Initialize the fleet optimizer.
        
        Args:
            delivery_data_path: Path to the delivery data CSV.
            fleet_data_path: Path to the fleet composition CSV.
            base_params: Tuple of (a, b) base parameters for the Stirling numbers.
        """
        self.base_a, self.base_b = base_params
        
        # Load data
        self.data_handler = DataHandler()
        self.delivery_data = self.data_handler.load_data(delivery_data_path)
        self.fleet_data = self._load_fleet_data(fleet_data_path)
        
        if self.delivery_data is None or self.fleet_data is None:
            raise ValueError("Failed to load delivery or fleet data.")
            
        self.route_solver = RouteSolver(self.delivery_data)
        self._compute_payload_complexity()
        
    def _load_fleet_data(self, path: str) -> pd.DataFrame:
        """Load and validate enhanced fleet data from CSV."""
        try:
            df = pd.read_csv(path)
            required = ['id', 'type', 'capacity', 'age', 'maintenance_cost', 'fuel_efficiency']
            optional = ['handling_rate', 'specialized_equipment', 'driver_skill_level', 'base_cost_per_km']
            
            missing = [col for col in required if col not in df.columns]
            if missing:
                raise ValueError(f"Fleet data missing required columns: {missing}")
                
            # Add default values for optional columns
            for col in optional:
                if col not in df.columns:
                    if col == 'handling_rate':
                        df[col] = 1.0  # Standard handling rate
                    elif col == 'specialized_equipment':
                        df[col] = 0  # No specialized equipment
                    elif col == 'driver_skill_level':
                        df[col] = 3  # Average skill level (1-5 scale)
                    elif col == 'base_cost_per_km':
                        df[col] = 0.5  # Default cost per km
                        
            logger.info(f"Loaded {len(df)} vehicles with enhanced attributes")
            return df
        except Exception as e:
            logger.error(f"Error loading fleet data: {e}")
            return None
            
    def _compute_payload_complexity(self):
        """Compute complexity metrics for deliveries based on package characteristics."""
        if 'package_size' in self.delivery_data.columns:
            sizes = self.delivery_data['package_size'].values
            self.delivery_data['size_complexity'] = sizes / np.mean(sizes)
        else:
            self.delivery_data['size_complexity'] = 1.0
            
        if 'delivery_priority' in self.delivery_data.columns:
            priorities = self.delivery_data['delivery_priority'].values
            self.delivery_data['priority_factor'] = priorities / 5.0  # Normalize to 0-1
        else:
            self.delivery_data['priority_factor'] = 0.6  # Medium priority
            
        # Compute handling complexity based on time windows
        if 'time_window_start' in self.delivery_data.columns and 'time_window_end' in self.delivery_data.columns:
            duration = (self.delivery_data['time_window_end'] - self.delivery_data['time_window_start']).dt.total_seconds() / 3600
            self.delivery_data['time_flexibility'] = np.clip(duration / 8.0, 0.1, 2.0)  # Normalize to 8-hour window
        else:
            self.delivery_data['time_flexibility'] = 1.0

    def _compute_dynamic_parameters(self, route_indices: list, vehicle: dict) -> tuple:
        """
        Compute dynamic affinity and barrier parameters based on route and vehicle characteristics.
        
        Args:
            route_indices: Indices of delivery points in the route
            vehicle: Vehicle dictionary with specifications
            
        Returns:
            Tuple of (dynamic_a, dynamic_b) parameters
        """
        route_data = self.delivery_data.iloc[route_indices]
        
        # Dynamic Affinity (a): Represents vehicle-payload compatibility
        # Higher values when vehicle is well-suited for payload characteristics
        size_match = np.mean(route_data['size_complexity'])
        priority_match = np.mean(route_data['priority_factor'])
        time_match = np.mean(route_data['time_flexibility'])
        
        # Vehicle capability factors
        capacity_utilization = route_data['package_size'].sum() / vehicle['capacity']
        skill_factor = vehicle['driver_skill_level'] / 5.0
        equipment_bonus = 1.0 + (vehicle['specialized_equipment'] * 0.2)
        
        # Affinity increases with better vehicle-payload matching
        dynamic_a = self.base_a * (
            1.0 + 
            (skill_factor * priority_match) +  # Skilled drivers for high-priority packages
            (equipment_bonus * size_match) +   # Specialized equipment for complex packages
            (capacity_utilization * 0.5)       # Efficient capacity utilization
        )
        
        # Dynamic Barrier (b): Represents operational and cost barriers
        # Higher values when operational costs are significant
        fuel_cost_factor = 1.0 / vehicle['fuel_efficiency']  # Higher for less efficient vehicles
        maintenance_factor = vehicle['maintenance_cost']
        age_penalty = vehicle['age'] / 10.0  # Penalty for older vehicles
        handling_efficiency = vehicle['handling_rate']
        
        # Time constraint penalties
        time_pressure = 1.0 / np.mean(route_data['time_flexibility'])
        
        # Barrier increases with operational complexity and costs
        dynamic_b = self.base_b * (
            1.0 +
            (fuel_cost_factor * 0.3) +         # Fuel efficiency impact
            (maintenance_factor * 10.0) +      # Maintenance cost impact
            (age_penalty * 0.2) +              # Age-related reliability issues
            (time_pressure * 0.4) +            # Time constraint pressure
            (1.0 / handling_efficiency)        # Handling efficiency impact
        )
        
        return dynamic_a, dynamic_b

    def optimize(self):
        """Run the generalized fleet optimization process."""
        n_points = len(self.delivery_data)
        n_vehicles = len(self.fleet_data)
        
        # Initial route determination using base parameters
        k_opt, _, _ = StirlingOptimizer.find_optimal_k(n_points, self.base_a, self.base_b, min_k=1, max_k=n_vehicles)
        logger.info(f"Initial optimal routes (base a={self.base_a}, b={self.base_b}): {k_opt}")
        
        route_clusters = self.route_solver.constructive_approach(k_opt)
        routes = self._compute_routes(route_clusters)
        
        # Enhanced assignment with dynamic parameters
        assignments, unassigned = self._assign_routes_dynamic(routes)
        self._report_enhanced(assignments, unassigned)

    def _compute_routes(self, route_clusters: dict) -> list:
        """Compute route details from clustered delivery points."""
        routes = []
        for i, indices in route_clusters.items():
            route_points = self.delivery_data.iloc[indices]
            ordered_indices = self.route_solver.optimize_route(indices)
            
            total_distance = sum(self.route_solver.distance_matrix[ordered_indices[j], ordered_indices[j+1]]
                                for j in range(len(ordered_indices)-1)) if len(ordered_indices) > 1 else 0
            
            # Aggregate package sizes for capacity check
            total_load = route_points['package_size'].sum()
            avg_priority = route_points['priority_factor'].mean()
            complexity_score = route_points['size_complexity'].mean()
            
            routes.append({
                "id": i,
                "point_count": len(route_points),
                "total_distance": total_distance,
                "total_load": total_load,
                "avg_priority": avg_priority,
                "complexity_score": complexity_score,
                "indices": indices
            })
        return routes

    def _assign_routes_dynamic(self, routes: list) -> tuple:
        """Enhanced assignment using dynamic Stirling parameters."""
        # Sort routes by average priority and load (descending)
        routes = sorted(routes, key=lambda r: (r['avg_priority'], r['total_load']), reverse=True)
        vehicles = self.fleet_data.to_dict('records')
        
        assignments, unassigned = [], list(routes)
        
        for vehicle in vehicles:
            best_route, best_cost, best_params = None, float('inf'), None
            
            for route in unassigned:
                if route['total_load'] <= vehicle['capacity']:
                    # Compute dynamic parameters for this vehicle-route combination
                    dynamic_a, dynamic_b = self._compute_dynamic_parameters(route['indices'], vehicle)
                    
                    # Compute Stirling-based assignment cost
                    stirling_cost = StirlingOptimizer.generalized_stirling(
                        route['point_count'], 1, dynamic_a, dynamic_b
                    )
                    
                    # Operational cost
                    base_cost = route['total_distance'] * vehicle['base_cost_per_km']
                    fuel_cost = route['total_distance'] / vehicle['fuel_efficiency']
                    maintenance_cost = route['total_distance'] * vehicle['maintenance_cost']
                    
                    # Priority and complexity adjustments
                    priority_bonus = 1.0 - (route['avg_priority'] * 0.2)  # Lower cost for high priority
                    complexity_penalty = 1.0 + (route['complexity_score'] * 0.3)
                    
                    total_cost = (base_cost + fuel_cost + maintenance_cost) * complexity_penalty * priority_bonus + stirling_cost
                    
                    if total_cost < best_cost:
                        best_route, best_cost, best_params = route, total_cost, (dynamic_a, dynamic_b)
            
            if best_route:
                assignments.append({
                    "vehicle_id": vehicle['id'],
                    "vehicle_type": vehicle['type'],
                    "vehicle_capacity": vehicle['capacity'],
                    "route_id": best_route['id'],
                    "route_points": best_route['point_count'],
                    "route_load": best_route['total_load'],
                    "route_distance": best_route['total_distance'],
                    "avg_priority": best_route['avg_priority'],
                    "complexity_score": best_route['complexity_score'],
                    "dynamic_a": best_params[0],
                    "dynamic_b": best_params[1],
                    "assignment_cost": best_cost
                })
                unassigned.remove(best_route)
        
        return assignments, unassigned

    def _report_enhanced(self, assignments: list, unassigned_routes: list):
        """Enhanced reporting with dynamic parameter analysis."""
        print("\n--- Enhanced Fleet Optimization Results ---")
        print(f"Base Parameters: a={self.base_a}, b={self.base_b}")
        
        if not assignments:
            print("No routes could be assigned to the available fleet.")
            return
            
        df = pd.DataFrame(assignments)
        
        print("\n**Route Assignments with Dynamic Parameters:**")
        display_cols = ['vehicle_id', 'vehicle_type', 'route_points', 'route_load', 
                       'avg_priority', 'complexity_score', 'dynamic_a', 'dynamic_b', 'assignment_cost']
        print(df[display_cols].round(3).to_string(index=False))
        
        print("\n**Summary:**")
        print(f"  - Total routes assigned: {len(assignments)}")
        print(f"  - Total distance covered: {df['route_distance'].sum():.2f}")
        print(f"  - Total estimated cost: ${df['assignment_cost'].sum():.2f}")
        print(f"  - Average dynamic affinity: {df['dynamic_a'].mean():.2f}")
        print(f"  - Average dynamic barrier: {df['dynamic_b'].mean():.2f}")
        print(f"  - Fleet utilization: {len(assignments)}/{len(self.fleet_data)} ({100*len(assignments)/len(self.fleet_data):.1f}%)")
        
        if unassigned_routes:
            print("\n**Unassigned Routes:**")
            for route in unassigned_routes:
                print(f"  - Route {route['id']}: {route['point_count']} points, "
                      f"Load: {route['total_load']:.2f}, Priority: {route['avg_priority']:.2f}")

def main():
    parser = argparse.ArgumentParser(description='Generalized Fleet Optimizer with Dynamic Stirling Parameters')
    parser.add_argument('--data', type=str, required=True, help='Path to delivery data CSV')
    parser.add_argument('--fleet', type=str, required=True, help='Path to enhanced fleet composition CSV')
    parser.add_argument('--params', type=str, default='1.0,1.0', help='Base a,b parameters')
    
    args = parser.parse_args()
    
    try:
        a, b = map(float, args.params.split(','))
    except ValueError:
        logger.error("Invalid format for --params. Use comma-separated floats.")
        return
        
    optimizer = GeneralizedFleetOptimizer(args.data, args.fleet, (a, b))
    optimizer.optimize()

if __name__ == "__main__":
    main()
