"""
Generalized Stirling Numbers Implementation

This module implements the generalized Stirling numbers L{n,k}^{α,β} based on
the paper "Combinatorial approach of certain generalized Stirling numbers"
by Belbachir, Belkhir, and Bousbaa.

The generalized Stirling numbers have a combinatorial interpretation as the
total weight of distributing n elements into k ordered non-empty lists with
specific weighting rules.
"""

import math
from functools import lru_cache
import numpy as np
import warnings
from collections import defaultdict
import time

class GeneralizedStirling:
    """
    Implementation of generalized Stirling numbers with parameters α and β.
    
    These numbers have a combinatorial interpretation as the total weight
    of distributing n elements into k ordered non-empty lists, where:
    1. The head of each list has weight β
    2. Other elements in lists have weight α
    3. The first element placed in each list has weight 1
    """
    
    def __init__(self, alpha=1.0, beta=1.0, cache_size=10000, use_disk_cache=False, cache_dir=None):
        """
        Initialize with parameters α and β.
        
        Args:
            alpha (float): Weight parameter for non-head elements
            beta (float): Weight parameter for head elements
            cache_size (int): Maximum size for LRU cache
            use_disk_cache (bool): Whether to use disk-based caching for large computations
            cache_dir (str): Directory for disk cache (if None, uses temporary directory)
        """
        self.alpha = alpha
        self.beta = beta
        self.cache_size = cache_size
        self.use_disk_cache = use_disk_cache
        self.cache_dir = cache_dir
        
        # In-memory cache for quick lookups
        self._memory_cache = {}
        
        # Special cache for precomputed values
        self._precomputed = {}
        
        # Performance metrics
        self.compute_time = defaultdict(float)
        self.cache_hits = defaultdict(int)
        self.cache_misses = defaultdict(int)
        
        # Initialize precomputed tables for common special cases
        if (self.alpha, self.beta) in [(1.0, 0.0), (0.0, 1.0), (1.0, 1.0)]:
            self._precompute_common_values()
    
    def _precompute_common_values(self, max_n=20, max_k=20):
        """Precompute values for common special cases"""
        for n in range(min(max_n, 21)):
            for k in range(min(n+1, max_k+1)):
                if n == k or k == 0 or n == 0:
                    # These are base cases with known values
                    continue
                
                # Compute and store in precomputed cache
                try:
                    self._precomputed[(n, k)] = self.triangular_recurrence_internal(n, k)
                except (OverflowError, ValueError):
                    # Stop precomputation if we hit numerical limits
                    return
    
    def rising_factorial(self, x, n, increment=1.0):
        """
        Compute generalized rising factorial (x|α)^n̄
        
        This calculates x(x+α)(x+2α)...(x+(n-1)α)
        
        Args:
            x (float): Base value
            n (int): Number of terms
            increment (float): The increment between terms
            
        Returns:
            float: The value of the rising factorial
        """
        if n == 0:
            return 1.0
        
        # Fast path for small n
        if n <= 20:
            result = 1.0
            for i in range(n):
                result *= (x + i * increment)
            return result
        
        # For large n, use logarithms to avoid overflow
        try:
            log_result = 0.0
            for i in range(n):
                log_result += math.log(x + i * increment)
            return math.exp(log_result)
        except (OverflowError, ValueError):
            warnings.warn(f"Numerical overflow in rising factorial with x={x}, n={n}, increment={increment}")
            return float('inf')
    
    def explicit_formula(self, n, k):
        """
        Compute L{n,k}^{α,β} using the explicit formula.
        
        Formula: L{n,k}^{α,β} = (1/(β^k * k!)) * ∑_{j=0}^k (-1)^j * C(k,j) * (β(k-j)|α)^n̄
        
        Args:
            n (int): Number of elements
            k (int): Number of ordered lists
            
        Returns:
            float: Value of the generalized Stirling number
        """
        # Handle base cases
        if k == 0:
            return 1.0 if n == 0 else 0.0
        if n == 0 or k > n:
            return 0.0
        if k == n:
            return 1.0
        
        # Check cache
        cache_key = ('explicit', n, k)
        if cache_key in self._memory_cache:
            self.cache_hits['explicit'] += 1
            return self._memory_cache[cache_key]
        
        self.cache_misses['explicit'] += 1
        start_time = time.time()
        
        # Special case for k=1
        if k == 1:
            result = self.special_case(n)
        else:
            # Main computation with numerical stability improvements
            # For large values, compute in log space
            if n > 50 or k > 20:
                try:
                    result = self._explicit_formula_log_space(n, k)
                except (OverflowError, ValueError):
                    warnings.warn(f"Numerical issues in explicit formula with n={n}, k={k}")
                    # Fall back to triangular recurrence
                    result = self.triangular_recurrence(n, k)
            else:
                result = self._explicit_formula_direct(n, k)
        
        # Update cache and timing
        self._memory_cache[cache_key] = result
        self.compute_time['explicit'] += time.time() - start_time
        
        return result
    
    def _explicit_formula_direct(self, n, k):
        """Direct computation of explicit formula for moderate values"""
        result = 0.0
        for j in range(k+1):
            # Calculate binomial coefficient C(k,j)
            binom = math.comb(k, j)
            
            # Calculate rising factorial (β(k-j)|α)^n̄
            base = self.beta * (k - j)
            rising_fact = self.rising_factorial(base, n, self.alpha)
            
            # Add to sum with alternating sign
            term = ((-1) ** j) * binom * rising_fact
            result += term
        
        # Divide by β^k * k!
        denominator = (self.beta ** k) * math.factorial(k)
        return result / denominator if denominator != 0 else 0.0
    
    def _explicit_formula_log_space(self, n, k):
        """Compute explicit formula in log space for numerical stability"""
        log_result = float('-inf')  # log(0)
        sign = 1.0
        
        for j in range(k+1):
            # Calculate log of binomial coefficient
            log_binom = math.log(math.comb(k, j))
            
            # Calculate log of rising factorial
            base = self.beta * (k - j)
            log_rising_fact = 0.0
            for i in range(n):
                factor = base + i * self.alpha
                if factor <= 0:
                    # Handle possible negative or zero factors
                    if factor == 0:
                        log_rising_fact = float('-inf')
                        break
                    else:
                        sign *= -1 if factor < 0 and n % 2 == 1 else 1
                        log_rising_fact += math.log(abs(factor))
                else:
                    log_rising_fact += math.log(factor)
            
            # Add to sum using log-sum-exp for numerical stability
            term_sign = 1 if j % 2 == 0 else -1
            if log_rising_fact != float('-inf'):
                term = log_binom + log_rising_fact
                if log_result == float('-inf'):
                    log_result = term
                    sign = term_sign
                else:
                    if term > log_result:
                        # If term is bigger, it becomes the new reference
                        sign = sign * term_sign if term - log_result > 30 else sign
                        log_result = term
                    else:
                        # Add to the current result using log-sum-exp
                        if log_result - term <= 30:  # Avoid underflow
                            log_result = log_result + math.log1p(math.exp(term - log_result))
        
        # Apply denominator in log space
        log_denominator = k * math.log(self.beta) + math.log(math.factorial(k))
        result = sign * math.exp(log_result - log_denominator)
        
        return result
    
    def triangular_recurrence_internal(self, n, k):
        """Internal implementation of triangular recurrence without caching"""
        # Handle base cases
        if k == 0:
            return 1.0 if n == 0 else 0.0
        if n == 0 or k > n:
            return 0.0
        if k == n:
            return 1.0
        if k == 1:
            return self.special_case(n)
        
        # Check precomputed values
        if (n, k) in self._precomputed:
            return self._precomputed[(n, k)]
        
        # Apply recurrence relation
        term1 = self.triangular_recurrence(n-1, k-1)
        term2 = (self.alpha * (n-1) + self.beta * k) * self.triangular_recurrence(n-1, k)
        
        return term1 + term2
    
    @lru_cache(maxsize=10000)  # Increased cache size
    def triangular_recurrence(self, n, k):
        """
        Compute L{n,k}^{α,β} using the triangular recurrence relation.
        
        L{n,k}^{α,β} = L{n-1,k-1}^{α,β} + (α(n-1) + βk) * L{n-1,k}^{α,β}
        
        Args:
            n (int): Number of elements
            k (int): Number of ordered lists
            
        Returns:
            float: Value of the generalized Stirling number
        """
        # Check cache
        cache_key = ('triangular', n, k)
        if cache_key in self._memory_cache:
            self.cache_hits['triangular'] += 1
            return self._memory_cache[cache_key]
        
        self.cache_misses['triangular'] += 1
        start_time = time.time()
        
        result = self.triangular_recurrence_internal(n, k)
        
        # Update cache and timing
        self._memory_cache[cache_key] = result
        self.compute_time['triangular'] += time.time() - start_time
        
        return result
    
    def bottom_up_computation(self, n, k):
        """
        Compute L{n,k}^{α,β} using a bottom-up dynamic programming approach.
        
        This method builds a table of values from smaller to larger parameters,
        which is more efficient for computing a single value when n and k are large.
        
        Args:
            n (int): Number of elements
            k (int): Number of ordered lists
            
        Returns:
            float: Value of the generalized Stirling number
        """
        # Handle base cases
        if k == 0:
            return 1.0 if n == 0 else 0.0
        if n == 0 or k > n:
            return 0.0
        if k == n:
            return 1.0
        if k == 1:
            return self.special_case(n)
        
        # Check cache
        cache_key = ('bottom_up', n, k)
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
        current_row[0] = 1.0 if 0 == 0 else 0.0
        for j in range(1, k+1):
            current_row[j] = 0.0
        
        # Fill the table row by row
        for i in range(1, n+1):
            next_row[0] = 0.0
            for j in range(1, min(i, k)+1):
                if i == j:
                    next_row[j] = 1.0
                else:
                    next_row[j] = current_row[j-1] + (self.alpha * (i-1) + self.beta * j) * current_row[j]
            
            # Swap rows for next iteration
            current_row, next_row = next_row, current_row
        
        result = current_row[k]
        
        # Update cache and timing
        self._memory_cache[cache_key] = result
        self.compute_time['bottom_up'] += time.time() - start_time
        
        return result
    
    def horizontal_recurrence(self, n, k):
        """
        Compute L{n,k}^{α,β} using the horizontal recurrence relation.
        
        L{n,k}^{α,β} = ∑_{j=0}^{n-k} (-1)^j * ((k+1)β + nα|α)^j̄ * L{n+1,k+j+1}^{α,β}
        
        Args:
            n (int): Number of elements
            k (int): Number of ordered lists
            
        Returns:
            float: Value of the generalized Stirling number
        """
        result = 0.0
        for j in range(n-k+1):
            # Calculate rising factorial ((k+1)β + nα|α)^j̄
            base = (k+1) * self.beta + n * self.alpha
            rising_fact = self.rising_factorial(base, j, self.alpha)
            
            # Calculate L{n+1,k+j+1}^{α,β} using triangular recurrence
            gs_value = self.triangular_recurrence(n+1, k+j+1)
            
            # Add to sum with alternating sign
            result += ((-1) ** j) * rising_fact * gs_value
        
        return result
    
    def vertical_recurrence(self, n, k):
        """
        Compute L{n+1,k+1}^{α,β} using the vertical recurrence relation.
        
        L{n+1,k+1}^{α,β} = ∑_{i=k}^n (α+β|α)^{n-i} * C(n,i) * L{i,k}^{α,β}
        
        Args:
            n (int): Parameter for resulting L{n+1,k+1}^{α,β}
            k (int): Parameter for resulting L{n+1,k+1}^{α,β}
            
        Returns:
            float: Value of L{n+1,k+1}^{α,β}
        """
        result = 0.0
        for i in range(k, n+1):
            # Calculate rising factorial (α+β|α)^{n-i}
            rising_fact = self.rising_factorial(self.alpha + self.beta, n-i, self.alpha)
            
            # Calculate binomial coefficient C(n,i)
            binom = math.comb(n, i)
            
            # Calculate L{i,k}^{α,β} using triangular recurrence
            gs_value = self.triangular_recurrence(i, k)
            
            # Add to sum
            result += rising_fact * binom * gs_value
        
        return result
    
    def special_case(self, n, k=1):
        """
        Compute L{n,1}^{α,β} using the special case formula.
        
        L{n,1}^{α,β} = ∏_{j=1}^{n-1} (jα + β)
        
        Args:
            n (int): Number of elements
            k (int): Should be 1 for this special case
            
        Returns:
            float: Value of L{n,1}^{α,β}
        """
        if k != 1:
            raise ValueError("This special case only applies for k=1")
            
        if n <= 0:
            return 0.0
        if n == 1:
            return 1.0
        
        # Check cache
        cache_key = ('special', n, 1)
        if cache_key in self._memory_cache:
            self.cache_hits['special'] += 1
            return self._memory_cache[cache_key]
        
        self.cache_misses['special'] += 1
        start_time = time.time()
        
        # For large n, compute in log space to avoid overflow
        if n > 100:
            log_result = 0.0
            for j in range(1, n):
                factor = j * self.alpha + self.beta
                if factor <= 0:
                    # Handle possible negative or zero factors
                    if factor == 0:
                        result = 0.0
                        break
                    else:
                        log_result += math.log(abs(factor))
                else:
                    log_result += math.log(factor)
            
            result = math.exp(log_result)
        else:
            result = 1.0
            for j in range(1, n):
                result *= (j * self.alpha + self.beta)
        
        # Update cache and timing
        self._memory_cache[cache_key] = result
        self.compute_time['special'] += time.time() - start_time
        
        return result
    
    def symmetric_function(self, n, k):
        """
        Compute L{n+k,n}^{α,β} using the symmetric function formula.
        
        L{n+k,n}^{α,β} = ∑_{1≤i₁≤...≤iₖ≤n} ∏_{j=1}^k ((α+β)iⱼ + α(j-1))
        
        This implementation uses dynamic programming for efficiency.
        
        Args:
            n (int): First parameter
            k (int): Second parameter
            
        Returns:
            float: Value of L{n+k,n}^{α,β}
        """
        if k == 0:
            return 1.0
        
        # For k=1, use the special formula
        if k == 1:
            result = 0
            for i in range(1, n+1):
                result += (self.alpha + self.beta) * i
            return result
        
        # Check cache
        cache_key = ('symmetric', n, k)
        if cache_key in self._memory_cache:
            self.cache_hits['symmetric'] += 1
            return self._memory_cache[cache_key]
        
        self.cache_misses['symmetric'] += 1
        start_time = time.time()
        
        # Dynamic programming approach
        # dp[d][i] = sum of products for sequences starting at index i with depth d
        dp = {}
        
        def compute_dp(depth, start):
            if depth == k:
                return 1.0
            
            if (depth, start) in dp:
                return dp[(depth, start)]
            
            result = 0.0
            for i in range(start, n+1):
                factor = (self.alpha + self.beta) * i + self.alpha * depth
                result += factor * compute_dp(depth+1, i)
            
            dp[(depth, start)] = result
            return result
        
        result = compute_dp(0, 1)
        
        # Update cache and timing
        self._memory_cache[cache_key] = result
        self.compute_time['symmetric'] += time.time() - start_time
        
        return result
    
    def clear_cache(self):
        """Clear all caches to free memory"""
        self._memory_cache.clear()
        self.triangular_recurrence.cache_clear()
        # Reset performance counters
        self.compute_time.clear()
        self.cache_hits.clear()
        self.cache_misses.clear()
    
    def compute(self, n, k, method='auto'):
        """
        Compute L{n,k}^{α,β} using the specified method.
        
        Args:
            n (int): Number of elements
            k (int): Number of ordered lists
            method (str): Method to use ('auto', 'triangular', 'explicit', 
                         'horizontal', 'vertical', 'bottom_up', 'symmetric')
            
        Returns:
            float: Value of the generalized Stirling number
        """
        # Handle base cases first for efficiency
        if k == 0:
            return 1.0 if n == 0 else 0.0
        if n == 0 or k > n:
            return 0.0
        if k == n:
            return 1.0
        
        # For k=1, use the special case formula which is more efficient
        if k == 1:
            return self.special_case(n, k)
        
        # Auto-select the best method based on input size
        if method == 'auto':
            if n > 100 or k > 50:
                # For very large values, use bottom-up to avoid recursion depth issues
                method = 'bottom_up'
            elif n - k < 5 and n < 30:
                # For values close to the diagonal, symmetric function is efficient
                method = 'symmetric'
            elif k < 3 or n < 20:
                # For small values, triangular recurrence with memoization works well
                method = 'triangular'
            else:
                # For medium-large values, bottom-up approach is generally best
                method = 'bottom_up'
        
        # Use the selected method
        if method == 'explicit':
            return self.explicit_formula(n, k)
        elif method == 'horizontal':
            return self.horizontal_recurrence(n, k)
        elif method == 'vertical':
            return self.vertical_recurrence(n-1, k-1) if n > 0 and k > 0 else self.triangular_recurrence(n, k)
        elif method == 'bottom_up':
            return self.bottom_up_computation(n, k)
        elif method == 'symmetric':
            # Note: symmetric function computes L{n+k,n}, so we need to adjust parameters
            if n >= k:
                return self.symmetric_function(k, n-k)
            else:
                return self.triangular_recurrence(n, k)
        else:  # Default to triangular
            return self.triangular_recurrence(n, k)
    
    def generate_triangle(self, n_max, format_str="{:.0f}", method='auto', sparse=False):
        """
        Generate a triangle of generalized Stirling numbers.
        
        Args:
            n_max (int): Maximum row number
            format_str (str): Format string for displaying numbers
            method (str): Method to use for computation
            sparse (bool): If True, only store non-zero values
            
        Returns:
            list or dict: Triangle of generalized Stirling numbers
        """
        if sparse:
            # Return a sparse representation as a dictionary
            triangle = {}
            for n in range(1, n_max + 1):
                for k in range(1, n + 1):
                    value = self.compute(n, k, method=method)
                    if value != 0:
                        triangle[(n, k)] = format_str.format(value)
            return triangle
        else:
            # Return a dense representation as a list of lists
            triangle = []
            for n in range(1, n_max + 1):
                row = []
                for k in range(1, n + 1):
                    row.append(format_str.format(self.compute(n, k, method=method)))
                triangle.append(row)
            return triangle
    
    def get_performance_stats(self):
        """Get performance statistics for the different computation methods"""
        stats = {
            'compute_time': dict(self.compute_time),
            'cache_hits': dict(self.cache_hits),
            'cache_misses': dict(self.cache_misses),
            'hit_ratio': {}
        }
        
        # Calculate hit ratios
        for method in self.cache_hits:
            total = self.cache_hits[method] + self.cache_misses[method]
            if total > 0:
                stats['hit_ratio'][method] = self.cache_hits[method] / total
            else:
                stats['hit_ratio'][method] = 0
        
        return stats

