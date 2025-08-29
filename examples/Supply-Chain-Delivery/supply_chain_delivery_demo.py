import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import os
import sys

# Add the main project directory to path to import our library
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.stirling_core import BellPolynomials, ParameterEstimation

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

def bell_enhanced_stirling_partitioning(data, min_k=2, max_k=15):
    """
    Enhanced Stirling partitioning algorithm using Bell polynomials for
    higher-order corrections to clustering parameters.
    
    Args:
        data: Feature matrix of delivery orders
        min_k, max_k: Range of cluster counts to test
        
    Returns:
        optimal_k: Optimal number of clusters/routes
        optimal_labels: Route assignments
        a_fit, b_fit: Enhanced parameters with higher-order corrections
        results: All results for different k values
    """
    results = []
    n_samples, n_dims = data.shape
    
    # For each potential number of clusters/routes
    for k in range(min_k, max_k + 1):
        # Run k-means clustering
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(data)
        centroids = kmeans.cluster_centers_
        
        # Calculate silhouette score
        sil_score = silhouette_score(data, labels) if k > 1 else 0.0
        
        # Calculate cluster statistics using Bell polynomials
        bell_metrics = []
        for i in range(k):
            cluster_data = data[labels == i]
            if len(cluster_data) > 1:
                # Compute Bell polynomials for orders 2 and 3
                # B_{2,1} and B_{2,2} capture variance/covariance
                # B_{3,1}, B_{3,2}, B_{3,3} capture higher-order moments (skewness, etc.)
                b_2_1 = BellPolynomials.multivariate_bell(2, 1, cluster_data)
                b_2_2 = BellPolynomials.multivariate_bell(2, 2, cluster_data)
                b_3_1 = BellPolynomials.multivariate_bell(3, 1, cluster_data)
                b_3_2 = BellPolynomials.multivariate_bell(3, 2, cluster_data)
                b_3_3 = BellPolynomials.multivariate_bell(3, 3, cluster_data)
                
                # Store all metrics
                bell_metrics.append({
                    'b_2_1': b_2_1,
                    'b_2_2': b_2_2,
                    'b_3_1': b_3_1,
                    'b_3_2': b_3_2,
                    'b_3_3': b_3_3,
                    'size': len(cluster_data)
                })
        
        # Extract advanced affinity and cost metrics using Bell polynomials
        if bell_metrics:
            # Compute weighted averages based on cluster sizes
            total_points = sum(m['size'] for m in bell_metrics)
            
            # Second-order metrics (variance-based)
            avg_b_2_1 = sum(np.linalg.norm(m['b_2_1']) * m['size'] for m in bell_metrics) / total_points
            avg_b_2_2 = sum(np.linalg.norm(m['b_2_2']) * m['size'] for m in bell_metrics) / total_points
            
            # Third-order metrics (skewness-based corrections)
            avg_b_3_1 = sum(np.linalg.norm(m['b_3_1']) * m['size'] for m in bell_metrics) / total_points
            avg_b_3_2 = sum(np.linalg.norm(m['b_3_2']) * m['size'] for m in bell_metrics) / total_points
            avg_b_3_3 = sum(np.linalg.norm(m['b_3_3']) * m['size'] for m in bell_metrics) / total_points
            
            # Enhanced affinity and cost with higher-order corrections
            # Lower dispersion (B_{2,1}) and higher skewness (B_{3,1}) = stronger affinity
            affinity = -avg_b_2_1 - 0.1 * avg_b_3_1
            
            # Higher between-cluster separation (B_{2,2}) and B_{3,2} = higher cost
            cost = avg_b_2_2 + 0.1 * avg_b_3_2
            
            # Store higher-order metrics for later analysis
            higher_order_metrics = {
                'b_2_1': avg_b_2_1,
                'b_2_2': avg_b_2_2,
                'b_3_1': avg_b_3_1,
                'b_3_2': avg_b_3_2,
                'b_3_3': avg_b_3_3
            }
        else:
            # Fallback to traditional method if Bell calculation fails
            affinity = np.mean([
                np.mean(np.linalg.norm(data[labels == i] - centroids[i], axis=1))
                for i in range(k)
            ])
            
            if k > 1:
                cost = np.mean([
                    np.linalg.norm(centroids[i] - centroids[j])
                    for i in range(k) for j in range(i+1, k)
                ])
            else:
                cost = 0.0
                
            higher_order_metrics = {}
        
        # Store all results
        results.append({
            'k': k,
            'affinity': affinity,
            'cost': cost,
            'silhouette': sil_score,
            'labels': labels,
            'higher_order_metrics': higher_order_metrics
        })
    
    # Find the best clustering based on silhouette score
    best_result = max(results, key=lambda r: r['silhouette'])
    optimal_k = best_result['k']
    optimal_labels = best_result['labels']
    
    # Extract all k values and corresponding metrics
    ks = np.array([r['k'] for r in results])
    affinities = np.array([r['affinity'] for r in results])
    costs = np.array([r['cost'] for r in results])
    
    # Use robust regression with higher-order corrections
    from sklearn.linear_model import HuberRegressor
    
    # Prepare data for regression: use k and k^2 for quadratic fit
    X = np.column_stack((ks, ks**2))
    
    # Fit robust models with quadratic terms
    a_model = HuberRegressor().fit(X, affinities)
    b_model = HuberRegressor().fit(X, costs)
    
    # Extract linear and quadratic coefficients
    a_linear = a_model.coef_[0]
    a_quadratic = a_model.coef_[1] if len(a_model.coef_) > 1 else 0
    
    b_linear = b_model.coef_[0]
    b_quadratic = b_model.coef_[1] if len(b_model.coef_) > 1 else 0
    
    # Combine into enhanced parameter estimates with higher-order corrections
    a_fit = [a_linear, a_quadratic]
    b_fit = [b_linear, b_quadratic]
    
    print(f"\nBell-Enhanced Stirling Partitioning (Supply Chain Routes):")
    print(f"Optimal number of routes: {optimal_k}")
    print(f"Affinity parameters: linear={a_fit[0]:.4f}, quadratic={a_fit[1]:.4f}")
    print(f"Cost parameters: linear={b_fit[0]:.4f}, quadratic={b_fit[1]:.4f}")
    print(f"Silhouette score: {best_result['silhouette']:.4f}")
    
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

