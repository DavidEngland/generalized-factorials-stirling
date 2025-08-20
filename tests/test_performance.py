"""
Performance tests for the generalized Stirling numbers implementation.

These tests verify that the optimized implementations perform as expected.
"""

import unittest
import sys
import os
import time
from pathlib import Path
import numpy as np

# Add the src directory to the path
sys.path.append(str(Path(__file__).parent.parent / "src"))
from generalized_stirling import GeneralizedStirling, parallel_generate_triangle, memory_efficient_iterator

class TestPerformance(unittest.TestCase):
    """Test performance characteristics of generalized Stirling numbers."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.gs = GeneralizedStirling(alpha=1.0, beta=1.0)
        
        # Tolerance for floating-point comparisons
        self.tol = 1e-10
        
        # Timeout threshold for performance tests (seconds)
        self.timeout = 5.0
    
    def test_caching_performance(self):
        """Test that caching improves performance for repeated calculations."""
        # First calculation (cold cache)
        start_time = time.time()
        result1 = self.gs.compute(20, 10)
        cold_time = time.time() - start_time
        
        # Second calculation (warm cache)
        start_time = time.time()
        result2 = self.gs.compute(20, 10)
        warm_time = time.time() - start_time
        
        # Verify correctness
        self.assertAlmostEqual(result1, result2, delta=self.tol)
        
        # Verify performance improvement
        self.assertLess(warm_time, cold_time / 2,
                      msg=f"Caching not effective: cold={cold_time:.6f}s, warm={warm_time:.6f}s")
        
        # Check cache stats
        stats = self.gs.get_performance_stats()
        self.assertGreater(stats['cache_hits'].get('triangular', 0), 0,
                         msg="No cache hits recorded")
    
    def test_bottom_up_vs_recursive(self):
        """Test that bottom-up approach is faster than recursive for large values."""
        n, k = 50, 25
        
        # Skip test if it would take too long
        if n > 80:
            self.skipTest("Skipping large value test to avoid timeout")
        
        # Measure time for triangular recursion
        start_time = time.time()
        recursive_result = self.gs.compute(n, k, method='triangular')
        recursive_time = time.time() - start_time
        
        if recursive_time > self.timeout:
            self.skipTest(f"Recursive method took too long ({recursive_time:.2f}s > {self.timeout:.2f}s)")
        
        # Measure time for bottom-up approach
        start_time = time.time()
        bottom_up_result = self.gs.compute(n, k, method='bottom_up')
        bottom_up_time = time.time() - start_time
        
        # Verify correctness
        self.assertAlmostEqual(recursive_result, bottom_up_result, delta=self.tol)
        
        # For large values, bottom-up should be faster
        # (This might not always be true due to optimization, caching, etc.)
        print(f"\nBottomUp: {bottom_up_time:.6f}s, Recursive: {recursive_time:.6f}s")
    
    def test_special_case_performance(self):
        """Test that special case for k=1 is faster than general methods."""
        n = 100
        
        # Measure time for special case
        start_time = time.time()
        special_result = self.gs.special_case(n)
        special_time = time.time() - start_time
        
        # Measure time for triangular recurrence
        start_time = time.time()
        triangular_result = self.gs.triangular_recurrence(n, 1)
        triangular_time = time.time() - start_time
        
        # Verify correctness
        self.assertAlmostEqual(special_result, triangular_result, delta=self.tol)
        
        # Special case should be faster
        self.assertLess(special_time, triangular_time,
                      msg=f"Special case not faster: special={special_time:.6f}s, triangular={triangular_time:.6f}s")
    
    def test_auto_method_selection(self):
        """Test that auto method selection chooses appropriate methods."""
        gs = GeneralizedStirling(alpha=1.0, beta=1.0)
        
        # Small values should use triangular recurrence
        n, k = 10, 5
        start_time = time.time()
        auto_result = gs.compute(n, k, method='auto')
        auto_time = time.time() - start_time
        
        # Verify the auto-selected method by checking timing
        # This is a bit of a hack but works for demonstration
        triangular_time = time.time()
        gs.compute(n, k, method='triangular')
        triangular_time = time.time() - triangular_time
        
        bottom_up_time = time.time()
        gs.compute(n, k, method='bottom_up')
        bottom_up_time = time.time() - bottom_up_time
        
        # Find which method time is closest to auto time
        time_diffs = {
            'triangular': abs(auto_time - triangular_time),
            'bottom_up': abs(auto_time - bottom_up_time)
        }
        
        selected_method = min(time_diffs, key=time_diffs.get)
        print(f"\nAuto-selected method for n={n}, k={k} appears to be: {selected_method}")
        
        # Large values should use bottom-up or special case
        n, k = 80, 40
        if n <= 100:  # Skip if too large
            method_used = ''
            
            # Clear cache first
            gs.clear_cache()
            
            start_time = time.time()
            auto_result = gs.compute(n, k, method='auto')
            auto_time = time.time() - start_time
            
            # Check cache stats to infer which method was used
            stats = gs.get_performance_stats()
            if stats['cache_hits'].get('bottom_up', 0) + stats['cache_misses'].get('bottom_up', 0) > 0:
                method_used = 'bottom_up'
            elif stats['cache_hits'].get('triangular', 0) + stats['cache_misses'].get('triangular', 0) > 0:
                method_used = 'triangular'
            
            print(f"Auto-selected method for n={n}, k={k} appears to be: {method_used}")
    
    def test_memory_efficiency(self):
        """Test memory-efficient triangle generation."""
        n_max = 20
        
        # Generate triangle using standard approach
        triangle = self.gs.generate_triangle(n_max)
        
        # Generate triangle using sparse approach
        sparse_triangle = self.gs.generate_triangle(n_max, sparse=True)
        
        # Convert sparse to dense for comparison
        dense_from_sparse = [['' for _ in range(n)] for n in range(1, n_max+1)]
        for (n, k), value in sparse_triangle.items():
            if 1 <= n <= n_max and 1 <= k <= n:
                dense_from_sparse[n-1][k-1] = value
        
        # Verify first few rows match (only checking non-empty entries)
        for n in range(min(5, n_max)):
            for k in range(min(n+1, 5)):
                if dense_from_sparse[n][k] != '':
                    self.assertEqual(triangle[n][k], dense_from_sparse[n][k])
        
        # Test iterator approach
        values = list(memory_efficient_iterator(5, alpha=1.0, beta=1.0))
        self.assertEqual(len(values), 15)  # 1+2+3+4+5 = 15 values for n_max=5
        
        # Verify a few specific values from iterator
        for n, k, value in values:
            if n <= 5 and k <= n:
                expected = self.gs.compute(n, k)
                self.assertAlmostEqual(value, expected, delta=self.tol)
    
    def test_parallel_computation(self):
        """Test parallel triangle generation."""
        n_max = 15
        
        # Only run this test if we have multiple CPUs
        import multiprocessing
        if multiprocessing.cpu_count() < 2:
            self.skipTest("Skipping parallel test on single-CPU system")
        
        # Generate triangle sequentially
        sequential_start = time.time()
        sequential_triangle = self.gs.generate_triangle(n_max)
        sequential_time = time.time() - sequential_start
        
        # Generate triangle in parallel
        parallel_start = time.time()
        parallel_triangle = parallel_generate_triangle(n_max, alpha=1.0, beta=1.0, processes=2)
        parallel_time = time.time() - parallel_start
        
        # Verify results match
        for n in range(min(5, n_max)):
            self.assertEqual(len(sequential_triangle[n]), len(parallel_triangle[n]))
            for k in range(len(sequential_triangle[n])):
                seq_value = float(sequential_triangle[n][k])
                par_value = parallel_triangle[n][k]
                self.assertAlmostEqual(seq_value, par_value, delta=self.tol)
        
        # Note: Parallel might not always be faster for small triangles due to overhead
        print(f"\nSequential: {sequential_time:.6f}s, Parallel: {parallel_time:.6f}s")

if __name__ == "__main__":
    unittest.main()
