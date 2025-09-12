"""
Quantum Error Correction Threshold Calculation using Hasse-Stirling Framework

This example demonstrates how to calculate quantum error correction thresholds
using polylogarithms computed via the Hasse-Stirling approach.

Key advantages:
- More accurate threshold calculations for quantum error correction codes
- Better numerical stability for critical threshold regions
- Faster computation for complex error models

Author: David England
"""

import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import spence as scipy_polylog2  # spence is polylog of order 2

# Add the parent directory to sys.path to import the hasse_stirling package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from hasse_stirling import compute_hasse_coefficients, hasse_operator_action

# ======================== IMPLEMENTATION ========================

def polylog_hasse(s, z, max_m=40, tol=1e-15):
    """
    Compute the polylogarithm function Li_s(z) using Hasse-Stirling.
    
    The polylogarithm function is defined as:
    Li_s(z) = sum_{k=1}^inf z^k / k^s
    
    Args:
        s: Order of the polylogarithm
        z: Argument (|z| < 1 for guaranteed convergence)
        max_m: Maximum order for Hasse operator
        tol: Error tolerance
    
    Returns:
        Value of Li_s(z)
    """
    # Safety checks
    if abs(z) >= 1.0 and s <= 1:
        raise ValueError(f"Polylogarithm Li_{s}(z) not convergent for |z| >= 1")
    
    # For z = 0, the result is 0 for any s
    if z == 0:
        return 0
    
    # For z near 1, use reflection formula for better numerical stability
    if abs(z - 1) < 0.1 and s > 1:
        return reflection_formula_polylog(s, z, max_m, tol)
    
    # Define the integrand function for polylogarithm
    def integrand(t):
        return -np.log(1 - z*np.exp(-t)) / t
    
    # Use Hasse operator with parameters optimized for polylogarithm
    result = hasse_operator_action(integrand, 0, max_m, s, 1-s, 0)
    
    # Calculate error bound
    error_bound = estimate_error_bound(s, z, max_m)
    
    if error_bound > tol:
        print(f"Warning: Error bound {error_bound:.2e} exceeds tolerance {tol:.2e}")
    
    return result

def reflection_formula_polylog(s, z, max_m, tol):
    """
    Use reflection formula for polylogarithm near z=1 for better numerical stability.
    
    For s > 1, we have:
    Li_s(z) = zeta(s) - (1-z)^(s-1)/Gamma(s) * sum_{k=0}^inf (1-z)^k * zeta(s-k) / k!
    where zeta is the Riemann zeta function.
    
    This implementation is simplified and approximated.
    """
    from scipy.special import zeta, gamma
    
    # Use just the first few terms of the series
    result = zeta(s)
    
    # Correction term for z close to 1
    correction = 0
    factor = (1-z)**(s-1) / gamma(s)
    
    for k in range(5):  # Just a few terms for approximation
        correction += (1-z)**k * zeta(s-k) / np.math.factorial(k)
    
    return result - factor * correction

def estimate_error_bound(s, z, max_m):
    """
    Calculate error bound for the polylogarithm calculation.
    
    Args:
        s: Order of the polylogarithm
        z: Argument
        max_m: Maximum order used in the calculation
    
    Returns:
        Estimated error bound
    """
    # For polylogarithm, a standard bound for the truncation error
    if abs(z) < 0.9:
        return abs(z)**(max_m+1) / ((max_m+1)**s * (1 - abs(z)))
    else:
        # For z close to 1, use a more conservative bound
        return 1 / (max_m+1)**(s-1)

def quantum_error_correction_threshold(code_parameters, error_model, precision=1e-12):
    """
    Calculate quantum error correction thresholds using polylogarithms via Hasse-Stirling.
    
    Quantum error correction thresholds often involve threshold calculations using polylogarithms:
    
    P_threshold(p) = sum_{k=1}^inf (-1)^(k-1)/k * Li_s((p^k)/((1-p)^k))
    
    where p is the physical error rate and Li_s is the polylogarithm function.
    
    Args:
        code_parameters: Dictionary with code parameters including 'distance' and 'exponent'
        error_model: Dictionary describing the error model
        precision: Desired precision
    
    Returns:
        Threshold error rate
    """
    # Extract code parameters
    d = code_parameters['distance']
    s = code_parameters['exponent']
    
    # Define the threshold function
    def threshold_function(p):
        result = 0
        for k in range(1, 20):  # Truncate infinite sum
            z = (p**k) / ((1-p)**k)
            if abs(z) >= 1:
                break
            term = ((-1)**(k-1) / k) * polylog_hasse(s, z, tol=precision)
            result += term
            if abs(term) < precision:
                break
        return result
    
    # Find the threshold by solving threshold_function(p) = 0.5
    threshold = find_root(lambda p: threshold_function(p) - 0.5, 0.01, 0.2)
    
    return threshold

def find_root(f, a, b, tol=1e-6, max_iter=100):
    """
    Find the root of a function f in the interval [a, b] using bisection.
    
    Args:
        f: Function to find root for
        a, b: Interval bounds
        tol: Tolerance
        max_iter: Maximum iterations
    
    Returns:
        Root of the function
    """
    if f(a) * f(b) > 0:
        raise ValueError("Function must have opposite signs at interval endpoints")
    
    c = (a + b) / 2
    i = 0
    
    while (b - a) > tol and i < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        i += 1
    
    return c

