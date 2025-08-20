"""
Example demonstrating the disk cache functionality of GeneralizedStirling.

This example shows how to enable and use disk caching for large computations.
"""

import sys
import os
import time
from pathlib import Path
import tempfile

# Add the src directory to the path
sys.path.append(str(Path(__file__).parent.parent / "src"))
from generalized_stirling import GeneralizedStirling

def demonstrate_disk_cache():
    """Demonstrate the disk cache functionality"""
    print("Disk Cache Example")
    print("-" * 50)
    
    # Create a temporary directory for the cache
    cache_dir = os.path.join(tempfile.gettempdir(), "gsn_disk_cache_example")
    
    # Create instance with disk cache enabled
    gs = GeneralizedStirling(alpha=1.0, beta=1.0, use_disk_cache=True, cache_dir=cache_dir)
    print(f"Disk cache enabled. Cache directory: {cache_dir}")
    
    # Compute a large value (will be slow the first time)
    n, k = 50, 25
    print(f"\nComputing L{{{n},{k}}}^{{1,1}} for the first time...")
    start_time = time.time()
    result1 = gs.compute(n, k)
    elapsed1 = time.time() - start_time
    
    print(f"Result: {result1}")
    print(f"Time taken: {elapsed1:.2f} seconds")
    
    # Show cache statistics
    stats = gs.get_performance_stats()
    print(f"\nCache statistics after first computation:")
    print(f"Cache hits: {stats['cache_hits']}")
    print(f"Cache misses: {stats['cache_misses']}")
    print(f"Disk cache size: {stats['disk_cache_size']} bytes")
    
    # Compute the same value again (should be faster due to caching)
    print(f"\nComputing L{{{n},{k}}}^{{1,1}} again (should be faster)...")
    start_time = time.time()
    result2 = gs.compute(n, k)
    elapsed2 = time.time() - start_time
    
    print(f"Result: {result2}")
    print(f"Time taken: {elapsed2:.2f} seconds")
    print(f"Speedup factor: {elapsed1/elapsed2:.1f}x")
    
    # Show updated cache statistics
    stats = gs.get_performance_stats()
    print(f"\nCache statistics after second computation:")
    print(f"Cache hits: {stats['cache_hits']}")
    print(f"Cache misses: {stats['cache_misses']}")
    
    # Create a new instance with the same cache directory
    print("\nCreating a new instance with the same cache directory...")
    gs2 = GeneralizedStirling(alpha=1.0, beta=1.0, use_disk_cache=True, cache_dir=cache_dir)
    
    # The value should still be cached on disk
    start_time = time.time()
    result3 = gs2.compute(n, k)
    elapsed3 = time.time() - start_time
    
    print(f"Result from new instance: {result3}")
    print(f"Time taken: {elapsed3:.2f} seconds")
    
    # Clean up
    print("\nCleaning up disk cache...")
    gs.clear_cache()
    
    # Verify the cache directory is empty
    if os.path.exists(cache_dir):
        files = os.listdir(cache_dir)
        print(f"Remaining files in cache directory: {files}")
    else:
        print("Cache directory was removed")

if __name__ == "__main__":
    demonstrate_disk_cache()
