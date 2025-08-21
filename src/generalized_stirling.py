"""
Generalized Stirling Numbers Implementation

This module implements the generalized Stirling numbers L{n,k}^{α,β} based on
the paper "Combinatorial approach of certain generalized Stirling numbers"
by Belbachir, Belkhir, and Bousbaa.

The generalized Stirling numbers have a combinatorial interpretation as the
total weight of distributing n elements into k ordered non-empty lists with
specific weighting rules.

Examples:
    Basic usage:
        >>> gs = GeneralizedStirling(alpha=1.0, beta=1.0)
        >>> gs.compute(3, 2)
        6.0
    
    Special cases:
        >>> # Stirling numbers of the first kind
        >>> s1 = GeneralizedStirling(alpha=1.0, beta=0.0)
        >>> s1.compute(4, 2)
        11.0
        
        >>> # Stirling numbers of the second kind
        >>> s2 = GeneralizedStirling(alpha=0.0, beta=1.0)
        >>> s2.compute(4, 2)
        7.0
        
        >>> # Lah numbers
        >>> lah = GeneralizedStirling(alpha=1.0, beta=1.0)
        >>> lah.compute(4, 2)
        36.0
"""

import math
from functools import lru_cache
import numpy as np
import warnings
from collections import defaultdict
import time
import os
import pickle
from typing import Dict, List, Tuple, Union, Optional, Callable, Iterator, Any, Set, DefaultDict