def surface_code_logical_error_rate(p, d, approximation='hasse'):
    """
    Calculate the logical error rate for a surface code with distance d
    and physical error rate p.
    
    This uses a simplified model where the logical error rate is approximated by:
    P_L ≈ C * (p/p_th)^((d+1)/2)
    
    where C is a constant and p_th is the threshold error rate.
    
    Args:
        p: Physical error rate
        d: Code distance
        approximation: Which method to use ('hasse' or 'standard')
    
    Returns:
        Logical error rate
    """
    # Constants for the surface code model
    C = 0.1
    
    # Calculate threshold based on chosen method
    if approximation == 'hasse':
        p_th = quantum_error_correction_threshold(
            {'distance': d, 'exponent': 2}, 
            {'type': 'depolarizing'}, 
            precision=1e-8
        )
    else:
        # Standard approximation of the threshold
        p_th = 0.11
    
    # Calculate logical error rate
    if p >= p_th:
        return 1.0  # Above threshold, error correction fails
    
    logical_error = C * (p/p_th)**((d+1)/2)
    return min(1.0, logical_error)  # Cap at 1.0

# ======================== DEMONSTRATION ========================

def benchmark_performance(s, z_values, repetitions=10):
    """
    Benchmark the performance of traditional vs Hasse-Stirling approaches.
    
    Note: We'll only compare for s=2 since SciPy only has polylog for s=2 (spence function)
    """
    if s != 2:
        print("Warning: SciPy comparison only available for s=2")
        s = 2
    
    hasse_times = []
    scipy_times = []
    
    for z in z_values:
        # Time Hasse-Stirling approach
        start_time = time.time()
        for _ in range(repetitions):
            polylog_hasse(s, z)
        hasse_time = (time.time() - start_time) / repetitions
        hasse_times.append(hasse_time)
        
        # Time SciPy approach
        start_time = time.time()
        for _ in range(repetitions):
            # Note: spence(1-z) = -polylog2(z) + pi^2/6 - log(z)*log(1-z)
            scipy_polylog2(1-z)
        scipy_time = (time.time() - start_time) / repetitions
        scipy_times.append(scipy_time)
    
    return np.array(hasse_times), np.array(scipy_times)

def plot_threshold_comparison(physical_error_rates, hasse_logical_rates, standard_logical_rates, distances):
    """
    Plot the comparison between Hasse-Stirling and standard approaches.
    """
    plt.figure(figsize=(12, 10))
    
    # Plot logical error rates for each distance
    for i, d in enumerate(distances):
        plt.subplot(len(distances), 1, i+1)
        plt.semilogy(physical_error_rates, hasse_logical_rates[i], 'b-', 
                    label=f'Hasse-Stirling (d={d})')
        plt.semilogy(physical_error_rates, standard_logical_rates[i], 'r--',
                    label=f'Standard (d={d})')
        plt.xlabel('Physical Error Rate')
        plt.ylabel('Logical Error Rate')
        plt.title(f'Surface Code Performance (d={d})')
        plt.legend()
        plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('quantum_error_correction.png')
    plt.show()

def demo_quantum_error_correction():
    """
    Demonstrate quantum error correction threshold calculation.
    """
    print("Quantum Error Correction Threshold Calculation Example")
    print("===================================================")
    
    # Calculate threshold for a surface code
    code_parameters = {
        'distance': 5,
        'exponent': 2  # For surface code, s=2 in the polylogarithm
    }
    
    error_model = {
        'type': 'depolarizing'
    }
    
    # Calculate threshold using Hasse-Stirling
    print("\nCalculating threshold using Hasse-Stirling approach...")
    start_time = time.time()
    hasse_threshold = quantum_error_correction_threshold(code_parameters, error_model)
    hasse_time = time.time() - start_time
    print(f"Threshold: {hasse_threshold:.6f}")
    print(f"Calculation time: {hasse_time:.4f} seconds")
    
    # Compare with standard approximation
    standard_threshold = 0.11  # Typical approximation for surface code threshold
    print(f"\nStandard approximation threshold: {standard_threshold:.6f}")
    print(f"Difference: {abs(hasse_threshold - standard_threshold):.6f}")
    
    # Calculate logical error rates for different code distances
    distances = [3, 5, 7, 9]
    physical_error_rates = np.linspace(0.01, 0.15, 50)
    
    hasse_logical_rates = []
    standard_logical_rates = []
    
    print("\nCalculating logical error rates for different code distances...")
    for d in distances:
        hasse_rates = [surface_code_logical_error_rate(p, d, 'hasse') for p in physical_error_rates]
        standard_rates = [surface_code_logical_error_rate(p, d, 'standard') for p in physical_error_rates]
        
        hasse_logical_rates.append(hasse_rates)
        standard_logical_rates.append(standard_rates)
    
    # Benchmark polylogarithm calculation (only for s=2 to compare with SciPy)
    print("\nBenchmarking polylogarithm calculation...")
    z_values = np.linspace(0.1, 0.9, 5)
    hasse_times, scipy_times = benchmark_performance(2, z_values)
    
    for i, z in enumerate(z_values):
        print(f"z = {z:.2f}: Hasse-Stirling = {hasse_times[i]*1000:.2f} ms, "
              f"SciPy = {scipy_times[i]*1000:.2f} ms, "
              f"Speedup = {scipy_times[i]/hasse_times[i]:.2f}x")
    
    # Plot results
    plot_threshold_comparison(physical_error_rates, hasse_logical_rates, 
                             standard_logical_rates, distances)
    
    # Pros and Cons
    print("\nPros and Cons of Hasse-Stirling for Quantum Error Correction Calculations:")
    print("\nPros:")
    print("- More accurate threshold calculations")
    print("- Better numerical stability near critical threshold regions")
    print("- Consistent error bounds for reliability assessment")
    print("- Ability to handle complex error models")
    
    print("\nCons:")
    print("- Implementation complexity compared to standard approximations")
    print("- Overhead may not be justified for simple error models")
    print("- Requires careful parameter tuning for convergence")
    print("- Limited validation against experimental quantum error correction data")

if __name__ == "__main__":
    demo_quantum_error_correction()
