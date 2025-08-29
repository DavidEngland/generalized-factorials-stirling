# Generalized Factorials and Stirling Numbers

This repository explores generalized factorial polynomials and Stirling numbers with applications to clustering and classification.

## Core Components

- **Generalized Stirling Numbers**: A unified framework for various combinatorial sequences
- **Bell Polynomial Integration**: Mathematical rigor through Bell polynomial transformations
- **Parameter Estimation**: Methods to derive parameters from data
- **Applications**: Practical uses in clustering, supply chain, and network optimization

## Examples

1. **Simple Retail Demo**: Product clustering using Bell-enhanced Stirling partitioning
2. **Supply Chain Delivery**: Route optimization with higher-order Bell polynomial corrections
3. **Data Packet Network**: Server allocation with multivariate Bell polynomials
4. **Urban Planning**: Community design using generalized Stirling parameters

## Key Mathematical Concepts

- **Generalized Stirling Numbers**: $S_{n,k}(a,b)$ with parameters $(a,b)$ controlling affinity and barrier
- **Bell Polynomials**: Used for exact transformation between function coefficients
- **Parameter Estimation**: Advanced methods leveraging Bell polynomials for higher-order corrections

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/generalized-factorials-stirling.git
cd generalized-factorials-stirling

# Install dependencies
pip install numpy pandas matplotlib scikit-learn sympy
```

## Library Usage

The repository now includes a comprehensive library (`src/`) with:

- Core mathematical functions for generalized Stirling numbers
- Bell polynomial implementations for higher-order corrections
- Application-specific algorithms for clustering and partitioning

```python
from src.stirling_core import StirlingComputation, BellPolynomials
from src.stirling_applications import StirlingPartitioning

# Create a Bell-enhanced partitioning algorithm
partitioner = StirlingPartitioning(use_bell_polynomials=True)
results = partitioner.fit(data)
```

## Documentation

- See the `docs/` folder for mathematical background
- Each example folder contains detailed documentation
- The core library is documented with docstrings

## Recent Enhancements

- **Bell Polynomial Integration**: All examples now use Bell polynomials for higher accuracy
- **Higher-Order Corrections**: Capturing non-linear effects in parameter estimation
- **Multivariate Extensions**: Handling complex multidimensional feature spaces
- **Core Library**: Unified implementation of algorithms across examples
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
