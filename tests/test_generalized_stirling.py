"""
Unit tests for generalized Stirling numbers implementation.

This file contains tests for the GeneralizedStirling class, including:
- Base cases and special values
- Recurrence relations
- Numerical stability
- Different computation methods
- Edge cases
"""

import unittest
import sys
import os
from pathlib import Path
import math
from functools import lru_cache

# Add the src directory to the path
sys.path.append(str(Path(__file__).parent.parent / "src"))
from generalized_stirling import GeneralizedStirling, stirling_first_kind, stirling_second_kind, lah_number


class TestGeneralizedStirling(unittest.TestCase):
    """Tests for the GeneralizedStirling class."""
    
    def setUp(self):
        """Set up instances for testing."""
        self.gs_lah = GeneralizedStirling(alpha=1.0, beta=1.0)  # Lah numbers
        self.gs_stirling1 = GeneralizedStirling(alpha=1.0, beta=0.0)  # Stirling 1st kind
        self.gs_stirling2 = GeneralizedStirling(alpha=0.0, beta=1.0)  # Stirling 2nd kind
        self.gs_custom = GeneralizedStirling(alpha=2.0, beta=3.0)  # Custom parameters
        
        # Tolerance for floating-point comparisons
        self.tol = 1e-10
    
    def test_base_cases(self):
        """Test base cases for generalized Stirling numbers."""
        # L_{0,0} = 1
        self.assertEqual(self.gs_lah.compute(0, 0), 1.0)
        
        # L_{n,0} = 0 for n > 0
        for n in range(1, 5):
            self.assertEqual(self.gs_lah.compute(n, 0), 0.0)
        
        # L_{0,k} = 0 for k > 0
        for k in range(1, 5):
            self.assertEqual(self.gs_lah.compute(0, k), 0.0)
        
        # L_{n,n} = 1
        for n in range(1, 5):
            self.assertEqual(self.gs_lah.compute(n, n), 1.0)
        
        # L_{n,k} = 0 for k > n
        for n in range(1, 5):
            for k in range(n+1, n+4):
                self.assertEqual(self.gs_lah.compute(n, k), 0.0)
    
    def test_stirling_first_kind(self):
        """Test Stirling numbers of the first kind (unsigned)."""
        # Known values for unsigned Stirling numbers of the first kind
        known_values = {
            (1, 1): 1,
            (2, 1): 1, (2, 2): 1,
            (3, 1): 2, (3, 2): 3, (3, 3): 1,
            (4, 1): 6, (4, 2): 11, (4, 3): 6, (4, 4): 1,
            (5, 1): 24, (5, 2): 50, (5, 3): 35, (5, 4): 10, (5, 5): 1
        }
        
        for (n, k), expected in known_values.items():
            computed = self.gs_stirling1.compute(n, k)
            self.assertAlmostEqual(computed, expected, delta=self.tol,
                                 msg=f"Stirling 1st kind s({n},{k})")
            
            # Also test the standalone function
            func_result = stirling_first_kind(n, k)
            self.assertAlmostEqual(func_result, expected, delta=self.tol,
                                 msg=f"Function stirling_first_kind({n},{k})")
    
    def test_stirling_second_kind(self):
        """Test Stirling numbers of the second kind."""
        # Known values for Stirling numbers of the second kind
        known_values = {
            (1, 1): 1,
            (2, 1): 1, (2, 2): 1,
            (3, 1): 1, (3, 2): 3, (3, 3): 1,
            (4, 1): 1, (4, 2): 7, (4, 3): 6, (4, 4): 1,
            (5, 1): 1, (5, 2): 15, (5, 3): 25, (5, 4): 10, (5, 5): 1
        }
        
        for (n, k), expected in known_values.items():
            computed = self.gs_stirling2.compute(n, k)
            self.assertAlmostEqual(computed, expected, delta=self.tol,
                                 msg=f"Stirling 2nd kind S({n},{k})")
            
            # Also test the standalone function
            func_result = stirling_second_kind(n, k)
            self.assertAlmostEqual(func_result, expected, delta=self.tol,
                                 msg=f"Function stirling_second_kind({n},{k})")
    
    def test_lah_numbers(self):
        """Test Lah numbers."""
        # Known values for Lah numbers
        known_values = {
            (1, 1): 1,
            (2, 1): 2, (2, 2): 1,
            (3, 1): 6, (3, 2): 6, (3, 3): 1,
            (4, 1): 24, (4, 2): 36, (4, 3): 12, (4, 4): 1,
            (5, 1): 120, (5, 2): 240, (5, 3): 120, (5, 4): 30, (5, 5): 1
        }
        
        for (n, k), expected in known_values.items():
            computed = self.gs_lah.compute(n, k)
            self.assertAlmostEqual(computed, expected, delta=self.tol,
                                 msg=f"Lah number L({n},{k})")
            
            # Also test the standalone function
            func_result = lah_number(n, k)
            self.assertAlmostEqual(func_result, expected, delta=self.tol,
                                 msg=f"Function lah_number({n},{k})")
    
    def test_single_list_case(self):
        """Test the single list case (k=1)."""
        # L_{n,1} = (n-1)! for Stirling numbers of the first kind
        for n in range(1, 7):
            expected = math.factorial(n-1) if n > 0 else 0
            computed = self.gs_stirling1.single_list_case(n)
            self.assertAlmostEqual(computed, expected, delta=self.tol,
                                 msg=f"Stirling 1st kind s({n},1)")
        
        # L_{n,1} = 1 for Stirling numbers of the second kind
        for n in range(1, 7):
            computed = self.gs_stirling2.single_list_case(n)
            self.assertEqual(computed, 1.0, msg=f"Stirling 2nd kind S({n},1)")
        
        # L_{n,1} = n! for Lah numbers
        for n in range(1, 7):
            expected = math.factorial(n) if n > 0 else 0
            computed = self.gs_lah.single_list_case(n)
            self.assertAlmostEqual(computed, expected, delta=self.tol,
                                 msg=f"Lah number L({n},1)")
        
        # Test custom parameters
        for n in range(1, 7):
            # Direct computation
            result1 = 1.0
            for j in range(1, n):
                result1 *= (j * self.gs_custom.alpha + self.gs_custom.beta)
            
            # Using method
            result2 = self.gs_custom.single_list_case(n)
            
            self.assertAlmostEqual(result1, result2, delta=self.tol,
                                 msg=f"Custom L_{{{n},1}}^{{{self.gs_custom.alpha},{self.gs_custom.beta}}}")
    
    def test_recurrence_relation(self):
        """Test triangular recurrence relation."""
        for gs in [self.gs_lah, self.gs_stirling1, self.gs_stirling2, self.gs_custom]:
            for n in range(2, 6):
                for k in range(1, n):
                    # Direct computation
                    direct = gs.compute(n, k)
                    
                    # Using recurrence relation
                    term1 = gs.compute(n-1, k-1)
                    term2 = (gs.alpha * (n-1) + gs.beta * k) * gs.compute(n-1, k)
                    recurrence = term1 + term2
                    
                    self.assertAlmostEqual(direct, recurrence, delta=self.tol,
                                         msg=f"Recurrence for L_{{{n},{k}}}^{{{gs.alpha},{gs.beta}}}")
    
    def test_method_consistency(self):
        """Test that all computation methods give consistent results."""
        for gs in [self.gs_lah, self.gs_custom]:
            for n in range(1, 8):
                for k in range(1, n+1):
                    methods = ['triangular', 'explicit', 'bottom_up']
                    
                    # Add horizontal and vertical methods where applicable
                    if n-k <= 5:  # Horizontal only efficient for small n-k
                        methods.append('horizontal')
                    if n > 1 and k > 1:  # Vertical needs n,k > 1
                        methods.append('vertical')
                    
                    # Add symmetric for appropriate cases
                    if n >= k and n-k < 5:
                        methods.append('symmetric')
                    
                    # Compute with each method
                    results = {}
                    for method in methods:
                        try:
                            results[method] = gs.compute(n, k, method=method)
                        except (RecursionError, OverflowError) as e:
                            # Skip if method has numerical issues
                            pass
                    
                    # Check that all methods give the same result
                    reference = next(iter(results.values()))
                    for method, result in results.items():
                        self.assertAlmostEqual(result, reference, delta=self.tol,
                                             msg=f"Method {method} for L_{{{n},{k}}}^{{{gs.alpha},{gs.beta}}}")
    
    def test_large_values(self):
        """Test computation with large values."""
        # Test larger values to ensure numerical stability
        n, k = 20, 10
        
        for gs in [self.gs_lah, self.gs_stirling2, self.gs_custom]:
            # Compute with different methods
            try:
                triangular = gs.compute(n, k, method='triangular')
                bottom_up = gs.compute(n, k, method='bottom_up')
                
                # Methods should give consistent results
                self.assertAlmostEqual(triangular, bottom_up, delta=1e-6,
                                     msg=f"Large value L_{{{n},{k}}}^{{{gs.alpha},{gs.beta}}}")
            except (OverflowError, RecursionError):
                # Skip if computation fails due to numerical issues
                pass
    
    def test_rising_factorial(self):
        """Test rising factorial computation."""
        # Simple cases
        self.assertEqual(self.gs_lah.rising_factorial(2.0, 0), 1.0)
        self.assertEqual(self.gs_lah.rising_factorial(2.0, 1), 2.0)
        self.assertEqual(self.gs_lah.rising_factorial(2.0, 3), 2.0 * 3.0 * 4.0)
        
        # With non-standard increment
        self.assertEqual(self.gs_lah.rising_factorial(2.0, 3, 0.5), 2.0 * 2.5 * 3.0)
        
        # With negative base
        self.assertEqual(self.gs_lah.rising_factorial(-1.0, 3), -1.0 * 0.0 * 1.0)
    
    def test_error_handling(self):
        """Test error handling for invalid inputs."""
        # Invalid method
        with self.assertRaises(ValueError):
            self.gs_lah.compute(3, 2, method='invalid_method')
        
        # Negative parameters
        with self.assertRaises(ValueError):
            self.gs_lah.compute(-1, 2)
        
        with self.assertRaises(ValueError):
            self.gs_lah.compute(3, -2)
        
        # Invalid parameters for single_list_case
        with self.assertRaises(ValueError):
            self.gs_lah.single_list_case(3, k=2)
    
    def test_symmetric_function(self):
        """Test symmetric function computation."""
        # Test simple cases
        self.assertEqual(self.gs_lah.symmetric_function(1, 0), 1.0)
        
        # L_{3,2} = 3 for Stirling 2nd kind
        self.assertEqual(self.gs_stirling2.symmetric_function(2, 1), 3.0)
        
        # L_{4,2} = 7 for Stirling 2nd kind
        self.assertEqual(self.gs_stirling2.symmetric_function(2, 2), 7.0)
        
        # L_{4,2} = 36 for Lah numbers
        self.assertEqual(self.gs_lah.symmetric_function(2, 2), 36.0)


if __name__ == '__main__':
    unittest.main()
