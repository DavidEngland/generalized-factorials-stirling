# Cross-Language Examples for Generalized Stirling Numbers

**Version: 0.2.0** (Updated: 2023-11-25)

This document provides examples of computing generalized Stirling numbers using different programming languages.

## Computing L{5,3}^{2,3}

We'll compute the generalized Stirling number L{5,3}^{2,3} with parameters α=2 and β=3.

### Python

```python
from generalized_stirling import GeneralizedStirling

gs = GeneralizedStirling(alpha=2.0, beta=3.0)
result = gs.compute(5, 3)
print(f"L{{5,3}}^{{2,3}} = {result}")
```

### JavaScript

```javascript
const { GeneralizedStirling } = require('./generalized_stirling');

const gs = new GeneralizedStirling(2.0, 3.0);
const result = gs.compute(5, 3);
console.log(`L{5,3}^{2,3} = ${result}`);
```

### PHP

```php
<?php
require_once 'GeneralizedStirling.php';

$gs = new GeneralizedStirling(2.0, 3.0);
$result = $gs->compute(5, 3);
echo "L{5,3}^{2,3} = $result\n";
?>
```

## Generating a Triangle

Generate a triangle of generalized Stirling numbers with parameters α=1 and β=1 (Lah numbers).

### Python

```python
from generalized_stirling import GeneralizedStirling

gs = GeneralizedStirling(alpha=1.0, beta=1.0)
triangle = gs.generate_triangle(6)

for n, row in enumerate(triangle, 1):
    print(f"{n}: {' '.join(row)}")
```

### JavaScript

```javascript
const { GeneralizedStirling } = require('./generalized_stirling');

const gs = new GeneralizedStirling(1.0, 1.0);
const triangle = gs.generateTriangle(6);

triangle.forEach((row, n) => {
    console.log(`${n+1}: ${row.join(' ')}`);
});
```

### PHP

```php
<?php
require_once 'GeneralizedStirling.php';

$gs = new GeneralizedStirling(1.0, 1.0);
$triangle = $gs->generateTriangle(6);

foreach ($triangle as $n => $row) {
    echo ($n + 1) . ": " . implode(' ', $row) . "\n";
}
?>
```

## Computing Classical Stirling Numbers

### Python

```python
from generalized_stirling import stirling_first_kind, stirling_second_kind, lah_number

# Stirling numbers of the first kind (unsigned)
for n in range(1, 6):
    row = [stirling_first_kind(n, k) for k in range(1, n+1)]
    print(f"s({n},k): {row}")

# Stirling numbers of the second kind
for n in range(1, 6):
    row = [stirling_second_kind(n, k) for k in range(1, n+1)]
    print(f"S({n},k): {row}")

# Lah numbers
for n in range(1, 6):
    row = [lah_number(n, k) for k in range(1, n+1)]
    print(f"L({n},k): {row}")
```

### JavaScript

```javascript
const { stirlingFirstKind, stirlingSecondKind, lahNumber } = require('./generalized_stirling');

// Stirling numbers of the first kind (unsigned)
for (let n = 1; n <= 5; n++) {
    const row = Array.from({length: n}, (_, k) => stirlingFirstKind(n, k+1));
    console.log(`s(${n},k): ${row}`);
}

// Stirling numbers of the second kind
for (let n = 1; n <= 5; n++) {
    const row = Array.from({length: n}, (_, k) => stirlingSecondKind(n, k+1));
    console.log(`S(${n},k): ${row}`);
}

// Lah numbers
for (let n = 1; n <= 5; n++) {
    const row = Array.from({length: n}, (_, k) => lahNumber(n, k+1));
    console.log(`L(${n},k): ${row}`);
}
```

### PHP

```php
<?php
require_once 'GeneralizedStirling.php';

// Stirling numbers of the first kind (unsigned)
for ($n = 1; $n <= 5; $n++) {
    $row = array_map(function($k) use ($n) {
        return stirling_first_kind($n, $k);
    }, range(1, $n));
    echo "s($n,k): " . implode(' ', $row) . "\n";
}

// Stirling numbers of the second kind
for ($n = 1; $n <= 5; $n++) {
    $row = array_map(function($k) use ($n) {
        return stirling_second_kind($n, $k);
    }, range(1, $n));
    echo "S($n,k): " . implode(' ', $row) . "\n";
}

// Lah numbers
for ($n = 1; $n <= 5; $n++) {
    $row = array_map(function($k) use ($n) {
        return lah_number($n, $k);
    }, range(1, $n));
    echo "L($n,k): " . implode(' ', $row) . "\n";
}
?>
```

