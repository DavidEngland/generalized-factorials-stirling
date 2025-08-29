"""
Basic usage examples for the generalized Stirling number library.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# Add the parent directory to the path so we can import the library
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.stirling_core import StirlingComputation, BellPolynomials, ParameterEstimation
from src.stirling_applications import StirlingPartitioning, InverseFunctionEstimation

def example_stirling_numbers():
    """Example: Computing generalized Stirling numbers"""
    print("\n=== Example: Computing Generalized Stirling Numbers ===")
    
    # Create instances for different parameter sets
    stirling_1st = StirlingComputation(1, 0)  # Stirling numbers of the first kind
    stirling_2nd = StirlingComputation(0, 1)  # Stirling numbers of the second kind
    lah = StirlingComputation(1, 1)           # Lah numbers
    
    # Compute some values
    n, k = 5, 2
    print(f"S({n},{k}) with (a,b) = (1,0) [Stirling 1st kind]: {stirling_1st.compute(n, k)}")
    print(f"S({n},{k}) with (a,b) = (0,1) [Stirling 2nd kind]: {stirling_2nd.compute(n, k)}")
    print(f"S({n},{k}) with (a,b) = (1,1) [Lah numbers]: {lah.compute(n, k)}")
    
    # Generate a table of values
    n_max = 6
    print("\nTable of generalized Stirling numbers (a=0.5, b=0.5):")
    gstirling = StirlingComputation(0.5, 0.5)
    table = gstirling.table(n_max)
    
    # Print the table
    for n in range(n_max + 1):
        row = [f"{table[n, k]:.1f}" if k <= n else "" for k in range(n_max + 1)]
        print(f"n={n}: {', '.join(row)}")

def example_bell_polynomials():
    """Example: Computing Bell polynomials"""
    print("\n=== Example: Computing Bell Polynomials ===")
    
    # Define some coefficients
    coeffs = [0, 1, 2, 3, 4]  # x_1, x_2, x_3, x_4
    
    # Compute partial Bell polynomials
    print("Partial Bell polynomials:")
    for n in range(1, 5):
        for k in range(1, n + 1):
            value = BellPolynomials.partial_bell(n, k, coeffs)
            print(f"B_{n,k}({coeffs[1:]}) = {value}")
    
    # Compute complete Bell polynomials
    print("\nComplete Bell polynomials:")
    for n in range(1, 5):
        value = BellPolynomials.complete_bell(n, coeffs)
        print(f"B_{n}({coeffs[1:]}) = {value}")

def example_parameter_estimation():
    """Example: Estimating parameters from inverse function pairs"""
    print("\n=== Example: Parameter Estimation ===")
    
    # Example: exp(x) - 1 and ln(1+x)
    exp_coeffs = [0, 1, 1/2, 1/6, 1/24]  # e^x - 1
    log_coeffs = [0, 1, -1/2, 1/3, -1/4]  # ln(1+x)
    
    a, b = ParameterEstimation.estimate_from_inverse_pair(exp_coeffs, log_coeffs)
    print(f"Estimated parameters for exp(x)-1 and ln(1+x): a={a:.4f}, b={b:.4f}")
    print(f"Expected parameters: a=1.0, b=-1.0")
    
    # Example: x/(1-x) and x/(1+x)
    geom_coeffs = [0, 1, 1, 1, 1]  # x/(1-x)
    alt_coeffs = [0, 1, -1, 1, -1]  # x/(1+x)
    
    a, b = ParameterEstimation.estimate_from_inverse_pair(geom_coeffs, alt_coeffs)
    print(f"Estimated parameters for x/(1-x) and x/(1+x): a={a:.4f}, b={b:.4f}")
    print(f"Expected parameters: a=0.0, b=-1.0")

def example_clustering():
    """Example: Clustering with Stirling partitioning"""
    print("\n=== Example: Clustering with Stirling Partitioning ===")
    
    # Generate synthetic data with three clusters
    np.random.seed(42)
    n_samples = 300
    
    # Cluster 1: (0, 0)
    cluster1 = np.random.randn(n_samples // 3, 2) * 0.5 + np.array([0, 0])
    
    # Cluster 2: (5, 0)
    cluster2 = np.random.randn(n_samples // 3, 2) * 0.5 + np.array([5, 0])
    
    # Cluster 3: (2.5, 5)
    cluster3 = np.random.randn(n_samples // 3, 2) * 0.5 + np.array([2.5, 5])
    
    # Combine data
    data = np.vstack([cluster1, cluster2, cluster3])
    
    # Apply Stirling partitioning
    partitioner = StirlingPartitioning(min_k=2, max_k=10, use_bell_polynomials=True)
    results = partitioner.fit(data)
    
    # Print results
    print(f"Optimal number of clusters: {results['optimal_k']}")
    print(f"Estimated parameters: a={results['a_param']:.4f}, b={results['b_param']:.4f}")
    print(f"Silhouette score: {results['silhouette']:.4f}")
    
    # Visualize results
    plt.figure(figsize=(10, 6))
    plt.scatter(data[:, 0], data[:, 1], c=results['labels'], cmap='viridis', s=30)
    plt.title(f"Cluster Assignments (k={results['optimal_k']})")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.colorbar(label="Cluster")
    plt.tight_layout()
    plt.savefig("clustering_example.png")
    plt.close()
    
    # Generate silhouette curve
    partitioner.plot_silhouette_curve(results, save_path="silhouette_curve.png")
    
    # Generate parameter space plot
    partitioner.plot_parameter_space(results['a_param'], results['b_param'], 
                                     save_path="parameter_space.png")
    
    print("Visualizations saved as clustering_example.png, silhouette_curve.png, and parameter_space.png")

def example_inverse_function():
    """Example: Estimating inverse functions"""
    print("\n=== Example: Inverse Function Estimation ===")
    
    # Define the function coefficients (exp(x) - 1)
    exp_coeffs = [0, 1, 1/2, 1/6, 1/24, 1/120]
    
    # Estimate the inverse function
    estimator = InverseFunctionEstimation()
    log_coeffs = estimator.estimate_inverse_function(exp_coeffs, degree=5, a=1, b=-1)
    
    # Print the results
    print("Original function (exp(x) - 1) coefficients:")
    for i, coef in enumerate(exp_coeffs):
        print(f"  x^{i}: {coef}")
    
    print("\nEstimated inverse function (ln(1+x)) coefficients:")
    for i, coef in enumerate(log_coeffs):
        print(f"  x^{i}: {coef}")
    
    print("\nActual ln(1+x) coefficients:")
    actual_log = [0, 1, -1/2, 1/3, -1/4, 1/5]
    for i, coef in enumerate(actual_log):
        print(f"  x^{i}: {coef}")

def main():
    """Run all examples"""
    print("=== Generalized Stirling Numbers and Bell Polynomials Library Examples ===")
    
    example_stirling_numbers()
    example_bell_polynomials()
    example_parameter_estimation()
    example_clustering()
    example_inverse_function()
    
    print("\nAll examples completed successfully!")

if __name__ == "__main__":
    main()
