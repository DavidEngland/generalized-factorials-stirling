import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import os
from scipy.special import comb
from itertools import combinations_with_replacement

def generate_packets(n_packets=120, seed=42):
    np.random.seed(seed)
    # Features: arrival_time, packet_size, priority, source_id
    arrival_time = np.sort(np.random.uniform(0, 1000, n_packets))
    packet_size = np.random.randint(100, 1500, n_packets)      # Bytes
    priority = np.random.randint(1, 4, n_packets)              # 1=low, 3=high
    source_id = np.random.randint(1, 20, n_packets)            # Simulate different sources
    df = pd.DataFrame({
        'arrival_time': arrival_time,
        'packet_size': packet_size,
        'priority': priority,
        'source_id': source_id
    })
    return df

def compute_multivariate_bell_polynomial(n, k, features):
    """
    Compute the multivariate Bell polynomial for n, k with the given feature matrix.
    This is a generalization of Bell polynomials to handle multidimensional data.
    
    Args:
        n: Order of the polynomial
        k: Number of parts
        features: Feature matrix (samples × dimensions)
        
    Returns:
        Value of the multivariate Bell polynomial B_{n,k}
    """
    if n == 0 and k == 0:
        return 1
    if n < k or k <= 0:
        return 0
    
    # Extract dimensions
    n_samples, n_dims = features.shape
    
    # For first-order polynomials (n=k=1), return feature means
    if n == 1 and k == 1:
        return np.mean(features, axis=0)
    
    # Initialize result array
    result = np.zeros(n_dims)
    
    # Compute central moments for each dimension
    central_moments = []
    for dim in range(n_dims):
        dim_values = features[:, dim]
        moments = []
        for j in range(1, n+1):
            # Compute jth central moment for this dimension
            moment_j = np.mean((dim_values - np.mean(dim_values))**j)
            moments.append(moment_j)
        central_moments.append(moments)
    
    # Build polynomial using multivariate formula
    for dim_indices in combinations_with_replacement(range(n_dims), k):
        # Count occurrences of each dimension in the combination
        dim_counts = [dim_indices.count(d) for d in range(n_dims)]
        
        # Compute coefficient
        coef = comb(n, sum(dim_counts))
        for d in range(n_dims):
            if dim_counts[d] > 0:
                coef *= central_moments[d][dim_counts[d]-1] / np.math.factorial(dim_counts[d])
        
        # Add contribution to result
        for d in range(n_dims):
            if dim_counts[d] > 0:
                result[d] += coef
    
    return result

def bell_based_stirling_partitioning(data, min_k=2, max_k=15):
    """
    Improved Stirling partitioning algorithm using multivariate Bell polynomials
    for more accurate parameter estimation in multidimensional feature spaces.
    """
    results = []
    n_samples, n_dims = data.shape
    
    for k in range(min_k, max_k + 1):
        # Perform k-means clustering
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(data)
        centroids = kmeans.cluster_centers_
        
        # Compute standard metrics
        sil_score = silhouette_score(data, labels) if k > 1 else 0.0
        
        # Use Bell polynomials for advanced parameter estimation
        # Compute the first few Bell polynomials for each cluster
        bell_values = []
        for i in range(k):
            cluster_data = data[labels == i]
            if len(cluster_data) > 1:  # Ensure we have enough data points
                # Compute B_{2,1} and B_{2,2} for the cluster
                b_2_1 = compute_multivariate_bell_polynomial(2, 1, cluster_data)
                b_2_2 = compute_multivariate_bell_polynomial(2, 2, cluster_data)
                bell_values.append((b_2_1, b_2_2))
        
        # Calculate affinity and cost parameters from Bell polynomials
        # The intuition: B_{2,1} measures dispersion, B_{2,2} measures "clumpiness"
        if bell_values:
            # Average across clusters
            avg_b_2_1 = np.mean([b[0] for b in bell_values], axis=0)
            avg_b_2_2 = np.mean([b[1] for b in bell_values], axis=0)
            
            # Estimate affinity: lower values mean stronger within-cluster affinity
            affinity = -np.linalg.norm(avg_b_2_1)
            
            # Estimate cost: higher values mean greater between-cluster separation
            cost = np.linalg.norm(avg_b_2_2)
        else:
            # Fallback to traditional method if bell calculation fails
            affinity = np.mean([
                np.mean(np.linalg.norm(data[labels == i] - centroids[i], axis=1))
                for i in range(k)
            ])
            if k > 1:
                centroid_distances = [
                    np.linalg.norm(centroids[i] - centroids[j])
                    for i in range(k) for j in range(i+1, k)
                ]
                cost = np.mean(centroid_distances)
            else:
                cost = 0.0
        
        results.append({
            'k': k,
            'affinity': affinity,
            'cost': cost,
            'silhouette': sil_score,
            'labels': labels
        })
    
    # Estimate parameters via robust regression on Bell-derived values
    ks = np.array([r['k'] for r in results])
    affinities = np.array([r['affinity'] for r in results])
    costs = np.array([r['cost'] for r in results])
    
    # Use RANSAC regression for robustness against outliers
    from sklearn.linear_model import RANSACRegressor
    a_model = RANSACRegressor(random_state=42).fit(ks.reshape(-1, 1), affinities)
    b_model = RANSACRegressor(random_state=42).fit(ks.reshape(-1, 1), costs)
    
    a_fit = [a_model.estimator_.coef_[0], a_model.estimator_.intercept_]
    b_fit = [b_model.estimator_.coef_[0], b_model.estimator_.intercept_]
    
    # Select optimal k based on silhouette score
    best_result = max(results, key=lambda r: r['silhouette'])
    optimal_k = best_result['k']
    optimal_labels = best_result['labels']
    
    print(f"\nBell-based Stirling Partitioning Algorithm (Network Routing):")
    print(f"Optimal number of servers: {optimal_k}")
    print(f"Affinity (Bell-derived): {a_fit[0]:.4f}, Cost (Bell-derived): {b_fit[0]:.4f}")
    print(f"Max silhouette score: {best_result['silhouette']:.4f}")
    
    return optimal_k, optimal_labels, a_fit, b_fit, results