# Function to create enhanced visualizations showing Bell polynomial benefits
def create_bell_enhanced_visualizations(df, results, optimal_k, a_fit, b_fit):
    """
    Create visualizations demonstrating the benefits of Bell polynomial enhancements.
    
    Args:
        df: Original dataframe
        results: Results from bell_enhanced_stirling_partitioning
        optimal_k: Optimal number of clusters
        a_fit, b_fit: Enhanced parameter fits
    """
    os.makedirs('visualizations', exist_ok=True)
    
    # 1. Create a 2x2 visualization grid
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    
    # Extract data for plotting
    ks = [r['k'] for r in results]
    affinities = [r['affinity'] for r in results]
    costs = [r['cost'] for r in results]
    silhouettes = [r['silhouette'] for r in results]
    
    # Plot 1: Silhouette scores
    axs[0, 0].plot(ks, silhouettes, 'o-', linewidth=2)
    axs[0, 0].set_title('Route Quality by Count')
    axs[0, 0].set_xlabel('Number of Routes')
    axs[0, 0].set_ylabel('Silhouette Score')
    axs[0, 0].grid(True, linestyle='--', alpha=0.7)
    
    # Plot 2: Affinity parameter with quadratic fit
    x_range = np.linspace(min(ks), max(ks), 100)
    y_pred = a_fit[0] * x_range + a_fit[1] * x_range**2
    
    axs[0, 1].plot(ks, affinities, 'o', label='Data points')
    axs[0, 1].plot(x_range, y_pred, 'r-', label=f'Quadratic fit: {a_fit[0]:.2f}k + {a_fit[1]:.2f}k²')
    axs[0, 1].set_title('Enhanced Affinity Parameter (with Bell corrections)')
    axs[0, 1].set_xlabel('Number of Routes')
    axs[0, 1].set_ylabel('Affinity Metric')
    axs[0, 1].grid(True, linestyle='--', alpha=0.7)
    axs[0, 1].legend()
    
    # Plot 3: Cost parameter with quadratic fit
    y_pred = b_fit[0] * x_range + b_fit[1] * x_range**2
    
    axs[1, 0].plot(ks, costs, 'o', label='Data points')
    axs[1, 0].plot(x_range, y_pred, 'r-', label=f'Quadratic fit: {b_fit[0]:.2f}k + {b_fit[1]:.2f}k²')
    axs[1, 0].set_title('Enhanced Cost Parameter (with Bell corrections)')
    axs[1, 0].set_xlabel('Number of Routes')
    axs[1, 0].set_ylabel('Cost Metric')
    axs[1, 0].grid(True, linestyle='--', alpha=0.7)
    axs[1, 0].legend()
    
    # Plot 4: Route assignment
    # Get the optimal labels
    optimal_result = [r for r in results if r['k'] == optimal_k][0]
    labels = optimal_result['labels']
    
    # Create a scatter plot of the routes
    scatter = axs[1, 1].scatter(df['location_x'], df['location_y'], 
                              c=labels, cmap='tab20', s=50, alpha=0.7)
    axs[1, 1].set_title(f'Route Assignments (k={optimal_k})')
    axs[1, 1].set_xlabel('Location X')
    axs[1, 1].set_ylabel('Location Y')
    plt.colorbar(scatter, ax=axs[1, 1], label='Route ID')
    
    plt.tight_layout()
    plt.savefig('visualizations/bell_enhanced_analysis.png')
    plt.close()
    
    # 2. Create higher-order metrics visualization
    plt.figure(figsize=(10, 6))
    
    # Extract higher-order metrics for each k
    higher_order_data = []
    for r in results:
        if 'higher_order_metrics' in r and r['higher_order_metrics']:
            metrics = r['higher_order_metrics']
            higher_order_data.append({
                'k': r['k'],
                'b_2_1': metrics.get('b_2_1', 0),
                'b_2_2': metrics.get('b_2_2', 0),
                'b_3_1': metrics.get('b_3_1', 0),
                'b_3_2': metrics.get('b_3_2', 0),
                'b_3_3': metrics.get('b_3_3', 0)
            })
    
    if higher_order_data:
        # Convert to DataFrame for easier plotting
        metrics_df = pd.DataFrame(higher_order_data)
        
        # Plot the higher-order metrics
        plt.plot(metrics_df['k'], metrics_df['b_2_1'], 'o-', label='B₂,₁ (Variance)')
        plt.plot(metrics_df['k'], metrics_df['b_2_2'], 's-', label='B₂,₂ (Covariance)')
        plt.plot(metrics_df['k'], metrics_df['b_3_1'], '^-', label='B₃,₁ (3rd moment)')
        plt.plot(metrics_df['k'], metrics_df['b_3_2'], 'd-', label='B₃,₂ (Partial 3rd)')
        
        plt.title('Higher-Order Bell Polynomial Metrics')
        plt.xlabel('Number of Routes (k)')
        plt.ylabel('Metric Value')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.tight_layout()
        plt.savefig('visualizations/higher_order_metrics.png')
        plt.close()
    
    print("Bell-enhanced visualizations saved in the visualizations folder.")

