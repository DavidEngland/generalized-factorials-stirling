# On the Analytic Properties of a Generalized Binomial Function

## Abstract

This paper introduces and analyzes the properties of a generalized binomial function, denoted $\mathrm{Bi}(s,t)$, defined for complex variables $s$ and $t$ through an infinite product representation. We derive the function's total differential, revealing a fundamental connection to the digamma function, $\psi(z)$. This differential structure governs the function's analytic behavior, including the location of its poles and zeros. We establish that for arguments on the positive integer lattice, $\mathrm{Bi}(s,t)$ is identical to the classical binomial coefficient, satisfying Pascal's recurrence relation. This correspondence provides the basis for its analytic continuation to the entire complex plane, which is formally expressed through the Gamma function. The resulting function, $\mathrm{Bi}(s,t) = \Gamma(s+1) / (\Gamma(t+1)\Gamma(s-t+1))$, stands as a robust and analytically tractable generalization of a cornerstone combinatorial object, possessing a rich analytic structure governed by classical special functions.

---

## 1. Introduction

The classical binomial coefficient, $\binom{n}{k}$, is a fundamental object in combinatorics, representing the number of ways to choose $k$ elements from a set of $n$ elements. While its definition is inherently discrete, the desire to extend its domain to real and complex variables has motivated various generalizations. This paper investigates the analytic properties of one such generalization, a function $\mathrm{Bi}(s,t)$ of two complex variables, $s$ and $t$. This function is defined from first principles by the infinite product:

$$\mathrm{Bi}(s,t) = \prod_{n=1}^\infty \frac{(t+n)(s-t+n)}{(s+n)n}$$

The primary objective of this paper is to systematically derive the analytic properties of $\mathrm{Bi}(s,t)$. We will demonstrate how this infinite product definition leads naturally to a differential form involving the digamma function, which in turn illuminates the function's analytic structure. The analysis will culminate in showing that $\mathrm{Bi}(s,t)$ not only reduces to the classical binomial coefficient for positive integer arguments but also possesses a compact and elegant representation in terms of the Gamma function. This investigation proceeds by first deriving the function's differential, then characterizing its analytic structure and special values, establishing its relationship to the classical binomial coefficient, and finally formalizing its analytic continuation.

## 2. The Differential in Terms of the Digamma Function

A powerful method for understanding the analytic nature of a function defined by a product or series is to analyze its differential. The rate of change of a function with respect to its variables often reveals deep connections to other well-understood mathematical structures. This section derives the partial derivatives and total differential of $\mathrm{Bi}(s,t)$ to uncover its fundamental relationship with the digamma function, a key special function in complex analysis.

### 2.1. Derivation of the Total Differential

To analyze the differential of $\mathrm{Bi}(s,t)$, it is advantageous to first consider its logarithm, which transforms the infinite product into an infinite sum:

$$\log \mathrm{Bi}(s,t) = \sum_{n=1}^\infty \left[ \log(t+n) + \log(s-t+n) - \log(s+n) - \log n \right]$$

Differentiating this expression term-by-term yields the total differential of the logarithm:

$$d\,\log \mathrm{Bi}(s,t) = \sum_{n=1}^\infty \left(\frac{dt}{t+n} + \frac{ds - dt}{s-t+n} - \frac{ds}{s+n} \right)$$

From this expression, we can extract the partial derivatives with respect to $s$ and $t$ by collecting the $ds$ and $dt$ terms, respectively.

* **Partial Derivative with respect to $s$:**  
  $$\frac{\partial}{\partial s} \log \mathrm{Bi}(s,t) = \sum_{n=1}^\infty \left( \frac{1}{s-t+n} - \frac{1}{s+n} \right)$$
  
* **Partial Derivative with respect to $t$:**  
  $$\frac{\partial}{\partial t} \log \mathrm{Bi}(s,t) = \sum_{n=1}^\infty \left( \frac{1}{t+n} - \frac{1}{s-t+n} \right)$$

