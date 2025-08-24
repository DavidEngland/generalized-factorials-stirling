"""
Simple Retail Demo: Demonstrating the Stirling Measure approach
with a straightforward retail example.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import os
import random
from datetime import datetime, timedelta
import sys

# Add path to import Stirling functionality
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
try:
    from src.core.python.stirling import GeneralizedStirling
except ImportError:
    # Simple implementation if the main library isn't available
    class GeneralizedStirling:
        def __init__(self, a=1.0, b=1.0):
            self.a = a
            self.b = b
            self._cache = {}
        
        def compute(self, n, k):
            """Simplified implementation of generalized Stirling numbers."""
            if k == 0:
                return 1.0 if n == 0 else 0.0
            if n == 0 or k > n:
                return 0.0
            if k == n:
                return 1.0
            if (n, k) in self._cache:
                return self._cache[(n, k)]
            
            # Use triangular recurrence relation
            result = self.compute(n-1, k-1) + (self.a * (n-1) + self.b * k) * self.compute(n-1, k)
            self._cache[(n, k)] = result
            return result

# Set visual style
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["font.size"] = 12

# Create directory for visualizations
os.makedirs("visualizations", exist_ok=True)

def generate_sample_data(n_transactions=500, n_products=30, n_weeks=12, seed=42):
    """Generate synthetic retail transaction data."""
    np.random.seed(seed)
    random.seed(seed)
    
    # Create product list
    products = [f"Product_{i}" for i in range(1, n_products+1)]
    
    # Create product categories (for data generation)
    true_categories = {
        "Electronics": products[:5],
        "Clothing": products[5:12],
        "Home": products[12:18],
        "Food": products[18:25],
        "Other": products[25:]
    }
    
    # Generate transactions
    transactions = []
    start_date = datetime(2023, 1, 1)
    
    for i in range(n_transactions):
        # Pick transaction date
        days_offset = random.randint(0, n_weeks * 7 - 1)
        transaction_date = (start_date + timedelta(days=days_offset)).strftime("%Y-%m-%d")
        transaction_week = (start_date + timedelta(days=days_offset)).strftime("%Y-W%U")
        
        # Determine number of items purchased (1-5)
        n_items = random.choices([1, 2, 3, 4, 5], weights=[0.3, 0.3, 0.2, 0.1, 0.1])[0]
        
        # Determine shopping pattern:
        # 1. Category-focused (items from same category)
        # 2. Mixed (items from different categories)
        shopping_pattern = random.choices(["category", "mixed"], weights=[0.7, 0.3])[0]
        
        if shopping_pattern == "category":
            # Pick a random category
            category = random.choice(list(true_categories.keys()))
            # Pick random products from that category
            items = random.sample(true_categories[category], min(n_items, len(true_categories[category])))
        else:
            # Pick random products from any category
            items = random.sample(products, n_items)
        
        # Add to transactions
        for item in items:
            transactions.append({
                "transaction_id": i+1,
                "date": transaction_date,
                "week": transaction_week,
                "product": item
            })
    
    # Convert to DataFrame
    df = pd.DataFrame(transactions)
    
    # Save to CSV
    df.to_csv("sample_data.csv", index=False)
    print(f"Generated {len(df)} purchase records across {n_transactions} transactions")
    
    return df, true_categories

def analyze_product_clustering(df):
    """Analyze how products cluster over time using the Stirling Measure."""
    print("\n--- Analyzing Product Clustering Patterns ---")
    
    # Group by week
    weekly_stats = []
    
    for week, week_data in df.groupby('week'):
        # Count unique products and transactions
        n_products = week_data['product'].nunique()
        n_transactions = week_data['transaction_id'].nunique()
        
        # Create product co-occurrence matrix
        products = sorted(df['product'].unique())
        
        # Get products by transaction
        transaction_products = week_data.groupby('transaction_id')['product'].apply(list)
        
        # Create co-occurrence matrix
        co_matrix = np.zeros((len(products), len(products)))
        product_indices = {product: i for i, product in enumerate(products)}
        
        for products_list in transaction_products:
            for p1 in products_list:
                for p2 in products_list:
                    i, j = product_indices[p1], product_indices[p2]
                    co_matrix[i, j] += 1
        
        # Normalize and convert to distance matrix
        np.fill_diagonal(co_matrix, 0)  # Remove self-connections
        if co_matrix.sum() > 0:
            co_matrix = co_matrix / co_matrix.sum()  # Normalize
        distance_matrix = 1 - co_matrix  # Convert to distance
        
        # Determine number of clusters using simple method
        # In real application, would use Stirling parameter estimation
        # Here we'll use a simplified approach for demonstration
        inertia = []
        max_clusters = min(10, n_products // 3)
        for k in range(1, max_clusters+1):
            kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
            kmeans.fit(distance_matrix)
            inertia.append(kmeans.inertia_)
        
        # Simple elbow method
        if len(inertia) > 2:
            diffs = np.diff(inertia)
            k = 2  # Default
            for i in range(len(diffs)-1):
                if diffs[i] / max(0.0001, diffs[i+1]) < 1.5:
                    k = i + 2
                    break
        else:
            k = 2
            
        # Apply clustering with determined k
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        clusters = kmeans.fit_predict(distance_matrix)
        
        # Store weekly stats
        weekly_stats.append({
            'week': week,
            'n_products': n_products,
            'n_clusters': k,
            'n_transactions': n_transactions
        })
        
        print(f"Week {week}: {n_products} products in {k} clusters from {n_transactions} transactions")
    
    # Convert to DataFrame
    stats_df = pd.DataFrame(weekly_stats)
    
    return stats_df

def calculate_stirling_parameters(stats_df):
    """Calculate Stirling parameters using linear regression."""
    print("\n--- Estimating Stirling Parameters ---")
    
    # For demonstration, we'll use a theoretical approach
    # In real implementation, would calculate actual Stirling measures
    
    # Parameters for demonstration
    true_a = 0.25  # Moderate product affinity
    true_b = 1.70  # High category barrier
    
    # Calculate theoretical measures with some noise
    measures = []
    for i, row in stats_df.iterrows():
        n = row['n_products']
        k = row['n_clusters']
        theoretical_measure = true_a * n + true_b * k + np.random.normal(0, 0.3)
        measures.append(theoretical_measure)
    
    stats_df['measure'] = measures
    
    # Linear regression to estimate parameters
    X = stats_df[['n_products', 'n_clusters']].values
    y = stats_df['measure'].values
    
    # Perform regression (simplified)
    # In practice, use sklearn's LinearRegression
    XX = np.dot(X.T, X)
    Xy = np.dot(X.T, y)
    params = np.linalg.solve(XX, Xy)
    
    estimated_a = params[0]
    estimated_b = params[1]
    
    # Calculate R-squared
    y_pred = np.dot(X, params)
    ss_total = np.sum((y - np.mean(y))**2)
    ss_residual = np.sum((y - y_pred)**2)
    r_squared = 1 - (ss_residual / ss_total)
    
    print(f"Estimated parameters: a = {estimated_a:.4f}, b = {estimated_b:.4f}")
    print(f"R-squared: {r_squared:.4f}")
    print(f"True parameters (for demonstration): a = {true_a}, b = {true_b}")
    
    return estimated_a, estimated_b, r_squared, stats_df

def interpret_parameters(a, b):
    """Provide business interpretation of Stirling parameters."""
    print("\n--- Business Interpretation ---")
    
    # Interpret product affinity (a)
    if a < 0.2:
        affinity = "Low product affinity. Products are purchased independently with little tendency to cluster."
        affinity_strategy = "Focus on individual product promotions rather than category-based marketing."
    elif a < 0.4:
        affinity = "Moderate product affinity. Some natural clustering of products in purchases."
        affinity_strategy = "Balance category merchandising with cross-category promotions."
    else:
        affinity = "High product affinity. Strong tendency for products to be purchased together in clusters."
        affinity_strategy = "Emphasize category-based merchandising and promotions."
    
    # Interpret category barrier (b)
    if b < 1.0:
        barrier = "Low category barrier. New product categories form easily and frequently."
        barrier_strategy = "Frequently reassess product categories and be flexible with store layouts."
    elif b < 2.0:
        barrier = "Moderate category barrier. Some stability in product categories with occasional changes."
        barrier_strategy = "Review product categories quarterly and adjust as needed."
    else:
        barrier = "High category barrier. Very stable product categories that rarely change."
        barrier_strategy = "Invest in long-term category-based store design and marketing."
    
    # Combined strategy
    if a < 0.3 and b < 1.0:
        combined = "Dynamic Individual Focus: Products behave independently in a rapidly changing environment."
    elif a > 0.4 and b > 2.0:
        combined = "Stable Category Focus: Strong, stable product categories dominate purchasing patterns."
    elif a < 0.3 and b > 2.0:
        combined = "Stable Diversity: Products behave independently but within stable overall structure."
    elif a > 0.4 and b < 1.0:
        combined = "Dynamic Category Focus: Strong but rapidly evolving product categories."
    else:
        combined = "Balanced Approach: Moderate clustering in a moderately stable environment."
    
    print(f"Product Affinity (a = {a:.2f}): {affinity}")
    print(f"Category Barrier (b = {b:.2f}): {barrier}")
    print(f"Combined Strategy: {combined}")
    print(f"\nRecommended Strategies:")
    print(f"1. {affinity_strategy}")
    print(f"2. {barrier_strategy}")
    
    return {
        "affinity": affinity,
        "barrier": barrier,
        "combined": combined,
        "strategies": [affinity_strategy, barrier_strategy]
    }

def create_visualizations(stats_df, a, b, interpretations):
    """Create visualizations for the analysis."""
    print("\n--- Creating Visualizations ---")
    
    # 1. Time series of products and clusters
    plt.figure(figsize=(12, 6))
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    ax1.set_xlabel('Week')
    ax1.set_ylabel('Number of Products', color='tab:blue')
    ax1.plot(stats_df['week'], stats_df['n_products'], 'o-', color='tab:blue', label='Products')
    ax1.tick_params(axis='y', labelcolor='tab:blue')
    
    ax2 = ax1.twinx()
    ax2.set_ylabel('Number of Clusters', color='tab:red')
    ax2.plot(stats_df['week'], stats_df['n_clusters'], 's-', color='tab:red', label='Clusters')
    ax2.tick_params(axis='y', labelcolor='tab:red')
    
    # Add legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    plt.title('Product and Cluster Counts Over Time')
    plt.tight_layout()
    plt.savefig('visualizations/time_series.png')
    plt.close()
    
    # 2. Stirling Measure Analysis
    plt.figure(figsize=(10, 6))
    plt.scatter(stats_df['n_products'], stats_df['measure'], c=stats_df['n_clusters'], 
                cmap='viridis', s=100, alpha=0.7)
    
    # Add regression line
    x_range = np.linspace(min(stats_df['n_products']), max(stats_df['n_products']), 100)
    y_pred = a * x_range + b * np.mean(stats_df['n_clusters'])
    plt.plot(x_range, y_pred, 'r--', linewidth=2, 
             label=f'Fitted Line (a={a:.2f}, b={b:.2f})')
    
    plt.colorbar(label='Number of Clusters')
    plt.xlabel('Number of Products')
    plt.ylabel('Stirling Measure')
    plt.title('Stirling Measure Analysis')
    plt.legend()
    plt.tight_layout()
    plt.savefig('visualizations/stirling_measure.png')
    plt.close()
    
    # 3. Parameter Interpretation Dashboard
    plt.figure(figsize=(12, 8))
    
    # Create a 2x2 grid
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    
    # 3.1 Parameter gauge for a (top left)
    create_gauge(axes[0, 0], a, 0, 1, 'Product Affinity (a)', 
                ['Low', 'Moderate', 'High'], ['#ff9999', '#ffdd99', '#99ff99'])
    
    # 3.2 Parameter gauge for b (top right)
    create_gauge(axes[0, 1], b, 0, 3, 'Category Barrier (b)', 
                ['Low', 'Moderate', 'High'], ['#99ff99', '#ffdd99', '#ff9999'])
    
    # 3.3 Strategy quadrant (bottom left)
    axes[1, 0].set_xlim(0, 1)
    axes[1, 0].set_ylim(0, 3)
    
    # Add quadrant colors
    axes[1, 0].add_patch(plt.Rectangle((0, 0), 0.3, 1.0, color='#ffcc99', alpha=0.3))  # Dynamic Individual
    axes[1, 0].add_patch(plt.Rectangle((0.4, 2.0), 0.6, 1.0, color='#99ccff', alpha=0.3))  # Stable Category
    axes[1, 0].add_patch(plt.Rectangle((0, 2.0), 0.3, 1.0, color='#cc99ff', alpha=0.3))  # Stable Diversity
    axes[1, 0].add_patch(plt.Rectangle((0.4, 0), 0.6, 1.0, color='#99ffcc', alpha=0.3))  # Dynamic Category
    axes[1, 0].add_patch(plt.Rectangle((0.3, 1.0), 0.1, 1.0, color='#f0f0f0', alpha=0.3))  # Balanced
    axes[1, 0].add_patch(plt.Rectangle((0, 1.0), 0.3, 1.0, color='#f0f0f0', alpha=0.3))  # Balanced
    axes[1, 0].add_patch(plt.Rectangle((0.4, 1.0), 0.6, 1.0, color='#f0f0f0', alpha=0.3))  # Balanced
    
    # Add quadrant labels
    axes[1, 0].text(0.15, 0.5, "Dynamic\nIndividual\nFocus", ha='center', va='center', fontsize=10)
    axes[1, 0].text(0.7, 2.5, "Stable\nCategory\nFocus", ha='center', va='center', fontsize=10)
    axes[1, 0].text(0.15, 2.5, "Stable\nDiversity", ha='center', va='center', fontsize=10)
    axes[1, 0].text(0.7, 0.5, "Dynamic\nCategory\nFocus", ha='center', va='center', fontsize=10)
    axes[1, 0].text(0.5, 1.5, "Balanced\nApproach", ha='center', va='center', fontsize=10)
    
    # Plot the current parameters
    axes[1, 0].scatter([a], [b], color='red', s=200, marker='*', 
                      edgecolors='black', linewidth=2, zorder=5)
    
    axes[1, 0].set_xlabel('Product Affinity (a)')
    axes[1, 0].set_ylabel('Category Barrier (b)')
    axes[1, 0].set_title('Strategy Map')
    
    # 3.4 Recommendations (bottom right)
    axes[1, 1].axis('off')
    recommendation_text = (
        f"RETAIL STRATEGY RECOMMENDATIONS\n\n"
        f"Based on Stirling Parameters:\n"
        f"• a = {a:.2f} (Product Affinity)\n"
        f"• b = {b:.2f} (Category Barrier)\n\n"
        f"Combined Strategy:\n{interpretations['combined']}\n\n"
        f"1. {interpretations['strategies'][0]}\n\n"
        f"2. {interpretations['strategies'][1]}"
    )
    axes[1, 1].text(0.5, 0.5, recommendation_text, 
                   ha='center', va='center', fontsize=10, 
                   bbox=dict(boxstyle='round,pad=0.5', facecolor='#f0f0f0'),
                   wrap=True, transform=axes[1, 1].transAxes)
    
    plt.tight_layout()
    plt.savefig('visualizations/parameter_dashboard.png')
    plt.close()
    
    print("Visualizations created in the 'visualizations' directory")

def create_gauge(ax, value, min_val, max_val, title, labels, colors):
    """Create a gauge chart for parameter visualization."""
    # Normalize value
    norm_val = (value - min_val) / (max_val - min_val)
    norm_val = min(max(norm_val, 0), 1)  # Clamp between 0 and 1
    
    # Create gauge
    theta = np.linspace(0, np.pi, 100)
    x = np.cos(theta)
    y = np.sin(theta)
    
    # Background
    ax.plot(x, y, color='black', linewidth=2)
    ax.fill_between(x, 0, y, color='#f0f0f0', alpha=0.5)
    
    # Color zones
    n_zones = len(labels)
    for i in range(n_zones):
        start = i / n_zones
        end = (i + 1) / n_zones
        
        theta_zone = np.linspace(start * np.pi, end * np.pi, 100)
        x_zone = np.cos(theta_zone)
        y_zone = np.sin(theta_zone)
        
        ax.fill_between(x_zone, 0, y_zone, color=colors[i], alpha=0.7)
        
        # Add label
        mid_angle = (start + end) / 2 * np.pi
        label_x = 0.8 * np.cos(mid_angle)
        label_y = 0.8 * np.sin(mid_angle)
        ax.text(label_x, label_y, labels[i], ha='center', va='center', fontsize=10)
    
    # Add needle
    angle = norm_val * np.pi
    needle_x = [0, np.cos(angle)]
    needle_y = [0, np.sin(angle)]
    ax.plot(needle_x, needle_y, color='black', linewidth=3)
    
    # Add central dot
    ax.scatter([0], [0], color='black', s=50, zorder=5)
    
    # Clean up chart
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-0.1, 1.1)
    ax.axis('off')
    ax.set_aspect('equal')
    
    # Add title and value
    ax.set_title(f"{title}\n{value:.2f}", fontsize=12)

def create_summary_report(a, b, r_squared, interpretations):
    """Create a summary HTML report."""
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Retail Demo: Stirling Measure Analysis</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
            h1, h2, h3 {{ color: #2c3e50; }}
            .summary {{ background-color: #f8f9fa; padding: 20px; border-radius: 5px; margin-bottom: 20px; }}
            .parameters {{ display: flex; justify-content: space-around; margin: 20px 0; }}
            .parameter {{ text-align: center; padding: 15px; border-radius: 5px; width: 45%; }}
            .affinity {{ background-color: #e8f4f8; }}
            .barrier {{ background-color: #f0f8ea; }}
            .strategy {{ background-color: #fff4e6; padding: 20px; border-radius: 5px; margin: 20px 0; }}
            img {{ max-width: 100%; height: auto; margin: 20px 0; }}
            .visualization {{ margin: 30px 0; }}
            .value {{ font-size: 24px; font-weight: bold; margin: 10px 0; }}
            .interpretation {{ font-style: italic; }}
        </style>
    </head>
    <body>
        <h1>Simple Retail Demo: Stirling Measure Analysis</h1>
        
        <div class="summary">
            <h2>Analysis Summary</h2>
            <p>This analysis examines how products naturally cluster in customer purchases using the Stirling Measure approach.</p>
            <p>The model fit is <strong>R² = {r_squared:.4f}</strong>, indicating a {r_squared >= 0.8 and "strong" or "moderate"} relationship between the data and the Stirling parameters.</p>
        </div>
        
        <div class="parameters">
            <div class="parameter affinity">
                <h3>Product Affinity (a)</h3>
                <div class="value">{a:.2f}</div>
                <p class="interpretation">{interpretations['affinity']}</p>
            </div>
            
            <div class="parameter barrier">
                <h3>Category Barrier (b)</h3>
                <div class="value">{b:.2f}</div>
                <p class="interpretation">{interpretations['barrier']}</p>
            </div>
        </div>
        
        <div class="strategy">
            <h2>Recommended Strategy</h2>
            <h3>{interpretations['combined']}</h3>
            <ol>
                <li>{interpretations['strategies'][0]}</li>
                <li>{interpretations['strategies'][1]}</li>
            </ol>
        </div>
        
        <h2>Visualizations</h2>
        
        <div class="visualization">
            <h3>Parameter Dashboard</h3>
            <img src="visualizations/parameter_dashboard.png" alt="Parameter Dashboard">
        </div>
        
        <div class="visualization">
            <h3>Product and Cluster Evolution</h3>
            <img src="visualizations/time_series.png" alt="Time Series">
        </div>
        
        <div class="visualization">
            <h3>Stirling Measure Analysis</h3>
            <img src="visualizations/stirling_measure.png" alt="Stirling Measure">
        </div>
        
        <h2>How to Use These Insights</h2>
        <p>The Stirling parameters reveal fundamental properties of your retail environment:</p>
        <ul>
            <li><strong>Store Layout</strong>: Organize products based on the natural clustering tendencies revealed by parameter a.</li>
            <li><strong>Inventory Planning</strong>: Balance category-specific vs. diverse stock based on parameters a and b.</li>
            <li><strong>Marketing Campaigns</strong>: Design promotions that align with the natural purchasing patterns of your customers.</li>
            <li><strong>Category Management</strong>: Adjust your category review frequency based on parameter b.</li>
        </ul>
        
        <p style="margin-top: 40px; font-size: 0.8em; color: #7f8c8d;">
            Analysis generated using the Stirling Measure approach.
        </p>
    </body>
    </html>
    """
    
    with open('visualizations/report.html', 'w') as f:
        f.write(html)
    
    print("Summary report created: visualizations/report.html")

