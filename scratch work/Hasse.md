# The Hasse Operator and Hasse Coefficients

## Historical Context

The **Hasse operator** is named after Helmut Hasse (1898-1979), a prominent German mathematician who made significant contributions to algebraic number theory, class field theory, and the application of p-adic methods. He is particularly known for his fundamental work on quadratic forms, where he established the "Hasse principle" (also known as the local-global principle) which connects the solvability of equations over global fields to their solvability over local fields. His work on quadratic forms helped bridge abstract algebra and number theory, leading to significant advances in both fields.

Despite his mathematical brilliance, Hasse faced discrimination during the Nazi era due to having Jewish ancestry. He had hoped to retain his position and continue his work at the University of Göttingen, a center for mathematical excellence at the time. To do so, he applied for membership in the Nazi Party, a step many academics took under pressure to protect their careers. However, his application was rejected due to his grandfather's Jewish background, leading to his removal from Göttingen and relocation to lesser positions. His story is a poignant example of the tragic impact of Nazi racial policies on scientific progress and the mathematical community.

## Definition of Hasse Coefficients

The **Hasse coefficients** are defined as modified binomial coefficients:

$$H_{m,n} = \frac{(-1)^n \binom{m}{n}}{m+1}$$

where $\binom{m}{n}$ is the standard binomial coefficient representing "m choose n."

For clarity, expanded in terms of factorials:

$$H_{m,n} = \frac{(-1)^n}{m+1} \cdot \frac{m!}{n!(m-n)!}$$

## Properties of Hasse Coefficients

### Basic Properties

1. **Domain**: $H_{m,n}$ is defined for $0 \leq n \leq m$
2. **Alternating Signs**: The coefficient alternates sign based on $n$
3. **Normalization**: The sum $\sum_{n=0}^{m} H_{m,n} = 0$ for $m \geq 1$

#### Proof of the Normalization Property

For $m = 0$, we have $H_{0,0} = 1$, so $\sum_{n=0}^{0} H_{0,n} = 1$.

For $m \geq 1$, we can compute:
$$\sum_{n=0}^{m} H_{m,n} = \sum_{n=0}^{m} \frac{(-1)^n \binom{m}{n}}{m+1} = \frac{1}{m+1} \sum_{n=0}^{m} (-1)^n \binom{m}{n}$$

The sum $\sum_{n=0}^{m} (-1)^n \binom{m}{n}$ is the binomial expansion of $(1-1)^m$, which equals 0 for $m \geq 1$. Therefore:
$$\sum_{n=0}^{m} H_{m,n} = \frac{1}{m+1} \cdot 0 = 0 \quad \text{for } m \geq 1$$

This property is crucial for understanding the behavior of the Hasse operator on constant functions.

### Table of Hasse Coefficients

Below is a table showing the values of $H_{m,n}$ for small values of $m$ and $n$:

| $m\backslash n$ | 0 | 1 | 2 | 3 | 4 |
|-----------------|---|---|---|---|---|
| 0 | 1 | - | - | - | - |
| 1 | 1/2 | -1/2 | - | - | - |
| 2 | 1/3 | -2/3 | 1/3 | - | - |
| 3 | 1/4 | -3/4 | 3/4 | -1/4 | - |
| 4 | 1/5 | -4/5 | 6/5 | -4/5 | 1/5 |

*Table 1: Values of Hasse coefficients $H_{m,n}$ showing the alternating pattern and row-sum property*

Notice the alternating pattern within each row and that the sum of each row (except for $m=0$) is zero, confirming the normalization property.

### Recursive Relation

The Hasse coefficients satisfy the recurrence relation:

$$H_{m+1,n} = H_{m,n-1} - \frac{m+1-n}{m+2} \cdot H_{m,n}$$

for $1 \leq n \leq m+1$, with boundary conditions $H_{m,0} = \frac{1}{m+1}$.

## The Hasse Derivative Operator

These coefficients are not just an interesting mathematical curiosity; they form the basis for a powerful generalization of the standard derivative, known as the **Hasse derivative**.

The **Hasse derivative**, also known as the hyperderivative, is a generalization of the standard derivative that maintains many important properties while being better suited for certain algebraic contexts.

