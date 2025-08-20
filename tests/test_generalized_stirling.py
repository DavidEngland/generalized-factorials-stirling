"""
Tests for the generalized Stirling numbers implementation.

These tests verify that our implementation matches the theoretical results
from the paper "Combinatorial approach of certain generalized Stirling numbers".
"""

import unittest
import sys
import os
from pathlib import Path

# Add the src directory to the path
sys.path.append(str(Path(__file__).parent.parent / "src"))
from generalized_stirling import GeneralizedStirling, stirling_first_kind, stirling_second_kind, lah_number


class TestGeneralizedStirling(unittest.TestCase):
    """Test cases for the GeneralizedStirling class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.gs_default = GeneralizedStirling()  # Default α=β=1 (Lah numbers)
        self.gs_first = GeneralizedStirling(alpha=1.0, beta=0.0)  # First kind
        self.gs_second = GeneralizedStirling(alpha=0.0, beta=1.0)  # Second kind
        self.gs_custom = GeneralizedStirling(alpha=2.0, beta=3.0)  # Custom parameters
        
        # Set tolerance for floating-point comparisons
        self.tol = 1e-10
    
    def test_base_cases(self):
        """Test base cases for the generalized Stirling numbers."""
        gs = self.gs_default
        
        # L{0,0} = 1
        self.assertEqual(gs.compute(0, 0), 1.0)
        
        # L{n,0} = 0 for n > 0
        for n in range(1, 5):
            self.assertEqual(gs.compute(n, 0), 0.0)
        
        # L{0,k} = 0 for k > 0
        for k in range(1, 5):
            self.assertEqual(gs.compute(0, k), 0.0)
        
        # L{n,k} = 0 for k > n
        for n in range(1, 5):
            for k in range(n+1, n+3):
                self.assertEqual(gs.compute(n, k), 0.0)
        
        # L{n,n} = 1
        for n in range(1, 5):
            self.assertEqual(gs.compute(n, n), 1.0)
    
    def test_triangular_recurrence(self):
        """Test triangular recurrence relation."""
        gs = self.gs_custom
        
        for n in range(2, 6):
            for k in range(1, n):
                direct = gs.compute(n, k)
                
                # L{n,k} = L{n-1,k-1} + (α(n-1) + βk) * L{n-1,k}
                term1 = gs.compute(n-1, k-1)
                term2 = (gs.alpha * (n-1) + gs.beta * k) * gs.compute(n-1, k)
                recurrence = term1 + term2
                
                self.assertAlmostEqual(direct, recurrence, delta=self.tol,
                                    msg=f"Failed for n={n}, k={k}")
    
    def test_special_case_k1(self):
        """Test the special case formula for k=1."""
        gs = self.gs_custom
        
        for n in range(1, 6):
            direct = gs.compute(n, 1)
            special = gs.special_case(n, 1)
            
            self.assertAlmostEqual(direct, special, delta=self.tol,
                                msg=f"Failed for n={n}, k=1")
    
    def test_explicit_formula(self):
        """Test explicit formula matches triangular recurrence."""
        gs = self.gs_custom
        
        for n in range(1, 6):
            for k in range(1, n+1):
                triangular = gs.triangular_recurrence(n, k)
                explicit = gs.explicit_formula(n, k)
                
                self.assertAlmostEqual(triangular, explicit, delta=self.tol,
                                    msg=f"Failed for n={n}, k={k}")
    
    def test_first_kind_stirling(self):
        """Test reduction to Stirling numbers of the first kind."""
        # Known values for unsigned Stirling numbers of first kind
        known_values = {
            (1, 1): 1,
            (2, 1): 1, (2, 2): 1,
            (3, 1): 2, (3, 2): 3, (3, 3): 1,
            (4, 1): 6, (4, 2): 11, (4, 3): 6, (4, 4): 1
        }
        
        for (n, k), expected in known_values.items():
            computed = self.gs_first.compute(n, k)
            self.assertAlmostEqual(computed, expected, delta=self.tol,
                                msg=f"Failed for first kind S({n},{k})")
            
            # Also test the convenience function
            func_value = stirling_first_kind(n, k)
            self.assertAlmostEqual(func_value, expected, delta=self.tol,
                                msg=f"Failed for function S({n},{k})")
    
    def test_second_kind_stirling(self):
        """Test reduction to Stirling numbers of the second kind."""
        # Known values for Stirling numbers of second kind
        known_values = {
            (1, 1): 1,
            (2, 1): 1, (2, 2): 1,
            (3, 1): 1, (3, 2): 3, (3, 3): 1,
            (4, 1): 1, (4, 2): 7, (4, 3): 6, (4, 4): 1
        }
        
        for (n, k), expected in known_values.items():
            computed = self.gs_second.compute(n, k)
            self.assertAlmostEqual(computed, expected, delta=self.tol,
                                msg=f"Failed for second kind S({n},{k})")
            
            # Also test the convenience function
            func_value = stirling_second_kind(n, k)
            self.assertAlmostEqual(func_value, expected, delta=self.tol,
                                msg=f"Failed for function S({n},{k})")
    
    def test_lah_numbers(self):
        """Test reduction to Lah numbers."""
        # Known values for Lah numbers
        known_values = {
            (1, 1): 1,
            (2, 1): 2, (2, 2): 1,
            (3, 1): 6, (3, 2): 6, (3, 3): 1,
            (4, 1): 24, (4, 2): 36, (4, 3): 12, (4, 4): 1
        }
        
        for (n, k), expected in known_values.items():
            computed = self.gs_default.compute(n, k)
            self.assertAlmostEqual(computed, expected, delta=self.tol,
                                msg=f"Failed for Lah L({n},{k})")
            
            # Also test the convenience function
            func_value = lah_number(n, k)
            self.assertAlmostEqual(func_value, expected, delta=self.tol,
                                msg=f"Failed for function L({n},{k})")
    
    def test_example_n3_k1(self):
        """Test the example from the paper for n=3, k=1."""
        # For α=β=1, we expect L{3,1} = (α+β)(2α+β) = 2*3 = 6
        gs = GeneralizedStirling(alpha=1.0, beta=1.0)
        self.assertEqual(gs.compute(3, 1), 6.0)
        
        # For general α,β, verify formula (α+β)(2α+β)
        for alpha, beta in [(2.0, 3.0), (1.5, 2.5), (0.5, 1.5)]:
            gs = GeneralizedStirling(alpha=alpha, beta=beta)
            expected = (alpha + beta) * (2 * alpha + beta)
            computed = gs.compute(3, 1)
            self.assertAlmostEqual(computed, expected, delta=self.tol,
                                msg=f"Failed for α={alpha}, β={beta}")
    
    def test_horizontal_recurrence(self):
        """Test horizontal recurrence relation."""
        gs = self.gs_custom
        
        for n in range(2, 6):
            for k in range(1, n):
                direct = gs.compute(n, k)
                horizontal = gs.horizontal_recurrence(n, k)
                
                self.assertAlmostEqual(direct, horizontal, delta=self.tol,
                                    msg=f"Failed for n={n}, k={k}")
    
    def test_vertical_recurrence(self):
        """Test vertical recurrence relation."""
        gs = self.gs_custom
        
        for n in range(1, 5):
            for k in range(1, n):
                direct = gs.compute(n+1, k+1)
                vertical = gs.vertical_recurrence(n, k)
                
                self.assertAlmostEqual(direct, vertical, delta=self.tol,
                                    msg=f"Failed for n={n+1}, k={k+1}")


if __name__ == "__main__":
    unittest.main()
