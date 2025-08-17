# Generalized Factorial Polynomials & Stirling Coefficients - Quick Reference

## Basic Definitions

**Generalized Factorial Polynomial:**
$$P(x,a,m) = x(x+a)(x+2a)\cdots(x+(m-1)a)$$

**Generalized Stirling Transfer Coefficients:**
$$P(x,a,m) = \sum_{n=0}^{m} S_{m,n}(a,b) \cdot P(x,b,n)$$

**Special Cases:**
- $P(x,0,m) = x^m$ (monomials)
- $P(x,1,m) = x(x+1)\cdots(x+m-1)$ (rising factorial)
- $P(x,-1,m) = x(x-1)\cdots(x-m+1)$ (falling factorial)

## General Formula (Main Result)

$$\boxed{S_{m,n}(a,b) = \sum_{k=n}^{m} a^{m-k} b^{k-n} (-1)^{k-n} \left\{\begin{array}{c}m\\k\end{array}\right\} \left[\begin{array}{c}k\\n\end{array}\right]}$$

**Algorithm:**
```
S(m,n,a,b) = 0
for k = n to m:
    term = a^(m-k) * b^(k-n) * (-1)^(k-n)
    term *= Stirling2nd(m,k) * UnsignedStirling1st(k,n)
    S(m,n,a,b) += term
```

## Classical Stirling Numbers

### Recovery from General Formula

| Type | Parameters | Formula |
|------|------------|---------|
| **2nd Kind** | $S_{m,n}(1,0)$ | $\left\{\begin{array}{c}m\\n\end{array}\right\}$ |
| **1st Kind (Signed)** | $S_{m,n}(0,1)$ | $s(m,n) = (-1)^{m-n}\left[\begin{array}{c}m\\n\end{array}\right]$ |
| **1st Kind (Unsigned)** | $S_{m,n}(0,-1)$ | $\left[\begin{array}{c}m\\n\end{array}\right]$ |
| **Lah Numbers** | $S_{m,n}(1,-1)$ | $L(m,n)$ |

### Stirling Number Tables

**Second Kind** $\left\{\begin{array}{c}m\\n\end{array}\right\}$
| $m \setminus n$ | **1** | **2** | **3** | **4** | **5** |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | 1 | 0 | 0 | 0 | 0 |
| **2** | 1 | 1 | 0 | 0 | 0 |
| **3** | 1 | 3 | 1 | 0 | 0 |
| **4** | 1 | 7 | 6 | 1 | 0 |
| **5** | 1 | 15 | 25 | 10 | 1 |

**Unsigned First Kind** $\left[\begin{array}{c}m\\n\end{array}\right]$
| $m \setminus n$ | **1** | **2** | **3** | **4** | **5** |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | 1 | 0 | 0 | 0 | 0 |
| **2** | 1 | 1 | 0 | 0 | 0 |
| **3** | 2 | 3 | 1 | 0 | 0 |
| **4** | 6 | 11 | 6 | 1 | 0 |
| **5** | 24 | 50 | 35 | 10 | 1 |

## Key Properties

**Identity:** $S_{m,n}(a,a) = [m=n]$ (Kronecker delta)

**Triangular:** $S_{m,n}(a,b) = 0$ for $n > m$

**Matrix Inverse:** $\sum_{k=0}^{m} S_{m,k}(a,b) \cdot S_{k,n}(b,a) = [m=n]$

**Scaling:** $S_{m,n}(ca,cb) = c^{m-n} S_{m,n}(a,b)$ for $c \neq 0$

**Infinite Matrices:** Transformation matrices are infinite-dimensional but mathematically valid by induction. For computations up to degree $N$, only finite $(N+1) \times (N+1)$ submatrices are needed.

## Recurrence Relations

**Universal Recurrence:**
$$S_{m+1,n}(a,b) = S_{m,n-1}(a,b) + (ma - nb) S_{m,n}(a,b)$$

**Classical Cases:**
- **2nd Kind:** $\left\{\begin{array}{c}m+1\\n\end{array}\right\} = n \left\{\begin{array}{c}m\\n\end{array}\right\} + \left\{\begin{array}{c}m\\n-1\end{array}\right\}$
- **1st Kind:** $\left[\begin{array}{c}m+1\\n\end{array}\right] = m \left[\begin{array}{c}m\\n\end{array}\right] + \left[\begin{array}{c}m\\n-1\end{array}\right]$

**Polynomial Recurrence:** $P(x,a,m+1) = P(x,a,m) \cdot (x + ma)$

## Scaling Formulas

**To Monomials:**
$$S_{m,n}(a,0) = a^{m-n} \left\{\begin{array}{c}m\\n\end{array}\right\}$$

**From Monomials:**
$$S_{m,n}(0,b) = b^{k-n} (-1)^{m-n} \left[\begin{array}{c}m\\n\end{array}\right]$$

**Symmetric Cases:**
$$S_{m,n}(0,-b) = (-1)^{m-n} b^{k-n} \left[\begin{array}{c}m\\n\end{array}\right]$$

## Computational Notes

**Complexity:** $O(m-n+1)$ terms in general formula

**Numerical Stability:** 
- Use exact arithmetic for small parameters
- Monitor for overflow with large $a^{m-k}$ or $b^{k-n}$ terms
- Logarithmic computation for extreme values

**Precomputation:** Build Stirling number tables up to desired size

**Special Case Optimization:**
- $a=0$ or $b=0$: Use scaling formulas directly
- $a=b$: Return Kronecker delta $[m=n]$
- Small $m$: Use recurrence relation

## Generating Functions (Summary)

**Ordinary:** $\sum_{m=0}^{\infty} P(x,a,m) z^m = (1-az)^{-x/a}$ (if $a \neq 0$)

**Exponential:** $\sum_{m=0}^{\infty} P(x,a,m) \frac{z^m}{m!} = (1+az)^{x/a}$ (if $a \neq 0$)

**Monomial Cases:** Replace with $\frac{1}{1-xz}$ and $e^{xz}$ respectively when $a=0$

## Quick Verification

**Test Case:** $P(x,2,2) = x(x+2) = x^2 + 2x$

Transform to monomial basis $(b=0)$:
$$S_{2,0}(2,0) = 2^{2-0} \left\{\begin{array}{c}2\\0\end{array}\right\} = 4 \cdot 0 = 0$$
$$S_{2,1}(2,0) = 2^{2-1} \left\{\begin{array}{c}2\\1\end{array}\right\} = 2 \cdot 1 = 2$$
$$S_{2,2}(2,0) = 2^{2-2} \left\{\begin{array}{c}2\\2\end{array}\right\} = 1 \cdot 1 = 1$$

Result: $P(x,2,2) = 0 \cdot 1 + 2 \cdot x + 1 \cdot x^2 = x^2 + 2x$ ✓

## Common Applications

- **Hypergeometric series:** Basis transformations in special functions
- **Finite differences:** Converting between difference operators
- **Interpolation:** Generalized Newton formulas
- **Combinatorics:** Weighted counting problems
- **Computer algebra:** Automatic polynomial basis conversion
