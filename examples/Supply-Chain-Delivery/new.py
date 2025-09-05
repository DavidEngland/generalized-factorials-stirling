import numpy as np, pandas as pd, matplotlib.pyplot as plt, networkx as nx
from scipy.spatial.distance import pdist, squareform
import argparse, json, os, logging, folium
from sklearn.cluster import KMeans, SpectralClustering
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional, Any

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("dual_perspective_delivery")

class DataHandler:
    def __init__(self): self.data = None
    
    def load_data(self, path):
        try:
            df = pd.read_csv(path)
            self._validate_and_preprocess(df)
            logger.info(f"Loaded {len(df)} delivery points")
            self.data = df
            return df
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            return None
    
    def _validate_and_preprocess(self, df):
        required = ["id", "latitude", "longitude"]
        optional = ["package_size", "delivery_priority", "time_window_start", "time_window_end"]
        
        missing = [col for col in required if col not in df.columns]
        if missing: raise ValueError(f"Missing required columns: {missing}")
            
        if "time_window_start" in df.columns and "time_window_end" in df.columns:
            df["time_window_start"] = pd.to_datetime(df["time_window_start"])
            df["time_window_end"] = pd.to_datetime(df["time_window_end"])
        
        for col in [c for c in optional if c not in df.columns]:
            if col == "package_size": df[col] = 1
            elif col == "delivery_priority": df[col] = 3
            elif col in ["time_window_start", "time_window_end"]:
                today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                df[col] = today + timedelta(hours=8 if col == "time_window_start" else 18)

class StirlingOptimizer:
    @staticmethod
    def generalized_stirling(n, k, a, b):
        if k > n or k <= 0: return 0
        if n == 0: return 1 if k == 0 else 0
        
        dp = np.zeros((n+1, k+1))
        dp[0, 0] = 1
        
        for i in range(1, n+1):
            for j in range(1, min(i+1, k+1)):
                dp[i, j] = dp[i-1, j-1] + (a*(i-1) + b*j) * dp[i-1, j]
        
        return dp[n, k]
    
    @staticmethod
    def find_optimal_k(n, a, b, min_k=1, max_k=None):
        if max_k is None: max_k = n
        
        costs = [(k, StirlingOptimizer.generalized_stirling(n, k, a, b)) 
                for k in range(min_k, min(n+1, max_k+1))]
        
        if not costs: return min_k, float('inf'), []
        optimal = min(costs, key=lambda x: x[1])
        return optimal[0], optimal[1], costs
    
    @staticmethod
    def estimate_parameters(data, approach="constructive"):
        if data is None or len(data) == 0: return 0.0, 0.0
        
        coords = data[['latitude', 'longitude']].values
        distances = squareform(pdist(coords))
        mean_dist = np.mean(distances)
        
        size_var = np.std(data['package_size'].values / data['package_size'].max()) if 'package_size' in data.columns else 0.2
        priorities = data['delivery_priority'].values if 'delivery_priority' in data.columns else np.ones(len(data))
        
        if 'time_window_start' in data.columns and 'time_window_end' in data.columns:
            duration = (data['time_window_end'] - data['time_window_start']).dt.total_seconds() / 3600
            time_flex = np.mean(duration)
        else: time_flex = 8
            
        if approach == "constructive":
            a = mean_dist * (1 + size_var)
            b = mean_dist * 10 * (1 / time_flex)
        else:  # deconstructive
            a = mean_dist * (1 + np.mean(priorities) / 5)
            b = mean_dist * 5 * time_flex
        
        return float(a), float(b)

class RouteSolver:
    def __init__(self, data):
        self.data = data
        self.distance_matrix = None
        if data is not None: self._create_distance_matrix()
    
    def _create_distance_matrix(self):
        if self.data is None: return None
        coords = self.data[['latitude', 'longitude']].values
        self.distance_matrix = squareform(pdist(coords))
    
    def constructive_approach(self, k):
        coords = self.data[['latitude', 'longitude']].values
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        self.data['route_constructive'] = kmeans.fit_predict(coords)
        
        routes = {}
        for i in range(k):
            routes[i] = self.data[self.data['route_constructive'] == i].index.tolist()
        
        return routes
    
    def deconstructive_approach(self, k):
        G = nx.Graph()
        n = len(self.data)
        
        for i in range(n):
            G.add_node(i, pos=(self.data.iloc[i]['latitude'], self.data.iloc[i]['longitude']))
            
        threshold = np.percentile(self.distance_matrix.flatten(), 15)
        for i in range(n):
            for j in range(i+1, n):
                if self.distance_matrix[i, j] < threshold:
                    G.add_edge(i, j, weight=self.distance_matrix[i, j])
        
        adjacency = nx.adjacency_matrix(G).toarray()
        spectral = SpectralClustering(n_clusters=k, affinity='precomputed', random_state=42)
        self.data['route_deconstructive'] = spectral.fit_predict(adjacency)
        
        routes = {}
        for i in range(k):
            routes[i] = self.data[self.data['route_deconstructive'] == i].index.tolist()
        
        return routes, G
    
    def optimize_route(self, points, method="nearest_neighbor"):
        if len(points) <= 2: return points
        
        sub_matrix = self.distance_matrix[np.ix_(points, points)]
        
        if method == "nearest_neighbor":
            ordered = [0]
            unvisited = set(range(1, len(points)))
            
            while unvisited:
                current = ordered[-1]
                next_idx = min(unvisited, key=lambda x: sub_matrix[current, x])
                ordered.append(next_idx)
                unvisited.remove(next_idx)
                
            return [points[i] for i in ordered]
        
        return points

