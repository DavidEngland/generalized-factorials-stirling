"""
Approximation of Stieltjes constants using the Hasse operator method.

This module implements the numerical calculation of Stieltjes constants
based on the identity:
    γ_{k-1}(x) = -(1/k) * H([log t]^k)(x)
where H is the full Hasse shift operator.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpmath import mp
from typing import List, Tuple
import time

# Set precision for high-accuracy calculations
mp.dps = 30  # Decimal places of precision

def hasse_coefficient(m: int, n: int) -> mp.mpf:
    """
    Calculate the Hasse coefficient H_{m,n}.
    
    Args:
        m: First index
        n: Second index
    
    Returns:
        The Hasse coefficient as an mpmath high-precision float
    """
    if n < 0 or n > m:
        return mp.mpf(0)
    if m == 0 and n == 0:
        return mp.mpf(1)
    
    # H_{m,n} = (-1)^n * binomial(m, n) / (m+1)
    binomial = mp.binomial(m, n)
    sign = 1 if n % 2 == 0 else -1
    return mp.mpf(sign * binomial) / mp.mpf(m + 1)


def compute_hasse_coefficients(max_m: int) -> List[List[mp.mpf]]:
    """
    Precompute Hasse coefficients up to a given order.
    
    Args:
        max_m: Maximum order to compute
        
    Returns:
        2D list of coefficients H_{m,n} for m=0..max_m and n=0..m
    """
    coeffs = []
    for m in range(max_m + 1):
        row = [hasse_coefficient(m, n) for n in range(m + 1)]
        coeffs.append(row)
    return coeffs


def approximate_stieltjes(k: int, x: mp.mpf, max_m: int, 
                         hasse_coeffs: List[List[mp.mpf]]) -> mp.mpf:
    """
    Approximate the (k-1)th Stieltjes constant γ_{k-1}(x) using truncated Hasse sum.
    
    Args:
        k: Power of logarithm (k≥1)
        x: Argument (typically x=1 for classical Stieltjes constants)
        max_m: Maximum order for truncation
        hasse_coeffs: Precomputed Hasse coefficients
        
    Returns:
        Approximation of γ_{k-1}(x)
    """
    if k < 1:
        raise ValueError("k must be at least 1 to calculate a valid Stieltjes constant")
    
    # Compute the Hasse operator applied to [log(t)]^k at x more efficiently
    # by pre-computing logarithm values and reordering summation
    log_values = [mp.log(x + n) for n in range(max_m + 1)]
    log_powers = [mp.power(log_val, k) for log_val in log_values]
    
    # Sum over all combinations of m and n
    hasse_sum = mp.mpf(0)
    for n in range(max_m + 1):
        # For each n, sum over all valid m where n ≤ m ≤ max_m
        term_sum = mp.mpf(0)
        for m in range(n, max_m + 1):
            term_sum += hasse_coeffs[m][n]
        hasse_sum += term_sum * log_powers[n]
    
    # γ_{k-1}(x) = -(1/k) * H([log t]^k)(x)
    return -hasse_sum / k


def convergence_analysis(k: int, x: mp.mpf, max_orders: List[int], 
                        known_value: mp.mpf = None) -> Tuple[List[mp.mpf], List[mp.mpf]]:
    """
    Analyze convergence of the Hasse sum approximation for γ_{k-1}(x).
    
    Args:
        k: Power of logarithm (k≥1)
        x: Argument
        max_orders: List of maximum orders to test
        known_value: Exact value, if available, for error calculation
        
    Returns:
        Tuple of (approximations, errors)
    """
    approximations = []
    errors = []
    
    for max_m in max_orders:
        hasse_coeffs = compute_hasse_coefficients(max_m)
        approx = approximate_stieltjes(k, x, max_m, hasse_coeffs)
        approximations.append(approx)
        
        if known_value is not None:
            error = abs(approx - known_value)
            errors.append(error)
    
    return approximations, errors


def main():
    """
    Main function to demonstrate approximation of Stieltjes constants.
    """
    # Known values of first few Stieltjes constants
    known_values = {
        0: mp.euler,  # Euler-Mascheroni constant
        1: mp.mpf("-0.0728158454836767248605863758749013191377363383")
    }
    
    print("Approximating Stieltjes constants using the Hasse operator method")
    print("-" * 70)
    
    # Test various truncation orders
    max_orders = [10, 20, 50, 100, 200, 500]
    
    # Approximation for γ₀ (Euler's constant)
    print("Approximations for γ₀ (Euler's constant):")
    approximations, errors = convergence_analysis(1, mp.mpf(1), max_orders, known_values[0])
    
    for i, max_m in enumerate(max_orders):
        print(f"  m = {max_m:4d}: {approximations[i]:.15f} (error: {errors[i]:.15e})")
    
    # Approximation for γ₁
    print("\nApproximations for γ₁:")
    approximations, errors = convergence_analysis(2, mp.mpf(1), max_orders, known_values[1])
    
    for i, max_m in enumerate(max_orders):
        print(f"  m = {max_m:4d}: {approximations[i]:.15f} (error: {errors[i]:.15e})")
    
    # Plot convergence rates with improved labels
    plt.figure(figsize=(10, 6))
    plt.loglog(max_orders, errors, 'bo-', label='Empirical error')
    
    # Add reference line for O(1/m) convergence
    # Note: This is an expected asymptotic behavior, not a rigorous bound
    ref_line = [errors[0] * max_orders[0] / m for m in max_orders]
    plt.loglog(max_orders, ref_line, 'r--', label='O(1/m) reference')
    
    plt.xlabel('Truncation order (m)')
    plt.ylabel('Absolute error')
    plt.title(f'Convergence Analysis for Stieltjes Constant γ{k-1}')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'stieltjes_gamma{k-1}_convergence.png')
    
    # Timing experiment
    print("\nTiming for γ₀ calculation (m = 100):")
    start_time = time.time()
    hasse_coeffs = compute_hasse_coefficients(100)
    approx = approximate_stieltjes(1, mp.mpf(1), 100, hasse_coeffs)
    elapsed = time.time() - start_time
    print(f"  Computed value: {approx:.15f}")
    print(f"  Time taken: {elapsed:.4f} seconds")


if __name__ == "__main__":
    main()
