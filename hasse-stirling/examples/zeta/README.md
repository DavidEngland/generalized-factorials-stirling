# Hasse-Stirling Framework Examples

This directory contains examples demonstrating practical applications of the Hasse-Stirling framework for computational mathematics.

## Available Examples

### Riemann Zeta Function Zeros (`riemann_zeros.py`)

This example demonstrates how to use the Hasse-Stirling framework to efficiently compute the non-trivial zeros of the Riemann zeta function. Key features:

- Constructs a specialized `g(t)` function for the Hasse operator representation
- Develops an asymptotic expansion for the n-th zero
- Compares performance with traditional methods
- Discusses the assumptions and limitations of the approach

The implementation assumes the Riemann Hypothesis (all non-trivial zeros have real part 1/2) for simplicity, but the approach could be adapted for the general case.

**When to use this approach:**
- When computing very high zeros (n > 1000)
- When seeking high-precision approximations
- For theoretical studies of zero distribution

**When not to use this approach:**
- For low zeros where traditional methods are already efficient
- In time-critical applications requiring minimal setup
- When working with limited numerical precision

### Running the Examples

To run an example:

```bash
# From the hasse-stirling directory
python examples/riemann_zeros.py
```

Each example includes performance benchmarks and visualizations to help understand the advantages of the Hasse-Stirling approach.