class ReportGenerator:
    def __init__(self, data, results):
        self.data = data
        self.results = results
        os.makedirs("visualizations", exist_ok=True)
        os.makedirs("results", exist_ok=True)
    
    def visualize_routes(self, graph=None):
        if self.data is None: return
        self._create_cost_plot()
        self._create_route_map(graph)
        self._create_comparison_report()
    
    def _create_cost_plot(self):
        plt.figure(figsize=(10, 5))
        c, d = self.results["constructive"], self.results["deconstructive"]
        
        if "all_costs" in c:
            plt.plot([x[0] for x in c["all_costs"]], [x[1] for x in c["all_costs"]], 'b-o', 
                    label=f"Constructive (a={c['parameters']['a']:.2f}, b={c['parameters']['b']:.2f})")
            plt.axvline(x=c["optimal_k"], color='b', linestyle='--')
        
        if "all_costs" in d:
            plt.plot([x[0] for x in d["all_costs"]], [x[1] for x in d["all_costs"]], 'r-o', 
                    label=f"Deconstructive (a={d['parameters']['a']:.2f}, b={d['parameters']['b']:.2f})")
            plt.axvline(x=d["optimal_k"], color='r', linestyle='--')
        
        plt.xlabel("Routes (k)"), plt.ylabel("Cost"), plt.legend(), plt.grid(True)
        plt.savefig("visualizations/cost_comparison.png", dpi=300, bbox_inches='tight')
    
    def _create_route_map(self, graph=None):
        center = [self.data['latitude'].mean(), self.data['longitude'].mean()]
        m = folium.Map(location=center, zoom_start=12)
        colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'darkblue']
        
        for approach, layer_name in [("constructive", "Constructive"), ("deconstructive", "Deconstructive")]:
            col_name = f"route_{approach}"
            if col_name not in self.data.columns: continue
            
            for route_id in range(self.results[approach]["optimal_k"]):
                route_points = self.data[self.data[col_name] == route_id]
                color = colors[route_id % len(colors)]
                route_group = folium.FeatureGroup(name=f"{layer_name} Route {route_id+1}")
                
                ordered_points = route_points.sort_values('id')
                if len(ordered_points) > 1:
                    route_coords = [(row['latitude'], row['longitude']) for _, row in ordered_points.iterrows()]
                    folium.PolyLine(locations=route_coords, color=color, weight=3, opacity=0.7, 
                                  dash_array='5,10' if approach == "deconstructive" else None).add_to(route_group)
                
                for _, point in route_points.iterrows():
                    folium.CircleMarker(location=[point['latitude'], point['longitude']], radius=5, color=color,
                                      fill=True, fill_color=color, popup=f"ID: {point['id']}").add_to(route_group)
                
                route_group.add_to(m)
        
        if graph is not None:
            graph_layer = folium.FeatureGroup(name="Network Graph", show=False)
            for u, v, _ in graph.edges(data=True):
                if u >= len(self.data) or v >= len(self.data): continue
                u_lat, u_lon = self.data.iloc[u]['latitude'], self.data.iloc[u]['longitude']
                v_lat, v_lon = self.data.iloc[v]['latitude'], self.data.iloc[v]['longitude']
                folium.PolyLine(locations=[(u_lat, u_lon), (v_lat, v_lon)], color='gray', 
                              weight=1, opacity=0.5).add_to(graph_layer)
            graph_layer.add_to(m)
        
        folium.LayerControl().add_to(m)
        m.save("visualizations/route_map.html")
    
    def _create_comparison_report(self):
        if not self.results["constructive"] or not self.results["deconstructive"]: return
        
        c, d = self.results["constructive"], self.results["deconstructive"]
        c_pts = [r["point_count"] for r in c["routes"].values()]
        d_pts = [r["point_count"] for r in d["routes"].values()]
        
        c_metrics = {
            "min_pts": min(c_pts), "max_pts": max(c_pts), "avg_pts": np.mean(c_pts), "std_pts": np.std(c_pts),
            "avg_dist": c["total_distance"] / c["optimal_k"], "pts_per_dist": len(self.data) / c["total_distance"]
        }
        d_metrics = {
            "min_pts": min(d_pts), "max_pts": max(d_pts), "avg_pts": np.mean(d_pts), "std_pts": np.std(d_pts),
            "avg_dist": d["total_distance"] / d["optimal_k"], "pts_per_dist": len(self.data) / d["total_distance"]
        }
        
        html = f"""<!DOCTYPE html><html><head><title>Route Optimization Report</title>
        <style>body{{font-family:Arial;margin:20px;}}table{{border-collapse:collapse;width:100%;}}
        th,td{{border:1px solid #ddd;padding:8px;}}th{{background:#f2f2f2;}}
        .winner{{background:#e6ffe6;}}.metrics{{display:flex;flex-wrap:wrap;}}
        .card{{background:#f8f9fa;border-radius:5px;padding:15px;margin:10px;flex:1;}}
        .value{{font-size:24px;font-weight:bold;color:#333366;}}</style></head><body>
        <h1>Delivery Route Optimization Report</h1>
        
        <div class="metrics">
            <div class="card"><h3>Total Points</h3><div class="value">{len(self.data)}</div></div>
            <div class="card"><h3>Vehicles</h3><div class="value">{min(c["optimal_k"], d["optimal_k"])}</div></div>
            <div class="card"><h3>Distance Improvement</h3><div class="value">
                {(abs(c["total_distance"] - d["total_distance"]) / max(c["total_distance"], d["total_distance"]) * 100):.1f}%
            </div></div>
        </div>
        
        <h2>Comparison</h2>
        <table>
            <tr><th>Metric</th><th>Constructive</th><th>Deconstructive</th><th>Better</th></tr>
            <tr><td>Routes</td><td>{c["optimal_k"]}</td><td>{d["optimal_k"]}</td>
                <td class="winner">{"Deconstructive" if d["optimal_k"] < c["optimal_k"] else 
                "Constructive" if c["optimal_k"] < d["optimal_k"] else "Tie"}</td></tr>
            <tr><td>Total Distance</td><td>{c["total_distance"]:.2f}</td><td>{d["total_distance"]:.2f}</td>
                <td class="winner">{"Deconstructive" if d["total_distance"] < c["total_distance"] else 
                "Constructive" if c["total_distance"] < d["total_distance"] else "Tie"}</td></tr>
            <tr><td>Balance (std)</td><td>{c_metrics["std_pts"]:.2f}</td><td>{d_metrics["std_pts"]:.2f}</td>
                <td class="winner">{"Deconstructive" if d_metrics["std_pts"] < c_metrics["std_pts"] else 
                "Constructive" if c_metrics["std_pts"] < d_metrics["std_pts"] else "Tie"}</td></tr>
            <tr><td>Parameters (a,b)</td><td>({c["parameters"]["a"]:.2f}, {c["parameters"]["b"]:.2f})</td>
                <td>({d["parameters"]["a"]:.2f}, {d["parameters"]["b"]:.2f})</td><td>Different meaning</td></tr>
        </table>
        
        <div>
            <h3>Cost vs. Number of Routes</h3>
            <img src="cost_comparison.png" alt="Cost Comparison" style="width:100%">
        </div>
        <div>
            <h3>Route Map</h3>
            <iframe src="route_map.html" width="100%" height="400px"></iframe>
        </div>
        </body></html>"""
        
        with open("visualizations/delivery_report.html", "w") as f:
            f.write(html)

