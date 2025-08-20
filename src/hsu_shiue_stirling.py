"""
Hsu-Shiue Generalized Stirling Numbers Implementation

This module implements the Hsu-Shiue generalized Stirling numbers S(n,k;α,β,r)
based on the paper "A unified approach to generalized Stirling numbers"
by Hsu and Shiue (1998).

This is a more general framework that includes the L_{n,k}^{α,β} numbers
as a special case.
"""

import math
from functools import lru_cache
import numpy as np
import warnings
from collections import defaultdict
import time

class HsuShiueStirling:
    """
    Implementation of Hsu-Shiue generalized Stirling numbers S(n,k;α,β,r).
    
    These numbers are defined through the falling factorial relation:
    (x|α)^n = Σ_{k=0}^n S(n,k;α,β,r)(x-r|β)^k
    
    They include various Stirling-type numbers as special cases.
    """
    
    def __init__(self, alpha=0.0, beta=1.0, r=0.0, cache_size=10000):
        """
        Initialize with parameters α, β, and r.
        
        Args:
            alpha (float): First parameter of the generalized Stirling numbers
            beta (float): Second parameter of the generalized Stirling numbers
            r (float): Third parameter of the generalized Stirling numbers
            cache_size (int): Maximum size for LRU cache
        """
        self.alpha = alpha
        self.beta = beta
        self.r = r
        self.cache_size = cache_size
        
        # In-memory cache for quick lookups
        self._memory_cache = {}
        
        # Performance metrics
        self.compute_time = defaultdict(float)
        self.cache_hits = defaultdict(int)
        self.cache_misses = defaultdict(int)
    
    def falling_factorial(self, x, n, increment=1.0):
        """
        Compute generalized falling factorial (x|θ)^n
        
        This calculates x(x-θ)(x-2θ)...(x-(n-1)θ)
        
        Args:
            x (float): Base value
            n (int): Number of terms
            increment (float): The increment between terms
            
        Returns:
            float: The value of the falling factorial
        """
        if n == 0:
            return 1.0
        
        # Fast path for small n
        if n <= 20:
            result = 1.0
            for i in range(n):
                result *= (x - i * increment)
            return result
        
        # For large n, use logarithms to avoid overflow
        try:
            log_result = 0.0
            for i in range(n):
                factor = x - i * increment
                if factor <= 0:
                    # Handle possible negative or zero factors
                    if factor == 0:
                        return 0.0
                    else:
                        log_result += math.log(abs(factor))
                        if (n - i) % 2 == 1:  # Odd number of negative factors
                            sign = -1
                else:
                    log_result += math.log(factor)
            
            return math.exp(log_result)
        except (OverflowError, ValueError):
            warnings.warn(f"Numerical overflow in falling factorial with x={x}, n={n}, increment={increment}")
            return float('inf')
    
    @lru_cache(maxsize=10000)
    def triangular_recurrence(self, n, k):
        """
        Compute S(n,k;α,β,r) using the triangular recurrence relation.
        
        S(n,k;α,β,r) = S(n-1,k-1;α,β,r) + (βk - α(n-1) + r)S(n-1,k;α,β,r)
        
        Args:
            n (int): First parameter
            k (int): Second parameter
            
        Returns:
            float: Value of the generalized Stirling number
        """
        # Check cache
        cache_key = (n, k)
        if cache_key in self._memory_cache:
            self.cache_hits['triangular'] += 1
            return self._memory_cache[cache_key]
        
        self.cache_misses['triangular'] += 1
        start_time = time.time()
        
        # Base cases
        if k == 0:
            if n == 0:
                result = 1.0
            else:
                result = self.r ** n
        elif n == 0 or k > n:
            result = 0.0
        else:
            # Apply recurrence relation
            term1 = self.triangular_recurrence(n-1, k-1)
            term2 = (self.beta * k - self.alpha * (n-1) + self.r) * self.triangular_recurrence(n-1, k)
            result = term1 + term2
        
        # Update cache and timing
        self._memory_cache[cache_key] = result
        self.compute_time['triangular'] += time.time() - start_time
        
        return result
    
    def bottom_up_computation(self, n, k):
        """
        Compute S(n,k;α,β,r) using bottom-up dynamic programming.
        
        This method is more efficient for large values of n and k.
        
        Args:
            n (int): First parameter
            k (int): Second parameter
            
        Returns:
            float: Value of the generalized Stirling number
        """
        # Check cache
        cache_key = (n, k)
        if cache_key in self._memory_cache:
            self.cache_hits['bottom_up'] += 1
            return self._memory_cache[cache_key]
        
        self.cache_misses['bottom_up'] += 1
        start_time = time.time()
        
        # Create a 2D table for dynamic programming
        # Only need to store two rows at a time to save memory
        current_row = [0.0] * (k+1)
        next_row = [0.0] * (k+1)
        
        # Base cases
        if 0 == 0:
            current_row[0] = 1.0
        for j in range(1, k+1):
            current_row[j] = 0.0
        
        # Fill the table row by row
        for i in range(1, n+1):
            # Base case for k=0: r^i
            next_row[0] = self.r ** i
            
            for j in range(1, min(i, k)+1):
                # Recurrence relation
                next_row[j] = current_row[j-1] + (self.beta * j - self.alpha * (i-1) + self.r) * current_row[j]
            
            # Swap rows for next iteration
            current_row, next_row = next_row, current_row
        
        result = current_row[k]
        
        # Update cache and timing
        self._memory_cache[cache_key] = result
        self.compute_time['bottom_up'] += time.time() - start_time
        
        return result
    
    def compute(self, n, k, method='auto'):
        """
        Compute S(n,k;α,β,r) using the specified method.
        
        Args:
            n (int): First parameter
            k (int): Second parameter
            method (str): Method to use ('auto', 'triangular', 'bottom_up')
            
        Returns:
            float: Value of the generalized Stirling number
        """
        # Auto-select the best method based on input size
        if method == 'auto':
            if n > 50 or k > 25:
                # For very large values, use bottom-up to avoid recursion depth issues
                method = 'bottom_up'
            else:
                # For smaller values, triangular recurrence with memoization works well
                method = 'triangular'
        
        # Use the selected method
        if method == 'bottom_up':
            return self.bottom_up_computation(n, k)
        else:  # Default to triangular
            return self.triangular_recurrence(n, k)
    
    def generate_triangle(self, n_max, format_str="{:.0f}"):
        """
        Generate a triangle of generalized Stirling numbers.
        
        Args:
            n_max (int): Maximum row number
            format_str (str): Format string for displaying numbers
            
        Returns:
            list: Triangle of generalized Stirling numbers
        """
        triangle = []
        for n in range(n_max + 1):
            row = []
            for k in range(min(n, n_max) + 1):
                row.append(format_str.format(self.compute(n, k)))
            triangle.append(row)
        return triangle
    
    def clear_cache(self):
        """Clear all caches to free memory"""
        self._memory_cache.clear()
        self.triangular_recurrence.cache_clear()
        # Reset performance counters
        self.compute_time.clear()
        self.cache_hits.clear()
        self.cache_misses.clear()


