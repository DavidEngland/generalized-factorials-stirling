"""
Hasse-Stirling Computational Framework

This module implements computational methods for special functions using the 
Hasse-Stirling framework, including:
- Stieltjes constants
- Zeta function values
- Roots of the digamma function

Author: David England
"""

import math
import numpy as np
from functools import lru_cache
from typing import List, Tuple, Dict, Callable, Union
import mpmath as mp

# Set default precision
mp.mp.dps = 50  # 50 decimal digits of precision

###########################################
# Basic Hasse coefficient computations
###########################################

@lru_cache(maxsize=10000)
def binomial(n: int, k: int) -> int:
    """Compute binomial coefficient (n choose k) with caching."""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    # Use symmetry to reduce computation
    if k > n - k:
        k = n - k
    
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    
    return result

def hasse_coefficient(m: int, n: int, alpha: float = 0, beta: float = 1, r: float = 0) -> float:
    """
    Compute the generalized Hasse coefficient H_{m,n}^{alpha,beta,r}.
    
    Args:
        m: First index
        n: Second index
        alpha, beta, r: Parameters for generalized Hasse coefficients
        
    Returns:
        The Hasse coefficient value
    """
    if n > m or n < 0 or m < 0:
        return 0
    
    if m == 0 and n == 0:
        return 1
    
    # Standard Hasse coefficients
    if alpha == 0 and beta == 1 and r == 0:
        return ((-1)**n * binomial(m, n)) / (m + 1)
    
    # Use recurrence for generalized coefficients
    result = 0
    for j in range(n+1):
        s_value = generalized_stirling(m, j, alpha, beta, r)
        result += ((-1)**(n-j) * binomial(n, j) * s_value) / (m + 1)
    
    return result

def compute_hasse_coefficients(max_m: int, alpha: float = 0, beta: float = 1, r: float = 0) -> List[List[float]]:
    """
    Compute a triangular array of Hasse coefficients up to max_m.
    
    Args:
        max_m: Maximum first index
        alpha, beta, r: Parameters for generalized Hasse coefficients
        
    Returns:
        A list of lists representing the triangular array
    """
    H = [[0 for _ in range(m+1)] for m in range(max_m+1)]
    
    H[0][0] = 1
    
    for m in range(1, max_m+1):
        H[m][0] = 1/(m+1)
        for n in range(1, m+1):
            # Use recurrence relation for efficiency
            H[m][n] = H[m-1][n-1] - ((m*alpha + n*beta + r)/(m+1)) * H[m-1][n]
    
    return H

@lru_cache(maxsize=10000)
def generalized_stirling(n: int, k: int, alpha: float = 0, beta: float = 1, r: float = 0) -> float:
    """
    Compute generalized Stirling numbers S(n,k;alpha,beta,r).
    
    Args:
        n, k: Indices
        alpha, beta, r: Parameters
        
    Returns:
        The generalized Stirling number
    """
    if k > n or k < 0 or n < 0:
        return 0
    
    if n == 0 and k == 0:
        return 1
    
    # Standard Stirling numbers of the second kind
    if alpha == 0 and beta == 1 and r == 0:
        if k == 0:
            return 0 if n > 0 else 1
        if k == n:
            return 1
        if k == 1:
            return 1
        
        return k * generalized_stirling(n-1, k, 0, 1, 0) + generalized_stirling(n-1, k-1, 0, 1, 0)
    
    # General recurrence relation
    return generalized_stirling(n-1, k-1, alpha, beta, r) + (beta*k - alpha*n + r) * generalized_stirling(n-1, k, alpha, beta, r)

###########################################
# Hasse operator applications
###########################################

def hasse_operator_action(f: Callable[[float], float], x: float, max_m: int, 
                          alpha: float = 0, beta: float = 1, r: float = 0) -> float:
    """
    Apply the generalized Hasse operator to a function f at point x.
    
    Args:
        f: Function to apply the operator to
        x: Point at which to evaluate
        max_m: Truncation order
        alpha, beta, r: Parameters
        
    Returns:
        Result of applying the Hasse operator
    """
    H = compute_hasse_coefficients(max_m, alpha, beta, r)
    result = 0
    
    for m in range(max_m + 1):
        term = 0
        for n in range(m + 1):
            term += H[m][n] * f(x + n)
        result += term
    
    return result

def log_power_function(t: float, power: int) -> float:
    """Function that returns log(t)^power."""
    return math.log(t)**power if t > 0 else 0