## Benchmarking Different Methods

### Python

```python
import time
from generalized_stirling import GeneralizedStirling

def benchmark(n, k, alpha, beta):
    gs = GeneralizedStirling(alpha=alpha, beta=beta)
    
    # Triangular recurrence
    start = time.time()
    result1 = gs.compute(n, k, method='triangular')
    tri_time = time.time() - start
    
    # Explicit formula
    start = time.time()
    result2 = gs.compute(n, k, method='explicit')
    exp_time = time.time() - start
    
    # Special case (for k=1)
    if k == 1:
        start = time.time()
        result3 = gs.special_case(n, k)
        spec_time = time.time() - start
        print(f"Special case: {result3} (took {spec_time:.6f}s)")
    
    print(f"Triangular: {result1} (took {tri_time:.6f}s)")
    print(f"Explicit: {result2} (took {exp_time:.6f}s)")
    
    assert abs(result1 - result2) < 1e-10, "Results don't match!"

# Benchmark for different parameters
benchmark(15, 7, 1.5, 2.5)
```

## Expected Values for Verification

Here are some expected values for verification across language implementations:

| n | k | α | β | L{n,k}^{α,β} |
|---|---|---|---|--------------|
| 3 | 1 | 1.0 | 1.0 | 6 |
| 3 | 2 | 1.0 | 1.0 | 6 |
| 4 | 2 | 1.0 | 1.0 | 36 |
| 5 | 3 | 2.0 | 3.0 | 6220 |
| 6 | 3 | 1.5 | 2.5 | 17220 |
| 7 | 4 | 1.0 | 2.0 | 11760 |

## Common Patterns and Idioms

### Memoization

All implementations should use memoization for recursive methods to avoid redundant calculations.

### Parameter Validation

Validate parameters to avoid unnecessary computation:
- Check if k=0, n=0, k>n, or n=k
- For k=1, use the special case formula which is more efficient

### Floating-Point Precision

Be aware of floating-point precision when comparing results between languages. Consider using an epsilon value for comparisons:

```python
# Python
epsilon = 1e-10
assert abs(result1 - result2) < epsilon

# JavaScript
const epsilon = 1e-10;
assert(Math.abs(result1 - result2) < epsilon);

# PHP
$epsilon = 1e-10;
assert(abs($result1 - $result2) < $epsilon);
```

## Version History

- **0.2.0** (2023-11-25): Added performance optimizations and cross-language compatibility improvements
- **0.1.0** (2023-10-15): Initial implementation of generalized Stirling numbers

## Branch Structure

The project uses the following branch structure:

- `main`: Stable production code
- `develop`: Integration branch for new features
- `feature/[name]`: Individual feature branches (e.g., `feature/golang-implementation`)
- `release/v[version]`: Release preparation branches
- `hotfix/[name]`: Urgent fixes for production code

### Creating a New Feature Branch

```bash
# Ensure you're on the develop branch
git checkout develop
git pull origin develop

# Create a new feature branch
git checkout -b feature/your-feature-name

# Make your changes, then push to remote
git add .
git commit -m "Implement your feature"
git push -u origin feature/your-feature-name
```

### Preparing a Release

```bash
# Create a release branch from develop
git checkout develop
git checkout -b release/v0.3.0

# Make any final adjustments, version bumps, etc.
git add .
git commit -m "Bump version to 0.3.0"

# Merge to main and develop when ready
git checkout main
git merge --no-ff release/v0.3.0
git tag -a v0.3.0 -m "Version 0.3.0"
git push origin main --tags

git checkout develop
git merge --no-ff release/v0.3.0
git push origin develop

# Delete the release branch
git branch -d release/v0.3.0
```

## Implementation Checklist

When adding a new language implementation, ensure:

- [ ] Core generalized Stirling number calculation
- [ ] Special cases (first kind, second kind, Lah numbers)
- [ ] All recurrence relations
- [ ] Memoization for performance
- [ ] Comprehensive test suite
- [ ] Documentation and examples
- [ ] Cross-language validation tests