### 2.2. Representation via the Digamma Function

The infinite sums defining the partial derivatives have a known closed-form representation involving the digamma function, $\psi(z)$, which is the logarithmic derivative of the Gamma function. The relevant identity connecting such sums to the digamma function is:

$$\psi(a) - \psi(b) = \sum_{k=0}^\infty \left( \frac{1}{k+b} - \frac{1}{k+a} \right)$$

By shifting the index of summation ($k=n-1$), our partial derivative sums can be cast into this form.

* **Partial Derivative with respect to $s$:** The sum becomes $\sum_{k=0}^\infty (1/(s-t+1+k) - 1/(s+1+k))$. Applying the identity with $a = s+1$ and $b = (s+1)-t$ yields:  
  $$\frac{\partial}{\partial s} \log \mathrm{Bi}(s,t) = \psi(s+1) - \psi\bigl((s+1)-t\bigr)$$
  
* **Partial Derivative with respect to $t$:** The sum becomes $\sum_{k=0}^\infty (1/(t+1+k) - 1/(s-t+1+k))$. Applying the identity with $a = t+1$ and $b = (s+1)-t$ yields:  
  $$\frac{\partial}{\partial t} \log \mathrm{Bi}(s,t) = \psi\bigl((s+1)-t\bigr) - \psi(t+1)$$

Synthesizing these results, we obtain a compact and elegant expression for the total differential of $\log \mathrm{Bi}(s,t)$:

$$d\,\log \mathrm{Bi}(s,t) = \bigl[ \psi(s+1) - \psi\bigl((s+1)-t\bigr) \bigr] ds + \bigl[ \psi\bigl((s+1)-t\bigr) - \psi(t+1) \bigr] dt$$

This formulation clearly shows that the differential involves evaluating the digamma function at three key points: $s+1$, $(s+1)-t$, and $t+1$. The structure reveals that $(s+1)-t$ serves as a central pivot point, appearing in both partial derivatives.

Finally, since $d \log f = df / f$, the differential of $\mathrm{Bi}(s,t)$ itself is given by:

$$d\,\mathrm{Bi}(s,t) = \mathrm{Bi}(s,t) \left( \bigl[ \psi(s+1) - \psi\bigl((s+1)-t\bigr) \bigr] ds + \bigl[ \psi\bigl((s+1)-t\bigr) - \psi(t+1) \bigr] dt \right )$$

### 2.3. Interpretation of the Differential Form

The structure of this differential reveals several key properties of the function $\mathrm{Bi}(s,t)$:

* The differential $d\,\mathrm{Bi}(s,t)$ is directly proportional to $\mathrm{Bi}(s,t)$ itself. This structural property is characteristic of many important special functions, such as the Gamma and Beta functions, and indicates a deep connection to exponential and logarithmic behavior.
* The form of the differential as a logarithmic derivative is a common feature among special functions defined by infinite products or integrals, encoding how the function changes under infinitesimal variations of its parameters.
* The differential form proves that the only possible singularities of $\mathrm{Bi}(s,t)$ (away from the boundaries of the domain of convergence) arise from the poles of the digamma function, thus completely characterizing the function's singular structure.

This differential form provides a powerful tool for analyzing the function's global behavior, which we explore in the next section.

## 3. Analytic Structure and Special Values

A complete characterization of an analytic function requires understanding its domain of definition, including its poles, zeros, and its values at specific points or boundaries. Building on the connections to the digamma function established previously, this section investigates these foundational properties for $\mathrm{Bi}(s,t)$.

### 3.1. Poles and Zeros

The locations of the function's singularities can be inferred directly from the poles of the digamma function.

* **Poles:** The digamma function $\psi(z)$ has simple poles at all non-positive integers ($z = 0, -1, -2, \ldots$). Consequently, the differential of $\log \mathrm{Bi}(s,t)$ becomes singular, and $\mathrm{Bi}(s,t)$ itself will have poles, when the arguments of the digamma functions are non-positive integers. The arguments are $s+1$, $t+1$, and $s-t+1$. Poles therefore arise when $s$, $t$, or $s-t$ are negative integers ($\in \{-1, -2, -3, \ldots\}$).

