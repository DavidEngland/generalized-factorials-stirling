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


class GeneralizedStirling:
    """
    Implementation of generalized Stirling numbers with parameters α and β.
    
    These numbers have a combinatorial interpretation as the total weight
    of distributing n elements into k ordered non-empty lists, where:
    1. The head of each list has weight β
    2. Other elements in lists have weight α
    3. The first element placed in each list has weight 1
    """
    
    def __init__(self, alpha=1.0, beta=1.0):
        """
        Initialize with parameters α and β.
        
        Args:
            alpha (float): Weight parameter for non-head elements
            beta (float): Weight parameter for head elements
        """
        self.alpha = alpha
        self.beta = beta
        
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
        
        result = 1.0
        for i in range(n):
            result *= (x + i * increment)
        return result
    
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
        
        result = 0.0
        for j in range(k+1):
            # Calculate binomial coefficient C(k,j)
            binom = math.comb(k, j)
            
            # Calculate rising factorial (β(k-j)|α)^n̄
            base = self.beta * (k - j)
            rising_fact = self.rising_factorial(base, n, self.alpha)
            
            # Add to sum with alternating sign
            result += ((-1) ** j) * binom * rising_fact
        
        # Divide by β^k * k!
        denominator = (self.beta ** k) * math.factorial(k)
        return result / denominator if denominator != 0 else 0.0
    
    @lru_cache(maxsize=1000)
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
        # Handle base cases
        if k == 0:
            return 1.0 if n == 0 else 0.0
        if n == 0 or k > n:
            return 0.0
        if k == n:
            return 1.0
        
        # Apply recurrence relation
        term1 = self.triangular_recurrence(n-1, k-1)
        term2 = (self.alpha * (n-1) + self.beta * k) * self.triangular_recurrence(n-1, k)
        
        return term1 + term2
    
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
            
        result = 1.0
        for j in range(1, n):
            result *= (j * self.alpha + self.beta)
        
        return result
    
    def symmetric_function(self, n, k):
        """
        Compute L{n+k,n}^{α,β} using the symmetric function formula.
        
        L{n+k,n}^{α,β} = ∑_{1≤i₁≤...≤iₖ≤n} ∏_{j=1}^k ((α+β)iⱼ + α(j-1))
        
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
        
        # For larger k, recursively generate the sum
        # This is an inefficient implementation for demonstration
        # A more efficient implementation would use dynamic programming
        
        def recursive_sum(depth, start, product):
            if depth == k:
                return product
            
            result = 0
            for i in range(start, n+1):
                factor = (self.alpha + self.beta) * i + self.alpha * depth
                result += recursive_sum(depth+1, i, product * factor)
            
            return result
        
        return recursive_sum(0, 1, 1.0)
    
    def compute(self, n, k, method='triangular'):
        """
        Compute L{n,k}^{α,β} using the specified method.
        
        Args:
            n (int): Number of elements
            k (int): Number of ordered lists
            method (str): Method to use ('triangular', 'explicit', 'horizontal', 'vertical')
            
        Returns:
            float: Value of the generalized Stirling number
        """
        if method == 'explicit':
            return self.explicit_formula(n, k)
        elif method == 'horizontal':
            return self.horizontal_recurrence(n, k)
        elif method == 'vertical':
            return self.vertical_recurrence(n-1, k-1) if n > 0 and k > 0 else self.triangular_recurrence(n, k)
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
        for n in range(1, n_max + 1):
            row = []
            for k in range(1, n + 1):
                row.append(format_str.format(self.triangular_recurrence(n, k)))
            triangle.append(row)
        
        return triangle


def stirling_first_kind(n, k):
    """
    Compute the unsigned Stirling number of the first kind.
    
    This is equivalent to L{n,k}^{1,0}.
    
    Args:
        n (int): Number of elements
        k (int): Number of cycles
        
    Returns:
        float: Value of the Stirling number of the first kind
    """
    gs = GeneralizedStirling(alpha=1.0, beta=0.0)
    return gs.compute(n, k)


def stirling_second_kind(n, k):
    """
    Compute the Stirling number of the second kind.
    
    This is equivalent to L{n,k}^{0,1}.
    
    Args:
        n (int): Number of elements
        k (int): Number of subsets
        
    Returns:
        float: Value of the Stirling number of the second kind
    """
    gs = GeneralizedStirling(alpha=0.0, beta=1.0)
    return gs.compute(n, k)


def lah_number(n, k):
    """
    Compute the Lah number.
    
    This is equivalent to L{n,k}^{1,1}.
    
    Args:
        n (int): Number of elements
        k (int): Number of ordered lists
        
    Returns:
        float: Value of the Lah number
    """
    gs = GeneralizedStirling(alpha=1.0, beta=1.0)
    return gs.compute(n, k)
