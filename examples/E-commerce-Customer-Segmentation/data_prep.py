"""
Data preparation for E-commerce Customer Segmentation.

This script downloads and preprocesses the UCI Online Retail dataset
for use with the Stirling Measure analysis.
"""

import pandas as pd
import numpy as np
import os
import requests
from zipfile import ZipFile
from io import BytesIO
from datetime import datetime
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import warnings
import sys

# Increase recursion limit - temporary fix for deep recursion
sys.setrecursionlimit(10000)  # Increase from default (usually 1000)

warnings.filterwarnings('ignore')

# UCI Online Retail Dataset URL
DATASET_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
LOCAL_FILE = "online_retail.xlsx"


def download_dataset():
    """Download the UCI Online Retail dataset if not already available."""
    if os.path.exists(LOCAL_FILE):
        print(f"Dataset already exists at {LOCAL_FILE}")
        return
    
    print(f"Downloading dataset from {DATASET_URL}...")
    response = requests.get(DATASET_URL)
    
    if response.status_code == 200:
        with open(LOCAL_FILE, 'wb') as f:
            f.write(response.content)
        print(f"Dataset downloaded successfully to {LOCAL_FILE}")
    else:
        print(f"Failed to download dataset. Status code: {response.status_code}")


def load_and_clean_data():
    """Load and clean the Online Retail dataset."""
    print("Loading and cleaning data...")
    
    # Load the data
    df = pd.read_excel(LOCAL_FILE)
    
    # Basic information
    print(f"Original dataset shape: {df.shape}")
    
    # Clean the data
    # 1. Remove rows with missing customer IDs
    df = df.dropna(subset=['CustomerID'])
    
    # 2. Convert CustomerID to integer
    df['CustomerID'] = df['CustomerID'].astype(int)
    
    # 3. Remove canceled orders (quantity < 0)
    df = df[df['Quantity'] > 0]
    
    # 4. Remove rows with missing or invalid unit price
    df = df[df['UnitPrice'] > 0]
    
    # 5. Create order value column
    df['OrderValue'] = df['Quantity'] * df['UnitPrice']
    
    # 6. Convert InvoiceDate to datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    # 7. Extract date and month for aggregation
    df['InvoiceMonth'] = df['InvoiceDate'].dt.strftime('%Y-%m')
    
    # 8. Add country as a feature
    df['CountryCode'] = pd.factorize(df['Country'])[0]
    
    print(f"Cleaned dataset shape: {df.shape}")
    print(f"Date range: {df['InvoiceDate'].min()} to {df['InvoiceDate'].max()}")
    print(f"Number of customers: {df['CustomerID'].nunique()}")
    print(f"Number of products: {df['StockCode'].nunique()}")
    print(f"Number of countries: {df['Country'].nunique()}")
    
    return df


def create_customer_features(df):
    """Create customer-level features for segmentation."""
    print("Creating customer features...")
    
    # Group by customer and month
    monthly_stats = []
    
    for month, month_df in df.groupby('InvoiceMonth'):
        # Customer purchase stats
        customer_stats = month_df.groupby('CustomerID').agg({
            'InvoiceNo': 'nunique',  # Number of orders
            'OrderValue': ['sum', 'mean'],  # Total and average order value
            'Quantity': 'sum',  # Total quantity
            'StockCode': 'nunique',  # Number of unique products
            'CountryCode': 'first'  # Country
        })
        
        # Flatten the column hierarchy
        customer_stats.columns = [
            'orders', 'total_value', 'avg_order_value', 
            'total_quantity', 'unique_products', 'country'
        ]
        
        # Add month information
        customer_stats['month'] = month
        
        # Add recency (days since first purchase in dataset)
        latest_dates = month_df.groupby('CustomerID')['InvoiceDate'].max()
        first_date = df['InvoiceDate'].min()
        customer_stats['recency'] = (latest_dates - first_date).dt.days
        
        monthly_stats.append(customer_stats.reset_index())
    
    # Combine all months
    customer_features = pd.concat(monthly_stats)
    print(f"Created customer features: {customer_features.shape}")
    
    return customer_features


