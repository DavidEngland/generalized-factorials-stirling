# Generalized Factorial Polynomials

**Generalized factorial polynomials** are mathematical expressions that extend the concept of factorial functions to include a parameter that generalizes the increment between consecutive terms. These polynomials arise naturally in various areas of mathematics, including combinatorics, the theory of special functions, and finite difference calculus.

## Definition

### Primary Notation

The **generalized factorial polynomial** is denoted as $P(x,a,m)$ and is defined as:

$$P(x,a,m) = x(x+a)(x+2a)\cdots(x+(m-1)a)$$

where:

- $x$ is a real or complex variable
- $a$ is a constant (the **increment parameter**)
- $m$ is a non-negative integer (the **degree** of the polynomial)

**Note**: When $a = 0$, the definition reduces to the trivial monomial case $P(x,0,m) = x^m$.

### Relationship to Established Notations

The $P(x,a,m)$ notation unifies and generalizes several well-known mathematical objects:

#### Generalized Rising Factorials
$$P(x,a,m) = x^{\overline{m}}_a = (x)_{m,a}$$

This is the **generalized rising factorial** or **generalized Pochhammer symbol**.

#### Pochhammer Symbol (Standard Rising Factorial)
When $a = 1$:
$$P(x,1,m) = x^{\overline{m}} = (x)_m = x(x+1)(x+2)\cdots(x+m-1)$$

This is the classical **Pochhammer symbol**.

#### Generalized Falling Factorials
The **generalized falling factorial** relates to $P(x,a,m)$ by:
$$x^{\underline{m}}_a = P(x-a(m-1), a, m) = (x+(m-1)a)^{\underline{m}}_a$$

Alternatively:
$$x^{\underline{m}}_a = x(x-a)(x-2a)\cdots(x-(m-1)a)$$

#### Standard Falling Factorial

When $a = 1$:
$$x^{\underline{m}} = x(x-1)(x-2)\cdots(x-m+1)$$

#### Trivial Monomial Case

When $a = 0$, the generalized factorial polynomial reduces to the simple monomial:
$$P(x,0,m) = x^m$$

This case represents the degenerate limit where all increments vanish, yielding the standard power function. This limiting behavior is fundamental in connecting discrete factorial structures to continuous polynomial theory.

### Initial and Boundary Conditions

The generalized factorial polynomial $P(x,a,m)$ satisfies several fundamental conditions:

#### Initial Condition
$$P(x,a,0) = 1$$

This follows from the empty product convention.

#### Boundary Behavior
$$P(0,a,m) = \begin{cases} 
0 & \text{if } m > 0 \text{ and } a \neq 0 \\
0^m & \text{if } a = 0 \\
1 & \text{if } m = 0
\end{cases}$$

For the monomial case ($a = 0$), this gives the standard behavior: $P(0,0,m) = 0^m$, which equals 0 for $m > 0$ and 1 for $m = 0$.

#### Recursive Structure
$$P(x,a,m+1) = P(x,a,m) \cdot (x + ma)$$

This fundamental recurrence relation defines the polynomial structure.

**Monomial Case**: When $a = 0$, this becomes $P(x,0,m+1) = P(x,0,m) \cdot x = x^m \cdot x = x^{m+1}$, which is the standard power rule.

## Properties and Identities

### Fundamental Recurrence Relations

The generalized factorial polynomial satisfies several important recurrence relations:

#### Forward Recurrence
$$P(x,a,m+1) = P(x,a,m) \cdot (x + ma)$$

#### Backward Recurrence
$$P(x,a,m) = \frac{P(x,a,m+1)}{x + ma}$$

#### Shift Relations
$$P(x+a,a,m) = \frac{P(x,a,m+1)}{x}$$

### Connection to the Gamma Function

For complex arguments with $a \neq 0$, the generalized factorial polynomial can be expressed using the gamma function:

$$P(x,a,m) = a^m \frac{\Gamma(x/a + m)}{\Gamma(x/a)}$$

This representation extends the definition to non-integer values of $m$ and provides the analytic continuation.

**Special Case**: When $a = 0$, the gamma function representation is not applicable, and we have the direct monomial form $P(x,0,m) = x^m$.

#### Special Cases via Gamma Function

- **Pochhammer Symbol**: $P(x,1,m) = \frac{\Gamma(x+m)}{\Gamma(x)}$
- **Integer Arguments**: When $x$ is a positive integer $n$, $P(n,1,m) = \frac{(n+m-1)!}{(n-1)!}$