* **Zeros:** The original infinite product definition suggests that zeros occur when the numerator terms vanish, which happens if $t = -n$ or $s-t = -n$ for an integer $n \geq 1$.

Critically, the conditions for zeros coincide with two of the three conditions for poles. This indicates that at these locations, the function's behavior is determined by a competition between vanishing numerator terms and singular denominator terms, potentially leading to cancellation or reinforcement of singularities.

### 3.2. Boundary Conditions and Special Values

Evaluating $\mathrm{Bi}(s,t)$ at specific boundaries provides crucial insight into its behavior and serves as a necessary condition for its identification with other known functions.

* **Case $t = s$:** Substituting $t=s$ into the product definition yields:
  $$\mathrm{Bi}(s,s) = \prod_{n=1}^\infty \frac{(s+n)(s-s+n)}{(s+n)n} = \prod_{n=1}^\infty \frac{(s+n)n}{(s+n)n} = \prod_{n=1}^\infty 1 = 1$$

* **Case $t = 0$:** Similarly, substituting $t=0$ gives:
  $$\mathrm{Bi}(s,0) = \prod_{n=1}^\infty \frac{(0+n)(s-0+n)}{(s+n)n} = \prod_{n=1}^\infty \frac{n(s+n)}{(s+n)n} = 1$$

* **Case $s = 0$:** When $s=0$, the function takes the form:
  $$\mathrm{Bi}(0,t) = \prod_{n=1}^\infty \frac{(t+n)(-t+n)}{n^2}$$
  
  This product has a remarkable closed form expressed in terms of the sine function. To derive it, we employ the Weierstrass product representation for sine:
  $$\sin(\pi z) = \pi z \prod_{n=1}^\infty \left(1 - \frac{z^2}{n^2}\right)$$
  
  Setting $z = t$:
  $$\sin(\pi t) = \pi t \prod_{n=1}^\infty \left(1 - \frac{t^2}{n^2}\right) = \pi t \prod_{n=1}^\infty \frac{n^2 - t^2}{n^2}$$
  
  Rearranging the numerator:
  $$\sin(\pi t) = \pi t \prod_{n=1}^\infty \frac{(n-t)(n+t)}{n^2}$$
  
  Notice that $(n-t)(n+t) = (n+t)(-t+n)$, so:
  $$\sin(\pi t) = \pi t \prod_{n=1}^\infty \frac{(t+n)(-t+n)}{n^2}$$
  
  Therefore:
  $$\mathrm{Bi}(0,t) = \prod_{n=1}^\infty \frac{(t+n)(-t+n)}{n^2} = \frac{\sin(\pi t)}{\pi t}$$
  
  This elegant formula reveals that $\mathrm{Bi}(0,t)$ is the normalized sinc function, a ubiquitous object in signal processing and harmonic analysis. The poles of $\mathrm{Bi}(0,t)$ occur at all non-zero integers, while zeros occur at all positive and negative integers, consistent with the zero structure of $\sin(\pi t)$.

### 3.3. Summary of Analytic Behavior

The key analytic properties of $\mathrm{Bi}(s,t)$ are summarized in the table below.

| Case | Value/Behavior |
|------|----------------|
| $t=0$ | $\mathrm{Bi}(s,0) = 1$ |
| $t=s$ | $\mathrm{Bi}(s,s) = 1$ |
| $s=0$ | $\mathrm{Bi}(0,t) = \prod_{n=1}^\infty (t+n)(-t+n)/n^2$ |
| $s,t \in \mathbb{N}_0, \, s \geq t$ | Rational-valued; positive if $s \geq t \geq 0$ |
| Poles | Occur when $s, t,$ or $s-t \in \{-1,-2,-3,\ldots\}$ |
| Zeros | Coincide with pole locations; may cancel |