def create_enhanced_report(optimal_k, a_fit, b_fit, results):
    """Create an enhanced HTML report with Bell polynomial insights."""
    # Read the order table for HTML display
    table_html = ""
    try:
        order_table = pd.read_csv('visualizations/delivery_route_table.csv')
        table_html = order_table.head(10).to_html(index=False)
    except Exception:
        table_html = "<p>(Could not load order table)</p>"

    # Add Bell polynomial explanation
    bell_explanation = f"""
    <div class="methodology">
        <h2>Advanced Methodology: Bell Polynomials</h2>
        <p>This analysis uses Bell polynomials to derive higher-order corrections to routing parameters:</p>
        <ul>
            <li><strong>Affinity parameter:</strong> Linear term = {a_fit[0]:.4f}, Quadratic term = {a_fit[1]:.4f}</li>
            <li><strong>Barrier parameter:</strong> Linear term = {b_fit[0]:.4f}, Quadratic term = {b_fit[1]:.4f}</li>
        </ul>
        <p>The quadratic terms capture non-linear scaling effects as the number of routes increases, providing more 
        accurate predictions of system behavior at different scales.</p>
        
        <h3>Higher-Order Metrics Explained</h3>
        <p>Bell polynomials allow us to analyze higher-order moments in the delivery data:</p>
        <ul>
            <li><strong>B₂,₁ (Variance):</strong> Measures dispersion within routes</li>
            <li><strong>B₂,₂ (Covariance):</strong> Measures separation between routes</li>
            <li><strong>B₃,₁, B₃,₂ (Third moments):</strong> Capture skewness and asymmetric effects</li>
        </ul>
        <p>These higher-order corrections provide more robust route planning that adapts to complex delivery patterns
        and non-uniform geographic distributions.</p>
        
        <h3>Visualizations</h3>
        <img src="bell_enhanced_analysis.png" alt="Bell Enhanced Analysis">
        <img src="higher_order_metrics.png" alt="Higher Order Metrics">
    </div>
    """

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
        {bell_explanation}
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

    """
    Main function to run the supply chain delivery demo with Bell enhancements.
    """
    print("=== Supply Chain Delivery Demo with Bell Polynomial Enhancements ===")
    
    # Generate order data
    df = generate_orders()
    
    # Normalize the data for better Bell polynomial calculation
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    data_matrix = scaler.fit_transform(df.values)
    
    # Use the enhanced Bell polynomial-based algorithm
    optimal_k, optimal_labels, a_fit, b_fit, results = bell_enhanced_stirling_partitioning(data_matrix)
    
    # Create enhanced visualizations
    create_bell_enhanced_visualizations(df, results, optimal_k, a_fit, b_fit)
    
    # Create standard visualizations (from original code)
    df_with_labels = df.copy()
    df_with_labels['route'] = optimal_labels
    create_visualizations(df, optimal_labels, optimal_k)
    
    # Create enhanced report
    create_enhanced_report(optimal_k, a_fit, b_fit, results)
    
    print("=== Analysis Complete ===")
    print("Open visualizations/delivery_report.html in your browser to view the summary.")
