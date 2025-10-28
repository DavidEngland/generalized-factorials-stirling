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

A.5 Expanded formulas for \(c^{(k)}_{-1-t}\), explicit \(D_\rho\), and worked examples (k=0..2)

A.5.1 Convolution formula for the \(c\)-coefficients

Let, for fixed \(k\), the differentiated integrand be
\[
A_k(s)\;:=\;\frac{(-1)^k}{s}\frac{d^k}{ds^k}\!\Big[-\frac{\zeta'(s)}{\zeta(s)}\Big].
\]
Write the local Laurent expansion about a simple zero \(s=\rho\) as
\[
A_k(s)=\sum_{m\ge -M} a^{(k)}_m(\rho)\,(s-\rho)^m,
\]
where the finite pole order \(M\le k+1\) depends on \(k\) and the local jet of \(\zeta\). Also expand \(1/s\) about \(s=\rho\):
\[
\frac{1}{s}=\sum_{n\ge0}\frac{(-1)^n}{\rho^{\,n+1}}(s-\rho)^n.
\]
Multiplying the two series gives the convolution formula for the coefficients appearing in Appendix A.1:
\[
\boxed{\;
c^{(k)}_{r}(\rho)\;=\;\sum_{n\ge0}\frac{(-1)^n}{\rho^{\,n+1}}\,a^{(k)}_{\,r-n}(\rho),
\qquad r\in\mathbb Z,
\;}
\]
in particular, for the polynomial coefficients used in \(P_k\),
\[
c^{(k)}_{-1-t}(\rho)
=\sum_{n=0}^{\infty}\frac{(-1)^n}{\rho^{\,n+1}}\,a^{(k)}_{-1-t-n}(\rho),
\qquad 0\le t\le k,
\]
with the understanding that \(a^{(k)}_m=0\) for \(m<-M\).

A.5.2 Explicit finite‑matrix representation of \(D_\rho\)

Fix \(k\). Work on the vector space \(\mathcal P_k\) of polynomials in \(L=\log x\) of degree ≤k with monomial basis \(\{1,L,\dots,L^k\}\). Using
\[
P_k(L)=\sum_{t=0}^k \frac{c^{(k)}_{-1-t}}{t!}L^t,
\]
and the recurrence
\[
P_{k+1}=L\,P_k + D_\rho[P_k],
\]
one obtains a matrix representation \(D_\rho\in\mathbb C^{(k+1)\times(k+1)}\) acting on coefficient vectors \(\mathbf p\) (monomial basis ordered by degree). The convolution formula above yields explicit entries:
\[
\boxed{\;
\big(D_\rho\big)_{r,j}
\;=\;
\frac{(r)!}{j!}\,c^{(k+1)}_{-1-(r-j)}(\rho)\quad\text{for }0\le j\le r\le k,
\;}
\]
and \((D_\rho)_{r,j}=0\) for \(j>r\). In words: \(D_\rho\) is lower‑triangular in the monomial basis and each entry is built from the appropriate shifted \(c\)-coefficient. This formula is immediate from equating coefficients in the polynomial identity produced by the recurrence.

A.5.3 Worked symbolic expressions for k=0,1,2 (structure)

Using the convolution formula one can express the \(P_k\) coefficients explicitly in terms of the local \(a^{(k)}_m\). Writing \(L=\log x\):

- k=0:
  \[
  P_0(L)=\underbrace{c^{(0)}_{-1}}_{=\sum_{n\ge0}(-1)^n\rho^{-n-1} a^{(0)}_{-1-n}}.
  \]

- k=1:
  \[
  P_1(L)=c^{(1)}_{-1}+c^{(1)}_{-2}L,
  \quad\text{with}\quad
  c^{(1)}_{-1}=\sum_{n\ge0}\frac{(-1)^n}{\rho^{n+1}}a^{(1)}_{-1-n},\quad
  c^{(1)}_{-2}=\sum_{n\ge0}\frac{(-1)^n}{\rho^{n+1}}a^{(1)}_{-2-n}.
  \]

- k=2:
  \[
  P_2(L)=c^{(2)}_{-1}+c^{(2)}_{-2}L+\tfrac{1}{2}c^{(2)}_{-3}L^2,
  \]
  with each \(c^{(2)}_{-1-t}\) given by the convolution above.

A.5.4 Numerical extraction recipe (practical) and short Python example

Practical way to obtain the needed local coefficients \(a^{(k)}_m\) numerically (robust for small k):

1. Choose a small radius \(r_{\mathrm{circ}}\) (e.g. 1e-3 to 1e-2) and \(N\ge 2M+5\) sample points \(s_j=\rho + r_{\mathrm{circ}} e^{2\pi i j/N}\) on the circle around \(\rho\).
2. Evaluate the function \(A_k(s)\) at the \(s_j\).
3. Solve the linear system for the unknown Laurent coefficients \(a^{(k)}_{-M},\dots,a^{(k)}_{P}\) (take \(P\ge k\)) by matching
   \(A_k(s_j)=\sum_{m=-M}^{P} a^{(k)}_m (s_j-\rho)^m\).
4. Use the convolution formula to compute \(c^{(k)}_{-1-t}\).
5. Form \(P_k(L)=\sum_{t=0}^k\frac{c^{(k)}_{-1-t}}{t!}L^t\).

Compact Python (mpmath) implementation for k≤2 (illustrative; students can adapt precision and parameters):

```python
# filepath: /Users/davidengland/Documents/GitHub/generalized-factorials-stirling/docs/draftss/Notes on von Mangoldt Hierarchies.md
import mpmath as mp

mp.mp.dps = 60  # adjust precision

def Ak(s, k):
    # A_k(s) = (-1)^k / s * d^k/ds^k ( -zeta'(s)/zeta(s) )
    # compute inner f(s) = -zeta'(s)/zeta(s)
    f = lambda z: -mp.diff(mp.zeta, z) / mp.zeta(z)
    # k-th derivative of f:
    fk = mp.diff(f, s, k)
    return ((-1)**k) * fk / s

def laurent_coeffs(Afunc, rho, M_neg=4, P_pos=4, radius=1e-3, N=40):
    # unknowns a_m for m=-M_neg..P_pos inclusive
    idxs = list(range(-M_neg, P_pos+1))
    Npts = max(N, len(idxs)+5)
    S = []
    B = []
    for j in range(Npts):
        sj = rho + radius * mp.e**(2j*mp.pi*1j/Npts)
        row = [ (sj - rho)**m for m in idxs ]
        B.append([complex(row_i) for row_i in row])
        S.append(complex(Afunc(sj)))
    # Solve linear system (least squares)
    import numpy as np
    A = np.array(B, dtype=complex)
    y = np.array(S, dtype=complex)
    coeffs, *_ = np.linalg.lstsq(A, y, rcond=None)
    # map back to m->coeff
    a = {m: coeffs[i] for i,m in enumerate(idxs)}
    return a  # complex valued dict

def compute_Pk_from_rho(rho, k):
    # 1) get laurent a^{(k)}_m of the differentiated integrand (before 1/s)
    # we'll extract a^{(k)} for A_k(s) already includes the 1/s factor as defined above
    a = laurent_coeffs(lambda z: Ak(z, k), rho, M_neg=k+1, P_pos=k+2, radius=1e-3, N= max(40, 6*(k+3)))
    # 2) form c_{-1-t} via c_r = sum_{n>=0} (-1)^n rho^{-n-1} a_{r-n}
    c = {}
    for t in range(0, k+1):
        r = -1 - t
        total = 0+0j
        # n up to some limit where a_{r-n} present (we extracted finite range)
        for n in range(0, k+4):
            am = a.get(r - n, 0)
            total += ((-1)**n) * am / (rho**(n+1))
        c[r] = total
    # 3) assemble P_k(L) coefficients (monomials L^t)
    Pc = [ c.get(-1 - t, 0) / mp.factorial(t) for t in range(0, k+1) ]
    return Pc  # list of coefficients for L^0..L^k

# Example usage (first nontrivial zero approx):
rho = 0.5 + 14.1347251417347j
for k in [0,1,2]:
    coeffs = compute_Pk_from_rho(rho, k)
    print("k=",k,"P_k coeffs (L^0..L^k):")
    for t,c in enumerate(coeffs):
        print(t, c)
```

Notes on the script:
- The function `laurent_coeffs` uses a least‑squares fit to obtain a stable set of Laurent coefficients from sampled values; increase `mp.mp.dps` and reduce `radius` if needed.
- `Ak` uses mpmath derivatives; for larger k or many zeros this becomes costly—use symbolic precomputation where possible.
- The extracted coefficients are complex; when pairing conjugate zeros in the explicit formula one takes appropriate real combinations so the total contribution is real.

A.5.5 Remarks and recommended checks
- Verify accuracy by (i) comparing the directly computed residue of \(A_k(s)\) (e.g. via a small contour integral) with the reconstructed \(c^{(k)}_{-1}\); (ii) checking the linear system conditioning when solving for Laurent coefficients.
- For k≤2 the approach above is typically robust at moderate precision; for k≥3 increase `mp.mp.dps` and number of sample points.

---

## Naming, generating functions, and properties of the residue polynomials \(P_k\)

Short answers first:
- Standard name: there is no universally accepted single name in the literature for these objects; they are most safely referred to as the residue polynomials (or residue factors) \(P_k(\rho,\log x)\) attached to the explicit formula. Calling them "residue polynomials at \(\rho\)" or "zero‑residue polynomials" is clear and descriptive.
- Generating function in k: yes — there is a natural exponential generating function (EGF) in the differentiation order k, obtained by the operator identity \(\exp(t\partial_s)f(s)=f(s+t)\). Using the Dirichlet/derivative definition one gets
\[
\sum_{k\ge0}\frac{t^k}{k!}\sum_{n\ge1}\frac{\Lambda_k(n)}{n^s}
=\sum_{n\ge1}\frac{\Lambda(n)}{n^{\,s-t}}
=-\frac{\zeta'(s-t)}{\zeta(s-t)}.
\]
Consequently one may probe all \(k\) at once by studying the shift \(s\mapsto s-t\) of \(-\zeta'/\zeta\); extracting residues in \(s\) then produces a k‑EGF for the family \(\{P_k(\rho,L)\}_{k\ge0}\).
- Relation to incomplete‑Gamma: the incomplete‑Gamma representation discussed in §4 is a convenient finite‑dimensional way to express the same polynomial dependence in \(L=\log x\). It is not a fundamental definition but an equivalent linear representation: for each fixed \(\rho\) the polynomial \(P_k(\rho,L)\) lies in the span of \(\{\partial_\alpha^j\Gamma(\alpha,L)\}_{0\le j\le k}\) evaluated at a convenient \(\alpha\) (conventionally \(\alpha\approx c/\rho\)). This gives a numerically practical basis for fitting and identifying coefficients, but the intrinsic definition of \(P_k\) remains the residue coefficient coming from the Laurent expansion of the integrand at \(s=\rho\).
- Why subscripts/superscripts proliferate: we use multiple indices because objects play two roles:
  • the subscript k labels the differentiation/hierarchy order (how many s‑derivatives were taken);  
  • superscripts on local coefficients (e.g. \(c^{(k)}_m\)) indicate the k‑th differentiated integrand’s Laurent coefficient. Thus \(c^{(k)}_{m}\) denotes "coefficient index m coming from the k‑th derivative". This bookkeeping is necessary because the residue coefficients depend both on the local power (m) and on which derivative (k) produced them.
- Key algebraic/analytic properties (summary):
  1. Degree: \(\deg_L P_k(\rho,L)\le k\).
  2. Coefficients: each coefficient of \(L^j\) is an algebraic (rational) combination of the local jet of \(\zeta\) at \(\rho\); for simple zeros they depend on \(\zeta^{(m)}(\rho)\) for finitely many m.
  3. Recurrence: the polynomials satisfy a practical recurrence of the form
     \[
     P_{k+1}(\rho,L) = L\,P_k(\rho,L) + D_\rho\big[P_k(\rho,L)\big],
     \]
     where \(D_\rho\) is the finite linear operator recorded in Appendix A (built from shifted \(c\)-coefficients). This recurrence is convenient for numeric generation.
  4. Generating‑function viewpoint: the k‑EGF of the entire family is tied to the meromorphic function \(-\zeta'(s-t)/\zeta(s-t)\); studying the local expansion in s near \(\rho\) of this shifted function produces the EGF of the residue coefficients.
  5. Growth and stability: coefficients typically grow with k (factorial‑type scaling appears in related saddle‑point analyses). Numerically extracting high‑k coefficients is delicate; using the incomplete‑Gamma basis or the recurrence with high precision mitigates instability.
- Practical tests the reader/student should run:
  1. EGF test: numerically compute residues of \(-\zeta'(s-t)/\zeta(s-t)\) at s=ρ for several small t, expand in powers of t and compare the Taylor coefficients in t with the computed P_k (gives an independent check of the k‑dependence).  
  2. Recurrence test: build P_0,P_1 by direct residue extraction and verify the recurrence P_{k+1}=L P_k + D_ρ[P_k] for k=0,1 (low‑order sanity).  
  3. Incomplete‑Gamma fit: perform the linear solve described in §4 for a small k (≤4) and compare fitted coefficients with the residue coefficients; check conditioning and vary α normalization.
- References and context: the above organizing observations are, in part, a repackaging of standard residue calculus and explicit formula machinery (see Titchmarsh, Edwards). The EGF/shift identity is an elementary consequence of the definition of \(\Lambda_k(n)\) and is a tidy way to unify k‑dependence.

#### What we mean by "cumulants" (clarification)

- Operator / generating‑function viewpoint.  In probability the cumulant generating function (CGF) is \(\kappa(t)=\log \mathbb{E}[e^{tX}]\); its \(k\)-th derivative at \(t=0\) is the \(k\)-th cumulant.  In our setting the direct analogue is the family of shifted logarithmic derivatives
  \[
  K_s(t)\;:=\; -\frac{\zeta'(s-t)}{\zeta(s-t)} \;=\; \sum_{n\ge1}\frac{\Lambda(n)}{n^{\,s-t}},
  \]
  so that expanding in \(t\) (or differentiating in \(s\)) produces the hierarchy:
  \[
  \sum_{n\ge1}\frac{\Lambda_k(n)}{n^s}
  =(-1)^k\frac{d^k}{ds^k}\!\Big[-\frac{\zeta'(s)}{\zeta(s)}\Big]
  \;=\;\left.\frac{d^k}{dt^k}K_s(t)\right|_{t=0}.
  \]
  Thus \(\Lambda_k\) are the Dirichlet‑coefficients encoding the \(k\)-th derivatives (cumulant‑type data) of the CGF analogue \(K_s(t)\).  Viewing all \(k\) at once is natural via the EGF in §(Naming/EGF).

- Weighted‑distribution viewpoint.  Fix \(s>1\) and define a (complex) discrete measure on the "log‑scale" by placing mass \(\Lambda(n)/n^s\) at the point \(\log n\).  Then the ordinary moments of this measure are
  \[
  m_j(s)=\sum_{n\ge1}\frac{\Lambda(n)}{n^s}(\log n)^j,
  \]
  and the cumulant‑like quantities obtained by algebraically combining these moments (via Bell‑polynomial relations) coincide with the Dirichlet coefficients \(\Lambda_k(n)\) when transferred back through the Mellin/Dirichlet dictionary.  Equivalently, \(\Lambda_k\) encode the \(k\)-th cumulant‑style response of the measure of \(\log n\) under the weight \(\Lambda(n)/n^s\).

- Two important caveats.
  1. These "cumulants" are not cumulants of a probability measure on \(\mathbb R\) in the usual positive sense: the masses \(\Lambda(n)/n^s\) are signed/complex when continued and the resulting coefficients (Stieltjes constants, \(\Lambda_k\), \(P_k\) entries) may change sign.  The analogy is structural (same algebraic/combinatorial relations) rather than literal positivity.
  2. The Dirichlet/formal‑series viewpoint is valid for \(\Re(s)>1\); residues and zeros enter via analytic continuation. Interpret cumulant statements that involve zeros as statements about the analytically continued CGF analogue \(K_s(t)\).

- Practical tests for clarity (quick):
  1. For fixed \(s>1\), compute empirical moments \(m_j(s)\) up to j=k and form the combinatorial cumulant via Bell‑polynomial relations; compare the resulting Dirichlet combination with the coefficient vector given by the left side \(\sum_n \Lambda_k(n)n^{-s}\).
  2. Numerically check the operator identity by computing finite differences in t of \(K_s(t)=-\zeta'(s-t)/\zeta(s-t)\) at t=0 and comparing with the derivatives obtained by differentiating in s.