The behavior of $\mathrm{Bi}(s,t)$ at its boundaries and the nature of its singularities provide a clear picture of its structure. The function's behavior on the integer lattice, in particular, suggests a direct connection to classical combinatorics, which we will now explore.

## 4. Relation to the Classical Binomial Coefficient

A crucial test for any generalized function is to demonstrate that it correctly reproduces its classical counterpart in the appropriate domain. This section establishes that $\mathrm{Bi}(s,t)$ is identical to the standard binomial coefficient when its arguments $s$ and $t$ are non-negative integers.

### 4.1. Discrete Recurrence Relation

For non-negative integer arguments $s, t \in \mathbb{N}_0$ with $s \geq t$, the function $\mathrm{Bi}(s,t)$ satisfies a simple additive recurrence relation:

$$\mathrm{Bi}(s,t) = \mathrm{Bi}(s-1,t) + \mathrm{Bi}(s-1,t-1)$$

This relationship is precisely analogous to Pascal's rule, the defining recurrence for binomial coefficients. It arises because, for integer arguments, the infinite product defining $\mathrm{Bi}(s,t)$ effectively truncates, becoming a finite product of rational terms. This finite structure gives rise to the simple additive property.

### 4.2. Explicit Formula for Integer Arguments

Given that $\mathrm{Bi}(s,t)$ satisfies Pascal's recurrence relation and adheres to the boundary conditions $\mathrm{Bi}(s,0)=1$ and $\mathrm{Bi}(s,s)=1$, it must be identical to the classical binomial coefficient for integers $s$ and $t$ where $0 \leq t \leq s$. This leads to the well-known explicit formula:

$$\mathrm{Bi}(s,t) = \frac{s!}{t! (s-t)!} = \binom{s}{t}$$

This identity confirms that $\mathrm{Bi}(s,t)$ is a true generalization of the binomial coefficient. This factorial-based formula provides a natural bridge for extending the function's definition from the integers into the complex plane through analytic continuation.

## 5. Analytic Continuation via the Gamma Function

Analytic continuation is the canonical method in complex analysis for extending a function's domain from a smaller set, such as the integers, to the broader complex plane while preserving its analytic properties. This section formalizes the generalization of $\mathrm{Bi}(s,t)$ to all complex numbers by leveraging the Gamma function, the standard extension of the factorial function.

### 5.1. The Gamma Function Representation

The factorial function $n!$ is generalized to complex arguments $z$ by the Gamma function, $\Gamma(z+1)$. By replacing the factorials in the integer formula for $\mathrm{Bi}(s,t)$ with their Gamma function counterparts, we arrive at the definitive analytic continuation of the function:

$$\mathrm{Bi}(s,t) = \frac{\Gamma(s+1)}{\Gamma(t+1)\Gamma(s-t+1)}$$

This representation is valid for all complex $s$ and $t$, provided that the arguments of the Gamma functions in the denominator are not non-positive integers. That is, the formula holds for all $s, t \in \mathbb{C}$ such that $t, s-t \notin \{-1, -2, \ldots\}$. The pole locations of this representation correspond exactly to those identified earlier from the digamma function analysis.

### 5.2. Relationship to the Weierstrass Product

This Gamma function formulation is deeply connected to the original infinite product definition of $\mathrm{Bi}(s,t)$. This can be shown through the Weierstrass product representation for the reciprocal Gamma function. The Weierstrass product for $1/\Gamma(z)$ is given by:

$$\frac{1}{\Gamma(z)} = z e^{\gamma z} \prod_{n=1}^\infty \left(1 + \frac{z}{n}\right) e^{-z/n}$$