For a polynomial $p(x) = \sum_{k=0}^{d} a_k x^k$, the Hasse derivative of order $n$ is defined as:

$$D^{(n)}p(x) = \sum_{k=n}^{d} \binom{k}{n} a_k x^{k-n}$$

Using the Hasse coefficients, we can define a normalized Hasse operator $\mathcal{H}_m$ that acts on polynomials:

$$\mathcal{H}_m(p)(x) = \sum_{n=0}^{m} H_{m,n} x^{m-n} p^{(n)}(x)$$

where $p^{(n)}(x)$ is the $n$-th derivative of $p(x)$.

## The Hasse Shift Operator

In addition to the derivative form, we can define another important version of the **Hasse operator** that acts on functions by evaluating them at shifted points:

$$\mathcal{H}_m(f)(x) = \sum_{n=0}^{m} H_{m,n} f(x+n)$$

This operator has remarkable properties when applied to certain families of functions.

### Interpretation as a Weighted Average

The Hasse shift operator can be interpreted as a special type of weighted average. For a function $f(x)$, the operator $\mathcal{H}_m(f)(x)$ computes a weighted average of the values $f(x), f(x+1), ..., f(x+m)$ with weights given by the Hasse coefficients $H_{m,n}$.

This interpretation has several interesting properties:

1. **Non-standard weights**: Unlike typical weighted averages where all weights are positive and sum to 1, the Hasse shift operator uses weights that alternate in sign and sum to:
   - 1 when $m=0$ (a standard average)
   - 0 when $m \geq 1$ (a "balanced" or "centered" average)

2. **Balanced average properties**: For $m \geq 1$, because the weights sum to zero, the operator annihilates constant functions. This property makes it behave like a discrete differential operator, extracting information about the rate of change rather than the absolute value.

3. **Connection to finite differences**: The Hasse shift operator shares similarities with finite difference formulas, which can also be viewed as weighted averages with alternating weights that sum to zero.

This weighted average perspective helps explain why the Hasse operator is so effective at extracting meaningful patterns from functions, particularly polynomial and exponential functions, while maintaining useful algebraic properties.

### Special Properties of the Hasse Shift Operator

1. **Linearity**: The operator is linear, i.e., $\mathcal{H}_m(\alpha f + \beta g) = \alpha \mathcal{H}_m(f) + \beta \mathcal{H}_m(g)$

2. **Action on Exponential Functions**: When applied to exponential functions, the operator has interesting properties that connect to logarithmic functions

3. **Generating Function Relationship**: The sequence $\{\mathcal{H}_m(f)(x)\}_{m=0}^{\infty}$ has a generating function that often simplifies in remarkable ways

4. **Connection to Difference Calculus**: The Hasse shift operator provides a bridge between differential and difference calculus

### The Hasse Operator Applied to Constants

When we apply the Hasse shift operator to a constant function $f(x) = c$, each term in the sum becomes:

$$\mathcal{H}_m(c) = \sum_{n=0}^{m} H_{m,n} \cdot c = c \sum_{n=0}^{m} H_{m,n}$$

Using the normalization property:
- For $m = 0$: $\mathcal{H}_0(c) = c \cdot 1 = c$
- For $m \geq 1$: $\mathcal{H}_m(c) = c \cdot 0 = 0$

Therefore, when we sum over all $m$:

$$\sum_{m=0}^{\infty} \mathcal{H}_m(c) = \mathcal{H}_0(c) + \sum_{m=1}^{\infty} \mathcal{H}_m(c) = c + 0 = c$$

This demonstrates an important property: **The infinite sum of the Hasse operator applied to a constant is the constant itself**. This is a fundamental property that distinguishes the behavior of the Hasse operator from other differential operators.

## Applications

### 1. Algebraic Geometry

The Hasse derivative is particularly useful in algebraic geometry over fields of positive characteristic, where the standard derivative can behave poorly (e.g., the derivative of $x^p$ in characteristic $p$ is zero).

### 2. Number Theory

In number theory, the Hasse operator appears in the study of:
- Formal group laws
- Elliptic curves
- Local zeta functions

### 3. Combinatorial Identities

The Hasse coefficients relate to various combinatorial sums and identities, including:

