import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import os

# Generate synthetic task data
def generate_tasks(n_tasks=50, seed=42):
    np.random.seed(seed)
    times = np.random.randint(1, 8, n_tasks)          # Estimated time (hours)
    skills = np.random.randint(1, 5, n_tasks)         # Skill level (1-4)
    priorities = np.random.randint(1, 4, n_tasks)     # Priority (1-3)
    df = pd.DataFrame({
        'time': times,
        'skill': skills,
        'priority': priorities
    })
    return df

def stirling_partitioning_algorithm(data, min_k=2, max_k=8):
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
    print(f"\nStirling Partitioning Algorithm (Task Grouping):")
    print(f"Optimal number of groups (k): {optimal_k}")
    print(f"Affinity (slope): {a_fit[0]:.4f}, Cost (slope): {b_fit[0]:.4f}")
    print(f"Max silhouette score: {best_result['silhouette']:.4f}")
    return optimal_k, optimal_labels, a_fit, b_fit, results

def create_visualizations(df, optimal_labels, optimal_k):
    os.makedirs('visualizations', exist_ok=True)
    plt.figure(figsize=(8, 5))
    plt.hist(optimal_labels, bins=optimal_k, color='skyblue', edgecolor='black')
    plt.title(f'Task Group Distribution (k={optimal_k})')
    plt.xlabel('Group Label')
    plt.ylabel('Number of Tasks')
    plt.tight_layout()
    plt.savefig('visualizations/task_group_distribution.png')
    plt.close()
    print("Task group distribution plot saved as 'visualizations/task_group_distribution.png'")

    # Also save a table of the tasks with their features and assigned group
    df_with_labels = df.copy()
    df_with_labels['group'] = optimal_labels
    df_with_labels.to_csv('visualizations/task_group_table.csv', index=False)
    print("Task group table saved as 'visualizations/task_group_table.csv'")

def create_report(optimal_k, a_fit, b_fit):
    # Read the task table for HTML display
    table_html = ""
    try:
        task_table = pd.read_csv('visualizations/task_group_table.csv')
        table_html = task_table.head(10).to_html(index=False)
    except Exception:
        table_html = "<p>(Could not load task table)</p>"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Task Grouping Report</title>
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
        <h1>Simple Task Grouping Report</h1>
        <div class="summary">
            <h2>Results</h2>
            <ul>
                <li>Optimal number of groups (k): <strong>{optimal_k}</strong></li>
                <li>Affinity (slope): <strong>{a_fit[0]:.4f}</strong></li>
                <li>Cost (slope): <strong>{b_fit[0]:.4f}</strong></li>
            </ul>
        </div>
        <h2>Task Group Distribution</h2>
        <img src="task_group_distribution.png" alt="Task Group Distribution">
        <h2>Sample of Tasks and Assigned Groups</h2>
        <p>Below are the first 10 tasks with their features and assigned group:</p>
        {table_html}
        <p><b>Feature meanings:</b></p>
        <ul>
            <li><b>time</b>: Estimated time to complete the task (hours)</li>
            <li><b>skill</b>: Required skill level (1 = easiest, 4 = hardest)</li>
            <li><b>priority</b>: Task priority (1 = low, 3 = high)</li>
            <li><b>group</b>: Assigned group label from clustering</li>
        </ul>
        <p>Use these groupings to assign tasks efficiently based on similarity and resource constraints.</p>
    </body>
    </html>
    """
    with open('visualizations/task_grouping_report.html', 'w') as f:
        f.write(html)
    print("Summary report created: visualizations/task_grouping_report.html")

def main():
    print("=== Simple Task Grouping Demo ===")
    df = generate_tasks()
    data_matrix = df.values
    optimal_k, optimal_labels, a_fit, b_fit, results = stirling_partitioning_algorithm(data_matrix)
    create_visualizations(df, optimal_labels, optimal_k)
    create_report(optimal_k, a_fit, b_fit)
    print("=== Analysis Complete ===")
    print("Open visualizations/task_grouping_report.html in your browser to view the summary.")

if __name__ == "__main__":
    main()
