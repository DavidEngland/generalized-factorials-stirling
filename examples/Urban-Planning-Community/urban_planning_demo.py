import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import os

def generate_households(n_households=120, seed=42):
    np.random.seed(seed)
    # Features: location_x, location_y, household_size, income, lifestyle
    location_x = np.random.uniform(0, 100, n_households)
    location_y = np.random.uniform(0, 100, n_households)
    household_size = np.random.randint(1, 6, n_households)      # 1-5 people
    income = np.random.normal(50000, 15000, n_households)       # Annual income
    lifestyle = np.random.randint(1, 4, n_households)           # 1=active, 2=quiet, 3=family
    df = pd.DataFrame({
        'location_x': location_x,
        'location_y': location_y,
        'household_size': household_size,
        'income': income,
        'lifestyle': lifestyle
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
    print(f"\nStirling Partitioning Algorithm (Neighborhoods):")
    print(f"Optimal number of neighborhoods: {optimal_k}")
    print(f"Affinity (slope): {a_fit[0]:.4f}, Cost (slope): {b_fit[0]:.4f}")
    print(f"Max silhouette score: {best_result['silhouette']:.4f}")
    return optimal_k, optimal_labels, a_fit, b_fit, results

def create_visualizations(df, optimal_labels, optimal_k):
    os.makedirs('visualizations', exist_ok=True)
    plt.figure(figsize=(8, 6))
    plt.scatter(df['location_x'], df['location_y'], c=optimal_labels, cmap='tab20', s=60, edgecolor='black')
    plt.title(f'Neighborhood Assignment (k={optimal_k})')
    plt.xlabel('Location X')
    plt.ylabel('Location Y')
    plt.tight_layout()
    plt.savefig('visualizations/neighborhood_assignment.png')
    plt.close()
    print("Neighborhood assignment plot saved as 'visualizations/neighborhood_assignment.png'")

    df_with_labels = df.copy()
    df_with_labels['neighborhood'] = optimal_labels
    df_with_labels.to_csv('visualizations/neighborhood_table.csv', index=False)
    print("Household table saved as 'visualizations/neighborhood_table.csv'")

def create_report(optimal_k, a_fit, b_fit):
    table_html = ""
    try:
        household_table = pd.read_csv('visualizations/neighborhood_table.csv')
        table_html = household_table.head(10).to_html(index=False)
    except Exception:
        table_html = "<p>(Could not load household table)</p>"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Urban Planning & Community Design Report</title>
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
        <h1>Urban Planning & Community Design Report</h1>
        <div class="summary">
            <h2>Results</h2>
            <ul>
                <li>Optimal number of neighborhoods: <strong>{optimal_k}</strong></li>
                <li>Affinity (slope): <strong>{a_fit[0]:.4f}</strong></li>
                <li>Cost (slope): <strong>{b_fit[0]:.4f}</strong></li>
            </ul>
        </div>
        <h2>Neighborhood Assignment</h2>
        <img src="neighborhood_assignment.png" alt="Neighborhood Assignment">
        <h2>Sample of Households and Assigned Neighborhoods</h2>
        <p>Below are the first 10 households with their features and assigned neighborhood:</p>
        {table_html}
        <p><b>Feature meanings:</b></p>
        <ul>
            <li><b>location_x, location_y</b>: Household/building coordinates</li>
            <li><b>household_size</b>: Number of people in household</li>
            <li><b>income</b>: Annual household income</li>
            <li><b>lifestyle</b>: Lifestyle category (1=active, 2=quiet, 3=family)</li>
            <li><b>neighborhood</b>: Assigned neighborhood label from clustering</li>
        </ul>
        <p>Use these groupings to guide zoning, infrastructure investment, and community design.</p>
    </body>
    </html>
    """
    with open('visualizations/urban_planning_report.html', 'w') as f:
        f.write(html)
    print("Summary report created: visualizations/urban_planning_report.html")

def main():
    print("=== Urban Planning & Community Design Demo ===")
    df = generate_households()
    data_matrix = df.values
    optimal_k, optimal_labels, a_fit, b_fit, results = stirling_partitioning_algorithm(data_matrix)
    create_visualizations(df, optimal_labels, optimal_k)
    create_report(optimal_k, a_fit, b_fit)
    print("=== Analysis Complete ===")
    print("Open visualizations/urban_planning_report.html in your browser to view the summary.")

if __name__ == "__main__":
    main()
