# Generalized Factorials and Stirling Numbers

This repository explores generalized factorial polynomials, Stirling numbers, and the Hasse-Stirling Framework with applications across mathematics, computer science, and data analysis.

## Core Components

- **Generalized Stirling Framework**: A unified approach to combinatorial sequence analysis
- **Hasse-Stirling Framework**: Powerful computational approach to special functions using generalized Stirling numbers
- **Polynomial Moment Analysis**: Mathematical precision through Bell polynomial transformations
- **Coefficient Estimation**: Methods to extract structural parameters from data
- **Applied Partition Analytics**: Practical applications across multiple domains

## Examples

1. **Product Affinity Analysis**: Retail clustering using combinatorial moment estimation
2. **Delivery Route Optimization**: Supply chain planning with non-linear parameter refinements
3. **Network Resource Allocation**: Server distribution with multivariate moment analysis
4. **Community Structure Identification**: Urban planning through partition-based modeling
5. **Computational Finance**: Option pricing using Hasse-Stirling methods for hypergeometric functions
6. **Quantum Circuit Simulation**: Improved amplitude calculations using Hasse-Stirling optimized special functions

## Key Mathematical Concepts

- **Generalized Stirling Numbers**: $S(n,k;\alpha,\beta,r)$ with parameters controlling cohesion and separation
- **Hasse Operator**: $\mathcal{H}_{\alpha,\beta,r}\{f(t)\}(x) = \sum_{m=0}^{\infty} \sum_{n=0}^{m} H_{m,n}^{\alpha,\beta,r} f(x+n)$ as a powerful computational tool
- **Parameter Domains**: Key parameter triplets $(\alpha,\beta,r)$ such as Euler $(0,1,0)$, Digamma $(1,-1,0)$, and Stieltjes $(\frac{k+3}{2},-\frac{k+4}{2},0)$ domains
- **Factorial Polynomials**: Generalized rising/falling factorials with uniformly-spaced roots
- **Bell Polynomial Transformations**: Exact calculation of composite function coefficients
- **Moment-Based Parameter Estimation**: Advanced methods for capturing non-linear structural patterns

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/generalized-factorials-stirling.git
cd generalized-factorials-stirling

# Install dependencies
pip install numpy pandas matplotlib scikit-learn sympy
```

## Library Usage

The repository includes a comprehensive analytics framework (`src/`) with:

- Core mathematical functions for generalized combinatorial structures
- Hasse-Stirling computational methods for special functions and series acceleration
- Polynomial moment analysis for precise parameter estimation
- Domain-specific algorithms for partitioning and structure identification

```python
from src.stirling_core import StirlingComputation, BellPolynomials
from src.hasse_stirling import compute_hasse_coefficients, hasse_operator_action
from src.stirling_applications import PartitionAnalyzer

# Create a moment-enhanced partition analyzer
analyzer = PartitionAnalyzer(use_moment_refinement=True)
structure = analyzer.identify_partitions(data)

# Use Hasse-Stirling for computational special functions
# Calculate the Digamma function at x using the Hasse operator
result = -EULER_GAMMA + hasse_operator_action(lambda t: np.log(t), 1, 30, 1, -1, 0, x-1)
```

## Documentation

- See the `docs/` folder for mathematical foundations
- The `hasse-stirling/` directory contains cheatsheets and parameter interpretations
- The `computational/` folder includes application examples and performance analysis
- Each example domain contains detailed methodology documentation
- The core library includes comprehensive docstrings and examples

## Recent Enhancements

- **Hasse-Stirling Framework**: Unified computational approach to special functions using parameterized operators
- **Improved Notation**: Standardized notation $\mathcal{H}_{\alpha,\beta,r}\{f(t)\}(x)$ for clarity and consistency
- **Root Finding Applications**: Enhanced asymptotic expansions for special function roots
- **Logarithmic Derivatives**: Efficient computation using the Hasse-Stirling approach
- **Polynomial Moment Analysis**: All examples now use Bell polynomials for precise parameter estimation
- **Financial Applications**: Option pricing models using Hasse-Stirling optimized hypergeometric functions
- **Quantum Applications**: Improved computational methods for quantum circuit simulation