def stirling_partitioning_algorithm(data, min_k=2, max_k=None):
    """
    Apply the Stirling Partitioning Algorithm to find the optimal number of clusters.
    Returns the optimal k, clustering labels, and proxy parameters for affinity and cost.
    """
    n = len(data)
    if max_k is None:
        max_k = min(10, max(3, int(np.sqrt(n))))
    results = []

    for k in range(min_k, max_k + 1):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(data)
        centroids = kmeans.cluster_centers_

        # Affinity: mean intra-cluster distance
        affinity = np.mean([
            np.mean(np.linalg.norm(data[labels == i] - centroids[i], axis=1))
            for i in range(k)
        ])

        # Cost: mean distance between centroids
        if k > 1:
            centroid_distances = [
                np.linalg.norm(centroids[i] - centroids[j])
                for i in range(k) for j in range(i+1, k)
            ]
            cost = np.mean(centroid_distances)
        else:
            cost = 0.0

        # Silhouette score for cluster quality
        sil_score = silhouette_score(data, labels) if k > 1 else 0.0

        results.append({
            'k': k,
            'affinity': affinity,
            'cost': cost,
            'silhouette': sil_score,
            'labels': labels
        })

    # Linear regression to fit affinity and cost vs k
    ks = np.array([r['k'] for r in results])
    affinities = np.array([r['affinity'] for r in results])
    costs = np.array([r['cost'] for r in results])

    # Fit linear models (affinity and cost as functions of k)
    a_fit = np.polyfit(ks, affinities, 1)
    b_fit = np.polyfit(ks, costs, 1)

    # Find optimal k (max silhouette score)
    best_result = max(results, key=lambda r: r['silhouette'])
    optimal_k = best_result['k']
    optimal_labels = best_result['labels']

    print(f"\nStirling Partitioning Algorithm:")
    print(f"Optimal number of clusters (k): {optimal_k}")
    print(f"Affinity (slope): {a_fit[0]:.4f}, Cost (slope): {b_fit[0]:.4f}")
    print(f"Max silhouette score: {best_result['silhouette']:.4f}")

    return optimal_k, optimal_labels, a_fit, b_fit, results

