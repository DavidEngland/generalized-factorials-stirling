# Generalized Stirling Numbers Documentation

## Overview

The `generalized_stirling.py` module implements the generalized Stirling numbers, denoted as L{n,k}^{α,β}, based on the paper "Combinatorial approach of certain generalized Stirling numbers" by Belbachir, Belkhir, and Bousbaa. These numbers provide a unified framework that includes classical Stirling numbers, Lah numbers, and other important combinatorial sequences as special cases.

## Mathematical Background

### Definition

Generalized Stirling numbers L{n,k}^{α,β} represent the total weight of distributing n elements into k ordered non-empty lists, where:

1. The head of each list has weight β
2. Other elements in lists have weight α
3. The first element placed in each list has weight 1

### Recurrence Relation

The fundamental recurrence relation is:

$$L_{n,k}^{\alpha,\beta} = L_{n-1,k-1}^{\alpha,\beta} + (\alpha(n-1) + \beta k) \cdot L_{n-1,k}^{\alpha,\beta}$$

This has a clear combinatorial interpretation:
- The first term represents placing element n in its own list
- The second term represents placing element n into an existing list, either after an element (weight α) or at the head (weight β)

### Explicit Formula

$$L_{n,k}^{\alpha,\beta} = \frac{1}{\beta^k \cdot k!} \sum_{j=0}^{k} (-1)^j \binom{k}{j} (\beta(k-j)|\alpha)^{\overline{n}}$$

where $$(x|\alpha)^{\overline{n}}$$ is the rising factorial $x(x+\alpha)(x+2\alpha)\cdots(x+(n-1)\alpha)$$.

### Special Cases

- **Stirling numbers of the first kind** (unsigned): L{n,k}^{1,0}
  - Count permutations of n elements with exactly k cycles
  
- **Stirling numbers of the second kind**: L{n,k}^{0,1}
  - Count partitions of n elements into exactly k non-empty subsets
  
- **Lah numbers**: L{n,k}^{1,1}
  - Count partitions of n elements into exactly k ordered lists

## Installation and Requirements

### Requirements

- Python 3.6+
- NumPy
- SciPy (optional, but recommended for enhanced numerical stability)

The module will work without SciPy, but will use SciPy's `poch` function for better numerical stability when available.

## Basic Usage

### Computing Individual Values

```python
from generalized_stirling import GeneralizedStirling

# Create an instance with desired parameters
gs = GeneralizedStirling(alpha=1.0, beta=1.0)  # Lah numbers

# Compute L{5,3}^{1,1}
result = gs.compute(5, 3)
print(f"L{{5,3}}^{{1,1}} = {result}")  # Output: L{5,3}^{1,1} = 60.0
```

### Special Cases with Convenience Functions

```python
from generalized_stirling import stirling_first_kind, stirling_second_kind, lah_number

# Stirling number of the first kind (unsigned)
s1 = stirling_first_kind(5, 3)  # 35.0

# Stirling number of the second kind
s2 = stirling_second_kind(5, 3)  # 10.0

# Lah number
l = lah_number(5, 3)  # 60.0
```

### Generating Triangles

```python
# Generate a triangle of Lah numbers
gs = GeneralizedStirling(alpha=1.0, beta=1.0)
triangle = gs.generate_triangle(5)
for i, row in enumerate(triangle):
    print(f"Row {i+1}: {' '.join(row)}")

# Sparse representation
sparse = gs.generate_triangle(5, sparse=True)
print(sparse[(4, 2)])  # Value at position (4,2)
```

## Advanced Features

### Computation Methods

The module implements several algorithms for computing generalized Stirling numbers:

1. **triangular**: Uses the recursive triangular recurrence relation
2. **explicit**: Uses the explicit formula (inclusion-exclusion)
3. **bottom_up**: Uses dynamic programming for large values
4. **horizontal**: Uses the horizontal recurrence relation
5. **vertical**: Uses the vertical recurrence relation
6. **symmetric**: Uses the symmetric function formula
7. **single_list**: Specialized formula for k=1 cases

You can specify which method to use:

```python
gs = GeneralizedStirling(alpha=1.0, beta=0.0)
value1 = gs.compute(10, 5, method='triangular')
value2 = gs.compute(10, 5, method='explicit')
value3 = gs.compute(10, 5, method='bottom_up')
```

With `method='auto'` (the default), the module automatically selects the most efficient method based on the input size and parameters.

### Caching

The module implements two levels of caching:

1. **In-memory caching**: All computed values are cached in memory for quick lookups
2. **Disk-based caching**: Optionally, values can be cached to disk for persistence across runs

To enable disk caching:

```python
# Create instance with disk caching enabled
gs = GeneralizedStirling(alpha=1.0, beta=1.0, use_disk_cache=True)

# Optionally specify a cache directory
gs = GeneralizedStirling(alpha=1.0, beta=1.0, use_disk_cache=True, 
                         cache_dir="/path/to/cache")
```

### Performance Monitoring

Track performance statistics:

```python
gs = GeneralizedStirling(alpha=1.0, beta=1.0)

# Compute some values
for n in range(1, 10):
    for k in range(1, n+1):
        gs.compute(n, k)

# Print performance summary
gs.summary()

# Get raw statistics
stats = gs.get_performance_stats()
print(f"Cache hit ratio: {stats['hit_ratio']}")
```

### Parallel Computation

For generating large triangles, parallel computation can be used:

