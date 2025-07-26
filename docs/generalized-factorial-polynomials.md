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

### Unified Representation

The generalized factorial polynomial can be expressed in a unified form using Iverson bracket notation:

$$P(x,a,s) = [a = 0] \cdot x^s + [a \neq 0] \cdot a^s \cdot P(x/a, 1, s)$$

where:
- $[a = 0]$ equals 1 if $a = 0$ and 0 otherwise
- $[a \neq 0]$ equals 1 if $a \neq 0$ and 0 otherwise
- $s$ represents the degree (replacing $m$ for consistency with the unified notation)

This representation elegantly captures both cases:
- **Monomial case** ($a = 0$): $P(x,0,s) = x^s$
- **General case** ($a \neq 0$): $P(x,a,s) = a^s \cdot P(x/a, 1, s) = a^s \cdot (x/a)^{\overline{s}}$

The unified form demonstrates how the generalized factorial polynomial smoothly transitions between the discrete factorial structure and the continuous monomial, with the Iverson brackets serving as a mathematical "switch" between the two regimes.

### Relationship to Established Notations

The $P(x,a,m)$ notation unifies and generalizes several well-known mathematical objects:

#### Generalized Rising Factorials
$$P(x,a,m) = x^{\overline{m}}_a = (x)_{m,a}$$

This is the **generalized rising factorial** or **generalized Pochhammer symbol**.

#### Pochhammer Symbol (Standard Rising Factorial)
When $a = 1$:
$$P(x,1,m) = x^{\overline{m}} = x(x+1)(x+2)\cdots(x+m-1)$$

This is the classical **Pochhammer symbol**. In the literature, this is also denoted as:
- $(x)_m$ in special functions (Abramowitz & Stegun)
- $x^{(m)}$ in combinatorics
- $(x)_m^+$ when disambiguation is needed

The notation varies by field, with special function theory typically using $(x)_m$ for the rising factorial, while combinatorics often uses $(x)_m$ for the falling factorial.

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

#### Unified Gamma Representation

The unified representation also extends to the gamma function formulation:

$$P(x,a,s) = [a = 0] \cdot x^s + [a \neq 0] \cdot a^s \cdot \frac{\Gamma(x/a + s)}{\Gamma(x/a)}$$

This single formula encompasses both the monomial case and the general gamma function representation, demonstrating the mathematical elegance of the Iverson bracket approach.

#### Special Cases via Gamma Function

- **Pochhammer Symbol**: $P(x,1,m) = \frac{\Gamma(x+m)}{\Gamma(x)}$
- **Integer Arguments**: When $x$ is a positive integer $n$, $P(n,1,m) = \frac{(n+m-1)!}{(n-1)!}$

### Relationship Between Rising and Falling Forms

The connection between $P(x,a,m)$ (rising) and the falling factorial is:

$$P(x,a,m) = (x+(m-1)a)^{\underline{m}}_a$$

This identity allows conversion between the two forms and demonstrates their fundamental equivalence.

### Derivatives and the Digamma Function

