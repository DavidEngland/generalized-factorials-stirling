# Generalized Stirling Numbers

A cross-language implementation of generalized Stirling numbers based on the combinatorial approach developed by Belbachir, Belkhir, and Bousbaa.

## Overview

This library provides implementations of generalized Stirling numbers $L_{n,k}^{\alpha,\beta}$ in multiple programming languages. These numbers unify and generalize classical Stirling numbers of both kinds and Lah numbers, providing a flexible framework for combinatorial problems.

## Mathematical Background

The generalized Stirling numbers $L_{n,k}^{\alpha,\beta}$ represent the total weight of distributing $n$ elements into $k$ ordered non-empty lists, where:

1. The first element placed in each list has weight 1
2. Elements placed at the head of a list have weight $\beta$
3. Other elements in the lists have weight $\alpha$

### Special Cases

- $(\alpha,\beta) = (1,0)$: Unsigned Stirling numbers of the first kind
- $(\alpha,\beta) = (0,1)$: Stirling numbers of the second kind
- $(\alpha,\beta) = (1,1)$: Lah numbers

### Key Properties

- Triangular recurrence: $L_{n,k}^{\alpha,\beta} = L_{n-1,k-1}^{\alpha,\beta} + (\alpha(n-1) + \beta k)L_{n-1,k}^{\alpha,\beta}$
- Special case: $L_{n,1}^{\alpha,\beta} = \prod_{j=1}^{n-1}(j\alpha + \beta)$
- Explicit formula: $L_{n,k}^{\alpha,\beta} = \frac{1}{\beta^k k!}\sum_{j=0}^{k}(-1)^j \binom{k}{j}(\beta(k-j)|\alpha)^{\overline{n}}$

## Notation

You may also see the generalized Stirling numbers written as $S_{n,k}(a,b)$ instead of $L_{n,k}^{\alpha,\beta}$, where $a$ and $b$ play the roles of $\alpha$ and $\beta$. This notation is common in combinatorics and computer science literature.

- $S_{n,k}(a,b)$: Equivalent to $L_{n,k}^{\alpha,\beta}$, with $a = \alpha$ and $b = \beta$.
- $a$ (affinity) and $b$ (cost) are used for practical interpretation and parameter estimation.

## Alternative Recurrence

The recurrence relation can also be written by looking at the $(n+1)$-th point:
$$
S_{n+1,k}(a,b) = S_{n,k-1}(a,b) + (a n + b k) S_{n,k}(a,b)
$$
This form emphasizes how adding a new element ($n+1$) affects the distribution into $k$ groups, and is often more intuitive for algorithmic implementations.

## Interpreting Parameters $(\alpha, \beta)$: Affinity, Cost, and Clustering

The parameters $(\alpha, \beta)$ in generalized Stirling numbers have practical interpretations:

- **Affinity ($\alpha$):** Measures how strongly elements prefer to stay together in the same group. High affinity means elements naturally cluster, like friends forming tight-knit communities or products frequently bought together.
- **Cost ($\beta$):** Represents the barrier or overhead to starting a new group. High cost means it's harder to create new clusters, like the expense of launching a new delivery route or the effort to form a new team.

### Real-World Examples

- **Healthcare:** Patients with similar conditions (high affinity) are grouped for specialized care, while forming new care units (high cost) requires resources.
- **Education:** Students with similar learning styles cluster in classes (affinity), but opening new classes or programs (cost) depends on funding and demand.
- **Logistics:** Packages destined for the same area are grouped for delivery (affinity); starting a new route (cost) involves fuel, time, and planning.
- **Social Networks:** Users with shared interests form communities (affinity); creating new groups (cost) requires motivation and critical mass.

By tuning $(\alpha, \beta)$, you can model, predict, and optimize clustering in systems to improve outcomes—reducing isolation, increasing efficiency, and supporting better resource allocation.

## Implementations

### Python

```python
from generalized_stirling import GeneralizedStirling

# Create instance with α=2, β=3
gs = GeneralizedStirling(alpha=2.0, beta=3.0)

# Compute L{5,3}^{2,3}
result = gs.compute(5, 3)
print(f"L{{5,3}}^{{2,3}} = {result}")

# For classical cases
from generalized_stirling import stirling_first_kind, stirling_second_kind, lah_number

s1 = stirling_first_kind(5, 3)  # Stirling numbers of first kind
s2 = stirling_second_kind(5, 3)  # Stirling numbers of second kind
l = lah_number(5, 3)  # Lah numbers
```

