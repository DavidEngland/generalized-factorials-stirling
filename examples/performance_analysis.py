"""
Performance Analysis for Generalized Stirling Numbers

This module demonstrates and analyzes the performance of different computation
methods for generalized Stirling numbers.
"""

import sys
import os
import time
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import pandas as pd
from memory_profiler import memory_usage

# Add the src directory to the path
sys.path.append(str(Path(__file__).parent.parent / "src"))
from generalized_stirling import GeneralizedStirling, parallel_generate_triangle, memory_efficient_iterator

def benchmark_methods(n_values, k_values, alpha=1.0, beta=1.0):
    """
    Benchmark different computation methods across various input sizes.
    
    Args:
        n_values (list): List of n values to test
        k_values (list): List of k values to test
        alpha (float): Weight parameter for non-head elements
        beta (float): Weight parameter for head elements
        
    Returns:
        dict: Benchmark results
    """
    methods = ['triangular', 'explicit', 'bottom_up', 'symmetric']
    results = {method: {} for method in methods}
    
    for n in n_values:
        for k in k_values:
            if k > n:
                continue
                
            print(f"Benchmarking n={n}, k={k}...")
            gs = GeneralizedStirling(alpha=alpha, beta=beta)
            
            for method in methods:
                try:
                    start_time = time.time()
                    value = gs.compute(n, k, method=method)
                    elapsed_time = time.time() - start_time
                    
                    # Store result
                    key = f"n={n},k={k}"
                    results[method][key] = {
                        'time': elapsed_time,
                        'value': value
                    }
                    
                    print(f"  {method}: {elapsed_time:.6f} seconds")
                except Exception as e:
                    print(f"  {method}: Error - {str(e)}")
                    results[method][f"n={n},k={k}"] = {
                        'time': float('inf'),
                        'error': str(e)
                    }
    
    return results

def plot_benchmark_results(results, title="Method Performance Comparison"):
    """
    Plot benchmark results for visual comparison.
    
    Args:
        results (dict): Benchmark results from benchmark_methods
        title (str): Plot title
    """
    methods = list(results.keys())
    test_cases = list(results[methods[0]].keys())
    
    # Extract times for each method and test case
    times = {method: [results[method][case]['time'] for case in test_cases] for method in methods}
    
    # Create a DataFrame for easier plotting
    df = pd.DataFrame(times, index=test_cases)
    
    # Plot
    ax = df.plot(kind='bar', figsize=(12, 8), logy=True)
    ax.set_ylabel('Time (seconds, log scale)')
    ax.set_xlabel('Test Case (n,k)')
    ax.set_title(title)
    ax.legend(title='Method')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('method_performance_comparison.png')
    plt.close()
    
    # Also create a heatmap for each method
    for method in methods:
        # Extract n and k values from test case strings
        nk_values = [tuple(map(int, case.replace('n=', '').replace('k=', '').split(','))) for case in test_cases]
        n_values = sorted(set(n for n, _ in nk_values))
        k_values = sorted(set(k for _, k in nk_values))
        
        # Create a 2D array for the heatmap
        heatmap_data = np.zeros((len(n_values), len(k_values)))
        for i, n in enumerate(n_values):
            for j, k in enumerate(k_values):
                case = f"n={n},k={k}"
                if case in results[method]:
                    heatmap_data[i, j] = results[method][case]['time']
                else:
                    heatmap_data[i, j] = np.nan
        
        # Plot heatmap
        plt.figure(figsize=(10, 8))
        plt.imshow(heatmap_data, cmap='viridis', aspect='auto')
        plt.colorbar(label='Time (seconds)')
        plt.title(f'{method.capitalize()} Method Performance')
        plt.xlabel('k')
        plt.ylabel('n')
        plt.xticks(range(len(k_values)), k_values)
        plt.yticks(range(len(n_values)), n_values)
        
        # Add text annotations
        for i in range(len(n_values)):
            for j in range(len(k_values)):
                if not np.isnan(heatmap_data[i, j]):
                    plt.text(j, i, f'{heatmap_data[i, j]:.3f}', 
                             ha='center', va='center', color='w' if heatmap_data[i, j] > 0.5 else 'k')
        
        plt.tight_layout()
        plt.savefig(f'{method}_performance_heatmap.png')
        plt.close()

