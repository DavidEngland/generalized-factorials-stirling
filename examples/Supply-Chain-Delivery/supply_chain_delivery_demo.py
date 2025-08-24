import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import os

# --- Data Generation ---
# This function generates a synthetic dataset representing delivery orders.
# Each order has a 2D location, a package size, and an urgency level.
def generate_orders(n_orders=100, seed=42):
    """
    Generates synthetic delivery order data.

    Args:
        n_orders (int): The number of orders to generate.
        seed (int): A seed for reproducibility.

    Returns:
        pd.DataFrame: A DataFrame containing the generated order data.
    """
    np.random.seed(seed)
    # Features: location_x, location_y, size, urgency
    location_x = np.random.uniform(0, 100, n_orders)
    location_y = np.random.uniform(0, 100, n_orders)
    size = np.random.randint(1, 10, n_orders)         # Package size
    urgency = np.random.randint(1, 4, n_orders)       # 1=low, 3=high
    df = pd.DataFrame({
        'location_x': location_x,
        'location_y': location_y,
        'size': size,
        'urgency': urgency
    })
    return df

# --- Stirling Partitioning Algorithm ---
# This function implements the core logic of the Stirling-based clustering.
# It iterates through a range of clusters (k), measures the "affinity" (internal cohesion)
# and "cost" (external separation), and finds the optimal k using the silhouette score.
def stirling_partitioning_algorithm(data, min_k=2, max_k=12):
    """
    Applies the Stirling Partitioning Algorithm to find the optimal number of clusters.

    Args:
        data (pd.DataFrame): The input data for clustering.
        min_k (int): The minimum number of clusters to test.
        max_k (int): The maximum number of clusters to test.

    Returns:
        tuple: A tuple containing the optimal k, optimal labels, fitted parameters, and all results.
    """
    results = []
    for k in range(min_k, max_k + 1):
        # Use KMeans for clustering at each k
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(data)
        centroids = kmeans.cluster_centers_

        # Calculate "affinity" as the average distance from points to their cluster centroid
        affinity = np.mean([
            np.mean(np.linalg.norm(data[labels == i] - centroids[i], axis=1))
            for i in range(k)
        ])

        # Calculate "cost" as the average distance between cluster centroids
        if k > 1:
            centroid_distances = [
                np.linalg.norm(centroids[i] - centroids[j])
                for i in range(k) for j in range(i + 1, k)
            ]
            cost = np.mean(centroid_distances)
        else:
            cost = 0.0

        # Use silhouette score to evaluate clustering quality (higher is better)
        sil_score = silhouette_score(data, labels) if k > 1 else 0.0
        
        results.append({
            'k': k,
            'affinity': affinity,
            'cost': cost,
            'silhouette': sil_score,
            'labels': labels
        })

    # Find the best result based on the highest silhouette score
    best_result = max(results, key=lambda r: r['silhouette'])
    optimal_k = best_result['k']
    optimal_labels = best_result['labels']

    # Use linear regression to find the a and b parameters
    ks = np.array([r['k'] for r in results])
    affinities = np.array([r['affinity'] for r in results])
    costs = np.array([r['cost'] for r in results])
    a_fit = np.polyfit(ks, affinities, 1)  # Parameter 'a' is the slope of affinity vs k
    b_fit = np.polyfit(ks, costs, 1)       # Parameter 'b' is the slope of cost vs k

    # Print the final results for easy viewing
    print(f"\nStirling Partitioning Algorithm (Delivery Routes):")
    print(f"Optimal number of routes (trucks): {optimal_k}")
    print(f"Affinity (slope): {a_fit[0]:.4f}, Cost (slope): {b_fit[0]:.4f}")
    print(f"Max silhouette score: {best_result['silhouette']:.4f}")
    
    return optimal_k, optimal_labels, a_fit, b_fit, results

# --- Visualization and Reporting ---
# These functions create a visual plot of the routes and a summary HTML report.
def create_visualizations(df, optimal_labels, optimal_k):
    """
    Creates and saves a scatter plot of the delivery routes.
    """
    os.makedirs('visualizations', exist_ok=True)
    plt.figure(figsize=(8, 6))
    plt.scatter(df['location_x'], df['location_y'], c=optimal_labels, cmap='tab10', s=60, edgecolor='black')
    plt.title(f'Delivery Route Assignment (k={optimal_k})')
    plt.xlabel('Location X')
    plt.ylabel('Location Y')
    plt.tight_layout()
    plt.savefig('visualizations/delivery_route_assignment.png')
    plt.close()
    print("Route assignment plot saved as 'visualizations/delivery_route_assignment.png'")

    # Save a table of orders with their assigned route
    df_with_labels = df.copy()
    df_with_labels['route'] = optimal_labels
    df_with_labels.to_csv('visualizations/delivery_route_table.csv', index=False)
    print("Order table saved as 'visualizations/delivery_route_table.csv'")

def create_report(optimal_k, a_fit, b_fit):
    """
    Generates and saves a simple HTML report summarizing the analysis.
    """
    # Read the order table for HTML display
    table_html = ""
    try:
        order_table = pd.read_csv('visualizations/delivery_route_table.csv')
        table_html = order_table.head(10).to_html(index=False)
    except Exception:
        table_html = "<p>(Could not load order table)</p>"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Supply Chain Delivery Optimization Report</title>
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
        <h1>Supply Chain Delivery Optimization Report</h1>
        <div class="summary">
            <h2>Results</h2>
            <ul>
                <li>Optimal number of routes (trucks): <strong>{optimal_k}</strong></li>
                <li>Affinity (slope): <strong>{a_fit[0]:.4f}</strong></li>
                <li>Cost (slope): <strong>{b_fit[0]:.4f}</strong></li>
            </ul>
        </div>
        <h2>Delivery Route Assignment</h2>
        <img src="delivery_route_assignment.png" alt="Delivery Route Assignment">
        <h2>Sample of Orders and Assigned Routes</h2>
        <p>Below are the first 10 orders with their features and assigned route:</p>
        {table_html}
        <p><b>Feature meanings:</b></p>
        <ul>
            <li><b>location_x, location_y</b>: Delivery coordinates</li>
            <li><b>size</b>: Package size</li>
            <li><b>urgency</b>: Delivery urgency (1 = low, 3 = high)</li>
            <li><b>route</b>: Assigned route label from clustering</li>
        </ul>
        <p>Use these groupings to optimize fleet size, route planning, and delivery efficiency.</p>
    </body>
    </html>
    """
    with open('visualizations/delivery_report.html', 'w') as f:
        f.write(html)
    print("Summary report created: visualizations/delivery_report.html")

def main():
    """
    Main function to run the entire demo.
    """
    print("=== Supply Chain Delivery Demo ===")
    df = generate_orders()
    # The data matrix for clustering includes all features
    data_matrix = df.values
    optimal_k, optimal_labels, a_fit, b_fit, results = stirling_partitioning_algorithm(data_matrix)
    create_visualizations(df, optimal_labels, optimal_k)
    create_report(optimal_k, a_fit, b_fit)
    print("=== Analysis Complete ===")
    print("Open visualizations/delivery_report.html in your browser to view the summary.")

if __name__ == "__main__":
    main()
