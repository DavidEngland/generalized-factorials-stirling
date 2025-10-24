# Draft for “Notes on von Mangoldt Hierarchies and Cumulant Structures”
**Author:** D. England
**Status:** In preparation (2025)

---

## Abstract

These notes develop a unified framework connecting the differentiated von Mangoldt functions—termed the von Mangoldt hierarchies—to classical cumulant and moment‐generating structures in probability. After defining the hierarchy \(\{\Lambda_k(n)\}_{k\ge0}\) via successive derivatives of \(-\zeta'/\zeta\), we exhibit generating‐function identities that parallel cumulant–moment relations. The text derives explicit residue‐based formulas, illuminates a Bell‐polynomial interpretation of the corrective polynomials \(P_k\), and explores applications to prime‐distribution fluctuations. Numerical examples and open problems conclude.

---

## Table of Contents

1. Introduction and Motivation
2. Von Mangoldt Hierarchies
   - Definition via logarithmic‐derivative differentiation
   - Basic properties and prime‐power weights
3. Cumulant and Moment Analogues
   - Formal series comparison: \(\log M(t)\) vs.\ \(\sum\Lambda_k(n)n^{-s}\)
   - Bell‐polynomial representation of higher weights
4. Explicit Formulas
   - Mellin inversion and residue expansions
   - Pole at \(s=1\): Stieltjes–constant polynomials
   - Nontrivial zeros: oscillatory terms and \(P_k(\rho,\log x)\)
   - P_k and incomplete‑Gamma representations (sketch and experiments)
5. Combinatorial Structures
   - Faà di Bruno framework
   - Integer‐triangle interpretation of \(\tfrac{k!}{(k-j)!}\) coefficients
   - Connections to incomplete exponential Bell polynomials
6. Applications to Prime Fluctuations
   - Refined error bounds under RH
   - Cumulant‐style bounds on remainder terms
7. Numerical Experiments
   - Implementation via prime‐power enumeration
   - Visualization of \(\Psi_k(x)-M_k(x)\) and zero‐sum oscillations
8. Future Directions
   - Higher‐order zero multiplicities and multi‐cumulant analogues
   - Weighted summation schemes and smoothing kernels
   - Links to random‐matrix cumulants and statistical inference
9. References

---

## Section Summaries

### 1. Introduction and Motivation
We explain why differentiating \(-\zeta'/\zeta\) yields a natural “prime‐power cumulant” and outline parallels with classical cumulant–moment theory, positioning the von Mangoldt hierarchies as a bridge between analytic number theory and combinatorial probability.

### 2. Von Mangoldt Hierarchies
Formal definition:
\[
(-1)^k\frac{d^k}{ds^k}\!\bigl(-\tfrac{\zeta'(s)}{\zeta(s)}\bigr)
=\sum_{n\ge1}\frac{\Lambda_k(n)}{n^s},
\]
with \(\Lambda_k(p^r)=(\log p)^{k+1}r^k\). We record fundamental identities and Dirichlet‐series consequences.

### 3. Cumulant and Moment Analogues
By analogy with moment‐ and cumulant‐generating functions \(M(t)=\mathbb{E}[e^{tX}]\), we identify formal expansions in powers of \(\log x\) with cumulant‐style coefficients. A direct combinatorial mapping to Bell polynomials is developed.

#### From formal series to analytic continuation (bridging paragraph)
The formal cumulant analogy developed in §3 motivates the analytic steps in §4: treating \(-\zeta'/\zeta\) as a generating object suggests shifting Mellin/Perron contours to read off "cumulant" residues. Analytically, residues at \(s=1\) give the main (deterministic) cumulant expansion in \(\log x\); residues at zeros \(\rho\) yield the stochastic/oscillatory cumulants encoded by the \(x^{\rho}P_k(\rho,\log x)\) terms. This paragraph is intended to orient readers connecting the combinatorial viewpoint to the contour calculus that follows.

### 4. Explicit Formulas
We reproduce the Mellin‑inversion framework, shifting contours to capture residues at \(s=1\) (yielding main terms in \(\log x\) with Stieltjes constants) and at nontrivial zeros (yielding oscillatory corrections via polynomials \(P_k\)).
 
#### Proposition 4.1 (Residue form of the von Mangoldt hierarchy)
Let \(k\ge0\) and suppose \(\zeta\) has only simple nontrivial zeros in the region considered. Then for \(x>1\) and \(c>1\),
\[
\Psi_k(x)=\operatorname{Main}_k(x)\;+\;\sum_{\rho}\operatorname{Res}_{s=\rho}\!\left(\frac{(-1)^k}{s}\frac{d^k}{ds^k}\!\Big[-\frac{\zeta'(s)}{\zeta(s)}\Big]x^s\right)\;+\;\text{(small tails)},
\]
and each residue at a simple zero \(\rho\) yields a term \(x^{\rho}P_k(\rho,\log x)\) where \(P_k\) is a polynomial in \(\log x\) of degree ≤k whose coefficients depend algebraically on the jet of \(\zeta\) at \(\rho\).

Proof (sketch). Expand the integrand in a Laurent series around \(s=\rho\), multiply by \(x^s=e^{s\log x}\) and pick the \((s-\rho)^{-1}\) coefficient; powers of \((s-\rho)\) multiply through the Taylor expansion of \(e^{s\log x}\) producing a finite polynomial in \(\log x\). The coefficient algebra is finite-dimensional and depends only on derivatives of \(\zeta\) at \(\rho\). □

#### P_k and incomplete‑Gamma representations (sketch and experiments)

1) Origin of the \(x^{\rho}P_k(\rho,\log x)\) terms.

  The oscillatory contribution from a (simple) nontrivial zero \(\rho\) appears when shifting the Mellin contour and taking the residue at \(s=\rho\) of
  \[
    \frac{(-1)^k}{s}\frac{d^k}{ds^k}\!\Big[-\frac{\zeta'(s)}{\zeta(s)}\Big]\,x^s.
  \]
  For a simple zero the residue produces a term of the form \(x^{\rho}P_k(\rho,\log x)\), where \(P_k\) is a polynomial in \(\log x\) of degree at most \(k\). The polynomial coefficients are determined by the derivatives (at \(s=\rho\)) of the local factors coming from the Laurent/Taylor expansion of \(-\zeta'/\zeta\).

2) Why incomplete‑Gamma functions are natural here.

  The incomplete Gamma
  \[
    \Gamma(\alpha,z)=\int_z^\infty t^{\alpha-1}e^{-t}\,dt
  \]
  has the key property that derivatives with respect to \(\alpha\) bring down powers of \(\log t\) inside the integrand:
  \[
    \partial_\alpha^j\Gamma(\alpha,z)=\int_z^\infty t^{\alpha-1}(\log t)^j e^{-t}\,dt.
  \]
  If one inserts the factor \(x^s=e^{s\log x}\) under such an integral it is straightforward to move the exponential outside the \(t\)-integral and to see that polynomial factors in \(\log x\) can be matched against \(\partial_\alpha^j\Gamma(\alpha,\log x)\) evaluated at a suitable \(\alpha\).

3) Heuristic representation.

  Writing the residue at a simple zero \(\rho\) in terms of the local data gives
  \[
    x^{\rho}P_k(\rho,\log x)
    \;=\; x^{\rho}\sum_{j=0}^k a_{k,j}(\rho)\,(\log x)^j,
  \]
  where the coefficients \(a_{k,j}(\rho)\) are rational combinations of derivatives of \(\zeta\) at \(\rho\). Equivalently (up to harmless normalization factors depending on conventions for \(\Gamma\)), one may seek coefficients \(b_{k,j}(\rho)\) so that
  \[
    x^{\rho}P_k(\rho,\log x)
    \;=\; \sum_{j=0}^k b_{k,j}(\rho)\,\partial_\alpha^{\,j}\Gamma\!\big(\alpha,\log x\big)\Big|_{\alpha=-1/\rho}.
  \]
  The choice \(\alpha=-1/\rho\) is convenient because, under Mellin‑type substitutions, factors of the form \((s-\rho)^{-m}\) translate to powers \(t^{\alpha-1}\) with \(\alpha\) proportional to \(-1/\rho\); different choices (equivalent after reweighting) are possible depending on the precise integral transform used.

4) Derivation sketch (how to produce the \(b_{k,j}(\rho)\)).

  a. Express the \(k\)-th derivative factor near \(s=\rho\) by its Taylor expansion:
  \[
    \frac{(-1)^k}{s}\frac{d^k}{ds^k}\!\Big[-\frac{\zeta'(s)}{\zeta(s)}\Big] = \sum_{m\ge -M} c_m(\rho)\,(s-\rho)^m,
  \]
  and isolate the coefficient of \((s-\rho)^{-1}\) after multiplying by \(x^s\).

  b. Use a Mellin–Barnes or exponential integral device to rewrite \(x^s\) as an integral factor involving \(e^{-t}\) and \(t^{\alpha-1}\) so that powers of \((s-\rho)\) convert to moments (i.e. powers of \(\log t\)) in the \(t\)-integrand.

  c. Identifying the moments with \(\partial_\alpha^j\Gamma(\alpha,\log x)\) yields linear relations between the residue coefficients \(c_m(\rho)\) and the desired \(b_{k,j}(\rho)\).

  This calculation is algebraic: the \(b_{k,j}(\rho)\) are finite linear combinations of the local coefficients \(c_m(\rho)\), hence ultimately of derivatives of \(\zeta\) at \(\rho\).

5) Practical checks and numerical experiments.

  • Compute \(P_k(\rho,\log x)\) numerically by (i) evaluating the residue at \(s=\rho\) directly from truncated local expansions of \(\zeta\), and (ii) fitting the resulting dependence on \(\log x\) to extract the coefficients \(a_{k,j}(\rho)\).
  • Independently compute the family \(\{\partial_\alpha^j\Gamma(\alpha,\log x)\}_{0\le j\le k}\) at \(\alpha=-1/\rho\) and solve the small linear system for \(b_{k,j}(\rho)\). Compare with the \(a_{k,j}(\rho)\) from the residue method; agreement validates the representation.
  • Start with simple test cases: use a single (artificial) zero \(\rho\) for which \(\zeta\)-like local expansions are prescribed, or use the first few nontrivial zeros (paired conjugates) and small \(k\) (e.g. \(k\le 4\)) to avoid numerical instability.

6) Remarks and limitations.

  • The representation is most transparent for simple zeros; multiple zeros require higher-order residue calculus but the same integral/moment idea applies.
  • The mapping to incomplete‑Gamma derivatives is not unique — choices of normalizing factors (Γ(·) vs. Γ(·,·), sign conventions, and substitution constants) produce equivalent linear representations. What matters is the finite-dimensional span generated by \(\{\partial_\alpha^j\Gamma(\alpha,\log x)\}\).
  • Numerically, evaluating \(\partial_\alpha^j\Gamma(\alpha,z)\) for complex \(\alpha\) and moderate \(z=\log x\) is stable with standard scientific libraries; this makes the approach attractive for identifying which zeros dominate which polynomial coefficients.

7) Suggested text for inclusion in the main exposition.

  Add a compact boxed statement:

  \"For each nontrivial zero \(\rho\) (simple, for concreteness) there exist coefficients \(b_{k,j}(\rho)\) depending only on the local zeta‑data at \(\rho\) such that
  \[
    x^{\rho}P_k(\rho,\log x)
    \;=\;\sum_{j=0}^k b_{k,j}(\rho)\,\partial_\alpha^{\,j}\Gamma\!\big(\alpha,\log x\big)\Big|_{\alpha=-1/\rho}.
  \]
  Consequently the polynomial structure in \(\log x\) arising from residues can be viewed as the finite‑dimensional span of incomplete‑Gamma moments at the scale \(z=\log x\).\"\n

⸻

This subsection gives a concrete analytic/computational bridge between the usual polynomial form \(P_k(\rho,\log x)\) and classical special‑function moments; it is intended both as a conceptual viewpoint and as a practical route to computing or isolating zero‑contributions numerically.

### 5. Combinatorial Structures
This section shows the coefficients \(\tfrac{k!}{(k-j)!}\) arise as permutation numbers in incomplete Bell polynomials. We present a streamlined Faà di Bruno derivation of the closed‐form for \(P_k\).

### 6. Applications to Prime Fluctuations
Conditional on RH, we derive unified error‐term bounds of the form
\[
\Psi_k(x)=x(\log x)^k + O\bigl(x^{1/2}\log^{k+2}x\bigr),
\]
and propose cumulant‐style estimators for higher‐order fluctuations.

### 7. Numerical Experiments
Guidelines for efficient computation:
- Prime‐power enumeration for \(\Psi_k(x)\)
- High‐precision evaluation of Stieltjes constants
- Summation of conjugate zero‐pairs to visualize real oscillations

#### Pseudocode and plotting suggestions (practical)
Pseudocode for the prime‑power enumeration approach (straightforward to implement in JS/Python/Sage):

```
# compute Psi_k(x) by prime-power enumeration
Psi_k = 0
for p in primes_up_to(x):
    pk = p
    r = 1
    while pk <= x:
        Psi_k += (log p)^(k+1) * r^k
        r += 1
        pk *= p
```

Plot suggestion (to visualize RH‑scaled oscillations):
\[
\text{plot } x^{-1/2}\bigl(\Psi_k(x)-x(\log x)^k\bigr)\quad\text{vs.}\quad \log x,
\]
which highlights the zero‑driven oscillatory terms at the scale predicted by RH.

Numerical check for P_k vs incomplete‑Gamma representation:
  • Fit the polynomial coefficients \(a_{k,j}(\rho)\) from direct residue evaluation (small k).  
  • Form the small linear system using \(\{\partial_\alpha^j\Gamma(\alpha,\log x)\}\) at \(\alpha=-1/\rho\) and solve for \(b_{k,j}(\rho)\).  
  • Compare the two coefficient vectors; within numerical error they should match.

### 8. Future Directions
Potential extensions include multiple‐zero residue calculus, smoothed summation analogues reminiscent of cumulant‐based smoothing in statistics, and exploratory links with random‐matrix cumulants.

---

## Notation and conventions (short)
Before proceeding we record fixed conventions used throughout:
- \(\Lambda_k(n)\): k-th von Mangoldt hierarchy weight so that
\[
(-1)^k\frac{d^k}{ds^k}\!\bigl(-\tfrac{\zeta'(s)}{\zeta(s)}\bigr)=\sum_{n\ge1}\frac{\Lambda_k(n)}{n^s}.
\]
- \(\Psi_k(x)=\sum_{n\le x}\Lambda_k(n)\).
- On prime powers: \(\Lambda_k(p^r)=(\log p)^{k+1}r^k\) (included here as a defining property).
- \(P_k(\rho,\log x)\): polynomial factor of degree \(\le k\) accompanying \(x^\rho\) from the residue at the zero \(\rho\).
- Sign conventions: derivatives are classical; the outer factor \((-1)^k\) ensures \(\Lambda_0=\Lambda\).

---

### Appendix A — Local jets, the operator \(D_\rho\), and explicit P_k for k=0..4

A.1 Local Laurent data and the residue formula

Let, for fixed \(k\), the integrand near a (simple) zero \(\rho\) admit the Laurent expansion
\[
\frac{(-1)^k}{s}\frac{d^k}{ds^k}\!\Big[-\frac{\zeta'(s)}{\zeta(s)}\Big]
= \sum_{m\ge -M} c^{(k)}_m(\rho)\,(s-\rho)^m,
\]
for suitable finite \(M\) determined by \(k\) and local multiplicities. Writing \(x^s = x^\rho e^{(s-\rho)\log x}\) and expanding the exponential, the residue at \(s=\rho\) is the coefficient of \((s-\rho)^{-1}\), hence
\[
x^{\rho}P_k(\rho,\log x)
= x^{\rho}\sum_{t=0}^k \frac{c^{(k)}_{-1-t}(\rho)}{t!}\,(\log x)^t.
\]
Equivalently (dropping the global factor \(x^\rho\)), the polynomial is
\[
P_k(\rho,L)\;=\;\sum_{t=0}^k \frac{c^{(k)}_{-1-t}(\rho)}{t!}\,L^t,\qquad L:=\log x.
\]

A.2 Definition of the operator \(D_\rho\)

On the finite-dimensional polynomial space of degree \(\le k\) in \(L=\log x\), define \(D_\rho\) by its action on the monomial basis:
\[
D_\rho\big[L^j\big] \;=\; j!\sum_{t=0}^{j-1} \frac{c^{(k)}_{-1-t}(\rho)}{t!}\,\frac{L^t}{(j-t)!}\quad (0\le j\le k).
\]
(This formula expresses how differentiating the local jet shifts contributions between degrees; it is obtained by equating coefficients in the residue identity and the recurrence \(P_{k+1}=L P_k + D_\rho[P_k]\).)

A.3 Explicit P_k (k=0..4) in terms of the local c‑coefficients

Write \(L=\log x\). Then (suppressing dependence on \(\rho\) and \(k\) in the coefficients):
- k=0:
  \[
  P_0(L)=c^{(0)}_{-1}.
  \]
- k=1:
  \[
  P_1(L)=c^{(1)}_{-1}+c^{(1)}_{-2}\,L.
  \]
- k=2:
  \[
  P_2(L)=c^{(2)}_{-1}+c^{(2)}_{-2}\,L+\tfrac{1}{2}c^{(2)}_{-3}\,L^2.
  \]
- k=3:
  \[
  P_3(L)=c^{(3)}_{-1}+c^{(3)}_{-2}\,L+\tfrac{1}{2}c^{(3)}_{-3}\,L^2+\tfrac{1}{6}c^{(3)}_{-4}\,L^3.
  \]
- k=4:
  \[
  P_4(L)=c^{(4)}_{-1}+c^{(4)}_{-2}\,L+\tfrac{1}{2}c^{(4)}_{-3}\,L^2+\tfrac{1}{6}c^{(4)}_{-4}\,L^3+\tfrac{1}{24}c^{(4)}_{-5}\,L^4.
  \]

A.4 Remarks on computation
- The coefficients \(c^{(k)}_{-1-t}(\rho)\) are finite algebraic combinations of \(\zeta^{(m)}(\rho)\) and lower derivatives; for simple zeros they are stable to compute from truncated local expansions.
- Numerical test recipe: for small \(k\) (≤4) and given zero \(\rho\), (i) compute the local Laurent jet of the integrand to extract \(c^{(k)}_m\); (ii) build \(P_k\) via the formulas above; (iii) compare with a direct residue evaluation and with the incomplete‑Gamma linear fit described in §4.

*End of draft outline.*