# Try to import scipy for enhanced numerical stability
try:
    import scipy.special
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GeneralizedStirling:
    """
    Implementation of generalized Stirling numbers with parameters α and β.
    
    These numbers have a combinatorial interpretation as the total weight
    of distributing n elements into k ordered non-empty lists, where:
    1. The head of each list has weight β
    2. Other elements in lists have weight α
    3. The first element placed in each list has weight 1
    
    Attributes:
        alpha (float): Weight parameter for non-head elements
        beta (float): Weight parameter for head elements
        cache_size (int): Maximum size for LRU cache
        use_disk_cache (bool): Whether to use disk-based caching for large computations
        cache_dir (str): Directory for disk cache
        _memory_cache (Dict): In-memory cache for quick lookups
        _precomputed (Dict): Cache for precomputed values
        compute_time (DefaultDict): Time spent in each computation method
        cache_hits (DefaultDict): Number of cache hits for each method
        cache_misses (DefaultDict): Number of cache misses for each method
    """
    
    def __init__(self, alpha: float = 1.0, beta: float = 1.0, 
                 cache_size: int = 10000, use_disk_cache: bool = False, 
                 cache_dir: Optional[str] = None) -> None:
        """
        Initialize with parameters α and β.
        
        Args:
            alpha: Weight parameter for non-head elements
            beta: Weight parameter for head elements
            cache_size: Maximum size for LRU cache
            use_disk_cache: Whether to use disk-based caching for large computations
            cache_dir: Directory for disk cache (if None, uses temporary directory)
            
        Raises:
            ValueError: If alpha or beta are not valid floating point numbers
        """
        # Validate input parameters
        if not isinstance(alpha, (int, float)) or math.isnan(alpha) or math.isinf(alpha):
            raise ValueError(f"alpha must be a valid number, got {alpha}")
        if not isinstance(beta, (int, float)) or math.isnan(beta) or math.isinf(beta):
            raise ValueError(f"beta must be a valid number, got {beta}")
            
        self.alpha = float(alpha)
        self.beta = float(beta)
        self.cache_size = cache_size
        self.use_disk_cache = use_disk_cache
        
        # Set up disk cache directory
        if use_disk_cache:
            if cache_dir is None:
                import tempfile
                self.cache_dir = os.path.join(tempfile.gettempdir(), f"gsn_cache_{hash((alpha, beta))}")
            else:
                self.cache_dir = cache_dir
                
            # Create cache directory if it doesn't exist
            if not os.path.exists(self.cache_dir):
                os.makedirs(self.cache_dir)
                logger.info(f"Created disk cache directory: {self.cache_dir}")
        else:
            self.cache_dir = cache_dir
        
        # In-memory cache for quick lookups
        self._memory_cache: Dict[Any, float] = {}
        
        # Special cache for precomputed values
        self._precomputed: Dict[Tuple[int, int], float] = {}
        
        # Performance metrics
        self.compute_time: DefaultDict[str, float] = defaultdict(float)
        self.cache_hits: DefaultDict[str, int] = defaultdict(int)
        self.cache_misses: DefaultDict[str, int] = defaultdict(int)
        
        # Initialize precomputed tables for common special cases
        if (self.alpha, self.beta) in [(1.0, 0.0), (0.0, 1.0), (1.0, 1.0)]:
            self._precompute_common_values()
    
    def _precompute_common_values(self, max_n: int = 20, max_k: int = 20) -> None:
        """
        Precompute values for common special cases.
        
        This method calculates and stores values for common parameters to improve performance
        for frequently used values.
        
        Args:
            max_n: Maximum value of n to precompute
            max_k: Maximum value of k to precompute
            
        Returns:
            None
        """
        logger.info(f"Precomputing common values for α={self.alpha}, β={self.beta}")
        
        count = 0
        for n in range(min(max_n, 21)):
            for k in range(min(n+1, max_k+1)):
                if n == k or k == 0 or n == 0:
                    # These are base cases with known values
                    continue
                
                # Compute and store in precomputed cache
                try:
                    self._precomputed[(n, k)] = self.triangular_recurrence_internal(n, k)
                    count += 1
                except (OverflowError, ValueError):
                    # Stop precomputation if we hit numerical limits
                    logger.warning(f"Stopped precomputation at n={n}, k={k} due to numerical issues")
                    return
        
        logger.info(f"Precomputed {count} values for α={self.alpha}, β={self.beta}")
    
    def _get_disk_cache_key(self, method: str, n: int, k: int) -> str:
        """
        Generate a filename for disk caching based on method and parameters.
        
        Args:
            method: The calculation method used
            n: First parameter
            k: Second parameter
            
        Returns:
            A unique filename for the cache entry
        """
        return os.path.join(self.cache_dir, f"{method}_{n}_{k}_{self.alpha}_{self.beta}.pkl")
    
    def _save_to_disk_cache(self, key: str, value: float) -> None:
        """
        Save a value to the disk cache.
        
        Args:
            key: Cache key
            value: Value to cache
            
        Returns:
            None
        """
        if not self.use_disk_cache:
            return
            
        try:
            with open(key, 'wb') as f:
                pickle.dump(value, f)
        except (OSError, pickle.PickleError) as e:
            logger.warning(f"Failed to save to disk cache: {e}")
    
    def _load_from_disk_cache(self, key: str) -> Optional[float]:
        """
        Load a value from the disk cache.
        
        Args:
            key: Cache key
            
        Returns:
            The cached value or None if not found
        """
        if not self.use_disk_cache or not os.path.exists(key):
            return None
            
        try:
            with open(key, 'rb') as f:
                return pickle.load(f)
        except (OSError, pickle.PickleError) as e:
            logger.warning(f"Failed to load from disk cache: {e}")
            return None
    
    def rising_factorial(self, x: float, n: int, increment: float = 1.0) -> float:
        """
        Compute generalized rising factorial (x|α)^n̄
        
        This calculates x(x+α)(x+2α)...(x+(n-1)α)
        
        Uses scipy.special.poch for enhanced numerical stability when available.
        
        Args:
            x: Base value
            n: Number of terms
            increment: The increment between terms
            
        Returns:
            The value of the rising factorial
            
        Examples:
            >>> gs = GeneralizedStirling()
            >>> gs.rising_factorial(2.0, 3, 0.5)
            8.75  # 2.0 * 2.5 * 3.0
            
            >>> gs.rising_factorial(1.0, 4, 1.0)
            24.0  # 1 * 2 * 3 * 4
        """
        if n < 0:
            raise ValueError(f"n must be non-negative, got {n}")
            
        if n == 0:
            return 1.0
        
        # Use scipy's pochammer function if available (handles large values better)
        if HAS_SCIPY and increment == 1.0:
            try:
                return scipy.special.poch(x, n)
            except (OverflowError, ValueError):
                pass  # Fall back to our implementation
        
        # Fast path for small n
        if n <= 20:
            result = 1.0
            for i in range(n):
                result *= (x + i * increment)
            return result
        
        # For large n, use logarithms to avoid overflow
        try:
            log_result = 0.0
            sign = 1.0
            for i in range(n):
                factor = x + i * increment
                if factor <= 0:
                    # Handle possible negative or zero factors
                    if factor == 0:
                        return 0.0
                    else:
                        log_result += math.log(abs(factor))
                        if factor < 0:
                            sign *= -1
                else:
                    log_result += math.log(factor)
            return sign * math.exp(log_result)
        except (OverflowError, ValueError) as e:
            warnings.warn(f"Numerical overflow in rising factorial with x={x}, n={n}, increment={increment}: {e}")
            return float('inf') if sign > 0 else float('-inf')
    
    def explicit_formula(self, n: int, k: int) -> float:
        """
        Compute L{n,k}^{α,β} using the explicit formula.
        
        Formula: L{n,k}^{α,β} = (1/(β^k * k!)) * ∑_{j=0}^k (-1)^j * C(k,j) * (β(k-j)|α)^n̄
        
        Args:
            n: Number of elements
            k: Number of ordered lists
            
        Returns:
            Value of the generalized Stirling number
            
        Raises:
            ValueError: If n or k are negative
            
        Examples:
            >>> gs = GeneralizedStirling(alpha=1.0, beta=1.0)
            >>> gs.explicit_formula(3, 2)
            6.0
            
            >>> gs = GeneralizedStirling(alpha=0.0, beta=1.0)
            >>> gs.explicit_formula(4, 2)  # Stirling number of the second kind
            7.0
        """
        # Validate inputs
        if n < 0 or k < 0:
            raise ValueError(f"n and k must be non-negative, got n={n}, k={k}")
            
        # Handle base cases
        if k == 0:
            return 1.0 if n == 0 else 0.0
        if n == 0 or k > n:
            return 0.0
        if k == n:
            return 1.0
        
        # Check memory cache
        cache_key = ('explicit', n, k)
        if cache_key in self._memory_cache:
            self.cache_hits['explicit'] += 1
            return self._memory_cache[cache_key]
        
        # Check disk cache if enabled
        if self.use_disk_cache:
            disk_key = self._get_disk_cache_key('explicit', n, k)
            cached_value = self._load_from_disk_cache(disk_key)
            if cached_value is not None:
                self.cache_hits['explicit'] += 1
                self._memory_cache[cache_key] = cached_value  # Also cache in memory
                return cached_value
        
        self.cache_misses['explicit'] += 1
        start_time = time.time()
        
        # Special case for k=1
        if k == 1:
            result = self.single_list_case(n)
        else:
            # Main computation with numerical stability improvements
            # For large values, compute in log space
            if n > 50 or k > 20:
                try:
                    result = self._explicit_formula_log_space(n, k)
                except (OverflowError, ValueError) as e:
                    warnings.warn(f"Numerical issues in explicit formula with n={n}, k={k}: {e}")
                    # Fall back to triangular recurrence
                    result = self.triangular_recurrence(n, k)
            else:
                result = self._explicit_formula_direct(n, k)
        
        # Update caches and timing
        self._memory_cache[cache_key] = result
        if self.use_disk_cache:
            disk_key = self._get_disk_cache_key('explicit', n, k)
            self._save_to_disk_cache(disk_key, result)
            
        self.compute_time['explicit'] += time.time() - start_time
        
        return result
    
    def _explicit_formula_direct(self, n: int, k: int) -> float:
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
    
    def _explicit_formula_log_space(self, n: int, k: int) -> float:
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
    
    def triangular_recurrence_internal(self, n: int, k: int) -> float:
        """Internal implementation of triangular recurrence without caching"""
        # Handle base cases
        if k == 0:
            return 1.0 if n == 0 else 0.0
        if n == 0 or k > n:
            return 0.0
        if k == n:
            return 1.0
        if k == 1:
            return self.single_list_case(n)
        
        # Check precomputed values
        if (n, k) in self._precomputed:
            return self._precomputed[(n, k)]
        
        # Apply recurrence relation
        term1 = self.triangular_recurrence(n-1, k-1)
        term2 = (self.alpha * (n-1) + self.beta * k) * self.triangular_recurrence(n-1, k)
        
        return term1 + term2
    
    @lru_cache(maxsize=10000)  # Increased cache size
    def triangular_recurrence(self, n: int, k: int) -> float:
        """
        Compute L{n,k}^{α,β} using the triangular recurrence relation.
        
        L{n,k}^{α,β} = L{n-1,k-1}^{α,β} + (α(n-1) + βk) * L{n-1,k}^{α,β}
        
        This recurrence relation has a clear combinatorial interpretation:
        - The first term represents placing element n in its own list
        - The second term represents placing element n into an existing list,
          either after an element (weight α) or at the head (weight β)
        
        Args:
            n: Number of elements
            k: Number of ordered lists
            
        Returns:
            Value of the generalized Stirling number
            
        Raises:
            ValueError: If n or k are negative
            
        Examples:
            >>> gs = GeneralizedStirling(alpha=1.0, beta=1.0)
            >>> gs.triangular_recurrence(3, 2)
            6.0
            
            >>> gs = GeneralizedStirling(alpha=1.0, beta=0.0)
            >>> gs.triangular_recurrence(4, 2)  # Stirling number of the first kind
            11.0
        """
        # Validate inputs
        if n < 0 or k < 0:
            raise ValueError(f"n and k must be non-negative, got n={n}, k={k}")
            
        # Check memory cache
        cache_key = ('triangular', n, k)
        if cache_key in self._memory_cache:
            self.cache_hits['triangular'] += 1
            return self._memory_cache[cache_key]
        
        # Check disk cache if enabled
        if self.use_disk_cache:
            disk_key = self._get_disk_cache_key('triangular', n, k)
            cached_value = self._load_from_disk_cache(disk_key)
            if cached_value is not None:
                self.cache_hits['triangular'] += 1
                self._memory_cache[cache_key] = cached_value  # Also cache in memory
                return cached_value
        
        self.cache_misses['triangular'] += 1
        start_time = time.time()
        
        result = self.triangular_recurrence_internal(n, k)
        
        # Update caches and timing
        self._memory_cache[cache_key] = result
        if self.use_disk_cache:
            disk_key = self._get_disk_cache_key('triangular', n, k)
            self._save_to_disk_cache(disk_key, result)
            
        self.compute_time['triangular'] += time.time() - start_time
        
        return result
    
    def bottom_up_computation(self, n: int, k: int) -> float:
        """
        Compute L{n,k}^{α,β} using a bottom-up dynamic programming approach.
        
        This method builds a table of values from smaller to larger parameters,
        which is more efficient for computing a single value when n and k are large.
        
        Args:
            n: Number of elements
            k: Number of ordered lists
            
        Returns:
            Value of the generalized Stirling number
            
        Raises:
            ValueError: If n or k are negative
            
        Examples:
            >>> gs = GeneralizedStirling(alpha=1.0, beta=1.0)
            >>> gs.bottom_up_computation(3, 2)
            6.0
            
            >>> gs = GeneralizedStirling(alpha=1.0, beta=0.0)
            >>> gs.bottom_up_computation(4, 2)  # Stirling number of the first kind
            11.0
        """
        # Validate inputs
        if n < 0 or k < 0:
            raise ValueError(f"n and k must be non-negative, got n={n}, k={k}")
            
        # Handle base cases
        if k == 0:
            return 1.0 if n == 0 else 0.0
        if n == 0 or k > n:
            return 0.0
        if k == n:
            return 1.0
        if k == 1:
            return self.single_list_case(n)
        
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
    
    def horizontal_recurrence(self, n: int, k: int) -> float:
        """
        Compute L{n,k}^{α,β} using the horizontal recurrence relation.
        
        L{n,k}^{α,β} = ∑_{j=0}^{n-k} (-1)^j * ((k+1)β + nα|α)^j̄ * L{n+1,k+j+1}^{α,β}
        
        Args:
            n: Number of elements
            k: Number of ordered lists
            
        Returns:
            Value of the generalized Stirling number
            
        Examples:
            >>> gs = GeneralizedStirling(alpha=1.0, beta=1.0)
            >>> gs.horizontal_recurrence(3, 2)
            6.0
            
            >>> gs = GeneralizedStirling(alpha=1.0, beta=0.0)
            >>> gs.horizontal_recurrence(4, 2)  # Stirling number of the first kind
            11.0
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
    
    def vertical_recurrence(self, n: int, k: int) -> float:
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
    
    def single_list_case(self, n: int, k: int = 1) -> float:
        """
        Compute L{n,1}^{α,β} using the special case formula for k=1.
        
        L{n,1}^{α,β} = ∏_{j=1}^{n-1} (jα + β)
        
        This formula applies only when k=1 (single list case).
        
        Args:
            n: Number of elements
            k: Should be 1 for this special case
            
        Returns:
            Value of L{n,1}^{α,β}
            
        Raises:
            ValueError: If k is not 1 or n is negative
            
        Examples:
            >>> gs = GeneralizedStirling(alpha=1.0, beta=1.0)
            >>> gs.single_list_case(4)
            24.0  # Factorial of 4
            
            >>> gs = GeneralizedStirling(alpha=0.0, beta=2.0)
            >>> gs.single_list_case(3)
            8.0  # 2^(3-1)
        """
        if k != 1:
            raise ValueError("This special case only applies for k=1")
            
        if n < 0:
            raise ValueError(f"n must be non-negative, got {n}")
            
        # Special base cases
        if n == 0:
            return 0.0  # L_{0,1} = 0 by definition
        if n == 1:
            return 1.0  # L_{1,1} = 1 by definition
        
        # Check cache
        cache_key = ('single_list', n, 1)
        if cache_key in self._memory_cache:
            self.cache_hits['single_list'] += 1
            return self._memory_cache[cache_key]
        
        # Check disk cache if enabled
        if self.use_disk_cache:
            disk_key = self._get_disk_cache_key('single_list', n, 1)
            cached_value = self._load_from_disk_cache(disk_key)
            if cached_value is not None:
                self.cache_hits['single_list'] += 1
                self._memory_cache[cache_key] = cached_value
                return cached_value
                
        self.cache_misses['single_list'] += 1
        start_time = time.time()
        
        # Optimized calculation for special cases
        if self.alpha == 1.0 and self.beta == 0.0:
            # Stirling numbers of the first kind s(n,1) = (n-1)!
            result = math.factorial(n-1)
        elif self.alpha == 0.0 and self.beta == 1.0:
            # Stirling numbers of the second kind S(n,1) = 1
            result = 1.0
        elif self.alpha == 0.0:
            # When alpha = 0: L_{n,1} = β^(n-1)
            result = self.beta ** (n-1)
        elif self.alpha == 1.0 and self.beta == 1.0:
            # Lah numbers L(n,1) = n!
            result = math.factorial(n)
        else:
            # For large n, compute in log space to avoid overflow
            if n > 100:
                log_result = 0.0
                sign = 1.0
                for j in range(1, n):
                    factor = j * self.alpha + self.beta
                    if factor <= 0:
                        # Handle possible negative or zero factors
                        if factor == 0:
                            result = 0.0
                            break
                        else:
                            log_result += math.log(abs(factor))
                            if factor < 0:
                                sign *= -1
                    else:
                        log_result += math.log(factor)
                
                result = sign * math.exp(log_result)
            else:
                result = 1.0
                for j in range(1, n):
                    result *= (j * self.alpha + self.beta)
        
        # Update cache and timing
        self._memory_cache[cache_key] = result
        if self.use_disk_cache:
            disk_key = self._get_disk_cache_key('single_list', n, 1)
            self._save_to_disk_cache(disk_key, result)
            
        self.compute_time['single_list'] += time.time() - start_time
        
        return result
    
    # Maintain compatibility with old method name
    special_case = single_list_case
    
    def symmetric_function(self, n: int, k: int) -> float:
        """
        Compute L{n+k,n}^{α,β} using the symmetric function formula.
        
        L{n+k,n}^{α,β} = ∑_{1≤i₁≤...≤iₖ≤n} ∏_{j=1}^k ((α+β)iⱼ + α(j-1))
        
        This implementation uses lru_cache for efficient dynamic programming.
        
        The symmetric function formula provides an alternative way to compute
        generalized Stirling numbers, expressing them in terms of elementary
        symmetric functions of weighted sequences.
        
        Args:
            n: First parameter
            k: Second parameter
            
        Returns:
            Value of L{n+k,n}^{α,β}
            
        Raises:
            ValueError: If n or k are negative
            
        Examples:
            >>> gs = GeneralizedStirling(alpha=1.0, beta=1.0)
            >>> gs.symmetric_function(3, 2)  # Computes L{5,3}
            60.0
            
            >>> gs = GeneralizedStirling(alpha=0.0, beta=1.0)
            >>> gs.symmetric_function(2, 1)  # Computes L{3,2} = S(3,2)
            3.0
        """
        # Validate inputs
        if n < 0 or k < 0:
            raise ValueError(f"n and k must be non-negative, got n={n}, k={k}")
            
        if k == 0:
            return 1.0
        
        # For k=1, use the special formula
        if k == 1:
            result = 0
            for i in range(1, n+1):
                result += (self.alpha + self.beta) * i
            return result
        
        # Check memory cache
        cache_key = ('symmetric', n, k)
        if cache_key in self._memory_cache:
            self.cache_hits['symmetric'] += 1
            return self._memory_cache[cache_key]
        
        # Check disk cache if enabled
        if self.use_disk_cache:
            disk_key = self._get_disk_cache_key('symmetric', n, k)
            cached_value = self._load_from_disk_cache(disk_key)
            if cached_value is not None:
                self.cache_hits['symmetric'] += 1
                self._memory_cache[cache_key] = cached_value  # Also cache in memory
                return cached_value
        
        self.cache_misses['symmetric'] += 1
        start_time = time.time()
        
        # Define a nested function with lru_cache for efficient DP
        @lru_cache(maxsize=None)
        def compute_dp(depth: int, start: int) -> float:
            """Recursively compute the sum using dynamic programming with lru_cache"""
            if depth == k:
                return 1.0
            
            return sum(((self.alpha + self.beta) * i + self.alpha * depth) * 
                      compute_dp(depth+1, i) for i in range(start, n+1))
        
        result = compute_dp(0, 1)
        
        # Clear the lru_cache to avoid memory leaks
        compute_dp.cache_clear()
        
        # Update caches and timing
        self._memory_cache[cache_key] = result
        if self.use_disk_cache:
            disk_key = self._get_disk_cache_key('symmetric', n, k)
            self._save_to_disk_cache(disk_key, result)
            
        self.compute_time['symmetric'] += time.time() - start_time
        
        return result
    
    def compute(self, n: int, k: int, method: str = 'auto') -> float:
        """
        Compute L{n,k}^{α,β} using the specified method.
        
        This method automatically selects the most appropriate algorithm
        based on the input size if method='auto'.
        
        Args:
            n: Number of elements
            k: Number of ordered lists
            method: Method to use ('auto', 'triangular', 'explicit', 
                   'horizontal', 'vertical', 'bottom_up', 'symmetric')
            
        Returns:
            Value of the generalized Stirling number
            
        Raises:
            ValueError: If n or k are negative, or if method is not recognized
            
        Examples:
            >>> gs = GeneralizedStirling(alpha=1.0, beta=1.0)
            >>> gs.compute(3, 2)  # Auto-select method
            6.0
            
            >>> gs.compute(5, 3, method='explicit')  # Use explicit formula
            60.0
            
            >>> gs.compute(4, 2, method='bottom_up')  # Use bottom-up approach
            36.0
        """
        # Validate inputs
        if n < 0 or k < 0:
            raise ValueError(f"n and k must be non-negative, got n={n}, k={k}")
            
        valid_methods = {'auto', 'triangular', 'explicit', 'horizontal', 'vertical', 
                         'bottom_up', 'symmetric', 'single_list'}
        if method not in valid_methods:
            raise ValueError(f"Unknown method: {method}. Valid methods are: {valid_methods}")
        
        # Handle base cases first for efficiency
        if k == 0:
            return 1.0 if n == 0 else 0.0
        if n == 0:
            return 0.0  # L_{0,k} = 0 for k > 0
        if k > n:
            return 0.0  # L_{n,k} = 0 for k > n
        if k == n:
            return 1.0  # L_{n,n} = 1
        
        # For k=1, use the single_list_case formula which is more efficient
        if k == 1:
            return self.single_list_case(n, k)
        
        # Auto-select the best method based on input size and parameters
        if method == 'auto':
            # Special case for known parameter combinations
            if self.alpha == 0.0 or self.beta == 0.0:
                # For classical Stirling numbers, triangular recurrence is usually best
                method = 'triangular'
            elif n > 100 or k > 50:
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
            
            logger.debug(f"Auto-selected method '{method}' for n={n}, k={k}")
        
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
        elif method == 'single_list':
            if k == 1:
                return self.single_list_case(n, k)
            else:
                raise ValueError(f"single_list method only valid for k=1, got k={k}")
        else:  # Default to triangular
            return self.triangular_recurrence(n, k)
    
    def summary(self) -> None:
        """
        Print a summary of performance statistics.
        
        This method provides a nicely formatted display of cache performance,
        computation times, and other metrics.
        
        Examples:
            >>> gs = GeneralizedStirling()
            >>> for n in range(1, 10):
            ...     for k in range(1, n+1):
            ...         gs.compute(n, k)
            >>> gs.summary()
            Performance Summary
            ------------------
            Cache hits: 30
            Cache misses: 25
            Hit ratio: 54.5%
            ...
        """
        stats = self.get_performance_stats()
        
        print("\nPerformance Summary")
        print("-" * 50)
        print(f"Parameters: α={self.alpha}, β={self.beta}")
        
        # Cache statistics
        total_hits = sum(stats['cache_hits'].values())
        total_misses = sum(stats['cache_misses'].values())
        total_operations = total_hits + total_misses
        hit_ratio = total_hits / total_operations if total_operations > 0 else 0
        
        print(f"\nCache Statistics:")
        print(f"  Total operations: {total_operations}")
        print(f"  Cache hits: {total_hits}")
        print(f"  Cache misses: {total_misses}")
        print(f"  Overall hit ratio: {hit_ratio:.1%}")
        
        # Per-method statistics
        print("\nPer-Method Statistics:")
        for method in sorted(set(list(stats['cache_hits'].keys()) + list(stats['cache_misses'].keys()))):
            hits = stats['cache_hits'].get(method, 0)
            misses = stats['cache_misses'].get(method, 0)
            method_total = hits + misses
            ratio = hits / method_total if method_total > 0 else 0
            time = stats['compute_time'].get(method, 0)
            
            print(f"  {method}:")
            print(f"    Operations: {method_total}")
            print(f"    Hit ratio: {ratio:.1%}")
            print(f"    Compute time: {time:.6f} seconds")
        
        # Disk cache info
        if stats['disk_cache_enabled']:
            print(f"\nDisk Cache:")
            print(f"  Directory: {stats['disk_cache_dir']}")
            print(f"  Size: {stats['disk_cache_size'] / 1024:.1f} KB")
        
        print("-" * 50)
    
    # ... existing code ...
    Returns:
        Value of the Stirling number of the first kind
        
    Raises:
        ValueError: If n or k are negative
        
    Examples:
        >>> stirling_first_kind(4, 2)
        11.0
        >>> stirling_first_kind(5, 3)
        35.0
    """
    if n < 0 or k < 0:
        raise ValueError(f"n and k must be non-negative, got n={n}, k={k}")
        
    gs = GeneralizedStirling(alpha=1.0, beta=0.0)
    return gs.compute(n, k)


