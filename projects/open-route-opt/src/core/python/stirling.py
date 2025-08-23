"""
Generalized Stirling Numbers implementation for route optimization.

This module implements the core generalized Stirling number functionality
used for the OpenRouteOpt proof of concept.
"""

import numpy as np
from typing import Tuple, List, Dict, Optional, Union
from dataclasses import dataclass
from functools import lru_cache

@dataclass
class DeliveryPoint:
    """Represents a delivery location with constraints."""
    id: str
    lat: float
    lng: float
    time_window_start: Optional[float] = None  # In seconds from midnight
    time_window_end: Optional[float] = None    # In seconds from midnight
    service_duration: float = 300.0            # Default 5 minutes in seconds
    demand: float = 1.0                        # Default package size

@dataclass
class Vehicle:
    """Represents a delivery vehicle."""
    id: str
    start_lat: float
    start_lng: float
    capacity: float = 100.0
    max_distance: Optional[float] = None
    max_duration: Optional[float] = None  # In seconds

class GeneralizedStirling:
    """
    Implementation of generalized Stirling numbers with parameters a and b.
    
    These numbers have a combinatorial interpretation as the total weight
    of distributing n elements into k ordered non-empty lists, where:
    1. The head of each list has weight b
    2. Other elements in lists have weight a
    3. The first element placed in each list has weight 1
    """
    
    def __init__(self, a: float = 1.0, b: float = 1.0):
        """
        Initialize the generalized Stirling calculator.
        
        Args:
            a: Parameter for within-list weight
            b: Parameter for between-list weight
        """
        self.a = a
        self.b = b
        self._cache = {}
    
    @lru_cache(maxsize=10000)
    def compute(self, n: int, k: int) -> float:
        """
        Compute the generalized Stirling number S(n,k)(a,b).
        
        Args:
            n: Number of elements
            k: Number of lists
            
        Returns:
            The value of S(n,k)(a,b)
        """
        # Base cases
        if k == 0:
            return 1.0 if n == 0 else 0.0
        if n == 0 or k > n:
            return 0.0
        if k == n:
            return 1.0
        
        # Use triangular recurrence relation
        # S(n+1,k)(a,b) = S(n,k-1)(a,b) + (an + bk)S(n,k)(a,b)
        # Rewritten for computing S(n,k) as:
        # S(n,k)(a,b) = S(n-1,k-1)(a,b) + (a(n-1) + bk)S(n-1,k)(a,b)
        return self.compute(n-1, k-1) + (self.a * (n-1) + self.b * k) * self.compute(n-1, k)
    
    def generate_triangle(self, n_max: int) -> List[List[float]]:
        """
        Generate a triangle of generalized Stirling numbers up to n_max.
        
        Args:
            n_max: Maximum value of n to compute
            
        Returns:
            A list of lists containing the values
        """
        triangle = []
        for n in range(n_max + 1):
            row = []
            for k in range(min(n, n_max) + 1):
                row.append(self.compute(n, k))
            triangle.append(row)
        return triangle
    
    def estimate_parameters(self, n_k_pairs: List[Tuple[int, int, float]]) -> Tuple[float, float]:
        """
        Estimate parameters a and b from observed data using the Stirling measure.
        
        Args:
            n_k_pairs: List of (n, k, measure) tuples where measure is 
                       (S(n+1,k) - S(n,k-1))/S(n,k)
                       
        Returns:
            Estimated (a, b) parameters
        """
        X = np.array([[n, k] for n, k, _ in n_k_pairs])
        y = np.array([measure for _, _, measure in n_k_pairs])
        
        # Solve the linear system (an + bk = measure)
        result = np.linalg.lstsq(X, y, rcond=None)
        a, b = result[0]
        
        return a, b

class RouteOptimizer:
    """
    Route optimization using generalized Stirling numbers.
    """
    
    def __init__(self, a: float = 1.0, b: float = 1.0):
        """
        Initialize the route optimizer.
        
        Args:
            a: Parameter for intra-route cost
            b: Parameter for new route cost
        """
        self.stirling = GeneralizedStirling(a, b)
        self.a = a
        self.b = b
    
    def optimize(self, 
                 delivery_points: List[DeliveryPoint], 
                 vehicles: List[Vehicle]) -> Dict[str, List[str]]:
        """
        Optimize routes using generalized Stirling approach.
        
        Args:
            delivery_points: List of delivery points
            vehicles: List of available vehicles
            
        Returns:
            Dictionary mapping vehicle IDs to lists of delivery point IDs
        """
        n = len(delivery_points)
        k = len(vehicles)
        
        # Initialize empty routes
        routes = {vehicle.id: [] for vehicle in vehicles}
        
        # Simple implementation: assign each point one by one
        unassigned_points = delivery_points.copy()
        
        for point in unassigned_points:
            assigned = False
            
            # If we have unused vehicles, determine if we should create a new route
            if len([v for v in routes.values() if len(v) == 0]) > 0:
                n_current = sum(len(route) for route in routes.values())
                k_current = len([r for r in routes.values() if len(r) > 0])
                
                # Calculate Stirling-based decision
                add_cost = (self.a * n_current + self.b * k_current) * self.stirling.compute(n_current, k_current)
                new_route_cost = self.stirling.compute(n_current, k_current - 1)
                
                if new_route_cost < add_cost:
                    # Create new route
                    for v_id, route in routes.items():
                        if len(route) == 0:
                            routes[v_id].append(point.id)
                            assigned = True
                            break
            
            # If not assigned to a new route, add to existing route
            if not assigned:
                # Simple heuristic: add to the shortest route
                shortest_route_id = min(routes, key=lambda v_id: len(routes[v_id]))
                routes[shortest_route_id].append(point.id)
        
        return routes
    
    def calculate_route_cost(self, 
                            route: List[str], 
                            points_dict: Dict[str, DeliveryPoint],
                            vehicle: Vehicle) -> float:
        """
        Calculate the cost of a route based on distance.
        
        Args:
            route: List of delivery point IDs
            points_dict: Dictionary mapping IDs to DeliveryPoint objects
            vehicle: Vehicle performing the route
            
        Returns:
            Total route cost (distance)
        """
        if not route:
            return 0.0
        
        total_distance = 0.0
        
        # Distance from depot to first point
        first_point = points_dict[route[0]]
        total_distance += self._haversine(
            vehicle.start_lat, vehicle.start_lng,
            first_point.lat, first_point.lng
        )
        
        # Distance between consecutive points
        for i in range(len(route) - 1):
            point1 = points_dict[route[i]]
            point2 = points_dict[route[i+1]]
            total_distance += self._haversine(
                point1.lat, point1.lng,
                point2.lat, point2.lng
            )
        
        # Distance from last point back to depot
        last_point = points_dict[route[-1]]
        total_distance += self._haversine(
            last_point.lat, last_point.lng,
            vehicle.start_lat, vehicle.start_lng
        )
        
        return total_distance
    
    @staticmethod
    def _haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees).
        
        Returns:
            Distance in kilometers
        """
        # Convert decimal degrees to radians
        lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
        
        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
        c = 2 * np.arcsin(np.sqrt(a))
        r = 6371  # Radius of earth in kilometers
        return c * r
