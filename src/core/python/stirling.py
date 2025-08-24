from functools import lru_cache
from typing import Optional
import numpy as np

class GeneralizedStirling:
    """
    Implementation of generalized Stirling numbers with parameters a and b.
    """
    
    def __init__(self, a: float = 1.0, b: float = 1.0):
        """
        Initialize the generalized Stirling calculator.
        
        Args:
            a: Parameter for within-list weight
            b: Parameter for between-list weight
        """
        self.a = a
        self.b = b
        self._cache = {}
    
    @lru_cache(maxsize=10000)
    def compute(self, n: int, k: int) -> float:
        """
        Compute the generalized Stirling number S(n,k)(a,b).
        
        Args:
            n: Number of elements
            k: Number of lists
            
        Returns:
            The value of S(n,k)(a,b)
        """
        # Handle invalid cases that always result in zero
        if k == 0:
            return 1.0 if n == 0 else 0.0
        if n == 0 or k > n:
            return 0.0
        if k == n:
            return 1.0
        
        # Check for degenerate parameter cases
        if self.b == 0 and k > 1:
            # With b=0, can't create multiple lists
            return 0.0
        
        # Use triangular recurrence relation
        return self.compute(n-1, k-1) + (self.a * (n-1) + self.b * k) * self.compute(n-1, k)
    
    def is_valid_for_measure(self, n: int, k: int) -> bool:
        """
        Check if (n,k) pair is valid for Stirling measure calculation.
        
        Args:
            n: Number of elements
            k: Number of lists
            
        Returns:
            True if measure can be calculated, False otherwise
        """
        # Basic validity checks
        if n <= 0 or k <= 0 or k > n:
            return False
        
        # Check if S(n,k) would be zero
        s_n_k = self.compute(n, k)
        if s_n_k == 0 or abs(s_n_k) < 1e-15:  # Numerical zero threshold
            return False
        
        # Additional validity for measure calculation
        # Need k-1 >= 0 for S(n,k-1) term
        if k == 1:
            # Special case: S(n,0) = 0 for n > 0, so measure is undefined
            return False
        
        return True
    
    def calculate_stirling_measure(self, n: int, k: int) -> Optional[float]:
        """
        Calculate the Stirling measure with proper zero-division handling.
        
        Args:
            n: Number of elements
            k: Number of lists
            
        Returns:
            The Stirling measure or None if undefined
        """
        # Check validity first
        if not self.is_valid_for_measure(n, k):
            return None
        
        try:
            s_n_k = self.compute(n, k)
            s_n_plus_1_k = self.compute(n+1, k)
            s_n_k_minus_1 = self.compute(n, k-1)
            
            # Final check for numerical stability
            if abs(s_n_k) < 1e-15:
                return None
            
            measure = (s_n_plus_1_k - s_n_k_minus_1) / s_n_k
            
            # Check for numerical issues in result
            if not np.isfinite(measure):
                return None
            
            return measure
            
        except (ZeroDivisionError, OverflowError, ValueError):
            return None