where $\gamma` is the Euler-Mascheroni constant. This yields:

$$\frac{1}{\Gamma(z+1)} = e^{\gamma z} \prod_{n=1}^\infty \left(1 + \frac{z}{n}\right) e^{-z/n}$$

The function $\mathrm{Bi}(s,t)$ can be constructed as the ratio $\Gamma(s+1) / (\Gamma(t+1)\Gamma(s-t+1))$. Expressing this in terms of Weierstrass products:

$$\mathrm{Bi}(s,t) = \frac{1/[\Gamma(t+1)]^{-1}}{1/[\Gamma(s+1)]^{-1} \cdot 1/[\Gamma(s-t+1)]^{-1}}$$

Substituting the Weierstrass product for each term, the exponential terms cancel:

$$\frac{ e^{\gamma t} \cdot e^{\gamma(s-t)} }{ e^{\gamma s} } = \frac{ e^{\gamma s} }{ e^{\gamma s} } = 1$$

$$\frac{ \prod_{n=1}^\infty e^{-t/n} \cdot \prod_{n=1}^\infty e^{-(s-t)/n} }{ \prod_{n=1}^\infty e^{-s/n} } = \prod_{n=1}^\infty \frac{ e^{-t/n} e^{-(s-t)/n} }{ e^{-s/n} } = \prod_{n=1}^\infty e^0 = 1$$

The remaining ratio of products simplifies directly to our original definition:

$$\mathrm{Bi}(s,t) = \frac{\prod_{n=1}^\infty (1 + t/n) \cdot \prod_{n=1}^\infty (1 + (s-t)/n)}{\prod_{n=1}^\infty (1 + s/n)} = \prod_{n=1}^\infty \frac{(t+n)(n+s-t)}{n(n+s)} = \prod_{n=1}^\infty \frac{(t+n)(s-t+n)}{n(s+n)}$$

This demonstrates that the Gamma function representation is not merely an alternative form but is the rigorous analytic continuation of the infinite product with which we began, providing a satisfying unification of the function's definitions.

## 6. Further Analytic Properties and Interpretation

The well-defined differential and analytic forms of $\mathrm{Bi}(s,t)$ enable a deeper investigation into its behavior across the complex plane. This section explores the evaluation of the function at rational arguments and provides a geometric and arithmetic interpretation of its differential, highlighting the richness of its structure.

### 6.1. Evaluation at Rational Arguments

The function $\mathrm{Bi}(s,t)$ can be systematically evaluated at and continued between rational arguments. This process relies on Gauss's digamma theorem, which provides exact, closed-form expressions for the digamma function $\psi(p/q)$ at rational points $p/q$.

The procedure for analytic continuation is as follows: starting from a point $(s,t)$ where the value of $\mathrm{Bi}(s,t)$ is known (e.g., $\mathrm{Bi}(s,0)=1$), one can integrate the differential $d\,\mathrm{Bi}(s,t)$ along a chosen path in the complex plane. Since the differential is expressed in terms of digamma functions, Gauss's theorem provides the explicit values needed to perform this integration between rational points, allowing for the systematic computation of $\mathrm{Bi}(s,t)$ across the complex plane, provided the path of integration avoids the function's poles.

### 6.2. Geometric and Arithmetic Interpretation of the Differential

The differential of $\log \mathrm{Bi}(s,t)$ holds distinct interpretations depending on the domain of its arguments.

* **Integer Lattice:** For integer arguments, the digamma function is related to the harmonic numbers through the identity $\psi(n+1) = -\gamma + H_n$, where $H_n = \sum_{k=1}^n 1/k$. The differential therefore connects infinitesimal changes in $\mathrm{Bi}(s,t)$ to discrete changes in partial sums of the harmonic series.

* **Rational Points:** At rational points, Gauss's digamma theorem shows that $\psi(p/q)$ can be expressed in terms of elementary functions, including cotangent and logarithmic terms. Consequently, the differential of $\mathrm{Bi}(s,t)$ at these points is governed by a rich arithmetic structure involving trigonometric and logarithmic constants.

* **Geometric Meaning:** The differential $d\,\log \mathrm{Bi}(s,t)$ can be interpreted as defining a "vector field" in the $(s,t)$ complex plane. This field describes the local rate and direction of change of the function at every point, with its structure and singularities determined entirely by the properties of the digamma function.

This rich set of interpretations underscores the function's deep connections to number theory, combinatorics, and geometry.

## 7. Conclusion

This paper has systematically analyzed the properties of $\mathrm{Bi}(s,t)$, a generalized binomial function. Beginning with its definition as an infinite product, we have demonstrated its successful generalization from the discrete domain of combinatorics to the continuous domain of complex analysis. The key findings confirm that $\mathrm{Bi}(s,t)$ is a well-behaved analytic function with a rich and coherent structure. Its primary properties include a differential elegantly expressed in terms of the digamma function, a set of predictable poles and special values, and an ultimate representation via the Gamma function that confirms its identity as the analytic continuation of the classical binomial coefficient. $\mathrm{Bi}(s,t)$ therefore stands as a well-defined and analytically tractable extension of a fundamental mathematical object to the complex plane, embodying deep connections to the theory of special functions. The existence of such a robust generalization suggests its utility in fields where binomial coefficients arise in non-integer contexts, such as fractional calculus, theoretical physics, and the study of hypergeometric functions.

---

## 8. References

[1] Abramowitz, M., & Stegun, I. A. (1964). *Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables*. U.S. National Bureau of Standards.

[2] Artin, E. (1931). Einführung in die Theorie der Gammafunktion. *Teubner*, Leipzig.

[3] Binet, J. P. M. (1843). Sur les intégrales définies eulériennes et sur leur application à la théorie des suites, ainsi qu'à l'évaluation des fonctions des grands nombres. *Journal de l'École Polytechnique*, 27(16), 123-343.

[4] Davis, P. J. (1959). Leonhard Euler's integral: A historical profile of the Gamma function. *American Mathematical Monthly*, 66(10), 849-869.

[5] Erdélyi, A., Magnus, W., Oberhettinger, F., & Tricomi, F. G. (1953). *Higher Transcendental Functions* (Vol. 1). McGraw-Hill.

[6] Gauss, C. F. (1812). Disquisitiones generales circa seriem infinitam. *Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores*, 2, 3-46.

[7] Gamma function. (2024). In *Wikipedia*. Retrieved from https://en.wikipedia.org/wiki/Gamma_function

[8] Graham, R. L., Knuth, D. E., & Patashnik, O. (1994). *Concrete Mathematics: A Foundation for Computer Science* (2nd ed.). Addison-Wesley.

[9] Knopp, K. (1990). *Theory and Application of Infinite Series* (2nd ed.). Dover Publications.

[10] Lanczos, C. (1964). *A Precision Approximation of the Gamma Function*. Journal of the Society for Industrial and Applied Mathematics, Series B: Numerical Analysis, 1(1), 86-96.

[11] Pascal's triangle. (2024). In *Wikipedia*. Retrieved from https://en.wikipedia.org/wiki/Pascal%27s_triangle

[12] Pochhammer, L. (1890). Ueber hypergeometrische Functionen nter Ordnung. *Journal für die reine und angewandte Mathematik*, 71, 316-352.

[13] Riemann, B. (1859). Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse. *Monatsberichte der Berliner Akademie*, 671-680.

[14] Rubin, K. & Silverberg, A. (2002). Ranks of elliptic curves. *Bulletin of the American Mathematical Society*, 39(4), 455-474.

[15] Whittaker, E. T., & Watson, G. N. (1927). *A Course of Modern Analysis: An Introduction to the General Theory of Infinite Processes and of Analytic Functions; with an Account of the Principal Transcendental Functions* (4th ed.). Cambridge University Press.

[16] Weierstrass, K. (1876). Zur Theorie der eindeutigen analytischen Functionen. *Abhandlungen aus der Funktionenlehre*, 11-60. (Published in *Werke II*, 1895.)