def perform_clustering(customer_features):
    """Perform clustering on customer features to determine segments."""
    print("Performing customer segmentation by month...")
    
    # Features for clustering
    cluster_features = [
        'orders', 'total_value', 'avg_order_value', 
        'total_quantity', 'unique_products', 'recency'
    ]
    
    results = []
    
    for month, month_data in customer_features.groupby('month'):
        # Skip months with too few customers
        if len(month_data) < 10:
            continue
            
        # Extract features
        X = month_data[cluster_features].copy()
        
        # Handle missing values
        X = X.fillna(X.mean())
        
        # Standardize features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Reduce dimensionality with PCA - use non-recursive approach
        # Limiting components to avoid deep recursion in SVD
        max_components = min(3, len(cluster_features))
        pca = PCA(n_components=max_components)
        X_pca = pca.fit_transform(X_scaled)
        
        # Use iterative approach for elbow method instead of recursive
        wcss = []
        max_clusters = min(10, len(month_data) // 5)  # Maximum clusters to try
        
        for i in range(2, max_clusters + 1):
            # Use explicit max_iter to prevent infinite loops
            kmeans = KMeans(n_clusters=i, random_state=42, n_init=10, max_iter=300)
            kmeans.fit(X_pca)
            wcss.append(kmeans.inertia_)
        
        # Find elbow point (iterative method)
        k = 2  # Default
        if len(wcss) > 2:
            diffs = np.diff(wcss)
            elbow_found = False
            for i in range(len(diffs) - 1):
                if diffs[i] / max(0.0001, diffs[i+1]) < 1.5:  # Threshold for elbow
                    k = i + 3  # +2 because we started at 2, +1 for the index
                    elbow_found = True
                    break
            
            # Safety check if no elbow found
            if not elbow_found:
                k = min(5, max_clusters)  # Reasonable default
        
        # Apply KMeans with optimal k
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10, max_iter=300)
        month_data['cluster'] = kmeans.fit_predict(X_pca)
        
        # Get number of customers and clusters
        n_customers = len(month_data)
        n_clusters = month_data['cluster'].nunique()
        
        # Save results
        results.append({
            'month': month,
            'n_customers': n_customers,
            'n_clusters': n_clusters,
            'data': month_data
        })
        
        print(f"Month {month}: {n_customers} customers in {n_clusters} segments")
    
    return results


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


def generate_analysis_inputs(clustering_results):
    """Generate inputs for Stirling Measure analysis."""
    # Extract time periods, customer counts, and segment counts
    time_periods = [r['month'] for r in clustering_results]
    customer_counts = [r['n_customers'] for r in clustering_results]
    segment_counts = [r['n_clusters'] for r in clustering_results]
    
    # Create summary dataframe
    summary_df = pd.DataFrame({
        'month': time_periods,
        'n_customers': customer_counts,
        'n_segments': segment_counts
    })
    
    # Save summary to CSV
    summary_df.to_csv('segment_summary.csv', index=False)
    print(f"Saved segment summary to segment_summary.csv")
    
    # Plot customer and segment counts
    plt.figure(figsize=(12, 6))
    plt.plot(time_periods, customer_counts, 'o-', label='Customers')
    plt.plot(time_periods, segment_counts, 's-', label='Segments')
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Customer and Segment Counts by Month')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('customer_segment_counts.png')
    plt.close()
    
    return time_periods, customer_counts, segment_counts


if __name__ == "__main__":
    try:
        # Create directory for outputs
        os.makedirs('outputs', exist_ok=True)
        
        # Download and prepare data
        download_dataset()
        df = load_and_clean_data()
        
        # Generate customer features
        customer_features = create_customer_features(df)

        # Use customer features for clustering
        cluster_features = [
            'orders', 'total_value', 'avg_order_value',
            'total_quantity', 'unique_products', 'recency'
        ]
        features = customer_features[cluster_features].fillna(0).values

        # Apply Stirling Partitioning Algorithm
        optimal_k, optimal_labels, a_fit, b_fit, stirling_results = stirling_partitioning_algorithm_customer(features)

        # Visualize clustering results
        plt.figure(figsize=(10, 6))
        plt.hist(optimal_labels, bins=optimal_k, color='lightgreen', edgecolor='black')
        plt.title(f'Customer Segment Distribution (k={optimal_k})')
        plt.xlabel('Segment Label')
        plt.ylabel('Number of Customers')
        plt.tight_layout()
        plt.savefig('customer_segment_distribution.png')
        plt.close()

        print("Customer segment distribution plot saved as 'customer_segment_distribution.png'")

        # Remove or comment out any code that references 'clustering_results'
    except RecursionError:
        print("ERROR: Maximum recursion depth exceeded.")
        print("Suggestion: Try processing a smaller dataset or modify the clustering approach.")
        print("You can also increase Python's recursion limit with sys.setrecursionlimit()")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {str(e)}")
        sys.exit(1)
