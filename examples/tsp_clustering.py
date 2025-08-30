"""
Traveling Salesman Problem optimization using generalized Stirling parameters.

This approach uses (a,b)-generalized Stirling transforms to:
1. Identify natural clusters in the TSP graph
2. Optimize paths within clusters
3. Connect clusters efficiently

The key insight is that the (a,b) parameters naturally model:
- a: cohesion parameter (attraction within clusters)
- b: barrier parameter (separation between clusters)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb
import networkx as nx
from itertools import permutations
from sklearn.cluster import KMeans

def bell_polynomial_moment(points, k, a, b):
    """Compute the k-th moment using Bell polynomials with (a,b) parameters"""
    n = len(points)
    distances = np.zeros((n, n))
    
    # Compute pairwise distances
    for i in range(n):
        for j in range(i+1, n):
            distances[i, j] = distances[j, i] = np.linalg.norm(
                np.array(points[i]) - np.array(points[j])
            )
    
    # Apply (a,b)-weighted transformation using the generalized factorial basis
    transformed = np.zeros_like(distances)
    for i in range(n):
        for j in range(n):
            if i != j:
                # Apply the generalized Stirling transform
                d = distances[i, j]
                # Internal cohesion term (controlled by a)
                cohesion = a * np.exp(-d / (k+1))
                # Barrier term (controlled by b)
                barrier = b * (1 - np.exp(-d / (k+1)))
                transformed[i, j] = cohesion - barrier
    
    return transformed

def identify_clusters(points, a=0.5, b=1.0, n_clusters=None):
    """Identify natural clusters using (a,b)-weighted moments"""
    # Compute the transformed distance matrix
    transformed = bell_polynomial_moment(points, 2, a, b)
    
    # Create a graph from the transformed distances
    G = nx.Graph()
    n = len(points)
    for i in range(n):
        G.add_node(i, pos=points[i])
    
    # Add edges with weights from the transformed matrix
    for i in range(n):
        for j in range(i+1, n):
            weight = max(0.001, transformed[i, j])  # Ensure positive weights
            G.add_edge(i, j, weight=weight)
    
    # Determine optimal number of clusters if not specified
    if n_clusters is None:
        # Use spectral properties of the Laplacian to estimate clusters
        laplacian = nx.normalized_laplacian_matrix(G).todense()
        eigenvalues = np.linalg.eigvalsh(laplacian)
        # Eigengap heuristic
        gaps = np.diff(eigenvalues)
        n_clusters = np.argmax(gaps) + 1
        n_clusters = max(2, min(n_clusters, int(np.sqrt(n))))
    
    # Apply KMeans to cluster the points
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(points)
    
    return clusters, G

def solve_tsp_within_cluster(points, cluster_indices):
    """Solve TSP exactly within a small cluster"""
    if len(cluster_indices) <= 1:
        return cluster_indices
    
    # Extract the points in this cluster
    cluster_points = [points[i] for i in cluster_indices]
    
    # Compute pairwise distances
    n = len(cluster_points)
    distances = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            distances[i, j] = distances[j, i] = np.linalg.norm(
                np.array(cluster_points[i]) - np.array(cluster_points[j])
            )
    
    # Brute force for small clusters
    if n <= 10:
        best_distance = float('inf')
        best_path = None
        
        for path in permutations(range(n)):
            distance = 0
            for i in range(n-1):
                distance += distances[path[i], path[i+1]]
            distance += distances[path[-1], path[0]]  # Return to start
            
            if distance < best_distance:
                best_distance = distance
                best_path = path
        
        return [cluster_indices[i] for i in best_path]
    
    # For larger clusters, use a greedy approach
    else:
        path = [0]
        unvisited = set(range(1, n))
        
        while unvisited:
            current = path[-1]
            next_node = min(unvisited, key=lambda x: distances[current, x])
            path.append(next_node)
            unvisited.remove(next_node)
        
        return [cluster_indices[i] for i in path]

def optimize_tsp_with_stirling(points, a=0.5, b=1.0, n_clusters=None):
    """Optimize TSP using (a,b)-generalized Stirling parameters for clustering"""
    # Step 1: Identify clusters using the (a,b) parameters
    clusters, G = identify_clusters(points, a, b, n_clusters)
    
    # Get the unique cluster labels
    unique_clusters = np.unique(clusters)
    
    # Step 2: Solve TSP within each cluster
    cluster_paths = []
    cluster_centroids = []
    
    for cluster_id in unique_clusters:
        # Get indices of points in this cluster
        cluster_indices = np.where(clusters == cluster_id)[0]
        
        # Solve TSP within this cluster
        cluster_path = solve_tsp_within_cluster(points, cluster_indices)
        cluster_paths.append(cluster_path)
        
        # Compute centroid for this cluster
        cluster_points = np.array([points[i] for i in cluster_indices])
        centroid = np.mean(cluster_points, axis=0)
        cluster_centroids.append(centroid)
    
    # Step 3: Connect clusters using a simplified TSP on centroids
    centroid_order = solve_tsp_within_cluster(cluster_centroids, list(range(len(cluster_centroids))))
    
    # Step 4: Construct the final path by connecting clusters
    final_path = []
    for cluster_idx in centroid_order:
        path = cluster_paths[cluster_idx]
        # Connect in the direction that minimizes distance between clusters
        if final_path:
            # Check if we should reverse the path for better connection
            last_point = points[final_path[-1]]
            first_in_path = points[path[0]]
            last_in_path = points[path[-1]]
            
            if (np.linalg.norm(last_point - last_in_path) < 
                np.linalg.norm(last_point - first_in_path)):
                path = path[::-1]  # Reverse path for better connection
        
        final_path.extend(path)
    
    return final_path, clusters, G

def plot_tsp_solution(points, path, clusters=None, G=None):
    """Plot the TSP solution with optional cluster visualization"""
    plt.figure(figsize=(12, 10))
    
    # Plot the points and path
    path_points = [points[i] for i in path] + [points[path[0]]]  # Close the loop
    x, y = zip(*path_points)
    
    if clusters is not None:
        # Plot points colored by cluster
        unique_clusters = np.unique(clusters)
        colors = plt.cm.rainbow(np.linspace(0, 1, len(unique_clusters)))
        
        for i, cluster_id in enumerate(unique_clusters):
            cluster_indices = np.where(clusters == cluster_id)[0]
            cluster_points = np.array([points[j] for j in cluster_indices])
            plt.scatter(cluster_points[:, 0], cluster_points[:, 1], 
                        color=colors[i], s=100, alpha=0.7, label=f'Cluster {cluster_id}')
    else:
        # Plot all points in a single color
        all_points = np.array(points)
        plt.scatter(all_points[:, 0], all_points[:, 1], c='blue', s=100, alpha=0.7)
    
    # Plot the path
    plt.plot(x, y, 'r-', linewidth=2, alpha=0.7)
    
    # Add node indices
    for i, (x, y) in enumerate(points):
        plt.text(x, y, str(i), fontsize=12, ha='center', va='center', 
                 bbox=dict(facecolor='white', alpha=0.7))
    
    # Compute total distance
    total_distance = 0
    for i in range(len(path)):
        total_distance += np.linalg.norm(
            np.array(points[path[i]]) - np.array(points[path[(i+1) % len(path)]])
        )
    
    plt.title(f'TSP Solution with Distance: {total_distance:.2f}')
    if clusters is not None:
        plt.legend()
    
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    # Optionally plot the graph
    if G is not None:
        plt.figure(figsize=(10, 8))
        pos = nx.get_node_attributes(G, 'pos')
        
        # Draw nodes colored by cluster
        if clusters is not None:
            node_colors = [colors[clusters[i]] for i in range(len(points))]
            nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=100)
        else:
            nx.draw_networkx_nodes(G, pos, node_color='blue', node_size=100)
        
        # Draw edges with weights reflected in width and transparency
        edge_weights = [G[u][v]['weight'] for u, v in G.edges()]
        max_weight = max(edge_weights)
        edge_widths = [3 * (w / max_weight) for w in edge_weights]
        edge_alphas = [0.3 + 0.7 * (w / max_weight) for w in edge_weights]
        
        for i, (u, v) in enumerate(G.edges()):
            nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], 
                                   width=edge_widths[i], 
                                   alpha=edge_alphas[i])
        
        plt.title('Weighted Graph Representation')
        plt.axis('off')
        plt.tight_layout()
        plt.show()

def demonstrate_parameter_effects():
    """Demonstrate how different (a,b) parameters affect clustering and TSP solutions"""
    # Generate a random TSP instance with natural clusters
    np.random.seed(42)
    n_clusters = 4
    points_per_cluster = 10
    points = []
    
    # Create clustered points
    centers = [(np.random.rand() * 100, np.random.rand() * 100) for _ in range(n_clusters)]
    
    for center in centers:
        for _ in range(points_per_cluster):
            point = (center[0] + np.random.randn() * 5, 
                     center[1] + np.random.randn() * 5)
            points.append(point)
    
    # Test different parameter values
    parameter_sets = [
        (0.0, 1.0, "Barrier-only (b=1, classical Stirling 2nd kind)"),
        (1.0, 0.0, "Cohesion-only (a=1, classical Stirling 1st kind)"),
        (0.0, 0.5, "Half-barrier (hyperbolic strip, b=0.5)"),
        (0.0, -0.5, "Negative half-barrier (hyperbolic strip, b=-0.5)"),
        (0.5, 0.5, "Balanced (a=b=0.5)"),
        (1.0, 1.0, "Lah numbers (a=b=1)"),
    ]
    
    for a, b, title in parameter_sets:
        print(f"\nTesting parameters: {title}")
        path, clusters, G = optimize_tsp_with_stirling(points, a, b)
        
        # Calculate path length
        total_distance = 0
        for i in range(len(path)):
            j = (i + 1) % len(path)
            total_distance += np.linalg.norm(
                np.array(points[path[i]]) - np.array(points[path[j]])
            )
        
        print(f"Total path length: {total_distance:.2f}")
        print(f"Unique clusters identified: {len(np.unique(clusters))}")
        
        # Plot the result
        plt.figure(figsize=(10, 8))
        plot_tsp_solution(points, path, clusters, G)
        plt.suptitle(f"TSP Solution with {title}", fontsize=16)
        plt.tight_layout()
        plt.subplots_adjust(top=0.9)
        plt.savefig(f"tsp_solution_{a}_{b}.png")
        plt.close()

if __name__ == "__main__":
    # Demonstrate the effects of different (a,b) parameters on TSP solutions
    demonstrate_parameter_effects()
    
    # Additional example: Solve a specific TSP instance with custom parameters
    np.random.seed(123)
    points = [(np.random.rand() * 100, np.random.rand() * 100) for _ in range(30)]
    
    # Optimize using the hyperbolic strip case (a=0, b=0.5)
    path, clusters, G = optimize_tsp_with_stirling(points, a=0, b=0.5)
    plot_tsp_solution(points, path, clusters, G)