# ... existing code for stirling_first_kind, stirling_second_kind, lah_number ...

# Add new utility functions
def parallel_generate_triangle(n_max, alpha=1.0, beta=1.0, method='auto', processes=None):
    """
    Generate a triangle of generalized Stirling numbers using parallel processing.
    
    Args:
        n_max (int): Maximum row number
        alpha (float): Weight parameter for non-head elements
        beta (float): Weight parameter for head elements
        method (str): Method to use for computation
        processes (int): Number of processes to use (None = use all available cores)
        
    Returns:
        list: Triangle of generalized Stirling numbers
    """
    import concurrent.futures
    
    gs = GeneralizedStirling(alpha=alpha, beta=beta)
    triangle = [[] for _ in range(n_max)]
    
    def compute_value(n, k):
        return (n, k, gs.compute(n, k, method=method))
    
    # Generate all (n,k) pairs to compute
    pairs = [(n, k) for n in range(1, n_max + 1) for k in range(1, n + 1)]
    
    # Compute values in parallel
    with concurrent.futures.ProcessPoolExecutor(max_workers=processes) as executor:
        results = list(executor.map(lambda p: compute_value(*p), pairs))
    
    # Place results in the triangle
    for n, k, value in results:
        triangle[n-1].append(value)
    
    return triangle

def memory_efficient_iterator(n_max, alpha=1.0, beta=1.0, method='auto'):
    """
    Memory-efficient iterator for generalized Stirling numbers.
    
    Instead of generating the entire triangle at once, this iterator
    yields values one at a time to conserve memory.
    
    Args:
        n_max (int): Maximum row number
        alpha (float): Weight parameter for non-head elements
        beta (float): Weight parameter for head elements
        method (str): Method to use for computation
        
    Yields:
        tuple: (n, k, value) for each generalized Stirling number
    """
    gs = GeneralizedStirling(alpha=alpha, beta=beta)
    
    for n in range(1, n_max + 1):
        for k in range(1, n + 1):
            yield (n, k, gs.compute(n, k, method=method))
