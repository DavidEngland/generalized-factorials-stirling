# Hasse-Stirling Framework

A Python implementation of the Hasse-Stirling computational framework for efficient calculation of special functions.

## Features

- Generalized Hasse operator with parameterization
- Generalized Stirling numbers computation
- Applications to:
  - Stieltjes constants
  - Zeta values (odd and multiple)
  - Roots of special functions (digamma, etc.)
  - Hypergeometric functions
  - Bessel function zeros
  - Lambert W function

## Usage

Basic usage:

```python
from hasse_stirling import hasse_operator, generalized_stirling

# Compute generalized Stirling numbers
s = generalized_stirling(10, 4, alpha=1, beta=0)  # Stirling number of first kind

# Apply the Hasse operator
result = hasse_operator(lambda x: x**3, 1.0, alpha=0, beta=1)  # Returns B₃(1)/3!
```

See examples directory for advanced applications.

## Installation

## When to Use Hasse-Stirling

The Hasse-Stirling framework is a numerical method that offers significant advantages for certain classes of problems:
- Efficient and stable computation of special functions (e.g., Stieltjes constants, odd zeta values, hypergeometric and Bessel functions)
- Accelerated convergence for series with optimal parameter choices
- Useful for high-precision or large-parameter regimes where traditional methods struggle

However, for other problems, especially those with well-established direct algorithms or small parameter values, traditional methods may be faster or simpler. Always benchmark both approaches for your specific application.

## References

See the main project documentation and `/docs/arXiv-1411.6271v1/GSN.bbl` for relevant literature.

