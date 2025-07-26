# Rising and Falling Factorials: A Unified Framework

**Rising and falling factorials** are fundamental mathematical functions that extend the concept of ordinary factorials to polynomials with arithmetic progressions. This article presents a unified treatment using the generalized factorial polynomial notation P(x,a,m) and demonstrates how it encompasses all traditional forms as special cases.

## Traditional Definitions

### Classical Rising Factorial

The **rising factorial** (also called the **Pochhammer function** or **ascending factorial**) is traditionally defined as:

$$x^{(n)} = x^{\overline{n}} = x(x+1)(x+2)\cdots(x+n-1)$$

In special functions literature, this is often denoted as $(x)_n$, following the convention of Abramowitz and Stegun.

### Classical Falling Factorial

The **falling factorial** (also called the **descending factorial** or **lower factorial**) is traditionally defined as:

$$(x)_n = x^{\underline{n}} = x(x-1)(x-2)\cdots(x-n+1)$$

In combinatorics, this notation $(x)_n$ is preferred for the falling factorial, creating notational ambiguity with special functions.

## Unified Framework with P(x,a,m) Notation

### Generalized Factorial Polynomial Definition

The **generalized factorial polynomial** P(x,a,m) unifies both rising and falling factorials:

$$P(x,a,m) = x(x+a)(x+2a)\cdots(x+(m-1)a)$$

where:
- $x$ is the variable
- $a$ is the **increment parameter**
- $m$ is the degree (number of factors)

### Connection to Traditional Notations

#### Rising Factorial as Special Case
The traditional rising factorial corresponds to $a = 1$:
$$P(x,1,n) = x^{(n)} = x^{\overline{n}} = x(x+1)(x+2)\cdots(x+n-1)$$

#### Falling Factorial Connection
The falling factorial can be expressed using P(x,a,m) with $a = -1$ and a variable shift:
$$(x)_n = x^{\underline{n}} = P(x,{-1},n) = x(x-1)(x-2)\cdots(x-n+1)$$

Alternatively, using the relationship:
$$(x)_n = P(x-n+1, 1, n)$$

#### Monomial Case
When $a = 0$, the generalized factorial reduces to simple monomials:
$$P(x,0,m) = x^m$$

## Notation Correspondence Table

| Traditional Notation | P(x,a,m) Form | Parameter Values | Description |
|---------------------|---------------|------------------|-------------|
| $x^{(n)} = x^{\overline{n}}$ | $P(x,1,n)$ | $a=1$ | Rising factorial |
| $(x)_n = x^{\underline{n}}$ | $P(x,-1,n)$ | $a=-1$ | Falling factorial |
| $x^n$ | $P(x,0,n)$ | $a=0$ | Monomial |
| $(x)_n$ (Pochhammer) | $P(x,1,n)$ | $a=1$ | Special functions convention |
| $(x)_n$ (combinatorics) | $P(x,-1,n)$ | $a=-1$ | Combinatorics convention |

## Properties in Unified Framework

### Fundamental Recurrence
All forms satisfy the unified recurrence:
$$P(x,a,m+1) = P(x,a,m) \cdot (x + ma)$$

**Special cases:**
- Rising: $x^{(n+1)} = x^{(n)} \cdot (x + n)$
- Falling: $(x)_{n+1} = (x)_n \cdot (x - n)$
- Monomial: $x^{m+1} = x^m \cdot x$

### Initial Conditions
$$P(x,a,0) = 1 \quad \text{for all } a$$

This gives the standard initial conditions:
- $x^{(0)} = 1$
- $(x)_0 = 1$
- $x^0 = 1$

### Gamma Function Representation

For non-integer extensions, all forms can be expressed using gamma functions:

$$P(x,a,m) = \begin{cases} 
x^m & \text{if } a = 0 \\
a^m \frac{\Gamma(x/a + m)}{\Gamma(x/a)} & \text{if } a \neq 0
\end{cases}$$

**Traditional equivalents:**
- Rising: $x^{(n)} = \frac{\Gamma(x+n)}{\Gamma(x)}$
- Falling: $(x)_n = \frac{\Gamma(x+1)}{\Gamma(x-n+1)}$

## Relationship Between Rising and Falling Forms

### Direct Transformation
The rising and falling factorials are related by:
$$(x)_n = (-1)^n (-x)^{(n)}$$
$$x^{(n)} = (-1)^n (-x)_n$$

### Using P(x,a,m) Framework
This relationship becomes:
$$P(x,-1,n) = (-1)^n P(-x,1,n)$$

### Shift Relationships
$$P(x,a,m) = P(x-a(m-1), -a, m)$$

This shows how to convert between different increment parameters.

## Stirling Number Connections

### Classical Expansions in Monomial Basis

Both rising and falling factorials expand in terms of monomials using Stirling numbers:

#### Falling Factorial Expansion
$$(x)_n = \sum_{k=0}^n s(n,k) x^k = \sum_{k=0}^n s(n,k) P(x,0,k)$$

where $s(n,k)$ are **Stirling numbers of the first kind**.