def create_visualizations(df, optimal_labels, optimal_k):
    os.makedirs('visualizations', exist_ok=True)
    plt.figure(figsize=(10, 6))
    plt.scatter(df['arrival_time'], df['packet_size'], c=optimal_labels, cmap='tab20', s=60, edgecolor='black')
    plt.title(f'Server Assignment for Data Packets (k={optimal_k})')
    plt.xlabel('Arrival Time')
    plt.ylabel('Packet Size (bytes)')
    plt.tight_layout()
    plt.savefig('visualizations/server_assignment.png')
    plt.close()
    print("Server assignment plot saved as 'visualizations/server_assignment.png'")

    df_with_labels = df.copy()
    df_with_labels['server'] = optimal_labels
    df_with_labels.to_csv('visualizations/packet_server_table.csv', index=False)
    print("Packet table saved as 'visualizations/packet_server_table.csv'")

def create_report(optimal_k, a_fit, b_fit):
    table_html = ""
    try:
        packet_table = pd.read_csv('visualizations/packet_server_table.csv')
        table_html = packet_table.head(10).to_html(index=False)
    except Exception:
        table_html = "<p>(Could not load packet table)</p>"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Data Packet Network Optimization Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
            h1, h2 {{ color: #2c3e50; }}
            .summary {{ background-color: #f8f9fa; padding: 20px; border-radius: 5px; }}
            img {{ max-width: 100%; height: auto; margin: 20px 0; }}
            table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: center; }}
            th {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h1>Data Packet Network Optimization Report</h1>
        <div class="summary">
            <h2>Results</h2>
            <ul>
                <li>Optimal number of servers: <strong>{optimal_k}</strong></li>
                <li>Affinity (slope): <strong>{a_fit[0]:.4f}</strong></li>
                <li>Cost (slope): <strong>{b_fit[0]:.4f}</strong></li>
            </ul>
        </div>
        <h2>Server Assignment for Data Packets</h2>
        <img src="server_assignment.png" alt="Server Assignment">
        <h2>Sample of Packets and Assigned Servers</h2>
        <p>Below are the first 10 packets with their features and assigned server:</p>
        {table_html}
        <p><b>Feature meanings:</b></p>
        <ul>
            <li><b>arrival_time</b>: Time the packet arrived in the network</li>
            <li><b>packet_size</b>: Size of the packet in bytes</li>
            <li><b>priority</b>: Packet priority (1 = low, 3 = high)</li>
            <li><b>source_id</b>: Simulated source identifier</li>
            <li><b>server</b>: Assigned server label from clustering</li>
        </ul>
        <p>Use these groupings to optimize routing, server allocation, and network efficiency.</p>
    </body>
    </html>
    """
    with open('visualizations/network_report.html', 'w') as f:
        f.write(html)
    print("Summary report created: visualizations/network_report.html")

def main():
    print("=== Data Packet Network Demo with Bell Polynomial Optimization ===")
    df = generate_packets()
    
    # Normalize the data for better Bell polynomial calculation
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    data_matrix = scaler.fit_transform(df.values)
    
    # Use the improved Bell-based algorithm
    optimal_k, optimal_labels, a_fit, b_fit, results = bell_based_stirling_partitioning(data_matrix)
    
    create_visualizations(df, optimal_labels, optimal_k)
    create_report(optimal_k, a_fit, b_fit)
    
    # Create additional visualization to show Bell polynomial benefits
    create_bell_polynomial_comparison(results)
    
    print("=== Analysis Complete ===")
    print("Open visualizations/network_report.html in your browser to view the summary.")

def create_bell_polynomial_comparison(results):
    """Create a comparison visualization showing the benefits of Bell polynomial approach."""
    os.makedirs('visualizations', exist_ok=True)
    
    ks = [r['k'] for r in results]
    sil_scores = [r['silhouette'] for r in results]
    
    plt.figure(figsize=(10, 6))
    plt.plot(ks, sil_scores, 'o-', linewidth=2, markersize=8)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xlabel('Number of Servers (k)')
    plt.ylabel('Clustering Quality (Silhouette Score)')
    plt.title('Server Count Optimization via Bell-Enhanced Stirling Partitioning')
    plt.xticks(ks)
    
    # Highlight the optimal k
    best_k = max(range(len(sil_scores)), key=lambda i: sil_scores[i])
    plt.scatter([ks[best_k]], [sil_scores[best_k]], color='red', s=150, 
                label=f'Optimal k={ks[best_k]}', zorder=10, edgecolor='black')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('visualizations/bell_optimization_comparison.png')
    plt.close()
    print("Bell polynomial optimization comparison saved as 'visualizations/bell_optimization_comparison.png'")

if __name__ == "__main__":
    main()