$$\sum_{n=0}^{m} H_{m,n} \binom{x+n}{n} = \frac{x}{m+1} \binom{x+m}{m}$$

### 4. Connection to Stirling Numbers

There is a natural connection between Hasse coefficients and generalized Stirling numbers through umbral calculus. The Hasse coefficients can be seen as a specific case of a more general family of coefficients that include Stirling numbers.

## Examples

### Example 1: Computing Hasse Coefficients

For $m = 3$:

$$H_{3,0} = \frac{1}{4} \cdot \binom{3}{0} = \frac{1}{4}$$

$$H_{3,1} = \frac{-1}{4} \cdot \binom{3}{1} = \frac{-3}{4}$$

$$H_{3,2} = \frac{1}{4} \cdot \binom{3}{2} = \frac{3}{4}$$

$$H_{3,3} = \frac{-1}{4} \cdot \binom{3}{3} = \frac{-1}{4}$$

Notice that $\sum_{n=0}^{3} H_{3,n} = \frac{1}{4} - \frac{3}{4} + \frac{3}{4} - \frac{1}{4} = 0$, confirming the normalization property.

### Example 2: Hasse Operator Applied to a Polynomial

Let's apply the Hasse operator $\mathcal{H}_2$ to the polynomial $p(x) = x^3$:

$$\mathcal{H}_2(x^3) = H_{2,0} \cdot x^2 \cdot (x^3) + H_{2,1} \cdot x^1 \cdot (3x^2) + H_{2,2} \cdot x^0 \cdot (6x)$$

$$= \frac{1}{3} \cdot x^2 \cdot x^3 - \frac{2}{3} \cdot x \cdot 3x^2 + \frac{1}{3} \cdot 6x$$

$$= \frac{1}{3} x^5 - 2x^3 + 2x$$

### Example 3: Hasse Shift Operator Applied to a Linear Function

Let's apply the Hasse shift operator to $f(x) = ax + b$:

$$\mathcal{H}_2(ax + b) = H_{2,0} \cdot (a(x+0) + b) + H_{2,1} \cdot (a(x+1) + b) + H_{2,2} \cdot (a(x+2) + b)$$

$$= \frac{1}{3} \cdot (ax + b) - \frac{2}{3} \cdot (ax + a + b) + \frac{1}{3} \cdot (ax + 2a + b)$$

$$= \frac{1}{3}(ax + b) - \frac{2}{3}(ax + a + b) + \frac{1}{3}(ax + 2a + b)$$

$$= ax + b - \frac{2a}{3}$$

$$= a \cdot x + b - \frac{2a}{3}$$

$$= a \cdot (x - \frac{2}{3}) + b$$

This shows that the Hasse shift operator shifts the linear function to the left by $\frac{2}{3}$ without changing its slope.

### Example 4: Applying the Infinite Sum of Hasse Operators

Let's examine the effect of applying the infinite sum of Hasse shift operators to simple functions:

1. For a constant $f(x) = 5$:
   $$\sum_{m=0}^{\infty} \mathcal{H}_m(5) = 5$$
   This confirms our theoretical result for constants.

2. For a linear function $f(x) = 2x + 3$:
   First, note that $\mathcal{H}_0(2x + 3) = 2x + 3$
   For $m = 1$: $\mathcal{H}_1(2x + 3) = \frac{1}{2}(2x + 3) - \frac{1}{2}(2(x+1) + 3) = \frac{1}{2}(2x + 3) - \frac{1}{2}(2x + 5) = -1$
   
   The sum continues with terms that form a geometric series, resulting in a closed-form expression.

### Example 5: Hasse Operator Applied to the Logarithmic Function

Let's apply the Hasse shift operator to $f(x) = \log(1+x)$:

For $m = 0$:
$$\mathcal{H}_0(\log(1+x)) = \log(1+x)$$

For $m = 1$:
$$\mathcal{H}_1(\log(1+x)) = \frac{1}{2}\log(1+x) - \frac{1}{2}\log(1+(x+1))$$
$$= \frac{1}{2}\log\left(\frac{1+x}{2+x}\right) = \frac{1}{2}\log\left(1-\frac{1}{2+x}\right)$$

