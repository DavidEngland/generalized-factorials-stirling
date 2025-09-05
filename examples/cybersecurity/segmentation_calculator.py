import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from mpl_toolkits.mplot3d import Axes3D

def generalized_stirling(n, k, a, b):
    """
    Calculate generalized Stirling numbers S_{n,k}(a,b) using dynamic programming.
    
    Parameters:
        n (int): Number of elements (hosts)
        k (int): Number of partitions (network segments)
        a (float): Affinity parameter (cost to clean each host)
        b (float): Barrier parameter (cost to create a segment)
        
    Returns:
        float: The generalized Stirling number S_{n,k}(a,b)
    """
    # Handle base cases
    if k == 0:
        return 1 if n == 0 else 0
    if k > n or k == 0:
        return 0
    
    # Create table for dynamic programming
    dp = np.zeros((n+1, k+1), dtype=float)
    
    # Base case
    dp[0, 0] = 1
    
    # Fill table using recurrence relation
    for i in range(1, n+1):
        for j in range(1, min(i+1, k+1)):
            dp[i, j] = dp[i-1, j-1] + (a*(i-1) + b*j) * dp[i-1, j]
    
    return dp[n, k]

def find_optimal_k(n, a, b, max_k=None):
    """
    Find the optimal number of segments that minimizes total cost.
    
    Parameters:
        n (int): Number of hosts
        a (float): Affinity cost
        b (float): Barrier cost
        max_k (int): Maximum number of segments to consider
        
    Returns:
        tuple: (optimal_k, minimum_cost)
    """
    if max_k is None:
        max_k = n
    
    costs = [generalized_stirling(n, k, a, b) for k in range(1, min(n, max_k) + 1)]
    optimal_k = np.argmin(costs) + 1
    return optimal_k, costs[optimal_k - 1]

def plot_cost_curve(n, a, b, max_k=None):
    """
    Plot the cost curve for different numbers of segments.
    """
    if max_k is None:
        max_k = n
    
    k_values = list(range(1, min(n, max_k) + 1))
    costs = [generalized_stirling(n, k, a, b) for k in k_values]
    
    plt.figure(figsize=(10, 6))
    plt.plot(k_values, costs, 'o-', linewidth=2)
    plt.xlabel('Number of Network Segments (k)')
    plt.ylabel(f'Total Cost S_{{{n},k}}({a},{b})')
    plt.title(f'Network Segmentation Cost for {n} Hosts')
    plt.grid(True)
    
    # Find and mark the optimal k
    optimal_k = np.argmin(costs) + 1
    plt.plot(optimal_k, costs[optimal_k - 1], 'ro', markersize=10)
    plt.annotate(f'Optimal: k={optimal_k}',
                xy=(optimal_k, costs[optimal_k - 1]),
                xytext=(optimal_k + 0.5, costs[optimal_k - 1] * 1.1),
                arrowprops=dict(facecolor='black', shrink=0.05))
    
    return plt

def generate_network_visualization(n, k):
    """
    Generate a visualization of network before and after segmentation.
    """
    # Create original network (fully connected for simplicity)
    G_original = nx.grid_2d_graph(5, 4)
    
    # Create segmented network
    G_segmented = nx.Graph()
    
    # Distribute nodes into k segments
    nodes_per_segment = n // k
    remainder = n % k
    
    current_node = 0
    segments = []
    
    for i in range(k):
        segment_size = nodes_per_segment + (1 if i < remainder else 0)
        segment = list(range(current_node, current_node + segment_size))
        segments.append(segment)
        current_node += segment_size
        
        # Create connections within segment
        for node in segment:
            G_segmented.add_node(node)
            for other_node in segment:
                if node != other_node:
                    G_segmented.add_edge(node, other_node)
    
    # Plot the networks
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    pos_original = {node: node for node in G_original.nodes()}
    nx.draw(G_original, pos_original, ax=ax1, with_labels=False, node_color='skyblue', 
            node_size=100, font_size=10)
    ax1.set_title(f"Original Network (n={n})")
    
    # Use different colors for different segments
    colors = plt.cm.rainbow(np.linspace(0, 1, k))
    node_colors = []
    for node in G_segmented.nodes():
        for i, segment in enumerate(segments):
            if node in segment:
                node_colors.append(colors[i])
                break
    
    pos_segmented = nx.spring_layout(G_segmented, seed=42)
    nx.draw(G_segmented, pos_segmented, ax=ax2, with_labels=False, 
            node_color=node_colors, node_size=100, font_size=10)
    ax2.set_title(f"Segmented Network (k={k})")
    
    return fig

if __name__ == "__main__":
    # Example scenario
    n = 20  # Number of hosts
    a = 4   # Cost to clean each host
    b = 6   # Cost to create a segment
    
    # Find optimal number of segments
    optimal_k, min_cost = find_optimal_k(n, a, b)
    print(f"For {n} hosts with a={a}, b={b}:")
    print(f"Optimal number of segments: {optimal_k}")
    print(f"Minimum total cost: {min_cost:.2f}")
    
    # Plot cost curve
    cost_plot = plot_cost_curve(n, a, b)
    cost_plot.savefig("segmentation_cost_curve.png")
    
    # Generate network visualization
    network_plot = generate_network_visualization(n, optimal_k)
    network_plot.tight_layout()
    network_plot.savefig("network_segmentation.png")
    
    print("Plots saved. Analyzing different scenarios...")
    
    # Compare different scenarios
    scenarios = [
        {"name": "Cloud-native", "a": 2, "b": 3},
        {"name": "Hybrid", "a": 4, "b": 6},
        {"name": "On-premises", "a": 9, "b": 12}
    ]
    
    print("\nScenario Comparison:")
    print("-" * 60)
    print(f"{'Scenario':<15} {'Optimal k':<10} {'Total Cost':<15} {'Avg Cost/Host':<15}")
    print("-" * 60)
    
    for scenario in scenarios:
        opt_k, cost = find_optimal_k(n, scenario["a"], scenario["b"])
        print(f"{scenario['name']:<15} {opt_k:<10} {cost:<15.2f} {cost/n:<15.2f}")
    
    plt.show()