def hasse_operator_on_log_power(power: int, x: float, max_m: int, 
                                alpha: float = 0, beta: float = 1, r: float = 0) -> float:
    """
    Apply the generalized Hasse operator to log(t)^power at point x.
    
    Args:
        power: Power of the logarithm
        x: Point at which to evaluate
        max_m: Truncation order
        alpha, beta, r: Parameters
        
    Returns:
        Result of applying the Hasse operator to log(t)^power
    """
    H = compute_hasse_coefficients(max_m, alpha, beta, r)
    result = 0
    
    for n in range(1, max_m + 1):  # Start from 1 to avoid log(0)
        log_term = math.log(x + n)**power
        term_sum = 0
        for m in range(n, max_m + 1):
            term_sum += H[m][n]
        result += term_sum * log_term
    
    return result

###########################################
# Stieltjes constants computation
###########################################

def estimate_max_m_for_stieltjes(k: int, target_precision: float = 1e-15) -> int:
    """
    Estimate the required truncation order for Stieltjes constant computation.
    
    Args:
        k: Index of the Stieltjes constant
        target_precision: Desired precision
        
    Returns:
        Estimated truncation order
    """
    log_precision = -math.log10(target_precision)
    if k <= 5:
        return int(log_precision * 1.5) + 5
    else:
        return int(log_precision * (1 + 0.1*k)) + k + 5

def compute_stieltjes_constant(k: int, precision: float = 1e-15) -> float:
    """
    Compute the kth Stieltjes constant using the Hasse operator approach.
    
    Args:
        k: Index of the Stieltjes constant
        precision: Desired precision
        
    Returns:
        The Stieltjes constant gamma_k
    """
    if k == 0:
        # For gamma_0 (Euler's constant), use special parameterization
        alpha, beta, r = 1, -1, 0
    else:
        # For higher Stieltjes constants, use optimized parameters
        alpha = (k + 3) // 2
        beta = -(k + 4) // 2
        r = 0
    
    max_m = estimate_max_m_for_stieltjes(k, precision)
    
    # Apply the parameterized Hasse operator to log(t)^(k+1)
    result = hasse_operator_on_log_power(k+1, 1, max_m, alpha, beta, r)
    
    return -result / (k + 1)

def compute_stieltjes_constants(k_max: int, precision: float = 1e-15) -> List[float]:
    """
    Compute Stieltjes constants from gamma_0 to gamma_k_max.
    
    Args:
        k_max: Maximum index
        precision: Desired precision
        
    Returns:
        List of Stieltjes constants
    """
    return [compute_stieltjes_constant(k, precision) for k in range(k_max + 1)]

###########################################
# Zeta value computation
###########################################

def compute_zeta3(precision: float = 1e-15) -> float:
    """
    Compute zeta(3) using the Hasse-Stirling approach.
    
    Args:
        precision: Desired precision
        
    Returns:
        The value of zeta(3)
    """
    # For zeta(3), use parameters (1, -2, 0)
    alpha, beta, r = 1, -2, 0
    max_m = int(-math.log10(precision) * 2) + 10
    
    # The identity H_{1,-2,0}(log(t)^2)(1) = 2*zeta(3) + constants
    h_action = hasse_operator_on_log_power(2, 1, max_m, alpha, beta, r)
    
    # Extract zeta(3) from the identity
    pi_squared_over_6 = math.pi**2 / 6
    gamma = 0.57721566490153286060651209008240243104215933593992  # Euler's constant
    
    zeta3 = (h_action - gamma**2 - pi_squared_over_6) / 2
    
    return zeta3

def compute_zeta5(precision: float = 1e-15) -> float:
    """
    Compute zeta(5) using the Hasse-Stirling approach.
    
    Args:
        precision: Desired precision
        
    Returns:
        The value of zeta(5)
    """
    # For zeta(5), use parameters (2, -3, 0)
    alpha, beta, r = 2, -3, 0
    max_m = int(-math.log10(precision) * 2) + 15
    
    # The identity H_{2,-3,0}(log(t)^4)(1) = 24*zeta(5) - 10*pi^2*zeta(3) + ...
    h_action = hasse_operator_on_log_power(4, 1, max_m, alpha, beta, r)
    
    # Get zeta(3)
    zeta3 = compute_zeta3(precision)
    
    # Extract zeta(5) from the identity
    # Simplified version of the full identity
    zeta5 = (h_action + 10 * math.pi**2 * zeta3) / 24
    
    return zeta5