For $m = 2$:
$$\mathcal{H}_2(\log(1+x)) = \frac{1}{3}\log(1+x) - \frac{2}{3}\log(2+x) + \frac{1}{3}\log(3+x)$$
$$= \frac{1}{3}\log\left(\frac{(1+x)(3+x)}{(2+x)^2}\right)$$

Applying the full Hasse operator:
$$\mathcal{H}(\log(1+x)) = \sum_{m=0}^{\infty}\mathcal{H}_m(\log(1+x))$$

This sum relates directly to the digamma function $\psi(x)$, which is the logarithmic derivative of the gamma function. Specifically:

$$\mathcal{H}(\log(1+x)) = \psi(x+1) + \gamma$$

where $\gamma$ is the Euler-Mascheroni constant.

This connection arises because the digamma function satisfies:
$$\psi(x+1) - \psi(x) = \frac{1}{x}$$

And when computing $\mathcal{H}_m(\log(1+x))$, we're effectively calculating higher-order differences of logarithms, which correspond to specific combinations of reciprocals that relate to the digamma function.

This example demonstrates how the Hasse operator naturally connects elementary functions to special functions in analysis and number theory.

## The Umbral Nature of Hasse Operators

The Hasse operator can be understood within the broader framework of **umbral calculus**, a powerful mathematical approach that formalizes operations with "shadowy" quantities in polynomial sequences. This perspective reveals deeper connections between the Hasse operator and other fundamental operators in mathematics.

### Umbral Operators and Polynomial Sequences

In umbral calculus, we consider polynomial sequences $\{p_n(x)\}_{n\geq 0}$ where $\deg(p_n) = n$. An umbral operator acts on these sequences through specific evaluation and shifting rules. The Hasse operator fits naturally into this framework as it transforms the standard monomial basis into the Bernoulli polynomial basis.

The key insight is that we can view the Hasse operator as an umbral shift operator with respect to a specific measure or "weight sequence." Specifically:

$$\mathcal{H}_m(x^n) = \frac{B_{n,m}(x)}{n!}$$

where $B_{n,m}(x)$ represents a generalized Bernoulli polynomial. This interpretation connects the Hasse operator to the broader theory of Sheffer sequences and umbral composition.

### Differential Operators vs. Hasse Operators

While both differential operators and Hasse operators provide ways to analyze functions, they differ in several fundamental aspects:

1. **Domain of Applicability**: 
   - Differential operators require smoothness conditions
   - Hasse operators can be applied to functions in discrete settings and in fields of positive characteristic

2. **Algebraic Properties**:
   - The standard differential operator $D$ satisfies the Leibniz rule: $D(fg) = (Df)g + f(Dg)$
   - The Hasse derivative satisfies a modified Leibniz rule: $D^{(n)}(fg) = \sum_{k=0}^{n} \binom{n}{k} D^{(k)}(f) \cdot D^{(n-k)}(g)$

3. **Behavior in Positive Characteristic**:
   - The standard derivative of $x^p$ in characteristic $p$ is zero
   - The Hasse derivative maintains non-trivial information: $D^{(1)}(x^p) = \binom{p}{1}x^{p-1} = p \cdot x^{p-1} \equiv 0 \pmod{p}$, but $D^{(k)}(x^p) \neq 0$ for $1 < k < p$

### Umbral Composition and Operator Algebra

The Hasse operator can be expressed in terms of the forward difference operator $\Delta$ and the shift operator $E$ through umbral composition:

$$\mathcal{H}_m = \frac{1}{m+1} \sum_{k=0}^{m} (-1)^k \binom{m}{k} E^k$$

where $E^k f(x) = f(x+k)$. This representation connects the Hasse operator to the broader operator algebra of discrete calculus.

Furthermore, the Hasse operator satisfies the operational identity:

$$\mathcal{H}_m(x^n) = \begin{cases}
0 & \text{if } m > n \\
\text{non-zero polynomial} & \text{if } m \leq n
\end{cases}$$

This property resembles the evaluation functional in umbral calculus, further cementing the umbral nature of the Hasse operator.

### Applications in Combinatorial Identities

