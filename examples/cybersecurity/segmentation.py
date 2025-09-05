import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def generalized_stirling(n, k, a, b):
    """
    Calculates the generalized Stirling number S_{n,k}(a,b) using dynamic programming.
    This number represents the total cost of partitioning n hosts into k segments.

    Parameters:
        n (int): The total number of hosts.
        k (int): The number of network segments.
        a (float): The affinity parameter (cost per host to be secured).
        b (float): The barrier parameter (cost per new segment created).

    Returns:
        float: The generalized Stirling number, representing the total cost.
    """
    # Handle base and edge cases
    if k > n or k <= 0:
        return 0
    if n == 0:
        return 1 if k == 0 else 0

    # Initialize a table for dynamic programming
    dp = np.zeros((n + 1, k + 1), dtype=float)

    # Base case: one way to partition an empty set into zero segments.
    dp[0, 0] = 1

    # Fill the table using the recurrence relation:
    # S_{i,j}(a,b) = S_{i-1,j-1}(a,b) + (a(i-1) + bj)S_{i-1,j}(a,b)
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i, j] = dp[i - 1, j - 1] + (a * (i - 1) + b * j) * dp[i - 1, j]

    return dp[n, k]

def find_optimal_k(n, a, b):
    """
    Finds the optimal number of segments (k) that minimizes the total cost.

    Parameters:
        n (int): The total number of hosts.
        a (float): The affinity cost per host.
        b (float): The barrier cost per segment.

    Returns:
        tuple: A tuple containing the optimal k and the minimum cost.
    """
    # Calculate the cost for each possible number of segments (from 1 to n)
    costs = [generalized_stirling(n, k, a, b) for k in range(1, n + 1)]

    # Find the index of the minimum cost, and add 1 to get the optimal k
    if not costs:
        return 0, 0
    optimal_k = np.argmin(costs) + 1
    min_cost = costs[optimal_k - 1]

    return optimal_k, min_cost

def plot_cost_curve(n, a, b):
    """
    Generates a plot of the total cost versus the number of segments.
    """
    k_values = list(range(1, n + 1))
    costs = [generalized_stirling(n, k, a, b) for k in k_values]

    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(10, 6))
    plt.plot(k_values, costs, 'o-', color='navy', linewidth=2, markersize=8)
    plt.xlabel('Number of Network Segments (k)', fontsize=12)
    plt.ylabel('Total Cost', fontsize=12)
    plt.title(f'Network Segmentation Cost for {n} Hosts (a={a}, b={b})', fontsize=14)

    # Find and mark the optimal k on the plot
    optimal_k, min_cost = find_optimal_k(n, a, b)
    plt.plot(optimal_k, min_cost, 'ro', markersize=12, label=f'Optimal: k={optimal_k}')
    plt.annotate(f'Optimal k={optimal_k}\nCost={min_cost:.2f}',
                 xy=(optimal_k, min_cost),
                 xytext=(optimal_k + n * 0.05, min_cost * 1.1),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 fontsize=10)

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def generate_network_visualization(n, optimal_k):
    """
    Visualizes the network before and after segmentation.
    """
    # Create a simple connected network of n nodes
    G_original = nx.complete_graph(n)

    # Create the segmented network
    G_segmented = nx.Graph()
    segments = [[] for _ in range(optimal_k)]

    # Assign nodes to segments
    for i in range(n):
        segment_index = i % optimal_k
        segments[segment_index].append(i)
        G_segmented.add_node(i)

    # Add edges within each segment
    for segment in segments:
        for i, node1 in enumerate(segment):
            for node2 in segment[i+1:]:
                G_segmented.add_edge(node1, node2)

    # Plot the networks
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    # Plot original network
    pos_original = nx.spring_layout(G_original, seed=42)
    nx.draw_networkx_nodes(G_original, pos_original, node_size=150, ax=ax1, node_color='lightcoral')
    nx.draw_networkx_edges(G_original, pos_original, ax=ax1, alpha=0.5)
    ax1.set_title(f"Original Network ({n} Hosts)", fontsize=14)
    ax1.axis('off')

    # Plot segmented network
    pos_segmented = nx.spring_layout(G_segmented, seed=42)
    colors = plt.cm.get_cmap('tab10', optimal_k)
    node_colors = [colors(i % optimal_k) for i in range(n)]

    nx.draw_networkx_nodes(G_segmented, pos_segmented, node_size=150, ax=ax2, node_color=node_colors)
    nx.draw_networkx_edges(G_segmented, pos_segmented, ax=ax2, alpha=0.5)
    ax2.set_title(f"Segmented Network ({optimal_k} Segments)", fontsize=14)
    ax2.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Define a scenario: A medium-sized company network
    n = 25  # Number of hosts
    a = 5   # Cost of securing a single host
    b = 10  # Cost of creating a new network segment

    # Find the optimal number of segments
    optimal_k, min_cost = find_optimal_k(n, a, b)
    print(f"For a network of {n} hosts with per-host cost a={a} and per-segment cost b={b}:")
    print(f"Optimal number of segments (k): {optimal_k}")
    print(f"Minimum total cost: {min_cost:.2f}")

    # Generate the plots
    plot_cost_curve(n, a, b)
    generate_network_visualization(n, optimal_k)

    print("\n--- Scenario Comparison ---")
    print(f"{'Scenario':<20} {'Optimal k':<15} {'Total Cost':<15}")
    print("-" * 50)

    # Compare different scenarios with varying costs
    scenarios = [
        {"name": "Low Barrier (Cloud)", "a": 5, "b": 2},
        {"name": "Balanced (Hybrid)", "a": 5, "b": 10},
        {"name": "High Barrier (On-Prem)", "a": 5, "b": 50},
    ]

    for scenario in scenarios:
        opt_k, cost = find_optimal_k(n, scenario["a"], scenario["b"])
        print(f"{scenario['name']:<20} {opt_k:<15} {cost:<15.2f}")