# Conversion functions between different notations

def convert_L_to_hsu_shiue(n, k, alpha, beta):
    """
    Convert L_{n,k}^{α,β} parameters to S(n,k;α,β,r) parameters.
    
    Args:
        n (int): First parameter of L_{n,k}^{α,β}
        k (int): Second parameter of L_{n,k}^{α,β}
        alpha (float): Weight parameter for non-head elements
        beta (float): Weight parameter for head elements
        
    Returns:
        tuple: (n, k, alpha, beta, r) parameters for S(n,k;α,β,r)
    """
    return n, k, -alpha, beta, 0


def convert_hsu_shiue_to_L(n, k, alpha, beta, r):
    """
    Convert S(n,k;α,β,r) parameters to L_{n,k}^{α,β} parameters if possible.
    
    Args:
        n (int): First parameter of S(n,k;α,β,r)
        k (int): Second parameter of S(n,k;α,β,r)
        alpha (float): First parameter of S(n,k;α,β,r)
        beta (float): Second parameter of S(n,k;α,β,r)
        r (float): Third parameter of S(n,k;α,β,r)
        
    Returns:
        tuple: (n, k, alpha, beta) parameters for L_{n,k}^{α,β}
        
    Raises:
        ValueError: If r ≠ 0, as L_{n,k}^{α,β} is only defined for r = 0
    """
    if r != 0:
        raise ValueError("Cannot convert to L notation when r ≠ 0")
    return n, k, -alpha, beta


def compute_from_L_notation(n, k, alpha, beta):
    """
    Compute the Hsu-Shiue generalized Stirling number using L_{n,k}^{α,β} parameters.
    
    Args:
        n (int): First parameter of L_{n,k}^{α,β}
        k (int): Second parameter of L_{n,k}^{α,β}
        alpha (float): Weight parameter for non-head elements
        beta (float): Weight parameter for head elements
        
    Returns:
        float: The value of the generalized Stirling number
    """
    n, k, alpha, beta, r = convert_L_to_hsu_shiue(n, k, alpha, beta)
    gs = HsuShiueStirling(alpha=alpha, beta=beta, r=r)
    return gs.compute(n, k)


# Special cases of generalized Stirling numbers

def r_stirling_first_kind(n, k, r):
    """
    Compute the r-Stirling number of the first kind.
    
    These count permutations of n elements with k cycles where
    the elements 1,2,...,r are in different cycles.
    
    Args:
        n (int): Number of elements
        k (int): Number of cycles
        r (int): Parameter r
        
    Returns:
        float: Value of the r-Stirling number of the first kind
    """
    gs = HsuShiueStirling(alpha=-1.0, beta=0.0, r=r)
    return gs.compute(n, k)


def r_stirling_second_kind(n, k, r):
    """
    Compute the r-Stirling number of the second kind.
    
    These count partitions of n elements into k non-empty subsets where
    the elements 1,2,...,r are in different subsets.
    
    Args:
        n (int): Number of elements
        k (int): Number of subsets
        r (int): Parameter r
        
    Returns:
        float: Value of the r-Stirling number of the second kind
    """
    gs = HsuShiueStirling(alpha=0.0, beta=1.0, r=r)
    return gs.compute(n, k)


def whitney_first_kind(n, k, m):
    """
    Compute the Whitney number of the first kind.
    
    Args:
        n (int): First parameter
        k (int): Second parameter
        m (float): Parameter of the Dowling lattice
        
    Returns:
        float: Value of the Whitney number of the first kind
    """
    gs = HsuShiueStirling(alpha=-m, beta=0.0, r=0.0)
    return (-1)**(n-k) * gs.compute(n, k)


def whitney_second_kind(n, k, m):
    """
    Compute the Whitney number of the second kind.
    
    Args:
        n (int): First parameter
        k (int): Second parameter
        m (float): Parameter of the Dowling lattice
        
    Returns:
        float: Value of the Whitney number of the second kind
    """
    gs = HsuShiueStirling(alpha=0.0, beta=m, r=0.0)
    return gs.compute(n, k)