The umbral perspective provides elegant proofs of combinatorial identities involving the Hasse coefficients. For example, the identity:

$$\sum_{n=0}^{m} H_{m,n} \binom{x+n}{n} = \frac{x}{m+1} \binom{x+m}{m}$$

can be proved through umbral methods by considering the action of the Hasse operator on the falling factorial $(x)_n$.

Similarly, connections to Stirling numbers arise naturally through the umbral framework, as both Hasse coefficients and Stirling numbers can be viewed as connection coefficients between different polynomial bases.

### Generalized Factorial Functions

This umbral perspective also illuminates the connection between the Hasse operator and generalized factorial functions. The rising factorial $(x|\alpha)^{\overline{n}}$ (also denoted as $P(x, \alpha, n)$ in some literature) can be analyzed using Hasse operators to reveal structural properties and combinatorial interpretations.

In particular, the Hasse operator provides a natural framework for studying how these generalized factorial functions relate to classical special functions and combinatorial sequences.

## Homework Problems

### Problem 1: Exponential Functions and the Hasse Shift Operator

Show that when the Hasse shift operator is applied to the exponential function $f(x) = a^{tx}$, the infinite sum of all orders gives:

$$\sum_{m=0}^{\infty} \mathcal{H}_m(a^{tx}) = \frac{\log(a^t) \cdot a^{tx}}{a^t-1}$$

**Hint**: The sum $\sum_{m=0}^{\infty} \mathcal{H}_m(a^{tx})$ can be evaluated by first finding $\mathcal{H}_m(a^{tx})$ for specific values of $m$ and then recognizing the resulting infinite sum as the exponential generating function of the Bernoulli numbers, which is $\frac{z}{e^z-1}$. A change of variables will lead to the desired formula.

**Special Case**: What happens when $a = e$, where $e$ is the base of the natural logarithm?

When $a = e$, the formula becomes:
$$\sum_{m=0}^{\infty} \mathcal{H}_m(e^{tx}) = \frac{t \cdot e^{tx}}{e^t-1}$$

This special case reveals a connection to the generating function of Bernoulli numbers and the Riemann zeta function. Explore how this simplification relates to classical mathematical constants.

**Additional Hint**: Consider the connection to the polylogarithm function.

The polylogarithm function defined as $\text{Li}_s(z) = \sum_{k=1}^{\infty} \frac{z^k}{k^s}$ provides insight into this problem. When analyzing the Hasse shift operator applied to exponential functions, you may rewrite certain expressions in terms of polylogarithms, particularly for $s=1$ (which relates to the natural logarithm). This perspective can lead to an elegant proof using the functional equations satisfied by polylogarithms.

### Problem 2: Hasse Shift Operator and Polynomial Functions

Prove that for any polynomial $p(x)$ of degree $d$, the Hasse shift operator satisfies:

$$\mathcal{H}_m(p)(x) = 0 \quad \text{for all } m > d$$

### Problem 3: Connection to Stirling Numbers

Explore the relationship between the Hasse coefficients and Stirling numbers by proving:

$$\sum_{n=0}^{m} H_{m,n} \cdot S(n,k) = \frac{(-1)^{m-k}}{m+1} \binom{m}{k} \quad \text{for } 0 \leq k \leq m$$

where $S(n,k)$ is the Stirling number of the second kind.

### Problem 4: Hasse Operator and Bernoulli Polynomials

Show that the m-th Bernoulli polynomial $B_m(x)$ can be obtained by applying the Hasse operator to the power function $x^m$:

$$B_m(x) = \mathcal{H}(x^m)$$

**Hint**: Apply the Hasse operator to the exponential generating function $e^{tx}$ and compare with the generating function for Bernoulli polynomials:

$$\frac{te^{xt}}{e^t-1} = \sum_{m=0}^{\infty} B_m(x) \frac{t^m}{m!}$$

The result follows immediately from comparing coefficients of $t^m$.

### Problem 5: The Hasse Operator Applied to 1/x

Investigate the behavior of the full Hasse shift operator applied to the function $f(x) = 1/x = x^{-1}$:

$$\mathcal{H}(1/x) = \sum_{m=0}^{\infty} \mathcal{H}_m(1/x) = \sum_{m=0}^{\infty} \sum_{n=0}^{m} H_{m,n} \frac{1}{x+n}$$