def stirling_second_kind(n: int, k: int) -> float:
    """
    Compute the Stirling number of the second kind.
    
    This is equivalent to L{n,k}^{0,1}.
    
    Args:
        n: Number of elements
        k: Number of subsets
        
    Returns:
        Value of the Stirling number of the second kind
        
    Raises:
        ValueError: If n or k are negative
        
    Examples:
        >>> stirling_second_kind(4, 2)
        7.0
        >>> stirling_second_kind(5, 3)
        10.0
    """
    if n < 0 or k < 0:
        raise ValueError(f"n and k must be non-negative, got n={n}, k={k}")
        
    gs = GeneralizedStirling(alpha=0.0, beta=1.0)
    return gs.compute(n, k)


def lah_number(n: int, k: int) -> float:
    """
    Compute the Lah number.
    
    This is equivalent to L{n,k}^{1,1}.
    
    Args:
        n: Number of elements
        k: Number of ordered lists
        
    Returns:
        Value of the Lah number
        
    Raises:
        ValueError: If n or k are negative
        
    Examples:
        >>> lah_number(4, 2)
        36.0
        >>> lah_number(5, 3)
        60.0
    """
    if n < 0 or k < 0:
        raise ValueError(f"n and k must be non-negative, got n={n}, k={k}")
        
    gs = GeneralizedStirling(alpha=1.0, beta=1.0)
    return gs.compute(n, k)


