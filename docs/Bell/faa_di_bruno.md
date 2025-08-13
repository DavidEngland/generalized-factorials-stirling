# Faà di Bruno's Formula and Bell Polynomials

## The Fundamental Connection

Faà di Bruno's formula expresses the $m$-th derivative of a composite function $g(f(x))$ using Bell polynomials. This provides a crucial bridge between:
- **Analysis** (higher-order derivatives)
- **Combinatorics** (Bell polynomials and partitions)
- **Your sequence framework** (coefficient sequences)

## Classical Faà di Bruno's Formula

For functions $g$ and $f$, the $m$-th derivative of their composition is:
$$\frac{d^m}{dx^m} g(f(x)) = \sum_{k=0}^{m} g^{(k)}(f(x)) \cdot B_{m,k}(f'(x), f''(x), \ldots, f^{(m-k+1)}(x))$$

where $B_{m,k}$ are the **individual Bell polynomials** (partial Bell polynomials).

## Sequence Formulation

### Function as Exponential Series
Given $f(x) = \sum_{n=0}^{\infty} a_n \frac{x^n}{n!}$, the derivatives are:
- $f'(x) = \sum_{n=1}^{\infty} a_n \frac{x^{n-1}}{(n-1)!} = \sum_{n=0}^{\infty} a_{n+1} \frac{x^n}{n!}$
- $f''(x) = \sum_{n=0}^{\infty} a_{n+2} \frac{x^n}{n!}$
- $f^{(k)}(x) = \sum_{n=0}^{\infty} a_{n+k} \frac{x^n}{n!}$

### Coefficient Sequence
Define the **derivative coefficient sequence**:
$$\mathcal{A} = (a_1, a_2, a_3, a_4, \ldots)$$

This represents the coefficients of $f'(x), f''(x), f'''(x), \ldots$ evaluated at $x=0$:
- $f'(0) = a_1$
- $f''(0) = a_2$  
- $f'''(0) = a_3$
- etc.

### Sequence Form of Faà di Bruno
$$\frac{d^m}{dx^m} g(f(x))\bigg|_{x=0} = \sum_{k=0}^{m} g^{(k)}(f(0)) \cdot B_{m,k}(\mathcal{A})$$

where $B_{m,k}(\mathcal{A}) = B_{m,k}(a_1, a_2, \ldots, a_{m-k+1})$.

## Examples

### Example 1: Exponential Composition
Let $g(u) = e^u$ and $f(x) = \sum_{n=0}^{\infty} a_n \frac{x^n}{n!}$.

Then $g^{(k)}(u) = e^u$ for all $k$, so:
$$\frac{d^m}{dx^m} e^{f(x)}\bigg|_{x=0} = e^{f(0)} \sum_{k=0}^{m} B_{m,k}(\mathcal{A})$$

Since $\sum_{k=0}^{m} B_{m,k}(\mathcal{A}) = B_m(\mathcal{A})$ (complete Bell polynomial):
$$\frac{d^m}{dx^m} e^{f(x)}\bigg|_{x=0} = e^{a_0} \cdot B_m(\mathcal{A})$$

### Example 2: Logarithmic Composition
Let $g(u) = \log(u)$ and $f(x) = 1 + \sum_{n=1}^{\infty} a_n \frac{x^n}{n!}$ (so $f(0) = 1$).

The derivatives of $g(u) = \log(u)$ are:
- $g'(u) = \frac{1}{u}$
- $g''(u) = -\frac{1}{u^2}$
- $g'''(u) = \frac{2}{u^3}$
- $g^{(k)}(u) = (-1)^{k-1} \frac{(k-1)!}{u^k}$

So:
$$\frac{d^m}{dx^m} \log(f(x))\bigg|_{x=0} = \sum_{k=1}^{m} (-1)^{k-1} (k-1)! \cdot B_{m,k}(\mathcal{A})$$

### Example 3: Power Composition
Let $g(u) = u^r$ for some real $r$, and $f(x) = 1 + \sum_{n=1}^{\infty} a_n \frac{x^n}{n!}$.

Then $g^{(k)}(u) = r(r-1)\cdots(r-k+1) u^{r-k} = \binom{r}{k} k! u^{r-k}$, so:
$$\frac{d^m}{dx^m} [f(x)]^r\bigg|_{x=0} = \sum_{k=0}^{m} \binom{r}{k} k! \cdot B_{m,k}(\mathcal{A})$$

## Connection to Your Sequence Operations

### Scalar Multiplication Impact
If we scale the coefficient sequence: $k \cdot \mathcal{A} = (ka_1, ka_2, ka_3, \ldots)$

This corresponds to the function $f_k(x) = a_0 + k \sum_{n=1}^{\infty} a_n \frac{x^n}{n!}$.

By your scalar lemma: $B_{m,k}(k \cdot \mathcal{A}) = k^k B_{m,k}(\mathcal{A})$

So for the composition $g(f_k(x))$:
$$\frac{d^m}{dx^m} g(f_k(x))\bigg|_{x=0} = \sum_{k=0}^{m} g^{(k)}(f_k(0)) \cdot k^k B_{m,k}(\mathcal{A})$$

### Hadamard Product Impact
If $\mathcal{B} = \mathcal{A} \odot \mathcal{C}$, then the Bell polynomials $B_{m,k}(\mathcal{B})$ encode the derivatives of compositions involving the "product function" corresponding to $\mathcal{B}$.

## Combinatorial Interpretation

### Individual Bell Polynomials $B_{m,k}$
$B_{m,k}(a_1, a_2, \ldots, a_{m-k+1})$ counts weighted partitions of a set of $m$ elements into exactly $k$ blocks, where:
- A block of size $j$ contributes weight $a_j$
- The total weight is the product of all block weights

### Complete Bell Polynomials $B_m$
$B_m(a_1, a_2, \ldots, a_m) = \sum_{k=0}^{m} B_{m,k}(a_1, \ldots, a_{m-k+1})$ counts all weighted partitions of $m$ elements.

## Applications to Generalized Factorials

### Factorial Generating Functions
If $\mathcal{A} = \mathcal{F} = (1, 1, 2, 6, 24, \ldots)$ (factorial sequence), then $f(x) = \sum_{n=0}^{\infty} n! \frac{x^n}{n!} = \sum_{n=0}^{\infty} x^n = \frac{1}{1-x}$.

The derivatives of $g\left(\frac{1}{1-x}\right)$ involve Bell polynomials of the factorial sequence, connecting to Stirling numbers of the second kind.

### Stirling Number Generating Functions
If $\mathcal{A} = \mathcal{1} = (1, 1, 1, \ldots)$, then $f(x) = \sum_{n=0}^{\infty} \frac{x^n}{n!} = e^x$.

The derivatives of $g(e^x)$ involve Bell polynomials of the all-ones sequence, connecting to Stirling numbers via the Bell numbers.

## Computational Framework

### Algorithm: Faà di Bruno via Sequences
```python
def faa_di_bruno_derivative(g_derivatives, f_coefficients, m):
    """
    Compute m-th derivative of g(f(x)) at x=0 using Bell polynomials
    
    Args:
        g_derivatives: [g(f(0)), g'(f(0)), g''(f(0)), ..., g^(m)(f(0))]
        f_coefficients: [a_1, a_2, ..., a_m] (derivative coefficients of f)
        m: order of derivative
    
    Returns:
        m-th derivative of g(f(x)) at x=0
    """
    result = 0
    for k in range(m + 1):
        bell_mk = compute_individual_bell(m, k, f_coefficients)
        result += g_derivatives[k] * bell_mk
    return result

def compute_individual_bell(m, k, coefficients):
    """Compute individual Bell polynomial B_{m,k}"""
    # Implementation using your specific recursion
    pass
```

### Example: Computing $\frac{d^3}{dx^3} e^{f(x)}$ where $f(x) = x + x^2 + \frac{x^3}{2}$
```python
# f(x) coefficients: a_0=0, a_1=1, a_2=2, a_3=3
f_coeffs = [1, 2, 3]  # [a_1, a_2, a_3]
g_derivs = [1, 1, 1, 1]  # [e^0, e^0, e^0, e^0] = [1, 1, 1, 1]

# Compute 3rd derivative
result = faa_di_bruno_derivative(g_derivs, f_coeffs, 3)
```

## Theoretical Significance

Faà di Bruno's formula with Bell polynomials provides:

1. **Algorithmic computation** of higher derivatives of compositions
2. **Combinatorial interpretation** of analytical operations
3. **Bridge** between your sequence operations and classical analysis
4. **Generalization** to non-integer and complex derivatives via sequence extensions

This connection makes your sequence framework applicable to:
- **Differential equations** involving composite functions
- **Asymptotic analysis** of complex compositions
- **Special function theory** where compositions are fundamental
- **Generating function manipulations** in combinatorics

The scalar factorization lemma becomes particularly powerful here, as it shows how scaling the "inner function" coefficients scales the derivative computations in a predictable way.