Determine whether this series converges, and if so, find its closed form. Discuss any interesting analytical properties or relationships to special functions.

**Hint**: Consider partial fractions decomposition and the relationship between this sum and the digamma function $\psi(x)$, which is the logarithmic derivative of the gamma function.

### Problem 6: The Hasse Operator and Parametrized Powers

Examine the effect of the Hasse shift operator on the parametrized power function $f(x) = x^{1-t}$ for a parameter $t$:

$$\mathcal{H}_m(x^{1-t}) = \sum_{n=0}^{m} H_{m,n} (x+n)^{1-t}$$

Find a closed form for the full Hasse operator:

$$\mathcal{H}(x^{1-t}) = \sum_{m=0}^{\infty} \mathcal{H}_m(x^{1-t})$$

Discuss how this result varies with different values of the parameter $t$, and identify any connections to known special functions.

**Hint**: First, rewrite the power function in exponential form:
$$x^{1-t} = \exp((1-t)\log(x))$$

Now you can leverage the results from Problem 1 about how the Hasse operator acts on exponential functions. This transformation connects the problem to the Hurwitz zeta function and generalized harmonic numbers, especially for integer values of $t$.

### Problem 7: The Hasse Operator and Powers of Logarithms

Investigate the effect of applying the full Hasse shift operator to powers of the natural logarithm function:

$$\mathcal{H}([\log(1+x)]^k) = \sum_{m=0}^{\infty} \mathcal{H}_m([\log(1+x)]^k)$$

where $k$ is a positive integer. Find a closed form expression for this sum, and explore how it connects to the polylogarithm and other special functions.

**Hint**: You may approach this problem in two ways:

1. Express $[\log(1+x)]^k$ using its Taylor series, then apply the Hasse operator term by term.

2. For specific values of $k$, first compute $\mathcal{H}_m([\log(1+x)]^k)$ directly, identify patterns, and then generalize.

Note that the result relates to special values of the polylogarithm function and Stirling numbers of the first kind, which count permutations by their cycle structure.

### Problem 8: Polygamma Functions and Powers of Logarithms

Building on Problem 7, establish the precise relationship between the polygamma function ψ^(n)(x) and the Hasse operator applied to powers of logarithms:

$$\mathcal{H}([\log(1+x)]^k) = (-1)^k \sum_{j=0}^{k-1} c_j \cdot \psi^{(j)}(x+1)$$

where c_j are specific constants that depend on k and j.

**Hint**: Begin with the result from Problem 6 that:

$$(s-1) \cdot \zeta(s,x) = \mathcal{H}(x^{1-s})$$

where ζ(s,x) is the Hurwitz zeta function. Then use the known relationship between the polygamma function and the Hurwitz zeta function:

$$\psi^{(n)}(x) = (-1)^{n+1} n! \cdot \zeta(n+1,x)$$

To solve this problem, you'll need to express $[\log(1+x)]^k$ in terms of appropriate derivatives or transformations of $x^{1-s}$ for specific values of s, and then apply the Hasse operator to establish the connection with polygamma functions.

**Additional Challenge**: Determine the exact values of the coefficients c_j for small values of k (e.g., k=1, 2, 3) and identify any patterns that emerge.

## Conclusion

The **Hasse coefficients** and the associated **Hasse operators** provide a powerful framework for studying polynomials and their derivatives, especially in contexts where the standard derivative has limitations. Their connection to combinatorial identities and number theory makes them a valuable tool in the broader context of generalized Stirling numbers and factorial functions.

## References

1. Hasse, H. "Theorie der höheren Differentiale in einem algebraischen Funktionenkörper mit vollkommenem Konstantenkörper bei beliebiger Charakteristik." Journal für die reine und angewandte Mathematik, 175:50-54, 1936.

2. Scherk, P. "The Hasse derivative and characteristic p." American Mathematical Monthly, 80:1, 1973.

3. Johnson, W.P. "The Curious History of Faà di Bruno's Formula." American Mathematical Monthly, 109:217-234, 2002.

4. Roman, S. "The Umbral Calculus." Dover Publications, 2005.
