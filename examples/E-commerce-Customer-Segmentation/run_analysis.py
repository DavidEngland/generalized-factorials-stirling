"""
Main analysis script for E-commerce Customer Segmentation using Stirling Measure.

This script combines data preparation, Stirling Measure calculation, 
parameter estimation, and marketing insights.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data_prep import download_dataset, load_and_clean_data, create_customer_features, perform_clustering, generate_analysis_inputs
from stirling_measure import analyze_customer_segments, interpret_parameters
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def stirling_partitioning_algorithm_customer(features, min_k=2, max_k=None):
    """
    Apply Stirling Partitioning Algorithm to customer features.
    Returns optimal k, cluster labels, and proxy parameters.
    """
    n = len(features)
    if max_k is None:
        max_k = min(10, max(3, int(np.sqrt(n))))
    results = []

    scaler = StandardScaler()
    data = scaler.fit_transform(features)

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

    print(f"\nStirling Partitioning Algorithm (Customer Segmentation):")
    print(f"Optimal number of segments (k): {optimal_k}")
    print(f"Affinity (slope): {a_fit[0]:.4f}, Cost (slope): {b_fit[0]:.4f}")
    print(f"Max silhouette score: {best_result['silhouette']:.4f}")

    return optimal_k, optimal_labels, a_fit, b_fit, results

def main():
    """Run the complete E-commerce Customer Segmentation analysis."""
    print("=" * 80)
    print("E-commerce Customer Segmentation with Stirling Measure")
    print("=" * 80)
    
    # Step 1: Data Preparation
    print("\nStep 1: Data Preparation")
    if not os.path.exists('segment_summary.csv'):
        download_dataset()
        df = load_and_clean_data()
        customer_features = create_customer_features(df)
        clustering_results = perform_clustering(customer_features)
        time_periods, customer_counts, segment_counts = generate_analysis_inputs(clustering_results)
    else:
        # Load from previously prepared data
        print("Loading from previously prepared data...")
        summary = pd.read_csv('segment_summary.csv')
        time_periods = summary['month'].tolist()
        customer_counts = summary['n_customers'].tolist()
        segment_counts = summary['n_segments'].tolist()
    
    # Step 2: Stirling Measure Analysis
    print("\nStep 2: Stirling Measure Analysis")
    results = analyze_customer_segments(
        customer_counts=customer_counts,
        segment_counts=segment_counts,
        time_periods=time_periods,
        plot=True
    )
    
    # Step 3: Parameter Interpretation
    print("\nStep 3: Parameter Interpretation")
    a = results['estimated_a']
    b = results['estimated_b']
    r_squared = results['r_squared']
    
    print(f"Estimated parameters: a = {a:.4f}, b = {b:.4f}")
    print(f"R-squared: {r_squared:.4f}")
    
    interpretations = interpret_parameters(a, b)
    
    print("\nParameter a (Customer Affinity):")
    print(interpretations['a_interpretation'])
    
    print("\nParameter b (Segment Barrier):")
    print(interpretations['b_interpretation'])
    
    print("\nRecommended Marketing Strategy:")
    print(interpretations['strategy'])
    
    # Step 4: Generate Report
    print("\nStep 4: Generate Report")
    generate_report(results, interpretations)
    
    print("\nAnalysis complete! See report.html for detailed results.")


def generate_report(results, interpretations):
    """Generate an HTML report with analysis results."""
    a = results['estimated_a']
    b = results['estimated_b']
    r_squared = results['r_squared']
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>E-commerce Customer Segmentation Analysis</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
            h1, h2 {{ color: #2c3e50; }}
            .summary {{ background-color: #f8f9fa; padding: 20px; border-radius: 5px; }}
            .interpretation {{ margin-top: 20px; background-color: #e8f4f8; padding: 15px; border-radius: 5px; }}
            .strategy {{ margin-top: 20px; background-color: #f0f8ea; padding: 15px; border-radius: 5px; }}
            table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
            .parameter {{ font-weight: bold; }}
            img {{ max-width: 100%; height: auto; margin: 20px 0; }}
            .footer {{ margin-top: 50px; font-size: 0.8em; color: #7f8c8d; }}
        </style>
    </head>
    <body>
        <h1>E-commerce Customer Segmentation Analysis</h1>
        
        <div class="summary">
            <h2>Stirling Measure Analysis Results</h2>
            <p>The analysis of customer segmentation patterns has revealed the following parameters:</p>
            <ul>
                <li><span class="parameter">Customer Affinity (a):</span> {a:.4f}</li>
                <li><span class="parameter">Segment Barrier (b):</span> {b:.4f}</li>
                <li><span class="parameter">Model Fit (R²):</span> {r_squared:.4f}</li>
            </ul>
        </div>
        
        <div class="interpretation">
            <h2>Parameter Interpretation</h2>
            
            <h3>Customer Affinity (a = {a:.2f})</h3>
            <p>{interpretations['a_interpretation']}</p>
            
            <h3>Segment Barrier (b = {b:.2f})</h3>
            <p>{interpretations['b_interpretation']}</p>
        </div>
        
        <div class="strategy">
            <h2>Recommended Marketing Strategy</h2>
            <p>{interpretations['strategy']}</p>
        </div>
        
        <h2>Analysis Visualizations</h2>
        
        <h3>Stirling Measure Analysis</h3>
        <img src="customer_segmentation_analysis.png" alt="Stirling Measure Analysis">
        
        <h3>Customer and Segment Counts Over Time</h3>
        <img src="customer_segments_time_series.png" alt="Customer and Segment Time Series">
        
        <h2>Data Summary</h2>
        <table>
            <tr>
                <th>Month</th>
                <th>Customers</th>
                <th>Segments</th>
                <th>Stirling Measure</th>
            </tr>
    """
    
    # Add data rows
    for i, period in enumerate(results['time_periods']):
        html += f"""
            <tr>
                <td>{period}</td>
                <td>{results['customer_counts'][i]}</td>
                <td>{results['segment_counts'][i]}</td>
                <td>{results['measures'][i]:.4f}</td>
            </tr>
        """
    
    html += """
        </table>
        
        <div class="footer">
            <p>Generated using the Stirling Measure analysis framework</p>
        </div>
    </body>
    </html>
    """
    
    # Save the HTML report
    with open('report.html', 'w') as f:
        f.write(html)


if __name__ == "__main__":
    main()