### JavaScript (Implementation template)

```javascript
class GeneralizedStirling {
  constructor(alpha = 1.0, beta = 1.0) {
    this.alpha = alpha;
    this.beta = beta;
  }
  
  // Compute generalized Stirling number using triangular recurrence
  compute(n, k) {
    // Base cases
    if (k === 0) return n === 0 ? 1.0 : 0.0;
    if (n === 0 || k > n) return 0.0;
    if (k === n) return 1.0;
    
    // Recurrence relation
    const term1 = this.compute(n-1, k-1);
    const term2 = (this.alpha * (n-1) + this.beta * k) * this.compute(n-1, k);
    
    return term1 + term2;
  }
  
  // Additional methods...
}

// Helper functions for specific cases
function stirlingFirstKind(n, k) {
  const gs = new GeneralizedStirling(1.0, 0.0);
  return gs.compute(n, k);
}

function stirlingSecondKind(n, k) {
  const gs = new GeneralizedStirling(0.0, 1.0);
  return gs.compute(n, k);
}

function lahNumber(n, k) {
  const gs = new GeneralizedStirling(1.0, 1.0);
  return gs.compute(n, k);
}
```

### PHP (Implementation template)

```php
class GeneralizedStirling {
    private $alpha;
    private $beta;
    private $cache = [];
    
    public function __construct($alpha = 1.0, $beta = 1.0) {
        $this->alpha = $alpha;
        $this->beta = $beta;
    }
    
    public function compute($n, $k) {
        // Check cache
        $key = "{$n}:{$k}";
        if (isset($this->cache[$key])) {
            return $this->cache[$key];
        }
        
        // Base cases
        if ($k === 0) {
            return $n === 0 ? 1.0 : 0.0;
        }
        if ($n === 0 || $k > $n) {
            return 0.0;
        }
        if ($k === $n) {
            return 1.0;
        }
        
        // Recurrence relation
        $term1 = $this->compute($n-1, $k-1);
        $term2 = ($this->alpha * ($n-1) + $this->beta * $k) * $this->compute($n-1, $k);
        
        $result = $term1 + $term2;
        $this->cache[$key] = $result;
        
        return $result;
    }
    
    // Additional methods...
}

function stirling_first_kind($n, $k) {
    $gs = new GeneralizedStirling(1.0, 0.0);
    return $gs.compute($n, $k);
}

function stirling_second_kind($n, $k) {
    $gs = new GeneralizedStirling(0.0, 1.0);
    return $gs.compute($n, $k);
}

function lah_number($n, $k) {
    $gs = new GeneralizedStirling(1.0, 1.0);
    return $gs.compute($n, $k);
}
```

## Project Structure

```
generalized-stirling/
├── docs/
│   ├── algorithms.md            # Detailed algorithm explanations
│   ├── math_background.md       # Mathematical theory
│   └── language_specific/       # Language-specific documentation
├── src/                         # Python implementation
│   ├── __init__.py              # Package initialization
│   └── generalized_stirling.py  # Core implementation
├── tests/                       # Test cases
│   └── test_generalized_stirling.py
├── implementations/             # Implementations in other languages
│   ├── javascript/
│   │   └── generalized_stirling.js
│   └── php/
│       └── GeneralizedStirling.php
├── examples/                    # Example usage in different languages
├── README.md                    # Project documentation
└── setup.py                     # Python package configuration
```

## Getting Started

### Python Installation

```bash
# Install from PyPI (once published)
pip install generalized-stirling

# Or install from source
git clone https://github.com/yourusername/generalized-stirling.git
cd generalized-stirling
pip install -e .
```

### Running Tests

```bash
python -m unittest discover tests
```

## References

1. H. Belbachir, A. Belkhir, I.E. Bousbaa. "Combinatorial approach of certain generalized Stirling numbers." arXiv:1411.6271v1, 2014.
2. L.C. Hsu, P.J.-S. Shiue. "A unified approach to generalized Stirling numbers." Adv. in Appl. Math., 20(3):366-384, 1998.
3. A.Z. Broder. "The r-Stirling numbers." Discrete Math., 49(3):241-259, 1984.

## License

MIT License
