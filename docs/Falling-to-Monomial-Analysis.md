# Falling Factorial to Monomial Transformations: $S_{m,n}(0,-b)$ and $S_{m,n}(-b,0)$

## Overview

This document analyzes the transformation from falling factorials to monomials via the generalized Stirling transfer coefficients $S_{m,n}(0,-b)$ and their inverses $S_{m,n}(-b,0)$. We explore scaling relationships, combinatorial interpretations involving coloring and inclusion-exclusion principles, and the role of alternating signs.

## Basic Transformation: $S_{m,n}(0,-1)$

The fundamental case transforms monomials to falling factorials:

$$x^m = \sum_{n=0}^{m} S_{m,n}(0,-1) \cdot x(x-1)(x-2)\cdots(x-n+1)$$

where $S_{m,n}(0,-1) = \left[\begin{array}{c}m\\n\end{array}\right]$ are the **unsigned Stirling numbers of the first kind**.

### Classical Table: $\left[\begin{array}{c}m\\n\end{array}\right] = S_{m,n}(0,-1)$

| $m \setminus n$ | **0** | **1** | **2** | **3** | **4** | **5** |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **0** | 1 | 0 | 0 | 0 | 0 | 0 |
| **1** | 0 | 1 | 0 | 0 | 0 | 0 |
| **2** | 0 | 1 | 1 | 0 | 0 | 0 |
| **3** | 0 | 2 | 3 | 1 | 0 | 0 |
| **4** | 0 | 6 | 11 | 6 | 1 | 0 |
| **5** | 0 | 24 | 50 | 35 | 10 | 1 |

**Combinatorial meaning:** $\left[\begin{array}{c}m\\n\end{array}\right]$ counts permutations of $m$ objects with exactly $n$ cycles.

## Scaled Version: $S_{m,n}(0,-b)$

For general parameter $b > 0$, the scaling relationship is:

$$S_{m,n}(0,-b) = \left(\frac{-1}{b}\right)^n \left[\begin{array}{c}m\\n\end{array}\right]$$

### Derivation of Scaling Formula

Starting from the definition:
$$P(x,0,m) = \sum_{n=0}^{m} S_{m,n}(0,-b) \cdot P(x,-b,n)$$

We have:
- $P(x,0,m) = x^m$ (monomial)
- $P(x,-b,n) = x(x-b)(x-2b)\cdots(x-(n-1)b)$ (falling factorial with increment $-b$)

The scaling relationship $P(x,-b,n) = (-b)^n P(x/(-b), 1, n) = (-b)^n P(-x/b, 1, n)$ gives:

$$P(x,-b,n) = (-b)^n \cdot (-x/b)((-x/b)+1)\cdots((-x/b)+n-1)$$

This leads to the scaling formula with the alternating sign factor $(-1)^n$.

### Matrix for $S_{m,n}(0,-b)$

$$\mathbf{S}(0,-b) = \begin{pmatrix}
1 & 0 & 0 & 0 & 0 \\
0 & -\frac{1}{b} & 0 & 0 & 0 \\
0 & \frac{2}{b} & \left(\frac{1}{b}\right)^2 & 0 & 0 \\
0 & -\frac{6}{b} & -\frac{3}{\left(\frac{1}{b}\right)^2} & -\left(\frac{1}{b}\right)^3 & 0 \\
0 & \frac{24}{b} & \frac{11}{\left(\frac{1}{b}\right)^2} & \frac{6}{\left(\frac{1}{b}\right)^3} & \left(\frac{1}{b}\right)^4 \\
\end{pmatrix}$$

**Pattern:** Entry $(m,n)$ is $\left(\frac{-1}{b}\right)^n \left[\begin{array}{c}m\\n\end{array}\right]$.

## Inverse Transformation: $S_{m,n}(-b,0)$

The inverse transformation from falling factorials (with increment $-b$) to monomials:

$$P(x,-b,m) = \sum_{n=0}^{m} S_{m,n}(-b,0) \cdot x^n$$

### Scaling Formula for Inverse

$$S_{m,n}(-b,0) = (-b)^{m-n} \left\{\begin{array}{c}m\\n\end{array}\right\}$$

where $\left\{\begin{array}{c}m\\n\end{array}\right\}$ are Stirling numbers of the second kind.

### Matrix for $S_{m,n}(-b,0)$

$$\mathbf{S}(-b,0) = \begin{pmatrix}
1 & 0 & 0 & 0 & 0 \\
-b & 1 & 0 & 0 & 0 \\
b^2 & -3b & 1 & 0 & 0 \\
-b^3 & 7b^2 & -6b & 1 & 0 \\
b^4 & -15b^3 & 25b^2 & -10b & 1 \\
\end{pmatrix}$$