class DualPerspectiveOptimizer:
    def __init__(self, data_path=None):
        self.data_handler = DataHandler()
        self.data = self.data_handler.load_data(data_path) if data_path else None
        self.route_solver = RouteSolver(self.data)
        self.results = {"constructive": {}, "deconstructive": {}}

    def constructive_approach(self, min_vehicles=1, max_vehicles=None):
        if self.data is None: return None
        n = len(self.data)
        if max_vehicles is None: max_vehicles = n

        # Estimate parameters
        a, b = StirlingOptimizer.estimate_parameters(self.data, "constructive")
        logger.info(f"Constructive params: a={a:.2f}, b={b:.2f}")
        
        # Find optimal k
        k_opt, cost_opt, all_costs = StirlingOptimizer.find_optimal_k(n, a, b, min_vehicles, max_vehicles)
        logger.info(f"Optimal vehicles: {k_opt}")

        # Cluster points
        routes_dict = self.route_solver.constructive_approach(k_opt)

        # Calculate stats
        routes = {}
        for i, indices in routes_dict.items():
            route_points = self.data.iloc[indices]
            ordered_indices = self.route_solver.optimize_route(indices)
            
            total_distance = 0
            if len(ordered_indices) > 1:
                for j in range(len(ordered_indices)-1):
                    idx1, idx2 = ordered_indices[j], ordered_indices[j+1]
                    total_distance += self.route_solver.distance_matrix[idx1, idx2]
            
            routes[i] = {
                "point_count": len(route_points),
                "total_distance": total_distance,
                "points": route_points['id'].tolist(),
                "ordered_indices": ordered_indices
            }

        self.results["constructive"] = {
            "parameters": {"a": a, "b": b},
            "optimal_k": k_opt,
            "optimal_cost": cost_opt,
            "all_costs": all_costs,
            "routes": routes,
            "total_distance": sum(r["total_distance"] for r in routes.values())
        }
        return self.results["constructive"]

    def deconstructive_approach(self, min_vehicles=1, max_vehicles=None):
        if self.data is None: return None
        n = len(self.data)
        if max_vehicles is None: max_vehicles = n
            
        # Similar to constructive but with different parameters and clustering
        a, b = StirlingOptimizer.estimate_parameters(self.data, "deconstructive")
        logger.info(f"Deconstructive params: a={a:.2f}, b={b:.2f}")
        
        k_opt, cost_opt, all_costs = StirlingOptimizer.find_optimal_k(n, a, b, min_vehicles, max_vehicles)
        logger.info(f"Optimal vehicles: {k_opt}")

        routes_dict, G = self.route_solver.deconstructive_approach(k_opt)

        routes = {}
        for i, indices in routes_dict.items():
            route_points = self.data.iloc[indices]
            ordered_indices = self.route_solver.optimize_route(indices)
            
            total_distance = 0
            if len(ordered_indices) > 1:
                for j in range(len(ordered_indices)-1):
                    idx1, idx2 = ordered_indices[j], ordered_indices[j+1]
                    total_distance += self.route_solver.distance_matrix[idx1, idx2]
            
            routes[i] = {
                "point_count": len(route_points),
                "total_distance": total_distance,
                "points": route_points['id'].tolist(),
                "ordered_indices": ordered_indices
            }
        
        self.results["deconstructive"] = {
            "parameters": {"a": a, "b": b},
            "optimal_k": k_opt,
            "optimal_cost": cost_opt,
            "all_costs": all_costs,
            "routes": routes,
            "total_distance": sum(r["total_distance"] for r in routes.values()),
            "graph": G
        }
        return self.results["deconstructive"]
    
    def compare_approaches(self):
        if not self.results["constructive"] or not self.results["deconstructive"]: return
        
        c, d = self.results["constructive"], self.results["deconstructive"]
        logger.info(f"Constructive: {c['optimal_k']} routes, dist: {c['total_distance']:.2f}")
        logger.info(f"Deconstructive: {d['optimal_k']} routes, dist: {d['total_distance']:.2f}")
        
        report_generator = ReportGenerator(self.data, self.results)
        graph = self.results["deconstructive"].get("graph")
        report_generator.visualize_routes(graph)
    
    def save_results(self):
        def to_serializable(obj):
            if isinstance(obj, (np.int64, np.int32)): return int(obj)
            if isinstance(obj, (np.float64, np.float32)): return float(obj)
            if isinstance(obj, list): return [to_serializable(item) for item in obj]
            if isinstance(obj, dict): return {k: to_serializable(v) for k, v in obj.items()}
            if isinstance(obj, tuple) and len(obj) == 2: 
                return [to_serializable(obj[0]), to_serializable(obj[1])]
            return obj
        
        results_copy = {
            "constructive": self.results["constructive"].copy(),
            "deconstructive": self.results["deconstructive"].copy()
        }
        
        if "graph" in results_copy["deconstructive"]:
            del results_copy["deconstructive"]["graph"]
        
        os.makedirs("results", exist_ok=True)
        with open("results/optimization_results.json", "w") as f:
            json.dump(to_serializable(results_copy), f, indent=2)