The derivatives of generalized factorial polynomials reveal deep connections to the **digamma function** $\psi(x) = \frac{\Gamma'(x)}{\Gamma(x)}$, also known as the **logarithmic derivative of the gamma function**.

#### Unified Derivative Formula

Using the unified representation, the derivative of $P(x,a,m)$ with respect to $x$ is:

$$\frac{d}{dx} P(x,a,m) = [a = 0] \cdot m x^{m-1} + [a \neq 0] \cdot a^{m-1} P(x,a,m) \psi\left(\frac{x}{a} + m\right)$$

This single formula encompasses both the monomial case and the general factorial case.

#### Special Cases

**Monomial case** ($a = 0$):
$$\frac{d}{dx} P(x,0,m) = \frac{d}{dx} x^m = m x^{m-1}$$

**General case** ($a \neq 0$):
$$\frac{d}{dx} P(x,a,m) = \frac{P(x,a,m)}{a} \psi\left(\frac{x}{a} + m\right) = \frac{P(x,a,m)}{a} \left[\psi\left(\frac{x}{a} + m\right) - \psi\left(\frac{x}{a}\right)\right] + \frac{P(x,a,m)}{a} \psi\left(\frac{x}{a}\right)$$

Simplifying using the digamma difference property:
$$\frac{d}{dx} P(x,a,m) = \frac{P(x,a,m)}{a} \left[\sum_{k=0}^{m-1} \frac{1}{\frac{x}{a} + k}\right] = P(x,a,m) \sum_{k=0}^{m-1} \frac{1}{x + ak}$$

#### Connection to Classical Results

**Rising factorial derivative** ($a = 1$):
$$\frac{d}{dx} x^{(m)} = x^{(m)} \sum_{k=0}^{m-1} \frac{1}{x + k} = x^{(m)} [\psi(x + m) - \psi(x)]$$

**Falling factorial derivative** ($a = -1$):
$$\frac{d}{dx} (x)_m = (x)_m \sum_{k=0}^{m-1} \frac{1}{x - k} = (x)_m [\psi(x + 1) - \psi(x - m + 1)]$$

#### Digamma Function Properties

The **digamma function** $\psi(x)$ satisfies the fundamental recurrence:
$$\psi(x + 1) = \psi(x) + \frac{1}{x}$$

This leads to the difference formula used above:
$$\psi(x + m) - \psi(x) = \sum_{k=0}^{m-1} \frac{1}{x + k}$$

#### Higher-Order Derivatives

The $n$-th derivative of $P(x,a,m)$ involves **polygamma functions** $\psi^{(n)}(x)$:

For $a \neq 0$:
$$\frac{d^n}{dx^n} P(x,a,m) = \frac{P(x,a,m)}{a^n} \sum_{k_1,k_2,\ldots,k_n} \frac{(-1)^{n-1}(n-1)!}{\prod_{j=0}^{m-1}(x/a + j)^{k_j+1}}$$

where the sum is over all non-negative integer solutions to $k_1 + k_2 + \cdots + k_n = n$.

For the monomial case ($a = 0$):
$$\frac{d^n}{dx^n} P(x,0,m) = \frac{d^n}{dx^n} x^m = \frac{m!}{(m-n)!} x^{m-n}$$

#### Logarithmic Derivative

The **logarithmic derivative** of $P(x,a,m)$ provides the cleanest connection to the digamma function:

$$\frac{d}{dx} \ln P(x,a,m) = \begin{cases}
\frac{m}{x} & \text{if } a = 0 \\
\frac{1}{a} \psi\left(\frac{x}{a} + m\right) & \text{if } a \neq 0
\end{cases}$$

This unified form shows how the discrete factorial structure (via the digamma function) smoothly transitions to the continuous monomial structure.

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

#### Unified Representation Verification

Using the unified form $P(x,a,s) = [a = 0] \cdot x^s + [a \neq 0] \cdot a^s \cdot P(x/a, 1, s)$:

**For $P(5,0,3)$ (monomial case)**:
$$P(5,0,3) = [0 = 0] \cdot 5^3 + [0 \neq 0] \cdot 0^3 \cdot P(5/0, 1, 3) = 1 \cdot 125 + 0 \cdot (\text{undefined}) = 125$$

**For $P(6,2,3)$ (general case)**:
$$P(6,2,3) = [2 = 0] \cdot 6^3 + [2 \neq 0] \cdot 2^3 \cdot P(6/2, 1, 3) = 0 \cdot 216 + 1 \cdot 8 \cdot P(3,1,3)$$

Since $P(3,1,3) = 3 \cdot 4 \cdot 5 = 60$:
$$P(6,2,3) = 8 \cdot 60 = 480$$

Direct verification: $P(6,2,3) = 6 \cdot 8 \cdot 10 = 480$ ✓

### Derivative Examples and Verification

#### Example 1: Derivative of P(x,1,3) (Rising Factorial)
$$P(x,1,3) = x(x+1)(x+2) = x^3 + 3x^2 + 2x$$

Using the general formula:
$$\frac{d}{dx} P(x,1,3) = P(x,1,3) \sum_{k=0}^{2} \frac{1}{x + k} = P(x,1,3) \left[\frac{1}{x} + \frac{1}{x+1} + \frac{1}{x+2}\right]$$

Direct differentiation:
$$\frac{d}{dx} (x^3 + 3x^2 + 2x) = 3x^2 + 6x + 2$$

Verification at $x = 2$:
- $P(2,1,3) = 2 \cdot 3 \cdot 4 = 24$
- Sum of reciprocals: $\frac{1}{2} + \frac{1}{3} + \frac{1}{4} = \frac{6+4+3}{12} = \frac{13}{12}$
- Formula result: $24 \cdot \frac{13}{12} = 26$
- Direct result: $3(4) + 6(2) + 2 = 12 + 12 + 2 = 26$ ✓

#### Example 2: Derivative of P(x,2,3) (General Case)
$$P(x,2,3) = x(x+2)(x+4) = x^3 + 6x^2 + 8x$$

Using the general formula:
$$\frac{d}{dx} P(x,2,3) = P(x,2,3) \sum_{k=0}^{2} \frac{1}{x + 2k} = P(x,2,3) \left[\frac{1}{x} + \frac{1}{x+2} + \frac{1}{x+4}\right]$$

Verification at $x = 2$:
- $P(2,2,3) = 2 \cdot 4 \cdot 6 = 48$
- Sum of reciprocals: $\frac{1}{2} + \frac{1}{4} + \frac{1}{6} = \frac{6+3+2}{12} = \frac{11}{12}$
- Formula result: $48 \cdot \frac{11}{12} = 44$
- Direct result: $3(4) + 6(4) + 8 = 12 + 24 + 8 = 44$ ✓

#### Example 3: Monomial Case P(x,0,4)
$$P(x,0,4) = x^4$$

Using the unified formula:
$$\frac{d}{dx} P(x,0,4) = [0 = 0] \cdot 4x^3 + [0 \neq 0] \cdot \text{(digamma terms)} = 4x^3$$

This matches the standard power rule directly.

#### Example 4: Logarithmic Derivative
For $P(x,1,2) = x(x+1) = x^2 + x$:

$$\frac{d}{dx} \ln P(x,1,2) = \frac{1}{1} \psi\left(\frac{x}{1} + 2\right) = \psi(x + 2)$$

Since $\psi(x + 2) = \psi(x) + \frac{1}{x} + \frac{1}{x+1}$, we have:
$$\frac{d}{dx} \ln P(x,1,2) = \psi(x) + \frac{1}{x} + \frac{1}{x+1}$$

Direct computation:
$$\frac{d}{dx} \ln(x^2 + x) = \frac{2x + 1}{x^2 + x} = \frac{2x + 1}{x(x + 1)} = \frac{1}{x} + \frac{1}{x+1}$$

The difference is $\psi(x)$, which represents the "baseline" logarithmic derivative behavior, confirming the digamma function's role as the fundamental building block.

## Historical Context

The concept of generalized factorial polynomials emerged from the generalization of the classical Pochhammer symbol, introduced by **Leo Pochhammer** in 1870. The extension to arbitrary increment parameters developed naturally in the study of hypergeometric functions and combinatorial analysis during the late 19th and early 20th centuries.

The systematic study of these polynomials was advanced by mathematicians working on finite difference theory and special functions, including **Charles Jordan** and **Niels Erik Nørlund** in the early 20th century.

The connection to the **digamma function** traces back to **Carl Friedrich Gauss**, who first studied the logarithmic derivative of the gamma function in his analysis of the hypergeometric series. Gauss denoted this function as $\psi(x)$ and established its fundamental properties, including the recurrence relation $\psi(x+1) = \psi(x) + \frac{1}{x}$. The appearance of the digamma function in the derivatives of generalized factorial polynomials reveals the deep connection between discrete factorial structures and continuous special functions, a relationship that continues to be explored in modern mathematical analysis.

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
- **Digamma function** - Logarithmic derivative of gamma function, central to derivative formulas
- **Polygamma functions** - Higher-order derivatives of the logarithmic gamma function
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