**Pattern:** Entry $(m,n)$ is $(-b)^{m-n} \left\{\begin{array}{c}m\\n\end{array}\right\} = (-1)^{m-n} b^{m-n} \left\{\begin{array}{c}m\\n\end{array}\right\}$.

## Matrix Inversion Verification

The matrices $\mathbf{S}(0,-b)$ and $\mathbf{S}(-b,0)$ should be inverses:

$$\mathbf{S}(0,-b) \cdot \mathbf{S}(-b,0) = \mathbf{I}$$

### Verification Formula

**Verification formula:**
$$\sum_{k=0}^{m} \left(\frac{-1}{b}\right)^k \left[\begin{array}{c}m\\k\end{array}\right] \cdot \left(\frac{-1}{b}\right)^{k-n} \left\{\begin{array}{c}k\\n\end{array}\right\} = [m=n]$$

Simplifying:
$$\left(\frac{1}{b}\right)^n \sum_{k=0}^{m} \left[\begin{array}{c}m\\k\end{array}\right] \left\{\begin{array}{c}k\\n\end{array}\right\} = [m=n]$$

$$\left(\frac{-1}{b}\right)^n \sum_{k=0}^{m} \left[\begin{array}{c}m\\k\end{array}\right] \left\{\begin{array}{c}k\\n\end{array}\right\} = [m=n]$$

This reduces to the classical orthogonality since $\sum_{k=0}^{m} \left[\begin{array}{c}m\\k\end{array}\right] \left\{\begin{array}{c}k\\n\end{array}\right\} = [m=n]$.

## Combinatorial Interpretations

### Coloring Interpretation for $S_{m,n}(0,-b)$

The scaling factor $b^{-n}$ and alternating signs suggest a **colored inclusion-exclusion** interpretation:

**Interpretation:** Transform $m$ indistinguishable objects to $n$ distinguishable circular arrangements, where:
- Each arrangement can be "colored" with one of $b$ colors
- The negative powers $b^{-n}$ represent "inverse coloring" or constraint weighting
- Alternating signs $(-1)^n$ implement inclusion-exclusion principle

### Detailed Coloring Analysis

Consider $S_{3,2}(0,-b) = (-1)^2 b^{-2} \left[\begin{array}{c}3\\2\end{array}\right] = \frac{3}{b^2}$:

**Step 1:** Start with $\left[\begin{array}{c}3\\2\end{array}\right] = 3$ ways to arrange 3 objects in 2 cycles
**Step 2:** Each of the 2 cycles can be assigned one of $b$ colors
**Step 3:** The scaling $b^{-2}$ represents "average" or "constraint-weighted" counting
**Step 4:** Sign $(-1)^2 = +1$ indicates even inclusion-exclusion

### Inclusion-Exclusion Structure

The alternating signs $(-1)^n$ in $S_{m,n}(0,-b)$ suggest systematic inclusion-exclusion:

- **$n$ even:** Positive contribution (inclusion)
- **$n$ odd:** Negative contribution (exclusion)

This pattern appears in many combinatorial contexts involving:
- **Principle of inclusion-exclusion** for counting with constraints
- **Signed sums** in algebraic combinatorics
- **Alternating series** in generating function theory

### Connection to Rook Polynomials and Derangements

The alternating sign pattern relates to:

**Rook polynomials:** Counting rook placements on chessboards with forbidden positions
**Derangement problems:** Counting permutations with no fixed points
**Chromatic polynomials:** Graph coloring with exclusion principles

## Advanced Scaling Properties

### General Scaling Law

For any positive integer $c$:
$$S_{m,n}(0,-bc) = c^{-n} S_{m,n}(0,-b)$$

This shows **multiplicative scaling** in the parameter.

### Fractional Parameters

For rational $b = p/q$:
$$S_{m,n}(0,-p/q) = (-1)^n (q/p)^n \left[\begin{array}{c}m\\n\end{array}\right]$$

This extends the framework to rational scaling factors.

### Asymptotic Behavior

For large $b$:
$$S_{m,n}(0,-b) \sim (-1)^n b^{-n} \left[\begin{array}{c}m\\n\end{array}\right]$$

The dominant term behavior is controlled by the unsigned Stirling numbers.

## Generating Functions

### Exponential Generating Function

$$\sum_{m=0}^{\infty} S_{m,n}(0,-b) \frac{x^m}{m!} = (-1)^n b^{-n} \frac{(\log(1+x))^n}{n!}$$

### Ordinary Generating Function

$$\sum_{n=0}^{m} S_{m,n}(0,-b) z^n = \prod_{k=0}^{m-1} (1 - z/b)$$

This shows the **factorization structure** of the generating function.

## Computational Aspects

### Recurrence Relations

The scaled coefficients satisfy:
$$S_{m+1,n}(0,-b) = S_{m,n-1}(0,-b) - mb \cdot S_{m,n}(0,-b)$$

### Efficient Computation

For large $b$, use the scaling relationship:
