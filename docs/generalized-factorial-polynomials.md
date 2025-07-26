# Generalized Factorial Polynomials

**Generalized factorial polynomials** are mathematical expressions that extend the concept of factorial functions to include a parameter that generalizes the increment between consecutive terms. These polynomials arise naturally in various areas of mathematics, including combinatorics, the theory of special functions, and finite difference calculus.

## Definition

Generalized factorial polynomials are defined in two primary forms: **rising** and **falling** factorials.

### Generalized Rising Factorials

The **generalized rising factorial** (also called the **generalized Pochhammer symbol**) is denoted as $x^{\overline{m}}_a$ or $(x)_{m,a}$ and is defined as:

$$x^{\overline{m}}_a = x(x+a)(x+2a)\cdots(x+(m-1)a)$$

where:
- $x$ is a real or complex variable
- $m$ is a non-negative integer
- $a$ is a non-zero constant (the **increment parameter**)

### Generalized Falling Factorials

The **generalized falling factorial** is denoted as $x^{\underline{m}}_a$ or $(x)_m^a$ and is defined as:

$$x^{\underline{m}}_a = x(x-a)(x-2a)\cdots(x-(m-1)a)$$

with the same parameter constraints as the rising factorial.

### Special Cases

When $a = 1$, these reduce to the standard rising and falling factorials:
- $x^{\overline{m}}_1 = x^{\overline{m}} = x(x+1)(x+2)\cdots(x+m-1)$ (Pochhammer symbol)
- $x^{\underline{m}}_1 = x^{\underline{m}} = x(x-1)(x-2)\cdots(x-m+1)$ (falling factorial)

When $m = 0$, both forms equal 1 by convention.

## Properties and Identities

### Relationship Between Rising and Falling Forms

The generalized rising and falling factorials are related by the identity:

$$x^{\overline{m}}_a = (x+(m-1)a)^{\underline{m}}_a$$

This relationship allows conversion between the two forms.

### Connection to the Gamma Function

For complex arguments, generalized factorial polynomials can be expressed using the gamma function:

$$x^{\overline{m}}_a = a^m \frac{\Gamma(x/a + m)}{\Gamma(x/a)}$$

$$x^{\underline{m}}_a = a^m \frac{\Gamma(x/a + 1)}{\Gamma(x/a - m + 1)}$$

These expressions extend the definition to non-integer values of $m$.

### Recurrence Relations

Both forms satisfy simple recurrence relations:

$$x^{\overline{m+1}}_a = x^{\overline{m}}_a \cdot (x + ma)$$

$$x^{\underline{m+1}}_a = x^{\underline{m}}_a \cdot (x - ma)$$

## Examples

### Generalized Rising Factorial Example

For $x^{\overline{3}}_2$ with $x = 5$:
$$5^{\overline{3}}_2 = 5 \cdot (5+2) \cdot (5+4) = 5 \cdot 7 \cdot 9 = 315$$

### Generalized Falling Factorial Example

For $x^{\underline{4}}_3$ with $x = 10$:
$$10^{\underline{4}}_3 = 10 \cdot (10-3) \cdot (10-6) \cdot (10-9) = 10 \cdot 7 \cdot 4 \cdot 1 = 280$$

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

- Pochhammer symbol
- Gamma function
- Hypergeometric function
- Finite difference
- Factorial

## References

1. Jordan, C. (1939). *Calculus of Finite Differences*. Hungarian Academy of Sciences.
2. Nørlund, N. E. (1924). *Vorlesungen über Differenzenrechnung*. Springer-Verlag.
3. Rainville, E. D. (1960). *Special Functions*. Macmillan Company.
4. Graham, R. L., Knuth, D. E., & Patashnik, O. (1994). *Concrete Mathematics* (2nd ed.). Addison-Wesley.