def benchmark_memory_usage():
    """
    Benchmark memory usage of different approaches for generating Stirling number triangles.
    """
    print("Benchmarking memory usage...")
    n_max = 30
    
    # Define functions to test
    def generate_standard():
        gs = GeneralizedStirling(alpha=1.0, beta=1.0)
        return gs.generate_triangle(n_max)
    
    def generate_sparse():
        gs = GeneralizedStirling(alpha=1.0, beta=1.0)
        return gs.generate_triangle(n_max, sparse=True)
    
    def generate_iterator():
        result = []
        for n, k, value in memory_efficient_iterator(n_max):
            result.append((n, k, value))
        return result
    
    # Measure memory usage
    mem_standard = max(memory_usage((generate_standard, ())))
    mem_sparse = max(memory_usage((generate_sparse, ())))
    mem_iterator = max(memory_usage((generate_iterator, ())))
    
    print(f"Standard approach: {mem_standard:.2f} MiB")
    print(f"Sparse approach: {mem_sparse:.2f} MiB")
    print(f"Iterator approach: {mem_iterator:.2f} MiB")
    
    # Plot results
    methods = ['Standard', 'Sparse', 'Iterator']
    memory_usage_values = [mem_standard, mem_sparse, mem_iterator]
    
    plt.figure(figsize=(10, 6))
    plt.bar(methods, memory_usage_values)
    plt.ylabel('Memory Usage (MiB)')
    plt.title(f'Memory Usage Comparison (n_max={n_max})')
    plt.tight_layout()
    plt.savefig('memory_usage_comparison.png')
    plt.close()

def benchmark_caching_effectiveness():
    """
    Benchmark the effectiveness of caching in the GeneralizedStirling class.
    """
    print("Benchmarking caching effectiveness...")
    
    # Use a sequence that generates many overlapping subproblems
    gs = GeneralizedStirling(alpha=1.0, beta=1.0)
    
    # First run: cold cache
    start_time = time.time()
    gs.compute(20, 10)
    cold_time = time.time() - start_time
    
    # Get cache statistics
    stats_after_first = gs.get_performance_stats()
    
    # Second run: warm cache
    start_time = time.time()
    gs.compute(20, 10)
    warm_time = time.time() - start_time
    
    # Get updated cache statistics
    stats_after_second = gs.get_performance_stats()
    
    print(f"Cold cache time: {cold_time:.6f} seconds")
    print(f"Warm cache time: {warm_time:.6f} seconds")
    print(f"Speedup factor: {cold_time / warm_time:.2f}x")
    
    print("\nCache statistics after first computation:")
    for method, hits in stats_after_first['cache_hits'].items():
        misses = stats_after_first['cache_misses'][method]
        if hits + misses > 0:
            hit_ratio = hits / (hits + misses)
            print(f"  {method}: {hits} hits, {misses} misses, {hit_ratio:.2%} hit ratio")
    
    print("\nCache statistics after second computation:")
    for method, hits in stats_after_second['cache_hits'].items():
        misses = stats_after_second['cache_misses'][method]
        if hits + misses > 0:
            hit_ratio = hits / (hits + misses)
            print(f"  {method}: {hits} hits, {misses} misses, {hit_ratio:.2%} hit ratio")
    
    # Now try with a sequence of increasing values
    print("\nBenchmarking sequence of computations...")
    gs.clear_cache()
    
    times = []
    for n in range(5, 26):
        start_time = time.time()
        gs.compute(n, 5)
        elapsed = time.time() - start_time
        times.append(elapsed)
        print(f"n={n}, k=5: {elapsed:.6f} seconds")
    
    # Plot times
    plt.figure(figsize=(10, 6))
    plt.plot(range(5, 26), times, marker='o')
    plt.xlabel('n')
    plt.ylabel('Computation Time (seconds)')
    plt.title('Computation Time for L{n,5} with Caching')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('caching_effectiveness.png')
    plt.close()

def benchmark_parallel_computation():
    """
    Benchmark parallel computation of Stirling number triangles.
    """
    print("Benchmarking parallel computation...")
    n_max = 30
    
    # Sequential computation
    start_time = time.time()
    gs = GeneralizedStirling(alpha=1.0, beta=1.0)
    sequential_triangle = gs.generate_triangle(n_max)
    sequential_time = time.time() - start_time
    print(f"Sequential computation: {sequential_time:.6f} seconds")
    
    # Parallel computation with different numbers of processes
    process_counts = [2, 4, 8]
    parallel_times = []
    
    for processes in process_counts:
        start_time = time.time()
        parallel_triangle = parallel_generate_triangle(n_max, processes=processes)
        elapsed = time.time() - start_time
        parallel_times.append(elapsed)
        print(f"Parallel computation ({processes} processes): {elapsed:.6f} seconds")
        print(f"Speedup: {sequential_time / elapsed:.2f}x")
    
    # Plot results
    plt.figure(figsize=(10, 6))
    plt.bar(['Sequential'] + [f'Parallel ({p})' for p in process_counts], 
            [sequential_time] + parallel_times)
    plt.ylabel('Computation Time (seconds)')
    plt.title(f'Parallel vs Sequential Computation (n_max={n_max})')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('parallel_computation_comparison.png')
    plt.close()

def run_all_benchmarks():
    """Run all benchmarking functions"""
    # Define test cases
    n_values = [5, 10, 15, 20, 25]
    k_values = [2, 3, 5, 10]
    
    # Run method benchmarks
    results = benchmark_methods(n_values, k_values)
    plot_benchmark_results(results)
    
    # Run memory usage benchmark
    benchmark_memory_usage()
    
    # Run caching effectiveness benchmark
    benchmark_caching_effectiveness()
    
    # Run parallel computation benchmark
    benchmark_parallel_computation()

if __name__ == "__main__":
    run_all_benchmarks()