# Add new utility functions
def parallel_generate_triangle(n_max: int, alpha: float = 1.0, beta: float = 1.0, 
                              method: str = 'auto', processes: Optional[int] = None) -> List[List[float]]:
    """
    Generate a triangle of generalized Stirling numbers using parallel processing.
    
    This function uses multiple CPU cores to compute the triangle faster.
    
    Args:
        n_max: Maximum row number
        alpha: Weight parameter for non-head elements
        beta: Weight parameter for head elements
        method: Method to use for computation
        processes: Number of processes to use (None = use all available cores)
        
    Returns:
        Triangle of generalized Stirling numbers as list of lists
        
    Raises:
        ValueError: If n_max is negative
        
    Examples:
        >>> triangle = parallel_generate_triangle(5, alpha=1.0, beta=1.0)
        >>> print(triangle[2])  # Row for n=3
        [6.0, 6.0, 1.0]
    """
    import concurrent.futures
    
    if n_max < 0:
        raise ValueError(f"n_max must be non-negative, got {n_max}")
    
    gs = GeneralizedStirling(alpha=alpha, beta=beta)
    triangle = [[] for _ in range(n_max)]
    
    def compute_value(n: int, k: int) -> Tuple[int, int, float]:
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


def memory_efficient_iterator(n_max: int, alpha: float = 1.0, beta: float = 1.0, 
                             method: str = 'auto') -> Iterator[Tuple[int, int, float]]:
    """
    Memory-efficient iterator for generalized Stirling numbers.
    
    Instead of generating the entire triangle at once, this iterator
    yields values one at a time to conserve memory.
    
    Args:
        n_max: Maximum row number
        alpha: Weight parameter for non-head elements
        beta: Weight parameter for head elements
        method: Method to use for computation
        
    Yields:
        Tuples of (n, k, value) for each generalized Stirling number
        
    Raises:
        ValueError: If n_max is negative
        
    Examples:
        >>> for n, k, value in memory_efficient_iterator(3, alpha=1.0, beta=1.0):
        ...     if n == 3 and k == 2:
        ...         print(f"L{{3,2}}^{{1,1}} = {value}")
        L{3,2}^{1,1} = 6.0
    """
    if n_max < 0:
        raise ValueError(f"n_max must be non-negative, got {n_max}")
        
    gs = GeneralizedStirling(alpha=alpha, beta=beta)
    
    for n in range(1, n_max + 1):
        for k in range(1, n + 1):
            yield (n, k, gs.compute(n, k, method=method))
