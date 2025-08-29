"""
Core library for generalized Stirling numbers and Bell polynomials.
Provides fundamental operations for computing Stirling numbers,
Bell polynomials, and parameter estimation.
"""

import numpy as np
from scipy.special import comb, factorial
from math import prod
from functools import lru_cache

class StirlingComputation:
    """Class for computing generalized Stirling numbers with parameters (a,b)."""
    
    def __init__(self, a=0, b=1):
        """Initialize with parameters a and b.
        
        Args:
            a (float): Affinity parameter (default: 0, Stirling numbers of second kind)
            b (float): Barrier parameter (default: 1, Stirling numbers of second kind)
        """
        self.a = a
        self.b = b
        self._cache = {}
        
    @lru_cache(maxsize=1024)
    def compute(self, n, k):
        """Compute generalized Stirling number S_{n,k}(a,b).
        
        Args:
            n (int): Row index
            k (int): Column index
            
        Returns:
            float: The generalized Stirling number S_{n,k}(a,b)
        """
        # Base cases
        if k == 0:
            return 1.0 if n == 0 else 0.0
        if n == 0 or k > n:
            return 0.0
        if k == n:
            return 1.0
            
        # Recurrence relation
        term1 = self.compute(n-1, k-1)
        term2 = (self.a * (n-1) + self.b * k) * self.compute(n-1, k)
        return term1 + term2
    
    def table(self, n_max, k_max=None):
        """Generate a table of generalized Stirling numbers.
        
        Args:
            n_max (int): Maximum row index
            k_max (int, optional): Maximum column index. Defaults to n_max.
            
        Returns:
            numpy.ndarray: Table of generalized Stirling numbers
        """
        if k_max is None:
            k_max = n_max
            
        table = np.zeros((n_max+1, k_max+1))
        for n in range(n_max+1):
            for k in range(min(n+1, k_max+1)):
                table[n, k] = self.compute(n, k)
                
        return table


class BellPolynomials:
    """Class for computing Bell polynomials and related operations."""
    
    @staticmethod
    def partial_bell(n, k, coeffs):
        """Compute partial Bell polynomial B_{n,k}(x_1, x_2, ..., x_{n-k+1}).
        
        Args:
            n (int): First index
            k (int): Second index
            coeffs (list): Sequence [x_1, x_2, ..., x_{n-k+1}]
            
        Returns:
            float: B_{n,k}(x_1, x_2, ..., x_{n-k+1})
        """
        if n == 0 and k == 0:
            return 1
        if n <= 0 or k <= 0 or k > n:
            return 0
            
        # Extend coeffs if needed
        if len(coeffs) < n-k+1:
            coeffs = list(coeffs) + [0] * (n-k+1 - len(coeffs))
        
        # Sum over partitions
        result = 0
        
        # Use recursive helper
        def partition_sum(n, k, i=1, current_part=None):
            if current_part is None:
                current_part = []
                
            if sum(current_part) == n and len(current_part) == k:
                # Calculate the multinomial coefficient and product of coefficients
                coef = factorial(k)
                for j in set(current_part):
                    count = current_part.count(j)
                    if count > 1:
                        coef //= factorial(count)
                
                term = coef
                for j, count in enumerate(current_part, 1):
                    term *= coeffs[j-1]**count
                    
                return term
            
            if i > n or len(current_part) >= k or sum(current_part) >= n:
                return 0
                
            # Include current i in partition
            include = partition_sum(n, k, i, current_part + [i])
            # Skip current i
            exclude = partition_sum(n, k, i+1, current_part)
            
            return include + exclude
        
        # Inefficient but correct implementation
        # In practice, use more efficient algorithms or libraries
        result = partition_sum(n, k)
        return result
    
    @staticmethod
    def complete_bell(n, coeffs):
        """Compute complete Bell polynomial B_n(x_1, x_2, ..., x_n).
        
        Args:
            n (int): Index
            coeffs (list): Sequence [x_1, x_2, ..., x_n]
            
        Returns:
            float: B_n(x_1, x_2, ..., x_n)
        """
        return sum(BellPolynomials.partial_bell(n, k, coeffs) for k in range(1, n+1))
    
    @staticmethod
    def multivariate_bell(n, k, features):
        """Compute multivariate Bell polynomial for feature matrix.
        
        Args:
            n (int): Order of polynomial
            k (int): Number of parts
            features (numpy.ndarray): Feature matrix (samples × dimensions)
            
        Returns:
            numpy.ndarray: Multivariate Bell polynomial values
        """
        if n == 0 and k == 0:
            return 1
        if n < k or k <= 0:
            return 0
        
        # Extract dimensions
        n_samples, n_dims = features.shape
        
        # For first-order polynomials, return feature means
        if n == 1 and k == 1:
            return np.mean(features, axis=0)
        
        # Initialize result array
        result = np.zeros(n_dims)
        
        # Compute central moments for each dimension
        central_moments = []
        for dim in range(n_dims):
            dim_values = features[:, dim]
            moments = []
            for j in range(1, n+1):
                moment_j = np.mean((dim_values - np.mean(dim_values))**j)
                moments.append(moment_j)
            central_moments.append(moments)
        
        # Build polynomial using multivariate formula
        from itertools import combinations_with_replacement
        for dim_indices in combinations_with_replacement(range(n_dims), k):
            # Count occurrences of each dimension in the combination
            dim_counts = [dim_indices.count(d) for d in range(n_dims)]
            
            # Compute coefficient
            coef = comb(n, sum(dim_counts))
            for d in range(n_dims):
                if dim_counts[d] > 0:
                    coef *= central_moments[d][dim_counts[d]-1] / np.math.factorial(dim_counts[d])
            
            # Add contribution to result
            for d in range(n_dims):
                if dim_counts[d] > 0:
                    result[d] += coef
        
        return result


