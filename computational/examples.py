"""
Examples of using the Hasse-Stirling computational framework.

This script demonstrates various applications of the Hasse-Stirling framework
for computing special values and functions.
"""

import math
import time
import matplotlib.pyplot as plt
import numpy as np
from hasse_stirling import (
    compute_stieltjes_constants,
    compute_odd_zeta,
    find_digamma_roots,
    hasse_operator_on_log_power
)

def benchmark_stieltjes_computation():
    """Benchmark the computation of Stieltjes constants."""
    print("Benchmarking Stieltjes constant computation...")
    
    k_values = [0, 1, 5, 10, 20]
    times = []
    
    for k in k_values:
        start_time = time.time()
        gamma_k = compute_stieltjes_constants(k)[-1]  # Get the k-th constant
        end_time = time.time()
        
        times.append(end_time - start_time)
        print(f"γ_{k} = {gamma_k:.15f} (computed in {times[-1]:.4f} seconds)")
    
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(k_values, times, 'o-', linewidth=2)
    plt.xlabel('k (Stieltjes constant index)')
    plt.ylabel('Computation time (seconds)')
    plt.title('Stieltjes Constant Computation Time')
    plt.grid(True)
    plt.savefig('stieltjes_benchmark.png')
    plt.close()

def compare_zeta_values():
    """Compute and compare odd zeta values."""
    print("\nComputing odd zeta values...")
    
    n_values = [1, 2, 3, 4, 5]  # For zeta(3), zeta(5), etc.
    zeta_values = []
    
    for n in n_values:
        zeta_value = compute_odd_zeta(n)
        zeta_values.append(zeta_value)
        print(f"ζ({2*n+1}) = {zeta_value:.15f}")
    
    # Compute the ratio of consecutive values
    ratios = [zeta_values[i]/zeta_values[i-1] for i in range(1, len(zeta_values))]
    print("\nRatios of consecutive odd zeta values:")
    for i, ratio in enumerate(ratios):
        print(f"ζ({2*(i+2)+1})/ζ({2*(i+1)+1}) = {ratio:.6f}")

def visualize_digamma_roots():
    """Find and visualize roots of the digamma function."""
    print("\nFinding digamma function roots...")
    
    roots = find_digamma_roots(20)
    
    # Print the first few roots
    for i, root in enumerate(roots[:5]):
        print(f"Root #{i+1}: {root:.15f}")
    
    # Plot the roots and their asymptotic behavior
    plt.figure(figsize=(12, 7))
    
    # Actual roots
    plt.scatter(range(1, len(roots)+1), roots, color='blue', label='Exact roots')
    
    # Asymptotic approximation
    n_values = np.arange(1, len(roots)+1)
    asymptotic = n_values - 0.5 + 1/(24*(n_values - 0.5))
    plt.plot(n_values, asymptotic, 'r--', label='Asymptotic approximation')
    
    plt.xlabel('Root index')
    plt.ylabel('Root value')
    plt.title('Roots of the Digamma Function ψ(x)')
    plt.grid(True)
    plt.legend()
    plt.savefig('digamma_roots.png')
    plt.close()

def explore_hasse_parameter_effects():
    """Explore how different parameters affect the Hasse operator."""
    print("\nExploring parameter effects on the Hasse operator...")
    
    # Define parameter sets to test
    parameter_sets = [
        (0, 1, 0, "Standard Hasse"),
        (1, -1, 0, "For Euler's constant"),
        (1, -2, 0, "For ζ(3)"),
        (2, -3, 0, "For ζ(5)"),
        (3, -4, 0, "For ζ(7)")
    ]
    
    # Evaluate Hasse operator on log(t)^2 at x=1 for each parameter set
    results = []
    for alpha, beta, r, name in parameter_sets:
        result = hasse_operator_on_log_power(2, 1, 20, alpha, beta, r)
        results.append(result)
        print(f"{name} (α={alpha}, β={beta}, r={r}): {result:.15f}")
    
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.bar([p[3] for p in parameter_sets], results)
    plt.ylabel('H(log(t)²)(1)')
    plt.title('Effect of Parameters on Hasse Operator')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('parameter_effects.png')
    plt.close()

if __name__ == "__main__":
    print("=== Hasse-Stirling Framework Examples ===\n")
    
    # Run all examples
    benchmark_stieltjes_computation()
    compare_zeta_values()
    visualize_digamma_roots()
    explore_hasse_parameter_effects()
    
    print("\nAll examples completed. Check the generated plots for visualizations.")
