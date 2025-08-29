# Generalized Factorials and Stirling Numbers

This repository explores generalized factorial polynomials and Stirling numbers with applications to clustering and classification.

## Core Components

- **Generalized Stirling Framework**: A unified approach to combinatorial sequence analysis
- **Polynomial Moment Analysis**: Mathematical precision through Bell polynomial transformations
- **Coefficient Estimation**: Methods to extract structural parameters from data
- **Applied Partition Analytics**: Practical applications across multiple domains

## Examples

1. **Product Affinity Analysis**: Retail clustering using combinatorial moment estimation
2. **Delivery Route Optimization**: Supply chain planning with non-linear parameter refinements
3. **Network Resource Allocation**: Server distribution with multivariate moment analysis
4. **Community Structure Identification**: Urban planning through partition-based modeling

## Key Mathematical Concepts

- **Generalized Stirling Numbers**: $S_{n,k}(a,b)$ with parameters $(a,b)$ controlling cohesion and separation
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
- Polynomial moment analysis for precise parameter estimation
- Domain-specific algorithms for partitioning and structure identification

```python
from src.stirling_core import StirlingComputation, BellPolynomials
from src.stirling_applications import PartitionAnalyzer

# Create a moment-enhanced partition analyzer
analyzer = PartitionAnalyzer(use_moment_refinement=True)
structure = analyzer.identify_partitions(data)
```

## Documentation

- See the `docs/` folder for mathematical foundations
- Each example domain contains detailed methodology documentation
- The core library includes comprehensive docstrings and examples

## Recent Enhancements

- **Polynomial Moment Analysis**: All examples now use Bell polynomials for precise parameter estimation
- **Non-Linear Scaling Refinements**: Capturing higher-order structural patterns in partition identification
- **Multivariate Coefficient Estimation**: Handling complex feature interactions in multidimensional spaces
- **Unified Partition Analytics**: Consistent methodology across application domains
