import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import os

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

def stirling_partitioning_algorithm(data, min_k=2, max_k=15):
    results = []
    for k in range(min_k, max_k + 1):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(data)
        centroids = kmeans.cluster_centers_
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
        sil_score = silhouette_score(data, labels) if k > 1 else 0.0
        results.append({
            'k': k,
            'affinity': affinity,
            'cost': cost,
            'silhouette': sil_score,
            'labels': labels
        })
    ks = np.array([r['k'] for r in results])
    affinities = np.array([r['affinity'] for r in results])
    costs = np.array([r['cost'] for r in results])
    a_fit = np.polyfit(ks, affinities, 1)
    b_fit = np.polyfit(ks, costs, 1)
    best_result = max(results, key=lambda r: r['silhouette'])
    optimal_k = best_result['k']
    optimal_labels = best_result['labels']
    print(f"\nStirling Partitioning Algorithm (Network Routing):")
    print(f"Optimal number of servers: {optimal_k}")
    print(f"Affinity (slope): {a_fit[0]:.4f}, Cost (slope): {b_fit[0]:.4f}")
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
    print("=== Data Packet Network Demo ===")
    df = generate_packets()
    data_matrix = df.values
    optimal_k, optimal_labels, a_fit, b_fit, results = stirling_partitioning_algorithm(data_matrix)
    create_visualizations(df, optimal_labels, optimal_k)
    create_report(optimal_k, a_fit, b_fit)
    print("=== Analysis Complete ===")
    print("Open visualizations/network_report.html in your browser to view the summary.")

if __name__ == "__main__":
    main()
