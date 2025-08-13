# Sequence Operations: Examples and Computations

## Concrete Examples

### Example 1: Power Sequence Operations

Let $x = 2$ and consider $\mathcal{P}_2 = (2^1, 2^2, 2^3, 2^4, \ldots) = (2, 4, 8, 16, \ldots)$

**Scalar multiplication:** $3 \cdot \mathcal{P}_2 = (6, 12, 24, 48, \ldots)$

### Example 2: Indexed Sequence with Coefficients

Let $\mathcal{A} = (1, 1, 2, 6, 24, \ldots)$ (factorial sequence starting from $0! = 1$)

**Product with power sequence:**
$$\mathcal{A} \odot \mathcal{P}_x = (1 \cdot x^1, 1 \cdot x^2, 2 \cdot x^3, 6 \cdot x^4, 24 \cdot x^5, \ldots)$$
$$= (x, x^2, 2x^3, 6x^4, 24x^5, \ldots)$$

This generates the exponential generating function:
$$\sum_{n=1}^{\infty} \frac{(n-1)!}{1} x^n = x + x^2 + 2x^3 + 6x^4 + 24x^5 + \ldots$$

## Bell Polynomial Definitions and Recursions

### Individual (Partial) Bell Polynomials

The individual Bell polynomials $B_{m,n}(\mathcal{X})$ satisfy the recursion:
$$B_{m,n}(\mathcal{X}) = \sum_{k=1}^{n-m+1} \binom{n-1}{k-1} x_k B_{m-1, n-k}(\mathcal{X})$$

This relation holds for $n \geq m \geq 1$ with initialization $B_{0,0} = 1$.

**Parameters:**
- $m$: the number of parts in the partition  
- $n$: the size of the set being partitioned

**Boundary conditions:**
- $B_{0,0} = 1$
- $B_{m,n} = 0$ if $m > n$ or $m < 0$ or $n < 0$

### Complete Bell Polynomials

The complete Bell polynomials are the sum over all partitions:
$$B_n(\mathcal{X}) = \sum_{m=0}^{n} B_{n,m}(\mathcal{X})$$

Alternatively, they satisfy the recursion:
$$B_{n+1}(\mathcal{X}) = \sum_{k=0}^{n} \binom{n}{k} B_k(\mathcal{X}) \cdot x_{n-k+1}$$

### Connection Between Individual and Complete

The complete Bell polynomial $B_n(\mathcal{X})$ counts all weighted partitions of an $n$-element set, while the individual Bell polynomial $B_{m,n}(\mathcal{X})$ counts only those partitions with exactly $m$ parts.

## Examples Using the Recursion

### Example 1: Computing $B_{2,3}(\mathcal{X})$

Using the recursion with $m = 2, n = 3$:
$$B_{2,3}(\mathcal{X}) = \sum_{k=1}^{3-2+1} \binom{3-1}{k-1} x_k B_{2-1, 3-k}(\mathcal{X})$$
$$= \sum_{k=1}^{2} \binom{2}{k-1} x_k B_{1, 3-k}(\mathcal{X})$$
$$= \binom{2}{0} x_1 B_{1,2}(\mathcal{X}) + \binom{2}{1} x_2 B_{1,1}(\mathcal{X})$$
$$= 1 \cdot x_1 \cdot B_{1,2}(\mathcal{X}) + 2 \cdot x_2 \cdot B_{1,1}(\mathcal{X})$$

Now we need $B_{1,2}$ and $B_{1,1}$:
- $B_{1,1}(\mathcal{X}) = \sum_{k=1}^{1} \binom{0}{k-1} x_k B_{0,1-k}(\mathcal{X}) = \binom{0}{0} x_1 B_{0,0} = x_1$
- $B_{1,2}(\mathcal{X}) = \sum_{k=1}^{2} \binom{1}{k-1} x_k B_{0,2-k}(\mathcal{X}) = \binom{1}{0} x_1 B_{0,1} + \binom{1}{1} x_2 B_{0,0} = x_1 \cdot 0 + x_2 \cdot 1 = x_2$

Therefore:
$$B_{2,3}(\mathcal{X}) = x_1 \cdot x_2 + 2 \cdot x_2 \cdot x_1 = 3x_1 x_2$$

### Example 2: Computing $B_{2,4}(\mathcal{X})$

Using $m = 2, n = 4$:
$$B_{2,4}(\mathcal{X}) = \sum_{k=1}^{3} \binom{3}{k-1} x_k B_{1, 4-k}(\mathcal{X})$$
$$= \binom{3}{0} x_1 B_{1,3} + \binom{3}{1} x_2 B_{1,2} + \binom{3}{2} x_3 B_{1,1}$$
$$= 1 \cdot x_1 \cdot x_3 + 3 \cdot x_2 \cdot x_2 + 3 \cdot x_3 \cdot x_1$$
$$= x_1 x_3 + 3 x_2^2 + 3 x_1 x_3 = 4 x_1 x_3 + 3 x_2^2$$