def main():
    """Main function to run the demo."""
    print("=== Simple Retail Demo: Stirling Measure in Action ===\n")
    
    # Check if data exists, otherwise generate
    if os.path.exists("sample_data.csv"):
        print("Loading existing sample data...")
        df = pd.read_csv("sample_data.csv")
        true_categories = None  # We don't know the true categories for existing data
    else:
        print("Generating sample retail data...")
        df, true_categories = generate_sample_data()
    
    # Analyze product clustering
    stats_df = analyze_product_clustering(df)
    
    # Calculate Stirling parameters
    a, b, r_squared, stats_df = calculate_stirling_parameters(stats_df)
    
    # Interpret parameters
    interpretations = interpret_parameters(a, b)
    
    # Create visualizations
    create_visualizations(stats_df, a, b, interpretations)
    
    # Create summary report
    create_summary_report(a, b, r_squared, interpretations)
    
    # Use product features for clustering (e.g., one-hot encoding)
    product_features = pd.get_dummies(df['product'])
    data_matrix = product_features.values

    # Apply Stirling Partitioning Algorithm
    optimal_k, optimal_labels, a_fit, b_fit, stirling_results = stirling_partitioning_algorithm(data_matrix)

    # Visualize clustering results
    plt.figure(figsize=(10, 6))
    plt.hist(optimal_labels, bins=optimal_k, color='skyblue', edgecolor='black')
    plt.title(f'Cluster Distribution (k={optimal_k})')
    plt.xlabel('Cluster Label')
    plt.ylabel('Number of Transactions')
    plt.tight_layout()
    plt.savefig('visualizations/stirling_partitioning_clusters.png')
    plt.close()

    print("Cluster distribution plot saved as 'visualizations/stirling_partitioning_clusters.png'")

    print("\n=== Analysis Complete ===")
    print("Review the visualizations directory for results")
    print("Open visualizations/report.html in a web browser to see the full report")

if __name__ == "__main__":
    main()
