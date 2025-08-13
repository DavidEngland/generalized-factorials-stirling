# Quick Reference: Sequence Notation for Bell Polynomials

## Core Notation Summary

| Notation | Description | Example |
|----------|-------------|---------|
| $\mathcal{P}_x = \{x^n\}_{n=1}^{\infty}$ | Power sequence | $(x^1, x^2, x^3, \ldots)$ |
| $\mathcal{A} = \{a_n\}_{n=1}^{\infty}$ | Indexed sequence | $(a_1, a_2, a_3, \ldots)$ |
| $k \cdot \mathcal{A}$ | Scalar multiplication | $(ka_1, ka_2, ka_3, \ldots)$ |
| $\mathcal{A} \odot \mathcal{B}$ | Hadamard product | $(a_1b_1, a_2b_2, a_3b_3, \ldots)$ |
| $\mathcal{A} \odot \mathcal{P}_x$ | Product with powers | $(a_1x^1, a_2x^2, a_3x^3, \ldots)$ |

## Key Operations

### Scalar Multiplication
$$k \cdot \mathcal{A} = \{k \cdot a_n\}_{n=1}^{\infty}$$

### Element-wise Product (Hadamard)
$$\mathcal{A} \odot \mathcal{B} = \{a_n \cdot b_n\}_{n=1}^{\infty}$$

### Generating Series from Product
$$\mathcal{A} \odot \mathcal{P}_x \rightarrow \sum_{n=1}^{\infty} a_n x^n$$

## Bell Polynomial Application

### Basic Definition
$$B_n(\mathcal{X}) = B_n(x_1, x_2, \ldots, x_n)$$

### Recursion Formula
$$B_{n+1}(\mathcal{X}) = \sum_{k=0}^{n} \binom{n}{k} B_k(\mathcal{X}) \cdot x_{n-k+1}$$

### First Few Bell Polynomials
- $B_0(\mathcal{X}) = 1$
- $B_1(\mathcal{X}) = x_1$
- $B_2(\mathcal{X}) = x_1^2 + x_2$
- $B_3(\mathcal{X}) = x_1^3 + 3x_1x_2 + x_3$

## Lemma Templates

### Template 1: Linearity
**For sequences $\mathcal{A}, \mathcal{B}$ and scalars $\alpha, \beta$:**
$$B_n(\alpha \mathcal{A} \oplus \beta \mathcal{B}) = \text{[expansion with multinomial structure]}$$

### Template 2: Product with Powers
**For indexed sequence $\mathcal{A}$ and power sequence $\mathcal{P}_x$:**
$$\sum_{n=0}^{\infty} B_n(\mathcal{A}) \frac{(\mathcal{A} \odot \mathcal{P}_x)^n}{n!} = \exp\left(\sum_{n=1}^{\infty} a_n \frac{x^n}{n}\right)$$

### Template 3: Faà di Bruno's Formula (Composite Function Derivatives)
**For composite functions $g(f(x))$ where $f(x) = \sum_{n=0}^{\infty} a_n \frac{x^n}{n!}$:**
$$\frac{d^m}{dx^m} g(f(x)) = \sum_{k=0}^{m} g^{(k)}(f(x)) \cdot B_{m,k}(a_1, a_2, \ldots, a_{m-k+1})$$

**Sequence form:** If $\mathcal{A} = (a_1, a_2, a_3, \ldots)$ represents the coefficients of $f'(x), f''(x), f'''(x), \ldots$:
$$\frac{d^m}{dx^m} g(f(x)) = \sum_{k=0}^{m} g^{(k)}(f(x)) \cdot B_{m,k}(\mathcal{A})$$

### Template 4: Stirling Connection
**For Stirling numbers as sequences:**
$$\sum_{k=1}^{n} S(n,k) = B_n(1,1,1,\ldots,1)$$

**Individual Bell polynomials and Stirling numbers of the first kind:**
$$B_{m,n}(1,1,1,\ldots,1) = |s(m,n)|$$
where $s(m,n)$ are the (signed) Stirling numbers of the first kind.

**Bell polynomials of factorial sequence and Stirling numbers of the second kind:**
$$B_n(0!, 1!, 2!, 3!, \ldots) = S(n,k) \text{ (unsigned, for appropriate } k \text{)}$$

## Special Sequences

### Factorial Sequence
$$\mathcal{F} = \{n!\}_{n=0}^{\infty} = (0!, 1!, 2!, 3!, \ldots) = (1, 1, 2, 6, 24, \ldots)$$

**Key Property:** $B_n(\mathcal{F})$ relates to unsigned Stirling numbers of the second kind.

### All Ones Sequence  
$$\mathcal{1} = (1, 1, 1, \ldots)$$

**Key Properties:**
- Complete Bell polynomial: $B_n(\mathcal{1}) = \text{Bell}(n)$
- Individual Bell polynomials: $B_{m,n}(\mathcal{1}) = |s(m,n)|$ (unsigned Stirling numbers of first kind)

### Stirling Second Kind (fixed n)
$$\mathcal{S}_n = \{S(n,k)\}_{k=1}^{n} = (S(n,1), S(n,2), \ldots, S(n,n))$$

### Moment Sequence
$$\mathcal{M} = \{\mu_n\}_{n=1}^{\infty} = (\mu_1, \mu_2, \mu_3, \ldots)$$

### Cumulant Sequence
$$\mathcal{K} = \{\kappa_n\}_{n=1}^{\infty} = (\kappa_1, \kappa_2, \kappa_3, \ldots)$$

## Key Relationships

### Moments and Cumulants
$$\mu_n = B_n(\mathcal{K})$$

### Exponential Generating Function
$$\sum_{n=0}^{\infty} \mu_n \frac{t^n}{n!} = \exp\left(\sum_{n=1}^{\infty} \kappa_n \frac{t^n}{n!}\right)$$

### Bell Numbers
$$\text{Bell}(n) = B_n(1,1,1,\ldots,1) = \sum_{k=1}^{n} S(n,k)$$

## Computational Formulas

### Sequence Operations (finite length N)
```
Scalar: (k·A)[i] = k * A[i] for i = 1 to N
Hadamard: (A⊙B)[i] = A[i] * B[i] for i = 1 to N  
Addition: (A⊕B)[i] = A[i] + B[i] for i = 1 to N
```

### Bell Polynomial Computation
```
B[0] = 1
for n = 1 to max_degree:
    B[n] = sum over k=0 to n-1 of:
           binomial(n-1, k) * B[k] * x[n-k]
```

## Lemma Development Framework

When developing lemmas about Bell polynomials acting on sequences:

1. **Define the sequences** clearly using the notation above
2. **State the operation** (scalar mult., product, etc.)
3. **Apply Bell polynomial** to the result
4. **Use recursion formula** to expand
5. **Collect and simplify** terms
6. **State the final relationship**

### Example Lemma Structure
**Lemma:** *[Statement about $B_n$ applied to sequence operation]*

**Proof:**
1. Let $\mathcal{A} = \{a_n\}$ and $\mathcal{B} = \{b_n\}$
2. Consider the operation $\mathcal{C} = \mathcal{A} \text{ op } \mathcal{B}$
3. Apply $B_n(\mathcal{C})$ using recursion...
4. Expand and collect terms...
5. Therefore, $B_n(\mathcal{C}) = \text{[final expression]}$ □

This framework provides everything you need to develop rigorous notation and prove lemmas about Bell polynomials acting on sequences!