#### Rising Factorial Expansion
$$x^{(n)} = \sum_{k=0}^n \begin{bmatrix} n \\ k \end{bmatrix} x^k = \sum_{k=0}^n \begin{bmatrix} n \\ k \end{bmatrix} P(x,0,k)$$

where $\begin{bmatrix} n \\ k \end{bmatrix}$ are **unsigned Stirling numbers of the first kind**.

### Inverse Transformations

The monomial-to-factorial expansions use **Stirling numbers of the second kind**:

$$x^n = \sum_{k=0}^n \begin{Bmatrix} n \\ k \end{Bmatrix} (x)_k = \sum_{k=0}^n \begin{Bmatrix} n \\ k \end{Bmatrix} P(x,-1,k)$$

### Unified Stirling Framework

Using the P(x,a,m) notation and generalized Stirling transfer coefficients $S_{m,n}(a,b)$:

$$P(x,a,m) = \sum_{n=0}^m S_{m,n}(a,b) \cdot P(x,b,n)$$

**Classical cases:**
- $S_{m,n}(0,-1) = s(m,n)$ (Stirling first kind)
- $S_{m,n}(-1,0) = \begin{Bmatrix} m \\ n \end{Bmatrix}$ (Stirling second kind, with appropriate scaling)

## Lah Numbers Connection

The **Lah numbers** connect rising and falling factorials directly:

$$x^{(n)} = \sum_{k=0}^n L(n,k) (x)_k$$
$$(x)_n = \sum_{k=0}^n L(n,k) (-1)^{n-k} x^{(k)}$$

where $L(n,k) = \binom{n-1}{k-1} \frac{n!}{k!}$ are the unsigned Lah numbers.

### In P(x,a,m) Framework
These relationships correspond to the generalized Stirling coefficients:
$$S_{n,k}(1,-1) = (-1)^{n-k} L(n,k)$$

This shows that **Lah numbers are special cases of generalized Stirling transfer coefficients**.

## Combinatorial Interpretations

### Traditional Interpretations

#### Falling Factorial $(x)_n$
- Number of $n$-permutations from a set of size $x$
- Number of ways to arrange $n$ distinct objects in $n$ positions, chosen from $x$ available objects

#### Rising Factorial $x^{(n)}$
- Number of ways to place $n$ distinct objects into $x$ distinguishable boxes with order mattering within each box
- Number of surjective functions from a set of size $n$ to a set of size $x$ (with multiplicity)

### Unified Combinatorial Framework

The P(x,a,m) notation generalizes these interpretations:
- **$a > 0$**: Arrangements with increasing constraints
- **$a < 0$**: Arrangements with decreasing constraints  
- **$a = 0$**: Simple multiplicative counting (monomials)

## Applications in Mathematics

### Finite Difference Calculus

The falling factorial serves as the discrete analog of $x^n$ in difference calculus:
$$\Delta (x)_n = n(x)_{n-1}$$

Compare with: $\frac{d}{dx} x^n = nx^{n-1}$

### Hypergeometric Functions

Rising factorials appear in hypergeometric series:
$${}_2F_1(a,b;c;z) = \sum_{n=0}^\infty \frac{a^{(n)} b^{(n)}}{c^{(n)}} \frac{z^n}{n!}$$

In P(x,a,m) notation: $a^{(n)} = P(a,1,n)$

### Generating Functions

#### Rising Factorial Generating Function
$$\sum_{n=0}^\infty (x)_n \frac{t^n}{n!} = (1+t)^x$$

#### Falling Factorial Generating Function  
$$\sum_{n=0}^\infty x^{(n)} \frac{t^n}{n!} = (1-t)^{-x}$$

## Conclusion

The unified P(x,a,m) framework demonstrates that rising and falling factorials are not separate concepts but rather special cases of a single mathematical structure. This perspective:

1. **Resolves notational ambiguities** by making the increment parameter explicit
2. **Unifies combinatorial interpretations** under a single framework
3. **Generalizes Stirling number theory** through transfer coefficients
4. **Provides computational advantages** through systematic parameter handling

The traditional notations remain important for their historical significance and specialized applications, but the unified framework offers deeper mathematical insight and broader applicability.

## See Also

- **Generalized factorial polynomials** - The P(x,a,m) framework
- **Generalized Stirling transfer coefficients** - Unified transformation theory
- **Pochhammer symbol** - Traditional rising factorial notation
- **Stirling numbers** - Connection coefficients between factorial bases
- **Lah numbers** - Rising-to-falling factorial transformations
- **Hypergeometric functions** - Applications in special function theory
- **Finite difference calculus** - Discrete analog applications

## References

1. Pochhammer, L. (1870). *Über die Hypergeometrischen Reihen*. Journal für die reine und angewandte Mathematik.
2. Knuth, D. E. (1992). Two notes on notation. *American Mathematical Monthly*, 99(5), 403-422.
3. Graham, R. L., Knuth, D. E., & Patashnik, O. (1994). *Concrete Mathematics* (2nd ed.). Addison-Wesley.
4. Abramowitz, M., & Stegun, I. A. (Eds.). (1964). *Handbook of Mathematical Functions*. National Bureau of Standards.
5. Comtet, L. (1974). *Advanced Combinatorics: The Art of Finite and Infinite Expansions*. D. Reidel Publishing Company.