### Relationship Between Rising and Falling Forms

The connection between $P(x,a,m)$ (rising) and the falling factorial is:

$$P(x,a,m) = (x+(m-1)a)^{\underline{m}}_a$$

This identity allows conversion between the two forms and demonstrates their fundamental equivalence.

## Examples

### Computational Examples

#### Example 1: P(5,2,3)
$$P(5,2,3) = 5 \cdot (5+2) \cdot (5+4) = 5 \cdot 7 \cdot 9 = 315$$

This demonstrates the basic computation with $x=5$, $a=2$, and $m=3$.

#### Example 2: P(10,3,4)
$$P(10,3,4) = 10 \cdot (10+3) \cdot (10+6) \cdot (10+9) = 10 \cdot 13 \cdot 16 \cdot 19 = 39{,}520$$

#### Example 3: Pochhammer Symbol P(x,1,m)
$$P(3,1,4) = 3 \cdot 4 \cdot 5 \cdot 6 = 360 = \frac{6!}{2!}$$

This is equivalent to the standard Pochhammer symbol $(3)_4$.

#### Example 4: Trivial Monomial Case P(x,0,m)
$$P(5,0,3) = 5^3 = 125$$

$$P(2,0,4) = 2^4 = 16$$

This demonstrates the degenerate case where the generalized factorial reduces to simple monomials.

### Verification of Properties

#### Recurrence Relation Verification
Starting with $P(5,2,2) = 5 \cdot 7 = 35$:
$$P(5,2,3) = P(5,2,2) \cdot (5 + 2 \cdot 2) = 35 \cdot 9 = 315$$

This confirms the forward recurrence relation.

#### Gamma Function Verification
For $P(3,1,2)$:
$$P(3,1,2) = \frac{\Gamma(3+2)}{\Gamma(3)} = \frac{4!}{2!} = \frac{24}{2} = 12$$

Direct computation: $P(3,1,2) = 3 \cdot 4 = 12$ ✓

#### Monomial Case Verification
For $P(4,0,3)$:
$$P(4,0,3) = 4^3 = 64$$

Using recurrence: $P(4,0,3) = P(4,0,2) \cdot (4 + 0 \cdot 2) = 16 \cdot 4 = 64$ ✓

## Historical Context

The concept of generalized factorial polynomials emerged from the generalization of the classical Pochhammer symbol, introduced by **Leo Pochhammer** in 1870. The extension to arbitrary increment parameters developed naturally in the study of hypergeometric functions and combinatorial analysis during the late 19th and early 20th centuries.

The systematic study of these polynomials was advanced by mathematicians working on finite difference theory and special functions, including **Charles Jordan** and **Niels Erik Nørlund** in the early 20th century.

## Applications

Generalized factorial polynomials have applications in several mathematical fields:

### Finite Difference Calculus
These polynomials are fundamental in the theory of finite differences, where they serve as discrete analogs of power functions in continuous calculus.

### Special Functions Theory
They appear in the series expansions of hypergeometric functions and other special functions, particularly in generalizations of the binomial theorem.

### Combinatorics
In combinatorial analysis, generalized factorial polynomials (especially with $a = 1$) count arrangements and selections in various discrete structures.

### Numerical Analysis
They are used in interpolation formulas, particularly in Newton's forward and backward difference formulas when generalized to non-uniform grids.

### Mathematical Physics
These polynomials appear in the study of quantum mechanical systems and statistical mechanics, particularly in problems involving discrete energy levels or lattice structures.

## See Also

- **Pochhammer symbol** - The standard case $P(x,1,m)$
- **Gamma function** - Provides analytic continuation
- **Rising factorial** - Alternative notation for $P(x,1,m)$
- **Falling factorial** - Related by shift transformation
- **Monomial** - The trivial case $P(x,0,m) = x^m$
- **Hypergeometric function** - Uses generalized factorials in series
- **Finite difference** - Applications in discrete calculus
- **Binomial coefficient** - Related combinatorial objects
- **Beta function** - Connected special function

## References

1. Jordan, C. (1939). *Calculus of Finite Differences*. Hungarian Academy of Sciences.
2. Nørlund, N. E. (1924). *Vorlesungen über Differenzenrechnung*. Springer-Verlag.
3. Rainville, E. D. (1960). *Special Functions*. Macmillan Company.
4. Graham, R. L., Knuth, D. E., & Patashnik, O. (1994). *Concrete Mathematics* (2nd ed.). Addison-Wesley.
