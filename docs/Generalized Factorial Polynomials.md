***

# Generalized Factorial Polynomials

In mathematics, a **generalized factorial polynomial**, also known as a **generalized rising factorial** or **generalized Pochhammer symbol**, is a polynomial function that extends the concepts of the factorial, rising factorial, and falling factorial. These polynomials form a basis for the vector space of all polynomials and are fundamental in combinatorics, finite difference calculus, and the theory of special functions.

## Definition

The generalized factorial polynomial of degree $m$ with increment parameter $a$ is defined as the product:

$$P_m(x; a) = \prod_{k=0}^{m-1}(x+ka) = x(x+a)(x+2a)\cdots(x+(m-1)a)$$

with the base case $P_0(x; a) = 1$ by convention as an empty product. The variable $x$ and the increment parameter $a$ can be any complex numbers.

### Naming and Notation

The notation $P_m(x; a)$ is a clear and unambiguous way to denote the generalized factorial polynomial, explicitly listing the variable, degree, and increment parameter. Other notations for these polynomials include:

* **Pochhammer Symbol**: The rising factorial, or Pochhammer symbol, is a special case with $a=1$, and is denoted by $(x)_m$. This is the most common notation for this specific case.
* **Falling Factorial**: The falling factorial, with increment $a=-1$, is denoted by $x^{(m)}$ or $(x)_m$.
* **Generalized Pochhammer**: Some sources use the notation $(x)_m^a$ or $(x;a)_m$.

For a general audience, using a notation like $P_m(x;a)$ and explicitly defining it is the most transparent approach.

## Special Cases

The generalized factorial polynomial encompasses several important classical functions as special cases:

* **Rising Factorial (Pochhammer Symbol)**: When the increment is $a=1$, the polynomial becomes the rising factorial, a staple of special function theory.
    $$P_m(x; 1) = x(x+1)\cdots(x+m-1) = (x)_m$$
* **Falling Factorial**: When the increment is $a=-1$, the polynomial becomes the falling factorial, which is central to finite difference calculus.
    $$P_m(x; -1) = x(x-1)\cdots(x-m+1) = x^{\underline{m}}$$
* **Monomial**: When the increment is $a=0$, the product collapses to a simple power of $x$. This case is crucial for connecting to the standard polynomial basis.
    $$P_m(x; 0) = x \cdot x \cdots x = x^m$$
* **Factorial**: Evaluating the rising factorial at $x=1$ or the falling factorial at $x=m$ yields the standard factorial function.
    $$P_m(1; 1) = m! \quad \text{and} \quad P_m(m; -1) = m!$$

## Properties

* **Recursion Relation**: The polynomial of degree $m+1$ can be easily expressed in terms of the polynomial of degree $m$:
    $$P_{m+1}(x; a) = (x+ma) \cdot P_m(x; a)$$
* **Derivative and Finite Difference**: The generalized factorial polynomial is a natural basis for finite difference calculus. The forward difference operator, $\Delta_a f(x) = f(x+a)-f(x)$, has a simple effect on these polynomials, analogous to the derivative in standard calculus:
    $$\Delta_a P_m(x; a) = m \cdot a \cdot P_{m-1}(x; a)$$
* **Scaling Property**: The polynomials exhibit a simple scaling behavior, which is essential for understanding the generalized Stirling transfer coefficients.
    $$P_m(x; a) = a^m \cdot P_m\left(\frac{x}{a}; 1\right)$$
    This property shows that any generalized factorial polynomial is a scaled version of a rising factorial.

## Applications

* **Polynomial Bases**: The set of generalized factorial polynomials $\{P_0(x; a), P_1(x; a), \dots, P_n(x; a)\}$ forms a basis for the vector space of all polynomials of degree at most $n$. This property makes them useful for representing and manipulating polynomials in different contexts.
* **Connection Coefficients**: The coefficients for converting between different generalized factorial polynomial bases are the subject of generalized Stirling transfer coefficients, which find applications across combinatorics and special function theory.
* **Combinatorial identities**: The properties of these polynomials are used to derive and prove a variety of combinatorial identities, particularly those involving binomial coefficients and Stirling numbers.

## See also

* Rising factorial
* Falling factorial
* Stirling numbers
* Pochhammer symbol
* Finite difference calculus