```python
from generalized_stirling import parallel_generate_triangle

# Generate a triangle of Stirling numbers of the second kind
triangle = parallel_generate_triangle(20, alpha=0.0, beta=1.0)
```

### Memory-Efficient Generation

For very large triangles, use the memory-efficient iterator:

```python
from generalized_stirling import memory_efficient_iterator

# Iterate through values without storing the entire triangle
for n, k, value in memory_efficient_iterator(100, alpha=1.0, beta=1.0):
    # Process each value individually
    if value > 1e10:
        print(f"Large value at L{{{n},{k}}}^{{1,1}} = {value}")
```

## Numerical Stability

The module includes several features to enhance numerical stability:

1. **Log-space computation**: For large values, computations are performed in logarithmic space to avoid overflow
2. **SciPy integration**: Uses SciPy's specialized functions when available
3. **Early exit optimizations**: Checks for zeros and special cases to exit computations early
4. **Fallback mechanisms**: Automatically switches to more stable methods when numerical issues are detected

## API Reference

### GeneralizedStirling Class

```python
GeneralizedStirling(alpha=1.0, beta=1.0, cache_size=10000, use_disk_cache=False, cache_dir=None)
```

**Parameters**:
- `alpha` (float): Weight parameter for non-head elements
- `beta` (float): Weight parameter for head elements
- `cache_size` (int): Maximum size for LRU cache
- `use_disk_cache` (bool): Whether to use disk-based caching
- `cache_dir` (str, optional): Directory for disk cache

**Main Methods**:
- `compute(n, k, method='auto')`: Compute L{n,k}^{α,β} using the specified method
- `generate_triangle(n_max, format_str="{:.0f}", method='auto', sparse=False)`: Generate a triangle of values
- `summary()`: Print a summary of performance statistics
- `clear_cache()`: Clear all caches to free memory

**Computation Methods**:
- `explicit_formula(n, k)`: Compute using the explicit formula
- `triangular_recurrence(n, k)`: Compute using the triangular recurrence relation
- `bottom_up_computation(n, k)`: Compute using bottom-up dynamic programming
- `horizontal_recurrence(n, k)`: Compute using the horizontal recurrence
- `vertical_recurrence(n, k)`: Compute using the vertical recurrence
- `single_list_case(n, k=1)`: Compute using the special case formula for k=1
- `symmetric_function(n, k)`: Compute using the symmetric function formula

### Utility Functions

- `stirling_first_kind(n, k)`: Compute the unsigned Stirling number of the first kind
- `stirling_second_kind(n, k)`: Compute the Stirling number of the second kind
- `lah_number(n, k)`: Compute the Lah number
- `parallel_generate_triangle(n_max, alpha=1.0, beta=1.0, method='auto', processes=None)`: Generate triangle in parallel
- `memory_efficient_iterator(n_max, alpha=1.0, beta=1.0, method='auto')`: Memory-efficient iterator

## Performance Considerations

### Method Selection Guidelines

- For small values (n < 20, k < 10): `triangular` method is fastest
- For large values (n > 100 or k > 50): `bottom_up` method avoids recursion depth issues
- For values near the diagonal (n-k < 5): `symmetric` method is efficient
- For classical Stirling numbers: `triangular` method is optimized

### Memory Usage

- In-memory caching: O(N) where N is the number of computed values
- Bottom-up computation: O(k) memory usage regardless of n
- Memory-efficient iterator: O(1) additional memory for triangle generation

## Examples

### Verifying Special Cases

```python
from generalized_stirling import GeneralizedStirling

# Create instances for different special cases
s1 = GeneralizedStirling(alpha=1.0, beta=0.0)  # Stirling numbers of the first kind
s2 = GeneralizedStirling(alpha=0.0, beta=1.0)  # Stirling numbers of the second kind
lah = GeneralizedStirling(alpha=1.0, beta=1.0)  # Lah numbers

# Verify known values
assert s1.compute(4, 2) == 11.0
assert s2.compute(4, 2) == 7.0
assert lah.compute(4, 2) == 36.0
```

### Computing Large Values

```python
from generalized_stirling import GeneralizedStirling

gs = GeneralizedStirling(alpha=1.0, beta=1.0, use_disk_cache=True)

# Compute a large value
large_value = gs.compute(100, 50)
print(f"L{{100,50}}^{{1,1}} = {large_value:.2e}")
```

## References

1. H. Belbachir, A. Belkhir, and I. E. Bousbaa. "Combinatorial approach of certain generalized Stirling numbers." arXiv:1411.6271v1, 2014.

2. L. C. Hsu and P. J.-S. Shiue. "A unified approach to generalized Stirling numbers." Adv. in Appl. Math., 20(3):366-384, 1998.

3. A. Z. Broder. "The r-Stirling numbers." Discrete Math., 49(3):241-259, 1984.

4. M. Benoumhani. "On Whitney numbers of Dowling lattices." Discrete Math., 159(1-3):13-33, 1996.

5. L. Carlitz. "Weighted Stirling numbers of the first and second kind." Fibonacci Quart., 18(2):147-162, 1980.

6. F. T. Howard. "Associated Stirling numbers." Fibonacci Quart., 18(4):303-315, 1980.

## Future Directions

Potential extensions to the module include:

1. Supporting r-Stirling numbers and other generalizations
2. Adding visualization tools for triangle patterns
3. Implementing asymptotic approximations for very large values
4. Supporting symbolic computation for exact results
5. Enhancing the disk cache with compression for large values
