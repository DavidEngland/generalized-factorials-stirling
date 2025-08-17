# Falling Factorial Polynomials: Essential Background

## Definition and Basic Properties

### Primary Definition

The **falling factorial polynomial** $P(z,-1,m)$ is defined as:

$$P(z,-1,m) = z(z-1)(z-2)\cdots(z-m+1)$$

This represents the product of $m$ consecutive descending integers starting from $z$.

### Alternative Notations

In the literature, falling factorials appear under various notations:
- $z^{\underline{m}}$ (Knuth's underline notation)
- $(z)_m$ (combinatorics convention)
- $z^{[m]}$ (alternative bracket notation)

### Connection to Generalized Factorial Polynomials

The falling factorial is a special case of the generalized factorial polynomial $P(x,a,m)$ with increment parameter $a = -1$:

$$P(z,-1,m) = z(z+(-1))(z+2(-1))\cdots(z+(m-1)(-1))$$

## Fundamental Properties

### Initial and Boundary Conditions

- $P(z,-1,0) = 1$ (empty product convention)
- $P(0,-1,m) = 0$ for $m > 0$
- $P(z,-1,1) = z$

### Recurrence Relations

**Forward Recurrence:**
$$P(z,-1,m+1) = P(z,-1,m) \cdot (z-m)$$

**Backward Recurrence:**
$$P(z,-1,m) = \frac{P(z,-1,m+1)}{z-m}$$

### Connection to Binomial Coefficients

For non-negative integer $z = n$:
$$P(n,-1,m) = \frac{n!}{(n-m)!} = m! \binom{n}{m}$$

This gives the fundamental identity:
$$\binom{z}{k} = \frac{P(z,-1,k)}{k!}$$

## Gamma Function Representation

For general complex arguments:
$$P(z,-1,m) = (-1)^m \frac{\Gamma(m-z)}{\Gamma(-z)}$$

This provides analytic continuation to non-integer values of $z$ and $m$.

### Alternative Gamma Form

Using the reflection formula:
$$P(z,-1,m) = \frac{\Gamma(z+1)}{\Gamma(z-m+1)}$$

This form is often more convenient for computation.

## Derivatives and Special Function Connections

### First Derivative

$$\frac{d}{dz} P(z,-1,m) = P(z,-1,m) \sum_{k=0}^{m-1} \frac{1}{z-k}$$

This reveals the discrete harmonic structure underlying falling factorial derivatives.

### Connection to Digamma Function

$$\frac{d}{dz} \ln P(z,-1,m) = \psi(z+1) - \psi(z-m+1)$$

where $\psi(x) = \frac{\Gamma'(x)}{\Gamma(x)}$ is the digamma function.

## Generating Functions

### Exponential Generating Function

$$\sum_{m=0}^{\infty} P(z,-1,m) \frac{t^m}{m!} = (1+t)^z$$

This is the fundamental binomial series expansion.

### Ordinary Generating Function

$$\sum_{m=0}^{\infty} P(z,-1,m) t^m = (1-t)^{-z-1} \cdot \frac{1-t}{1-t} = (1-t)^{-z}$$

Wait, this needs correction. The correct OGF is more complex due to the polynomial structure.

### Corrected Ordinary Generating Function

For the falling factorial, the ordinary generating function is:
$$\sum_{m=0}^{\infty} P(z,-1,m) t^m = \frac{1}{(1-t)^{z+1}}$$

when $|t| < 1$ and $\text{Re}(z) > -1$.

## Connection to Stirling Numbers

### Expansion in Monomial Basis

$$P(z,-1,m) = \sum_{k=0}^{m} (-1)^{m-k} \left[\begin{array}{c}m\\k\end{array}\right] z^k$$

where $\left[\begin{array}{c}m\\k\end{array}\right]$ are unsigned Stirling numbers of the first kind.

### Inverse Expansion

$$z^m = \sum_{k=0}^{m} \left\{\begin{array}{c}m\\k\end{array}\right\} P(z,-1,k)$$

where $\left\{\begin{array}{c}m\\k\end{array}\right\}$ are Stirling numbers of the second kind.

## Applications in OGF Power Expansion

### Role in the Main Theorem

In the expansion $[f(x)]^z = \sum_{m=0}^{\infty} c_m(z) x^m$, falling factorials appear through the binomial coefficient identity:

$$\binom{z}{k} = \frac{P(z,-1,k)}{k!}$$

This connects the multinomial expansion of $[f(x)]^z$ to falling factorial polynomials.

### Computational Advantages

1. **Finite representation:** Each $P(z,-1,k)$ is a finite product
2. **Stable computation:** For moderate values, direct multiplication is efficient
3. **Gamma function methods:** For large parameters or non-integer arguments
4. **Recurrence relations:** Enable efficient sequential computation

## Asymptotic Properties

### Large Parameter Behavior

For fixed $z$ and large $m$:
$$P(z,-1,m) \sim (-1)^m \frac{\Gamma(m)}{\Gamma(-z)} \sim (-1)^m \frac{m^{-z-1}}{\Gamma(-z)}$$

### Large Argument Asymptotics

For fixed $m$ and large $|z|$:
$$P(z,-1,m) \sim z^m \left(1 + O\left(\frac{1}{z}\right)\right)$$

## Special Values and Identities

### Integer Values

For positive integer $n$:
- $P(n,-1,n) = n!$
- $P(n,-1,n+1) = 0$
- $P(n,-1,k) = \frac{n!}{(n-k)!}$ for $k \leq n$

### Symmetry Relations

$$P(z,-1,m) = (-1)^m P(-z-1,1,m)$$

This connects falling and rising factorials.

### Reflection Formula

$$P(z,-1,m) \cdot P(-z+m-1,-1,m) = (-1)^m m! \frac{\sin(\pi z)}{\sin(\pi(z-m))} \frac{\pi}{\pi}$$

This is a special case of the gamma function reflection formula.

## Computational Implementation

### Direct Evaluation

```python
def falling_factorial(z, m):
    """Compute P(z,-1,m) = z(z-1)...(z-m+1)"""
    if m == 0:
        return 1
    result = 1
    for k in range(m):
        result *= (z - k)
    return result
```

### Logarithmic Computation

For large parameters or to avoid overflow:
```python
def log_falling_factorial(z, m):
    """Compute log|P(z,-1,m)|"""
    if m == 0:
        return 0
    return sum(math.log(abs(z - k)) for k in range(m))
```

### Gamma Function Method

Using the gamma function representation:
```python
def falling_factorial_gamma(z, m):
    """Compute P(z,-1,m) using gamma functions"""
    return math.gamma(z + 1) / math.gamma(z - m + 1)
```

## Summary

Falling factorial polynomials $P(z,-1,m)$ serve as the algebraic backbone of the OGF power expansion framework. Their properties—finite representation, gamma function connections, generating functions, and Stirling number relationships—make them ideal for:

1. **Coefficient extraction** from generating function powers
2. **Combinatorial enumeration** through partition structures  
3. **Special function theory** via analytic continuation
4. **Computational implementation** with multiple algorithmic approaches

Understanding falling factorials is essential for working with the Bell polynomial expansion of OGF powers and their applications across mathematics and physics.
