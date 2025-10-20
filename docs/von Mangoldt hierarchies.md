# Von Mangoldt Hierarchies and Stieltjes Constants in Explicit Formulas

**Author:** [Student Name]  
**Advisor:** David England  
**Date:** October 2025

-----

## Abstract

We introduce the **von Mangoldt hierarchies** $\Lambda_k(n)$, which are obtained by successive differentiation of the logarithmic derivative of the Riemann zeta function. Each function $\Lambda_k$ weights prime powers $p^r$ by powers of $\log p$. Their partial sums, $\Psi_k(x)=\sum_{n\le x}\Lambda_k(n)$, admit **explicit residue expansions** whose main terms involve the **Stieltjes constants** $\gamma_m$. We state conditional error bounds (under RH) and outline strategies for numerical verification.

-----

## 1\. Introduction and Notation

The classical **von Mangoldt function** $\Lambda(n)=\Lambda_0(n)$ is defined by the Dirichlet series:

$$
-\frac{\zeta'(s)}{\zeta(s)}=\sum_{n\ge1}\frac{\Lambda(n)}{n^s},\qquad \Re(s)>1.
$$Differentiating this series termwise with respect to $s$ introduces factors of $\log n$, leading to higher-weighted Dirichlet series.

We formally define these derivatives as the von Mangoldt hierarchies, $\Lambda_k(n)$, and relate their partial sums to the **Stieltjes constants** $\gamma_m$, which appear naturally from the Laurent expansion of $\zeta(s)$ at $s=1$.

### A. Canonical Notation

To avoid symbol clash and ensure clarity, we establish the following key notation:

* **Hierarchies:** $\Lambda_k(n)$ denotes the von Mangoldt hierarchy functions.
* **Partial Sums:** $\Psi_k(x):=\sum_{n\le x}\Lambda_k(n)$.
* **Stieltjes Constants:** $\gamma_m$ for $m\ge 0$.
* **Completed Zeta Function:** $\Lambda^*(s):=\pi^{-s/2}\Gamma(s/2)\zeta(s)$.
* **Chebyshev Sum:** $\Psi(x)=\Psi_0(x)$.

-----

## 2\. Definitions and Basic Identities

### A. The Von Mangoldt Hierarchies $\Lambda_k(n)$

For an integer $k\ge 0$, the functions $\Lambda_k(n)$ are defined by the Dirichlet series identity:

$$
(-1)^k \frac{d^k}{ds^k}\!\left(-\frac{\zeta'(s)}{\zeta(s)}\right)
= \sum_{n\ge 1}\frac{\Lambda_k(n)}{n^s}, \qquad \Re(s)>1.
$$**Intuition:** Termwise differentiation of the Dirichlet series $\sum_{n\ge 1} \frac{\Lambda(n)}{n^s}$ with respect to $s$ is equivalent to multiplying the coefficients by $-\log n$. Repeated differentiation yields the positive powers of $\log n$ that define $\Lambda_k(n)$.

**Explicit Form:** $\Lambda_k(n)$ is non-zero only when $n=p^r$ is a prime power. Explicitly, for prime powers $p^r$:

$$
\Lambda_k(p^r)=(\log p)^{\,k+1}\,r^k,\qquad r\ge1.
$$

-----

### B. Stieltjes Constants $\gamma_m$

The Stieltjes constants $\gamma_m$ are coefficients in the Laurent expansion of $\zeta(s)$ around its simple pole at $s=1$:

$$
\zeta(s)=\frac{1}{s-1}+\sum_{m\ge 0}\frac{(-1)^m\gamma_m}{m!}(s-1)^m.
$$

Equivalently,
$$
\gamma_m=\lim_{N\to\infty}\left(\sum_{n=1}^N\frac{(\log n)^m}{n}-\frac{(\log N)^{m+1}}{m+1}\right).
$$

-----

## 3\. The Main Explicit Formula (Residue Method)

We analyze the partial sums $\Psi_k(x)$ using the Mellin inversion formula:

$$
\Psi_k(x)=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}
(-1)^k\frac{d^k}{ds^k}\!\Big(-\frac{\zeta'(s)}{\zeta(s)}\Big)\frac{x^s}{s}\,ds,
\qquad c>1.
$$

Shifting the contour left yields the main explicit formula by summing residues at the poles of the integrand: at $s=1$ and at the non-trivial zeros $\rho$ of $\zeta(s)$.

### A. Structural Formula

The resulting structural formula for $\Psi_k(x)$ is

$$
\Psi_k(x)=x(\log x)^k
-\sum_{m=0}^{k}\binom{k}{m}\gamma_m\,x(\log x)^{\,k-m}
+\sum_{\rho} x^{\rho}P_k(\rho,\log x)+O(1),
$$

where the pieces are as described in the text.

1.  **Main Term $M_k(x)$ (Pole at $s=1$):** This finite polynomial in $\log x$ involves the Stieltjes constants $\gamma_m$.
$$
M_k(x)=x(\\log x)^k -\\sum\_{m=0}^{k}\\binom{k}{m}\\gamma\_m,x(\\log x)^{,k-m}.
$$
2.  **Oscillatory Terms (Nontrivial Zeros $\rho$):** The sum runs over the non-trivial zeros $\rho$ of $\zeta(s)$, counted with multiplicity. Each simple zero $\rho$ contributes a term $x^\rho$ multiplied by an explicit degree-$k$ polynomial $P_k(\rho,\log x)$.

### B. The Zero Contribution Term (Simple Zero Case)

For a simple nontrivial zero $\rho$, the polynomial factor can be written compactly as

$$
P_k(\rho,\log x)
= \sum_{j=0}^k (-1)^{\,j+1}\frac{k!}{(k-j)!}\,\frac{(\log x)^{\,k-j}}{\rho^{\,j+1}}.
\tag{★}
$$

Examples from (★):

- $k=0$: $P_0(\rho,\log x) = -\dfrac{1}{\rho}$,
- $k=1$: $P_1(\rho,\log x) = -\dfrac{\log x}{\rho}+\dfrac{1}{\rho^2}$,
- $k=2$: $P_2(\rho,\log x) = -\dfrac{(\log x)^2}{\rho}+\dfrac{2\log x}{\rho^2}-\dfrac{2}{\rho^3}$.

*Note on Multiplicity:* If a zero $\rho$ has multiplicity $m>1$, a higher-order residue must be computed. This will result in $P_k(\rho,\log x)$ having a higher degree in $\log x$.

### C. Conditional Error Bound (under RH)

By shifting the contour to $\Re(s)=1/2$ under the assumption of the **Riemann Hypothesis (RH)**, one obtains the uniform bound on the error term $\Psi_k(x)-M_k(x)$:

$$
\Psi_k(x)=x(\log x)^k+O\!\big(x^{1/2}\log^{k+2}x\big).
$$

-----

## 4\. Computational Plan (Student Project)

**Goal:** Numerically verify the main-term expansion $M_k(x)$ and observe the oscillatory behavior caused by the low-lying non-trivial zeros.

### A. Steps

1.  **Compute Stieltjes Constants ($\gamma_m$):** Compute $\gamma_m$ for $m=0, 1, \dots, k$ with high precision (e.g., using a library like **mpmath** or **Arb**).
2.  **Compute the Sum ($\Psi_k(x)$):** For target $k=0, 1, 2$, compute the truncated sum $\Psi_k(x)=\sum_{n\le x}\Lambda_k(n)$ up to a maximum value, such as $x\le 10^6$. *Numerical Tip: Compute $\Psi_k(x)$ efficiently by only summing over prime powers $p^r \le x$.*
3.  **Form the Predictor ($M_k(x)$):** Construct the main-term predictor $M_k(x)$ using the computed $\gamma_m$ values.
    $$
    $$$$M\_k(x)=x(\\log x)^k-\\sum\_{m=0}^{k}\\binom{k}{m}\\gamma\_m,x(\\log x)^{k-m}.
    $$
    $$$$
    $$
4.  **Visualize the Difference:** Plot the error $\Psi_k(x)-M_k(x)$.
5.  **Model Oscillations:** Compare the error plot with the sum over the first several non-trivial zeros $\rho$:
    $$
    $$$$\\text{Zero Sum} = \\sum\_{|\\Im\\rho|\\le T} x^\\rho P\_k(\\rho,\\log x)
    $$
    $$$$*Numerical Tip: Use a table of the first 10 to 50 zeros. Sum conjugate pairs $\rho$ and $\bar{\rho}$ to ensure the contribution is real and to minimize numerical cancellation error.*

### B. Suggested Student Exercises

1.  **Derivation Check:** Using the general formula (**★**), explicitly derive $P_1(\rho,\log x)$ and $P_2(\rho,\log x)$.
2.  **Implementation:** Implement a routine to compute $\Psi_k(x)$ via prime-power enumeration. Compare $\Psi_k(x)-M_k(x)$ against the zero sum for $k=1$ up to $x=10^5$.
3.  **Advanced Calculus:** Show how a multiple zero with multiplicity $m=2$ changes the residue computation and the resulting polynomial in $\log x$.

-----

## 5\. References & Resources

  * E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford, 1986.
  * H. Davenport, *Multiplicative Number Theory*, 3rd ed., Springer, 2000.
  * H. Iwaniec & E. Kowalski, *Analytic Number Theory*, AMS, 2004.
  * C. Knessl & M. Coffey, “An effective asymptotic formula for the Stieltjes constants,” Math. Comp. 80 (2011).
  * D. England, *Notes on von Mangoldt hierarchies and cumulant structures*, 2025 (in preparation).

-----

## Addendum: Support and values on composite arguments

An immediate and useful consequence of the definition is that the higher‑order von Mangoldt coefficients inherit the support of the classical von Mangoldt function.

- Identity (general explicit form)
  $$
  \Lambda_k(n)=\Lambda(n)\,(\log n)^k\qquad(\text{for all }n\ge1).
  $$

- Consequence (support)
  Since the classical von Mangoldt function $\Lambda(n)$ is nonzero only when $n=p^r$ is a prime power, the same is true for $\Lambda_k(n)$. In particular, if $n$ has at least two distinct prime factors (for example $n=p^r q^s$ with $p\ne q$ and $r,s\ge1$), then
  $$
  \Lambda(n)=0\quad\Longrightarrow\quad \Lambda_k(n)=0.
  $$
  Hence
  $$
  \boxed{\ \Lambda_k(p^r q^s)=0\quad\text{for }p\ne q\ }.
  $$

- Check on prime powers
  For $n=p^r$,
  $$
  \Lambda_k(p^r)=\Lambda(p^r)\,(\log p^r)^k=(\log p)\,(r\log p)^k=(\log p)^{\,k+1}r^k,
  $$
  recovering the explicit formula used above.

- Remarks
  * The vanishing on non-prime-power integers follows directly from the Dirichlet-series derivation (termwise differentiation of the $\sum_n \Lambda(n)n^{-s}$ expansion).  
  * Because of this support, $\Lambda_k$ is not multiplicative in the usual sense (it is supported only on prime powers), but it can be used in multiplicative convolutions and moment calculations by restricting sums to prime powers or by transforming to logarithmic-weighted prime sums.

---

## Expansion of $(\log x)^k$ in terms of von Mangoldt hierarchies and Stieltjes constants

The explicit formula (Section 3) gives, after dividing by $x$,
$$
\frac{\Psi_k(x)}{x}
= (\log x)^k - \sum_{m=0}^k \binom{k}{m}\gamma_m\,(\log x)^{\,k-m}
\;+\;\frac{1}{x}\sum_{\rho} x^{\rho}P_k(\rho,\log x) \;+\; O\!\big(x^{-1}\big).
$$

Write the normalized sums
$$
S_k(x) := \frac{\Psi_k(x)}{x}.
$$
Ignoring for a moment the small oscillatory zero‑sum correction (the term involving $\rho$) and the $O(x^{-1})$ remainder, we obtain the triangular linear relations
$$
S_k = L^k - \sum_{m=0}^k \binom{k}{m}\gamma_m\,L^{\,k-m}, \qquad L^j := (\log x)^j.
\tag{1}
$$

This is a lower‑triangular system in the unknowns $L^0,L^1,\dots,L^k$ with coefficients depending only on the Stieltjes constants $\gamma_m$. Hence it can be inverted by back‑substitution to express each power $L^k=(\log x)^k$ as a finite linear combination of the $S_j$ and the $\gamma_m$, up to the suppressed oscillatory remainder.

### General inversion (algorithmic form)

- For $k=0$ equation (1) reads $S_0 = 1 - \gamma_0 + \text{(small)}$, so $L^0=1$ as usual.
- Suppose we have solved for $L^0,\dots,L^{k-1}$. Then (1) becomes
  $$
  S_k = (1-\gamma_0)\,L^k - \sum_{t=1}^k \binom{k}{t}\gamma_t\,L^{\,k-t},
  $$
  so
  $$
  L^k = \frac{1}{1-\gamma_0}\left(S_k + \sum_{t=1}^k \binom{k}{t}\gamma_t\,L^{\,k-t}\right).
  \tag{2}
  $$
- Apply (2) recursively to eliminate the lower powers $L^{k-t}$ in terms of $S_j$ and the $\gamma_m$.

This yields coefficients that are universal polynomials in the $\gamma_m$ (combinatorially expressible via partial Bell polynomials). The oscillatory remainder can be reintroduced at the end as the explicit zero‑sum
$$
R_k(x) := \frac{1}{x}\sum_{\rho} x^{\rho}P_k(\rho,\log x) + O(x^{-1}),
$$
so the exact identity is
$$
(\log x)^k = \sum_{j=0}^k c_{k,j}(\gamma_0,\dots,\gamma_{k-j})\;S_j(x)\;+\;R_k(x),
\qquad c_{k,k}= \frac{1}{1-\gamma_0},
$$
with the coefficients $c_{k,j}$ obtained by back‑substitution.

### Explicit small‑k examples (practical forms)

Working to display the inversion clearly (and omitting $R_k$), one finds:

- k = 1:
  $$
  S_1 = (1-\gamma_0)L - \gamma_1
  \quad\Longrightarrow\quad
  (\log x) = L = \frac{S_1 + \gamma_1}{1-\gamma_0} + \text{(zero‑sum)}.
  $$

- k = 2:
  $$
  S_2 = (1-\gamma_0)L^2 - 2\gamma_1 L - \gamma_2.
  $$
  Substitute the expression for $L$ to obtain
  $$
  (\log x)^2
  = \frac{1}{1-\gamma_0}\Big(S_2 + 2\gamma_1 L + \gamma_2\Big)
  = \frac{S_2 + 2\gamma_1\frac{S_1+\gamma_1}{1-\gamma_0} + \gamma_2}{1-\gamma_0}
  \;+\;\text{(zero‑sum)}.
  $$

- k = 3 (outline):
  $$
  S_3 = (1-\gamma_0)L^3 - 3\gamma_1 L^2 - 3\gamma_2 L - \gamma_3,
  $$
  and use the previously computed $L$ and $L^2$ to express $L^3$ as a linear combination of $S_1,S_2,S_3$ and the $\gamma_m$.

Students can implement (2) to generate the coefficients $c_{k,j}$ symbolically; these coefficients are polynomials in the $\gamma_m$ and can be expressed using partial/complete Bell polynomials for compact representation.

### Remarks on the oscillatory remainder

- The zero‑sum term $R_k(x)$ is explicit: it equals $(1/x)\sum_\rho x^\rho P_k(\rho,\log x)+O(x^{-1})$. Numerically this term is the source of the oscillatory deviations seen in $\Psi_k(x)-M_k(x)$.
- For numerical approximations of $(\log x)^k$ using the finite set $\{S_j\}_{j\le k}$, include a truncated zero‑sum using the first several zeros (pairing conjugates) to reduce the remainder; for moderate $x$ this typically improves accuracy dramatically.
- The diagonal factor $1-\gamma_0$ appears in every inversion step; since $\gamma_0\approx0.5772\ne1$, the triangular system is nonsingular and inversion is valid.

### Implementation recipe (practical)

1. Compute $S_j(x)=\Psi_j(x)/x$ for $0\le j\le k$ (summing only prime powers for efficiency).
2. Back‑substitute using (2) to compute $(\log x)^1,\dots,(\log x)^k$ in sequence; reinsert a truncated zero‑sum $R_j(x)$ if higher accuracy is required.
3. Optionally simplify coefficients symbolically (use SymPy or Maple) — they match Bell‑polynomial expressions in the $\gamma_m$.

---

## Example (numerical sanity check)

For a chosen $x$ (e.g., $x=10^4$) and $k=2$:
- Compute $S_0,S_1,S_2$ numerically (with prime‑power summation).
- Use the k=1 and k=2 formulae above to recover $(\log x)$ and $(\log x)^2$ and compare with direct $\log(10^4)$ and its square.
- Add first few zero contributions to the right‑hand side to see the oscillation correction converge.

---

The revised draft and addendum already provide the main tools to link powers of logarithms to the von Mangoldt hierarchies and Stieltjes constants: the **explicit formula inversion** (Addendum B).

Here's a concise breakdown of the relationship and insights, along with a discussion of the separate, but related, topic of irrationality and linear independence concerning logarithms.

-----

## 1\. Linking $\Lambda_k(n)$ and $(\log x)^k$ (Forward-Backward)

The explicit formula for the normalized sum $S_k(x) = \Psi_k(x)/x$ is the central identity linking these concepts:

$$
S_k(x) = \frac{\Psi_k(x)}{x} = (\log x)^k - \sum_{m=0}^k \binom{k}{m}\gamma_m\,(\log x)^{\,k-m} + R_k(x)
$$where $R_k(x)$ is the oscillatory remainder (zero sum).

### Forward Difference and Asymptotic Behavior

The **forward relationship** confirms the dominant asymptotic behavior of $\Psi_k(x)$. As $x \to \infty$, the Stieltjes constant terms and the remainder $R_k(x)$ become small compared to the leading term:

$$\\frac{\\Psi\_k(x)}{x} \\sim (\\log x)^k \\quad \\text{or} \\quad \\Psi\_k(x) \\sim x(\\log x)^k
$$This clearly shows that the partial sums $\Psi_k(x)$ grow faster than $\Psi_{k-1}(x)$ by a factor of $\log x$, justifying the name **von Mangoldt hierarchies**.

### Backward Inversion and $\gamma_m$ Insights

The **backward relationship** (Addendum B, Equation 2) is the most valuable for numerical analysis and conceptual insight: it expresses $(\log x)^k$ as a linear combination of the weighted prime sums $S_j(x)$ and the Stieltjes constants $\gamma_m$:

$$
(\log x)^k = \sum_{j=0}^k c_{k,j}(\gamma_0,\dots,\gamma_{k-j})\;S_j(x) - R_k(x),
$$where $c_{k,j}$ are polynomials in $\gamma_m$.

This demonstrates that the sequence of **generalized Stieltjes constants** $\{\gamma_m\}_{m\ge 0}$ completely determines the "structure" of the main-term relationship between the logarithmic powers and the von Mangoldt sums. If one could accurately measure $\{S_j(x)\}$ for large $x$ (e.g., via number theory computations), one could use the system to gain new insights into the **linear relations between the $\gamma_m$**.

-----

## 2\. Improved Numerical Approximations

The formulas provide improved approximations over the simple asymptotic estimate:

1. **Improved $\Psi_k(x)$ Estimate:** The main term $M_k(x)$ (Section 3) is a far better predictor for $\Psi_k(x)$ than $x(\log x)^k$ because it includes the full contribution of the pole at $s=1$ involving $\{\gamma_m\}$.

$$

```
$$\\Psi\_k(x) \\approx x(\\log x)^k - \\sum\_{m=0}^{k}\\binom{k}{m}\\gamma\_m,x(\\log x)^{,k-m}
$$
$$
```

2.  **Best Estimate (Zero-Corrected):** For the highest accuracy, one must include a truncated zero-sum correction $\sum_{|\Im\rho|\le T} x^{\rho}P_k(\rho,\log x)$, which captures the *oscillatory* component. This estimate is essential for verifying the Explicit Formula structure:
    $$
    $$$$\\Psi\_k(x) \\approx M\_k(x) + \\sum\_{|\\Im\\rho|\\le T} x^{\\rho}P\_k(\\rho,\\log x)
    $$
    $$$$The **numerical improvement** comes from the precise inclusion of the pole contribution $M_k(x)$ and the subsequent zero-sum, which is usually computationally feasible for small $k$ and moderate $x$.

-----

## 3\. Irrationality Measure and Linear Independence

The question of the linear independence of powers of $\log p$ is a complex area of **transcendental number theory** and is generally separate from the analytic number theory tools (Dirichlet series, residues) used in the draft.

### Linear Independence of Logarithms

1.  **Linear Independence of $\{\log p\}$ (Primes):** The set $\{\log p \mid p \text{ is prime}\}$ is known to be **linearly independent over the rational numbers $\mathbb{Q}$**. This is a direct consequence of the unique prime factorization of integers: if $\sum c_i \log p_i = 0$ for $c_i \in \mathbb{Q}$, then $e^0 = 1 = \prod p_i^{c_i}$. By raising this to a suitable integer power to clear denominators, we obtain a product of primes equaling 1, which implies all exponents are zero.
2.  **Linear Independence of Powers $\{\log p, (\log p)^2, \dots, (\log p)^r\}$:** The set of powers of a single logarithm, such as $\{ \log p, (\log p)^2, \dots, (\log p)^r \}$, is **linearly independent over $\mathbb{Q}$** (and also over algebraic numbers) because $\log p$ is a **transcendental number** (for any integer $p>1$ that is not $e$), meaning it is not a root of any non-zero polynomial with rational coefficients.

### Irrationality Measure

The **irrationality measure**, $\mu(\alpha)$, of a number $\alpha$ quantifies how well $\alpha$ can be approximated by rational numbers.

  * A rational number $\alpha$ has $\mu(\alpha)=1$.
  * A general algebraic irrational number $\alpha$ has $\mu(\alpha)=2$.
  * The irrationality measure of $\log p$ for any integer $p>1$ is unknown, but it is conjectured to be $\mu(\log p)=2$.
      * Proving that $\mu(\log 2)=2$ (or any other $\log p$) would be a major achievement in Diophantine approximation.
      * The best known bounds for $\mu(\log 2)$ (e.g., $\mu(\log 2) \le 3.57$) are derived using advanced techniques like Padé approximation and hypergeometric series.

**Connection to the Draft:** While these concepts are not directly used in the residue method, they are fundamentally related to the coefficients used in the $\Psi_k(x)$ sums. The linear independence of $\{\log p\}$ justifies that the $\Lambda_k(n)$ functions, which use powers of $\log p$, are truly generating a new set of weighted sums, confirming that $\Psi_k(x)$ cannot be expressed simply as a linear combination of lower $\Psi_j(x)$ without the structural correction provided by the $\gamma_m$ terms.