def compute_odd_zeta(n: int, precision: float = 1e-15) -> float:
    """
    Compute zeta(2n+1) for positive integer n.
    
    Args:
        n: Parameter such that 2n+1 is the zeta argument
        precision: Desired precision
        
    Returns:
        The value of zeta(2n+1)
    """
    if n == 0:
        raise ValueError("n must be positive")
    
    if n == 1:
        return compute_zeta3(precision)
    if n == 2:
        return compute_zeta5(precision)
    
    # For higher odd zeta values, use the general formula
    s = 2*n + 1
    
    # Parameters depend on whether s = 4k+1 or s = 4k+3
    if s % 4 == 1:
        # For zeta(4k+1)
        alpha = s // 2 - 1
        beta = -s // 2
    else:
        # For zeta(4k+3)
        alpha = s // 2
        beta = -s // 2 - 1
    
    r = 0
    max_m = int(-math.log10(precision) * 3) + 2*n + 10
    
    # Compute the necessary Hasse operator action
    # This is a simplified version that works for small n
    # For larger n, we would need a more sophisticated approach handling 
    # the relations to lower zeta values
    h_action = hasse_operator_on_log_power(2*n, 1, max_m, alpha, beta, r)
    
    # Adjust based on the specific identity for zeta(2n+1)
    # This is a placeholder - in practice we'd need the exact coefficient relations
    factorial_term = math.factorial(2*n)
    coefficient = factorial_term / ((-1)**n * 2)
    
    # This is a simplified approximation
    return h_action / coefficient

###########################################
# Digamma function roots
###########################################

def digamma_function(x: float) -> float:
    """
    Compute the digamma function psi(x).
    
    Args:
        x: Argument
        
    Returns:
        The value of psi(x)
    """
    return mp.psi(0, x)

def digamma_derivative(x: float) -> float:
    """
    Compute the derivative of the digamma function psi'(x).
    
    Args:
        x: Argument
        
    Returns:
        The value of psi'(x)
    """
    return mp.psi(1, x)

def newton_method_for_digamma(initial_guess: float, precision: float = 1e-15, max_iterations: int = 100) -> float:
    """
    Find a root of the digamma function using Newton's method.
    
    Args:
        initial_guess: Starting point
        precision: Desired precision
        max_iterations: Maximum number of iterations
        
    Returns:
        A root of the digamma function
    """
    x = initial_guess
    
    for _ in range(max_iterations):
        f_x = digamma_function(x)
        
        if abs(f_x) < precision:
            return float(x)
        
        f_prime_x = digamma_derivative(x)
        x = x - f_x / f_prime_x
    
    return float(x)

def find_digamma_roots(max_root: int = 10, precision: float = 1e-15) -> List[float]:
    """
    Find the first several roots of the digamma function.
    
    Args:
        max_root: Number of roots to find
        precision: Desired precision
        
    Returns:
        List of digamma function roots
    """
    roots = []
    
    # First root is special case
    roots.append(newton_method_for_digamma(1.5, precision))
    
    # For subsequent roots (n ≥ 2)
    for n in range(2, max_root + 1):
        # Initial approximation using Hasse-Stirling formula
        x_0 = n - 0.5 + 1/(24*(n - 0.5)) - 7/(960*(n - 0.5)**3)
        
        # Newton refinement
        x = newton_method_for_digamma(x_0, precision)
        roots.append(x)
    
    return roots

###########################################
# High precision computation
###########################################

def high_precision_hasse_coefficients(m: int, n: int, alpha: mp.mpf, beta: mp.mpf, r: mp.mpf, 
                                      prec: int = 100) -> mp.mpf:
    """
    Compute Hasse coefficients with arbitrary precision.
    
    Args:
        m, n: Indices
        alpha, beta, r: Parameters
        prec: Precision in decimal digits
        
    Returns:
        The Hasse coefficient with high precision
    """
    old_prec = mp.mp.dps
    mp.mp.dps = prec
    
    try:
        if n > m or n < 0 or m < 0:
            return mp.mpf(0)
        
        if m == 0 and n == 0:
            return mp.mpf(1)
        
        # Use recurrence for stability in high precision
        if n == 0:
            return mp.mpf(1) / (m + 1)
        
        prev_m = high_precision_hasse_coefficients(m-1, n-1, alpha, beta, r, prec)
        prev_n = high_precision_hasse_coefficients(m-1, n, alpha, beta, r, prec)
        
        return prev_m - ((m*alpha + n*beta + r)/(m+2)) * prev_n
    
    finally:
        mp.mp.dps = old_prec

###########################################
# Example usage and tests
###########################################

def run_examples():
    """Run some example computations as a demonstration."""
    print("Computing Stieltjes constants:")
    for k in range(5):
        gamma_k = compute_stieltjes_constant(k)
        print(f"γ_{k} = {gamma_k}")
    
    print("\nComputing zeta values:")
    zeta3 = compute_zeta3()
    print(f"ζ(3) = {zeta3}")
    zeta5 = compute_zeta5()
    print(f"ζ(5) = {zeta5}")
    
    print("\nFinding digamma roots:")
    roots = find_digamma_roots(5)
    for i, root in enumerate(roots):
        print(f"Root #{i+1}: {root}")

if __name__ == "__main__":
    run_examples()