def generate_sample_data(n=50, seed=42):
    np.random.seed(seed)
    centers = np.random.rand(5, 2) * 10
    
    lats, longs = [], []
    for _ in range(n):
        center = centers[np.random.randint(0, len(centers))]
        lats.append(center[0] + np.random.normal(0, 0.5))
        longs.append(center[1] + np.random.normal(0, 0.5))
    
    package_sizes = np.random.randint(1, 10, size=n)
    priorities = np.random.randint(1, 5, size=n)
    
    base_time = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
    time_windows_start, time_windows_end = [], []
    
    for _ in range(n):
        start_hour = np.random.randint(0, 8)
        window_length = np.random.randint(1, 4)
        time_windows_start.append(base_time + timedelta(hours=start_hour))
        time_windows_end.append(base_time + timedelta(hours=start_hour + window_length))
    
    df = pd.DataFrame({
        'id': range(1, n+1), 'latitude': lats, 'longitude': longs,
        'package_size': package_sizes, 'delivery_priority': priorities,
        'time_window_start': time_windows_start, 'time_window_end': time_windows_end
    })
    
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/sample_deliveries.csv", index=False)
    return "data/sample_deliveries.csv"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Dual-Perspective Route Optimizer')
    parser.add_argument('--data', type=str, help='Path to delivery data CSV')
    parser.add_argument('--vehicles', type=str, default='1-15', help='Vehicle range (min-max)')
    parser.add_argument('--generate', type=int, help='Generate N sample points')
    parser.add_argument('--log', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'], default='INFO')
    
    args = parser.parse_args()
    logger.setLevel(getattr(logging, args.log))
    
    data_path = generate_sample_data(args.generate) if args.generate else args.data
    min_v, max_v = map(int, args.vehicles.split('-')) if args.vehicles else (1, 15)
    
    if data_path:
        optimizer = DualPerspectiveOptimizer(data_path)
        optimizer.constructive_approach(min_vehicles=min_v, max_vehicles=max_v)
        optimizer.deconstructive_approach(min_vehicles=min_v, max_vehicles=max_v)
        optimizer.compare_approaches()
        optimizer.save_results()
        logger.info("Results saved to 'visualizations/' directory")
    else:
        logger.error("No data provided. Use --data or --generate options.")
            </table>
            
            <div class="explanation">
                <h3>Understanding Parameters</h3>
                <p><strong>Affinity (a)</strong>: Constructive - cost of connecting points; Deconstructive - cost of separating points</p>
                <p><strong>Barrier (b)</strong>: Constructive - cost of new route; Deconstructive - cost of creating boundary</p>
            </div>
            
            <iframe src="route_map.html" width="100%" height="400px"></iframe>
            
            <p>The dual-perspective analysis using generalized Stirling numbers demonstrates how viewing the same logistics 
            problem from different angles can lead to operational improvements and cost savings.</p>
        </body>
        </html>
        """
        
        with open("visualizations/delivery_report.html", "w") as f:
            f.write(html)

class DualPerspectiveOptimizer:
    def __init__(self, data_path=None):
        self.data_handler = DataHandler()
        self.data = self.data_handler.load_data(data_path) if data_path else None
        self.route_solver = RouteSolver(self.data)
        self.results = {"constructive": {}, "deconstructive": {}}

    def constructive_approach(self, min_vehicles=1, max_vehicles=None):
        if self.data is None:
            logger.error("No data available")
            return None
            
        n = len(self.data)
        if max_vehicles is None:
            max_vehicles = n

        # Step 1: Estimate parameters
        a, b = StirlingOptimizer.estimate_parameters(self.data, "constructive")
        logger.info(f"Constructive parameters: a={a:.2f}, b={b:.2f}")
        
        # Step 2: Find optimal number of routes
        k_opt, cost_opt, all_costs = StirlingOptimizer.find_optimal_k(n, a, b, min_vehicles, max_vehicles)
        logger.info(f"Optimal number of vehicles: {k_opt}")

        # Step 3: Assign delivery points to routes
        routes_dict = self.route_solver.constructive_approach(k_opt)

        # Step 4: Calculate route statistics
        routes = {}
        for i, indices in routes_dict.items():
            route_points = self.data.iloc[indices]
            ordered_indices = self.route_solver.optimize_route(indices)
            
            total_distance = 0
            if len(ordered_indices) > 1:
                for j in range(len(ordered_indices)-1):
                    idx1, idx2 = ordered_indices[j], ordered_indices[j+1]
                    total_distance += self.route_solver.distance_matrix[idx1, idx2]
            
            routes[i] = {
                "point_count": len(route_points),
                "total_distance": total_distance,
                "points": route_points['id'].tolist(),
                "ordered_indices": ordered_indices
            }

        # Store results
        self.results["constructive"] = {
            "parameters": {"a": a, "b": b},
            "optimal_k": k_opt,
            "optimal_cost": cost_opt,
            "all_costs": all_costs,
            "routes": routes,
            "total_distance": sum(r["total_distance"] for r in routes.values())
        }

        return self.results["constructive"]

    def deconstructive_approach(self, min_vehicles=1, max_vehicles=None):
        if self.data is None:
            logger.error("No data available")
            return None
            
        n = len(self.data)
        if max_vehicles is None:
            max_vehicles = n
            
        # Estimate parameters and find optimal k
        a, b = StirlingOptimizer.estimate_parameters(self.data, "deconstructive")
        logger.info(f"Deconstructive parameters: a={a:.2f}, b={b:.2f}")
        
        k_opt, cost_opt, all_costs = StirlingOptimizer.find_optimal_k(n, a, b, min_vehicles, max_vehicles)
        logger.info(f"Optimal number of vehicles: {k_opt}")

        # Create network and find optimal segmentation
        routes_dict, G = self.route_solver.deconstructive_approach(k_opt)

        # Calculate route statistics
        routes = {}
        for i, indices in routes_dict.items():
            route_points = self.data.iloc[indices]
            ordered_indices = self.route_solver.optimize_route(indices)
            
            total_distance = 0
            if len(ordered_indices) > 1:
                for j in range(len(ordered_indices)-1):
                    idx1, idx2 = ordered_indices[j], ordered_indices[j+1]
                    total_distance += self.route_solver.distance_matrix[idx1, idx2]
            
            routes[i] = {
                "point_count": len(route_points),
                "total_distance": total_distance,
                "points": route_points['id'].tolist(),
                "ordered_indices": ordered_indices
            }
        
        # Store results
        self.results["deconstructive"] = {
            "parameters": {"a": a, "b": b},
            "optimal_k": k_opt,
            "optimal_cost": cost_opt,
            "all_costs": all_costs,
            "routes": routes,
            "total_distance": sum(r["total_distance"] for r in routes.values()),
            "graph": G
        }

        return self.results["deconstructive"]
    
    def compare_approaches(self):
        if not self.results["constructive"] or not self.results["deconstructive"]:
            logger.error("Run both approaches first")
            return

        # Compare key metrics
        c = self.results["constructive"]
        d = self.results["deconstructive"]
        
        logger.info(f"Constructive: {c['optimal_k']} routes, distance: {c['total_distance']:.2f}")
        logger.info(f"Deconstructive: {d['optimal_k']} routes, distance: {d['total_distance']:.2f}")
        
        # Calculate route balance
        c_balance = np.std([r["point_count"] for r in c["routes"].values()])
        d_balance = np.std([r["point_count"] for r in d["routes"].values()])
        logger.info(f"Route balance - Constructive: {c_balance:.2f}, Deconstructive: {d_balance:.2f}")
        
        # Create visualizations
        report_generator = ReportGenerator(self.data, self.results)
        graph = self.results["deconstructive"].get("graph") if "graph" in self.results["deconstructive"] else None
        report_generator.visualize_routes(graph)
    
    def save_results(self):
        def convert_to_serializable(obj):
            if isinstance(obj, (np.int64, np.int32)):
                return int(obj)
            if isinstance(obj, (np.float64, np.float32)):
                return float(obj)
            if isinstance(obj, list):
                return [convert_to_serializable(item) for item in obj]
            if isinstance(obj, dict):
                return {k: convert_to_serializable(v) for k, v in obj.items()}
            if isinstance(obj, tuple) and len(obj) == 2:
                return [convert_to_serializable(obj[0]), convert_to_serializable(obj[1])]
            return obj
        
        results_copy = {
            "constructive": self.results["constructive"].copy(),
            "deconstructive": self.results["deconstructive"].copy()
        }
        
        if "graph" in results_copy["deconstructive"]:
            del results_copy["deconstructive"]["graph"]
        
        serializable_results = convert_to_serializable(results_copy)
        
        os.makedirs("results", exist_ok=True)
        with open("results/optimization_results.json", "w") as f:
            json.dump(serializable_results, f, indent=2)
        
        logger.info("Results saved to results/optimization_results.json")

def generate_sample_data(n=50, seed=42):
    np.random.seed(seed)
    centers = np.random.rand(5, 2) * 10
    
    lats, longs = [], []
    for _ in range(n):
        center = centers[np.random.randint(0, len(centers))]
        lats.append(center[0] + np.random.normal(0, 0.5))
        longs.append(center[1] + np.random.normal(0, 0.5))
    
    package_sizes = np.random.randint(1, 10, size=n)
    priorities = np.random.randint(1, 5, size=n)
    
    base_time = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
    time_windows_start, time_windows_end = [], []
    
    for _ in range(n):
        start_hour = np.random.randint(0, 8)
        window_length = np.random.randint(1, 4)
        start_time = base_time + timedelta(hours=start_hour)
        end_time = start_time + timedelta(hours=window_length)
        time_windows_start.append(start_time)
        time_windows_end.append(end_time)
    
    df = pd.DataFrame({
        'id': range(1, n+1),
        'latitude': lats,
        'longitude': longs,
        'package_size': package_sizes,
        'delivery_priority': priorities,
        'time_window_start': time_windows_start,
        'time_window_end': time_windows_end
    })
    
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/sample_deliveries.csv", index=False)
    print(f"Generated sample data with {n} delivery points")
    
    return "data/sample_deliveries.csv"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Dual-Perspective Delivery Route Optimizer')
    parser.add_argument('--data', type=str, help='Path to delivery data CSV')
    parser.add_argument('--vehicles', type=str, default='1-15', help='Range of vehicles to consider (min-max)')
    parser.add_argument('--generate', type=int, help='Generate sample data with N points')
    parser.add_argument('--log', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'], default='INFO', help='Set logging level')
    
    args = parser.parse_args()
    logger.setLevel(getattr(logging, args.log))
    
    # Generate sample data if requested
    data_path = generate_sample_data(args.generate) if args.generate else args.data
    
    # Parse vehicle range
    min_v, max_v = map(int, args.vehicles.split('-')) if args.vehicles else (1, 15)
    
    # Run optimization
    if data_path:
        optimizer = DualPerspectiveOptimizer(data_path)
        optimizer.constructive_approach(min_vehicles=min_v, max_vehicles=max_v)
        optimizer.deconstructive_approach(min_vehicles=min_v, max_vehicles=max_v)
        optimizer.compare_approaches()
        optimizer.save_results()
        logger.info("Visualization and report saved to 'visualizations/' directory")
    else:
        logger.error("No data provided. Use --data or --generate options.")
                    <h3>Cost vs. Number of Routes</h3>
                    <img src="cost_comparison.png" alt="Cost Comparison" style="width:100%">
                </div>
                <div class="chart">
                    <h3>Route Map</h3>
                    <iframe src="route_map.html" width="100%" height="400px"></iframe>
                </div>
            </div>

            <h3>Constructive Approach Routes</h3>
            <table>
                <tr>
                    <th>Route ID</th>
                    <th>Number of Deliveries</th>
                    <th>Distance</th>
                    <th>Points/Distance Ratio</th>
                </tr>
                {"".join(f"<tr><td>{i+1}</td><td>{r['point_count']}</td><td>{r['total_distance']:.2f}</td><td>{r['point_count']/r['total_distance']:.2f}</td></tr>"
                         for i, r in c["routes"].items())}
            </table>

            <h3>Deconstructive Approach Routes</h3>
            <table>
                <tr>
                    <th>Route ID</th>
                    <th>Number of Deliveries</th>
                    <th>Distance</th>
                    <th>Points/Distance Ratio</th>
                </tr>
                {"".join(f"<tr><td>{i+1}</td><td>{r['point_count']}</td><td>{r['total_distance']:.2f}</td><td>{r['point_count']/r['total_distance']:.2f}</td></tr>"
                         for i, r in d["routes"].items())}
            </table>

            <h2>Conclusion and Recommendation</h2>
            <p>
            {
                "Based on the analysis, the <strong>Deconstructive Approach</strong> is recommended as it provides "
                f"{'fewer routes' if d['optimal_k'] < c['optimal_k'] else 'more balanced routes'} "
                f"and {'lower total distance' if d['total_distance'] < c['total_distance'] else 'comparable efficiency'}."
                if d["total_distance"] < c["total_distance"] or d["optimal_k"] < c["optimal_k"] else
                "Based on the analysis, the <strong>Constructive Approach</strong> is recommended as it provides "
                f"{'fewer routes' if c['optimal_k'] < d['optimal_k'] else 'more balanced routes'} "
                f"and {'lower total distance' if c['total_distance'] < d['total_distance'] else 'comparable efficiency'}."
            }
            </p>

            <div class="explanation">
                <h3>Limitations and Future Improvements</h3>
                <ul>
                    <li><strong>Route Optimization:</strong> While the clustering is optimized using generalized Stirling numbers,
                    the actual route order within each cluster could be further improved with dedicated TSP solvers.</li>
                    <li><strong>Parameter Learning:</strong> The current parameter estimation is heuristic-based.
                    Future versions could use machine learning to predict optimal parameters based on historical data.</li>
                    <li><strong>Real-world Constraints:</strong> Additional constraints like vehicle capacity,
                    driver work hours, and traffic conditions could be incorporated for more realistic planning.</li>
                </ul>
            </div>

            <p>The dual-perspective analysis using generalized Stirling numbers demonstrates how viewing the same logistics
            problem from different angles can lead to operational improvements and cost savings.</p>

            <footer style="margin-top: 50px; border-top: 1px solid #ddd; padding-top: 20px; color: #777; font-size: 12px;">
                Generated using Generalized Stirling Framework.
                Find more examples at <a href="https://github.com/davidengland/generalized-factorials-stirling">github.com/davidengland/generalized-factorials-stirling</a>
            </footer>
        </body>
        </html>
        """

        with open("visualizations/delivery_report.html", "w") as f:
            f.write(html)


class DualPerspectiveOptimizer:
    """
    Main controller class for the dual-perspective optimization approach.
    Uses Generalized Stirling numbers to find optimal route configurations.
    """
    
    def __init__(self, data_path=None):
        """Initialize the optimizer with delivery data."""
        # Initialize components
        self.data_handler = DataHandler()
        self.data = self.data_handler.load_data(data_path) if data_path else None
        self.route_solver = RouteSolver(self.data)
        self.results = {"constructive": {}, "deconstructive": {}}

    def constructive_approach(self, min_vehicles=1, max_vehicles=None):
        """
        Implement the constructive approach - building routes from individual points.
        
        Args:
            min_vehicles: Minimum number of vehicles to consider
            max_vehicles: Maximum number of vehicles to consider

        Returns:
            Dictionary with optimization results
        """
        if self.data is None:
            logger.error("No data available for constructive approach")
            return None
            
        n = len(self.data)
        if max_vehicles is None:
            max_vehicles = n

        # Step 1: Estimate parameters
        a, b = StirlingOptimizer.estimate_parameters(self.data, "constructive")
        logger.info(f"Constructive parameters: a={a:.2f}, b={b:.2f}")
        
        # Step 2: Find optimal number of vehicles/routes
        k_opt, cost_opt, all_costs = StirlingOptimizer.find_optimal_k(n, a, b, min_vehicles, max_vehicles)
        logger.info(f"Optimal number of vehicles (constructive): {k_opt} with cost {cost_opt:.2f}")

        # Step 3: Assign delivery points to routes
        routes_dict = self.route_solver.constructive_approach(k_opt)

        # Step 4: Calculate route statistics
        routes = {}
        for i, indices in routes_dict.items():
            route_points = self.data.iloc[indices]
            
            # Optimize route using TSP
            ordered_indices = self.route_solver.optimize_route(indices, method="nearest_neighbor")
            
            # Calculate route distance (simple sum of point-to-point distances)
            total_distance = 0
            if len(ordered_indices) > 1:
                for j in range(len(ordered_indices)-1):
                    idx1, idx2 = ordered_indices[j], ordered_indices[j+1]
                    total_distance += self.route_solver.distance_matrix[idx1, idx2]
            
            routes[i] = {
                "point_count": len(route_points),
                "total_distance": total_distance,
                "points": route_points['id'].tolist(),
                "ordered_indices": ordered_indices
            }

        # Store results
        self.results["constructive"] = {
            "parameters": {"a": a, "b": b},
            "optimal_k": k_opt,
            "optimal_cost": cost_opt,
            "all_costs": all_costs,
            "routes": routes,
            "total_distance": sum(route["total_distance"] for route in routes.values())
        }

        return self.results["constructive"]

    def deconstructive_approach(self, min_vehicles=1, max_vehicles=None):
        """
        Implement the deconstructive approach - segmenting the delivery network.

        Args:
            min_vehicles: Minimum number of vehicles to consider
            max_vehicles: Maximum number of vehicles to consider
            
        Returns:
            Dictionary with optimization results
        """
        if self.data is None:
            logger.error("No data available for deconstructive approach")
            return None
            
        n = len(self.data)
        if max_vehicles is None:
            max_vehicles = n
            
        # Step 1: Estimate parameters for deconstructive approach
        a, b = StirlingOptimizer.estimate_parameters(self.data, "deconstructive")
        logger.info(f"Deconstructive parameters: a={a:.2f}, b={b:.2f}")
        
        # Step 2: Find optimal number of segments
        k_opt, cost_opt, all_costs = StirlingOptimizer.find_optimal_k(n, a, b, min_vehicles, max_vehicles)
        logger.info(f"Optimal number of vehicles (deconstructive): {k_opt} with cost {cost_opt:.2f}")

        # Step 3: Create network and find optimal segmentation
        routes_dict, G = self.route_solver.deconstructive_approach(k_opt)

        # Step 4: Calculate route statistics
        routes = {}
        for i, indices in routes_dict.items():
            route_points = self.data.iloc[indices]
            
            # Optimize route using TSP
            ordered_indices = self.route_solver.optimize_route(indices, method="nearest_neighbor")
            
            # Calculate route length using the ordered points
            total_distance = 0
            if len(ordered_indices) > 1:
                for j in range(len(ordered_indices)-1):
                    idx1, idx2 = ordered_indices[j], ordered_indices[j+1]
                    total_distance += self.route_solver.distance_matrix[idx1, idx2]
            
            routes[i] = {
                "point_count": len(route_points),
                "total_distance": total_distance,
                "points": route_points['id'].tolist(),
                "ordered_indices": ordered_indices
            }
        
        # Store results
        self.results["deconstructive"] = {
            "parameters": {"a": a, "b": b},
            "optimal_k": k_opt,
            "optimal_cost": cost_opt,
            "all_costs": all_costs,
            "routes": routes,
            "total_distance": sum(route["total_distance"] for route in routes.values()),
            "graph": G
        }

        return self.results["deconstructive"]
    
    def compare_approaches(self):
        """Compare results from both approaches."""
        if not self.results["constructive"] or not self.results["deconstructive"]:
            logger.error("Run both approaches first")
            return

        # Compare key metrics
        constructive = self.results["constructive"]
        deconstructive = self.results["deconstructive"]
        
        logger.info("\n=== Approach Comparison ===")
        logger.info(f"Constructive: {constructive['optimal_k']} routes, total distance: {constructive['total_distance']:.2f}")
        logger.info(f"Deconstructive: {deconstructive['optimal_k']} routes, total distance: {deconstructive['total_distance']:.2f}")
        
        # Calculate route balance (standard deviation of points per route)
        c_balance = np.std([r["point_count"] for r in constructive["routes"].values()])
        d_balance = np.std([r["point_count"] for r in deconstructive["routes"].values()])
        
        logger.info(f"Route balance (lower is better) - Constructive: {c_balance:.2f}, Deconstructive: {d_balance:.2f}")
        
        # Overall recommendation
        if deconstructive['total_distance'] < constructive['total_distance']:
            logger.info("\nRecommendation: Use the DECONSTRUCTIVE approach")
            if d_balance < c_balance:
                logger.info("Reason: Better route balance and lower total distance")
            else:
                logger.info("Reason: Lower total distance despite less balanced routes")
        else:
            logger.info("\nRecommendation: Use the CONSTRUCTIVE approach")
            if c_balance < d_balance:
                logger.info("Reason: Better route balance and comparable distance")
            else:
                logger.info("Reason: Lower total distance despite less balanced routes")
        
        # Create visualizations and report
        report_generator = ReportGenerator(self.data, self.results)
        graph = self.results["deconstructive"].get("graph") if "graph" in self.results["deconstructive"] else None
        report_generator.visualize_routes(graph)
    
    def save_results(self):
        """Save results to JSON file."""
        # Convert numpy values to native Python types for JSON serialization
        def convert_to_serializable(obj):
            if isinstance(obj, (np.int64, np.int32)):
                return int(obj)
            if isinstance(obj, (np.float64, np.float32)):
                return float(obj)
            if isinstance(obj, list):
                return [convert_to_serializable(item) for item in obj]
            if isinstance(obj, dict):
                return {k: convert_to_serializable(v) for k, v in obj.items()}
            if isinstance(obj, tuple) and len(obj) == 2:
                return [convert_to_serializable(obj[0]), convert_to_serializable(obj[1])]
            return obj
        
        # Remove non-serializable objects like the NetworkX graph
        results_copy = {
            "constructive": self.results["constructive"].copy(),
            "deconstructive": self.results["deconstructive"].copy()
        }
        
        if "graph" in results_copy["deconstructive"]:
            del results_copy["deconstructive"]["graph"]
        
        serializable_results = convert_to_serializable(results_copy)
        
        with open("results/optimization_results.json", "w") as f:
            json.dump(serializable_results, f, indent=2)
        
        logger.info("Results saved to results/optimization_results.json")


def generate_sample_data(n=50, seed=42):
    """Generate sample delivery data for testing."""
    np.random.seed(seed)

    # Generate locations in a city-like grid with some clusters
    centers = np.random.rand(5, 2) * 10  # 5 neighborhood centers

    lats = []
    longs = []
    for _ in range(n):
        # Pick a random center
        center = centers[np.random.randint(0, len(centers))]
        # Add noise to create points around the center
        lats.append(center[0] + np.random.normal(0, 0.5))
        longs.append(center[1] + np.random.normal(0, 0.5))

    # Generate other attributes
    package_sizes = np.random.randint(1, 10, size=n)  # 1-10 kg
    priorities = np.random.randint(1, 5, size=n)      # 1-5 priority levels

    # Generate time windows (8AM to 6PM)
    base_time = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
    time_windows_start = []
    time_windows_end = []

    for _ in range(n):
        start_hour = np.random.randint(0, 8)  # 8AM to 4PM
        window_length = np.random.randint(1, 4)  # 1-4 hour windows
        
        start_time = base_time + timedelta(hours=start_hour)
        end_time = start_time + timedelta(hours=window_length)
        
        time_windows_start.append(start_time)
        time_windows_end.append(end_time)

    # Create DataFrame
    df = pd.DataFrame({
        'id': range(1, n+1),
        'latitude': lats,
        'longitude': longs,
        'package_size': package_sizes,
        'delivery_priority': priorities,
        'time_window_start': time_windows_start,
        'time_window_end': time_windows_end
    })

    # Save to CSV
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/sample_deliveries.csv", index=False)
    print(f"Generated sample data with {n} delivery points at data/sample_deliveries.csv")

    return "data/sample_deliveries.csv"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Dual-Perspective Delivery Route Optimizer')
    parser.add_argument('--data', type=str, help='Path to delivery data CSV')
    parser.add_argument('--vehicles', type=str, default='1-15', help='Range of vehicles to consider (min-max)')
    parser.add_argument('--generate', type=int, help='Generate sample data with N points')
    parser.add_argument('--log', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'], default='INFO',
                       help='Set the logging level')
    
    args = parser.parse_args()
    
    # Set logging level
    logger.setLevel(getattr(logging, args.log))
    
    # Generate sample data if requested
    if args.generate:
        data_path = generate_sample_data(args.generate)
    else:
        data_path = args.data
    
    # Parse vehicle range
    if args.vehicles:
        min_v, max_v = map(int, args.vehicles.split('-'))
    else:
        min_v, max_v = 1, 15

    # Run optimization
    if data_path:
        optimizer = DualPerspectiveOptimizer(data_path)
        optimizer.constructive_approach(min_vehicles=min_v, max_vehicles=max_v)
        optimizer.deconstructive_approach(min_vehicles=min_v, max_vehicles=max_v)
        optimizer.compare_approaches()
        optimizer.save_results()

        logger.info("\nVisualization and report saved to 'visualizations/' directory")
    else:
        logger.error("No data provided. Use --data or --generate options.")