### Example 3: Verification with Complete Bell Polynomials

For $B_3(\mathcal{X})$, we have:
$$B_3(\mathcal{X}) = B_{0,3} + B_{1,3} + B_{2,3} + B_{3,3}$$

Where:
- $B_{0,3} = 0$ (no partition into 0 parts)
- $B_{1,3} = x_3$ (one part of size 3)
- $B_{2,3} = 3x_1 x_2$ (two parts: sizes 1,2)
- $B_{3,3} = x_1^3$ (three parts: sizes 1,1,1)

So: $B_3(\mathcal{X}) = x_3 + 3x_1 x_2 + x_1^3$

This matches the known formula for the third complete Bell polynomial!

## Computational Framework

### Algorithm 1: Sequence Scalar Multiplication

```pseudocode
Input: Sequence A = {a_n}, scalar k, length N
Output: Sequence k·A = {k·a_n}

for n = 1 to N:
    result[n] = k * A[n]
return result
```

### Algorithm 2: Hadamard Product

```pseudocode
Input: Sequences A = {a_n}, B = {b_n}, length N
Output: Sequence A⊙B = {a_n·b_n}

for n = 1 to N:
    result[n] = A[n] * B[n]
return result
```

### Algorithm 3: Bell Polynomial via Sequence Operations

```pseudocode
Input: Sequence X = {x_n}, degree n
Output: Bell polynomial B_n(X)

B[0] = 1
for k = 1 to n:
    B[k] = 0
    for j = 0 to k-1:
        B[k] += binomial(k-1, j) * B[j] * X[k-j]
return B[n]
```

## Lemma Templates for Bell Polynomials

### Lemma Template 1: Linearity

**Lemma:** For sequences $\mathcal{A}$ and $\mathcal{B}$, and scalars $\alpha, \beta$:
$$B_n(\alpha \mathcal{A} \oplus \beta \mathcal{B}) = \alpha^n B_n(\mathcal{A}) + \text{[mixed terms]} + \beta^n B_n(\mathcal{B})$$

**Proof Framework:**

1. Apply definition of sequence operations
2. Use Bell polynomial recursion
3. Expand using binomial theorem
4. Collect terms by powers of $\alpha$ and $\beta$

### Lemma Template 2: Product Rule

**Lemma:** For sequences $\mathcal{A}$ and power sequence $\mathcal{P}_x$:
$$\frac{d}{dx} \sum_{n=1}^{\infty} B_n(\mathcal{A}) \frac{(\mathcal{A} \odot \mathcal{P}_x)^n}{n!} = \sum_{n=1}^{\infty} n \cdot B_n(\mathcal{A}) \frac{(\mathcal{A} \odot \mathcal{P}_x)^{n-1}}{(n-1)!} \odot \mathcal{A}$$

### Lemma Template 3: Composition Property

**Lemma:** For sequence transformation $T(\mathcal{A})$:
$$B_n(T(\mathcal{A})) = F_n(B_1(\mathcal{A}), B_2(\mathcal{A}), \ldots, B_n(\mathcal{A}))$$

where $F_n$ is a polynomial determined by the transformation $T$.

## Special Cases and Applications

### Case 1: Stirling Numbers as Sequences

Let $\mathcal{S}_n = (S(n,1), S(n,2), \ldots, S(n,n))$ be the sequence of Stirling numbers of the second kind.

**Property:** $\sum_{k=1}^{n} S(n,k) = B_n(1,1,1,\ldots,1)$

### Case 2: Moments and Cumulants

For moment sequence $\mathcal{M} = (\mu_1, \mu_2, \mu_3, \ldots)$ and cumulant sequence $\mathcal{K} = (\kappa_1, \kappa_2, \kappa_3, \ldots)$:

$$\mu_n = B_n(\mathcal{K})$$

This establishes the fundamental relationship between moments and cumulants via Bell polynomials.

### Case 3: Generating Function Coefficients

For generating function $f(x) = \sum_{n=0}^{\infty} a_n x^n$:

The sequence $\mathcal{A} = (a_1, a_2, a_3, \ldots)$ can be operated on to produce:
$$(\mathcal{A} \odot \mathcal{P}_x)_{\text{sum}} = \sum_{n=1}^{\infty} a_n x^n = f(x) - a_0$$

## Implementation Notes

1. **Finite Truncation:** In practice, sequences are truncated to finite length $N$.
2. **Memory Management:** Store only computed terms up to required degree.
3. **Numerical Stability:** Use appropriate precision for factorial and power computations.
4. **Symbolic Computation:** For exact results, maintain symbolic representations.

## References for Further Development

- Comtet, L. "Advanced Combinatorics" (Bell polynomial properties)
- Riordan, J. "Combinatorial Identities" (sequence generating functions)
- Stanley, R.P. "Enumerative Combinatorics" (formal power series and sequences)