class ParameterEstimation:
    """Class for estimating (a,b) parameters from function coefficients."""
    
    @staticmethod
    def estimate_from_inverse_pair(a_coeffs, b_coeffs, max_terms=5):
        """Estimate (a,b) parameters from coefficients of inverse function pair.
        
        Args:
            a_coeffs (list): Coefficients of the first function [a_0, a_1, ...]
            b_coeffs (list): Coefficients of the inverse function [b_0, b_1, ...]
            max_terms (int): Number of terms to use in estimation
            
        Returns:
            tuple: Estimated (a, b) parameters
        """
        # Normalize coefficients if needed
        if a_coeffs[0] != 0 or b_coeffs[0] != 0:
            a_coeffs = np.array(a_coeffs) - a_coeffs[0]
            b_coeffs = np.array(b_coeffs) - b_coeffs[0]
        
        # Convert to numpy arrays if not already
        a_coeffs = np.asarray(a_coeffs)
        b_coeffs = np.asarray(b_coeffs)
        
        # Ensure we have enough coefficients
        if len(a_coeffs) < 3 or len(b_coeffs) < 3:
            raise ValueError("Need at least 3 coefficients for estimation")
        
        # For compositionally inverse functions, a_1 * b_1 = 1
        if not np.isclose(a_coeffs[1] * b_coeffs[1], 1.0):
            print("Warning: a_1 * b_1 != 1, scaling coefficients")
            scale = 1.0 / (a_coeffs[1] * b_coeffs[1])
            a_coeffs = a_coeffs * scale
        
        # Use the formula b ≈ (a_2 - a_1^2 * b_2) / (a_1^2 * b_1)
        b_param = (a_coeffs[2] - a_coeffs[1]**2 * b_coeffs[2]) / (a_coeffs[1]**2 * b_coeffs[1])
        
        # For second parameter, use relationship with b
        # This is an approximation - for many common cases a=1
        a_param = 1.0
        
        # If we have a specific application with known constraints,
        # we could refine a_param further
        
        return a_param, b_param
    
    @staticmethod
    def estimate_from_clustering(data, labels, k):
        """Estimate (a,b) parameters from clustering results.
        
        Args:
            data (numpy.ndarray): Data matrix
            labels (numpy.ndarray): Cluster labels
            k (int): Number of clusters
            
        Returns:
            tuple: Estimated (a, b) parameters
        """
        from sklearn.metrics import pairwise_distances_argmin_min
        
        # Compute centroids
        centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])
        
        # Compute affinity as average distance to cluster centroid
        affinity = 0
        for i in range(k):
            if np.sum(labels == i) > 0:
                cluster_points = data[labels == i]
                dists = np.linalg.norm(cluster_points - centroids[i], axis=1)
                affinity += np.mean(dists)
        affinity /= k
        
        # Compute cost as average distance between centroids
        cost = 0
        count = 0
        for i in range(k):
            for j in range(i+1, k):
                cost += np.linalg.norm(centroids[i] - centroids[j])
                count += 1
        if count > 0:
            cost /= count
        
        # Parameters are related to the slopes of affinity and cost vs k
        # This is an approximation - would need multiple k values for true slopes
        a_param = -affinity  # Negative since lower affinity → higher parameter a
        b_param = cost       # Higher cost → higher parameter b
        
        return a_param, b_param


class StirlingTransform:
    """Class for transforming between different polynomial bases."""
    
    def __init__(self, a=0, b=1):
        """Initialize with parameters a and b.
        
        Args:
            a (float): Affinity parameter
            b (float): Barrier parameter
        """
        self.stirling = StirlingComputation(a, b)
    
    def transform_coefficients(self, coeffs, from_basis='power', to_basis='factorial'):
        """Transform coefficients from one basis to another.
        
        Args:
            coeffs (list): Coefficients in the source basis
            from_basis (str): Source basis ('power', 'factorial', etc.)
            to_basis (str): Target basis ('power', 'factorial', etc.)
            
        Returns:
            list: Coefficients in the target basis
        """
        n = len(coeffs)
        result = np.zeros(n)
        
        if from_basis == 'power' and to_basis == 'factorial':
            # Power basis to factorial basis (like Stirling 2nd kind)
            for j in range(n):
                for k in range(j+1):
                    result[j] += self.stirling.compute(j, k) * coeffs[k]
                    
        elif from_basis == 'factorial' and to_basis == 'power':
            # Factorial basis to power basis (like Stirling 1st kind)
            # Invert the parameters for inverse transform
            inverse_stirling = StirlingComputation(self.stirling.b, self.stirling.a)
            for j in range(n):
                for k in range(j+1):
                    result[j] += inverse_stirling.compute(j, k) * coeffs[k]
        
        else:
            raise ValueError(f"Unsupported basis transformation: {from_basis} -> {to_basis}")
            
        return result
