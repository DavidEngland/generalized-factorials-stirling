# Von Mangoldt Hierarchies and Stieltjes Constants in Explicit Formulas

**Author:** [Student Name]  
**Advisor:** David England  
**Date:** October 2025

---

## Abstract

We introduce the von Mangoldt hierarchies $\Lambda_k(n)$ obtained by differentiating the logarithmic derivative of the Riemann zeta function. Each $\Lambda_k$ weights prime powers by powers of $\log p$, and their partial sums $\Psi_k(x)=\sum_{n\le x}\Lambda_k(n)$ admit explicit residue expansions whose main terms involve Stieltjes constants $\gamma_m$. We state conditional error bounds (under RH) and outline numerical verification strategies.

---

## 1. Introduction

The classical von Mangoldt function $\Lambda(n)$ satisfies
$$
-\frac{\zeta'(s)}{\zeta(s)}=\sum_{n\ge1}\frac{\Lambda(n)}{n^s},\qquad \Re(s)>1.
$$
Differentiating with respect to $s$ produces higher-weighted Dirichlet series. We define these derivatives as the von Mangoldt hierarchies and relate their partial sums to Stieltjes constants, which appear naturally from the Laurent expansion of $\zeta(s)$ at $s=1$.

---

## 2. Definitions and basic identities

- For integer $k\ge0$ define $\Lambda_k(n)$ by the Dirichlet series identity
$$
(-1)^k\frac{d^k}{ds^k}\!\left(-\frac{\zeta'(s)}{\zeta(s)}\right)=\sum_{n\ge1}\frac{\Lambda_k(n)}{n^s},\qquad \Re(s)>1.
$$

- Explicitly, for prime powers $p^r$,
$$
\boxed{\ \Lambda_k(p^r)=(\log p)^{\,k+1}\,r^k,\qquad r\ge1\ }
$$
and $\Lambda_k(n)=0$ when $n$ is not a prime power.

- The Stieltjes constants $\gamma_m$ are given by the Laurent expansion
$$
\zeta(1+u)=\frac{1}{u}+\sum_{m\ge0}\frac{(-1)^m\gamma_m}{m!}u^m,
$$
and equivalently
$$
\gamma_m=\lim_{N\to\infty}\Bigg(\sum_{n=1}^N\frac{(\log n)^m}{n}-\frac{(\log N)^{m+1}}{m+1}\Bigg).
$$

---

## 3. Main explicit formula (residue method)

Let
$$
\Psi_k(x):=\sum_{n\le x}\Lambda_k(n).
$$
For any $c>1$ we have the Mellin inversion representation
$$
\Psi_k(x)=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}(-1)^k\frac{d^k}{ds^k}\!\Big(-\frac{\zeta'(s)}{\zeta(s)}\Big)\frac{x^s}{s}\,ds.
$$

Shifting the contour left and summing residues at $s=1$ and at the nontrivial zeros $\rho$ yields the structural formula
$$
\Psi_k(x)=x(\log x)^k -\sum_{m=0}^{k}\binom{k}{m}\gamma_m\,x(\log x)^{\,k-m}
\;+\;\sum_{\rho} x^{\rho}P_k(\rho,\log x)\;+\;O(1),
$$
where:
- the finite polynomial part (first two terms) comes from the pole at $s=1$ and involves the $\gamma_m$;
- the sum over $\rho$ runs over nontrivial zeros of $\zeta(s)$; each $\rho$ contributes a term $x^\rho$ times an explicit degree-$k$ polynomial $P_k(\rho,\log x)$ whose coefficients depend on $\rho$ and the $\gamma_m$;
- under the Riemann Hypothesis (RH) one obtains the uniform bound
$$
\Psi_k(x)=x(\log x)^k+O\!\big(x^{1/2}\log^{k+2}x\big).
$$

*Proof sketch.* Differentiate the Dirichlet series under the integral, move the contour left, and compute residues at $s=1$ (giving the polynomial in $\log x$ with $\gamma_m$) and at nontrivial zeros (giving the oscillatory $x^\rho$ terms).

---

## 4. Computational plan (students' project)

Goal: verify the main-term expansion and observe oscillations coming from low-lying zeros.

Steps:
1. Compute $\gamma_m$ numerically (use high-precision evaluation of $\zeta(s)$ near $s=1$, or available tables).
2. For $k=0,1,2$ compute the truncated sum $\Psi_k^{(N)}(x)=\sum_{n\le x,\,n\le N}\Lambda_k(n)$ up to, say, $x\le 10^6$.
3. Form the main-term predictor
   $$
   M_k(x)=x(\log x)^k-\sum_{m=0}^{k}\binom{k}{m}\gamma_m\,x(\log x)^{k-m}.
   $$
4. Plot the difference $\Psi_k(x)-M_k(x)$ and compare its oscillatory behavior to the finite sum $\sum_{|\Im\rho|\le T} x^\rho P_k(\rho,\log x)$ using the first several zeros $\rho$.

Numerical tips:
- Use arbitrary-precision libraries (mpmath, Arb) for $\gamma_m$ and zeta zeros.
- Truncate zero-sum to first 10–50 zeros for visualization; increase precision for larger $x$.

---

## Peer-review notes, corrections and added derivations (to help the student)

Below are corrections, clarifications and concrete derivations to fill the gaps before handing the draft to the student.

### A. Notation and small fixes
- Be explicit at the start: use $\Lambda_k(n)$ for the higher von Mangoldt hierarchy, $\Psi_k(x)=\sum_{n\le x}\Lambda_k(n)$ for the corresponding partial sums, $\gamma_m$ for Stieltjes constants, and $\Lambda^*(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$ for the completed zeta factor (to avoid clash with arithmetic $\Lambda(n)$).
- In Section 3 (Main explicit formula) always state whether zeros $\rho$ are counted with multiplicity; the derivation below assumes simple zeros. Add an explicit remark when zeros are multiple (residue calculus requires higher-order residues).
- Minor typos fixed: replace ambiguous “polynomial corrections in \log x” with “polynomial factors in $\log x$ of degree $k$ (for simple zeros)”. Replace “residue expansions for $\Psi_k(x)$” with the Mellin + residue representation used in the text (explicit in Section 3).

### B. Explicit residue contribution from a simple zero (fill-in)

The draft states that each nontrivial zero $\rho$ contributes $x^\rho P_k(\rho,\log x)$ where $P_k$ is a polynomial of degree $k$. Here is an explicit, student-friendly derivation and closed-form for the simple-zero case.

Setup (simple zero $\rho$). Near a simple zero $\rho$ we have
\[
\zeta(s) \sim \zeta'(\rho)\,(s-\rho),\qquad
\frac{\zeta'(s)}{\zeta(s)} \sim \frac{1}{s-\rho}.
\]
Define the integrand
\[
I_k(s):=(-1)^k\frac{d^k}{ds^k}\!\Big(-\frac{\zeta'(s)}{\zeta(s)}\Big)\frac{x^s}{s}.
\]
A local expansion near $s=\rho$ gives (for a simple zero)
\[
(-1)^k\frac{d^k}{ds^k}\!\Big(-\frac{\zeta'}{\zeta}\Big)
\;\sim\; -\,k!\,(s-\rho)^{-(k+1)}.
\]
(See derivation note below.) Hence near $s=\rho$,
\[
I_k(s)\sim -k!\,\frac{x^s}{s}\,(s-\rho)^{-(k+1)}.
\]
To compute the residue at $s=\rho$ we expand the regular factors:
\[
\frac{x^s}{s} = \frac{x^\rho e^{(s-\rho)\log x}}{s}
= x^\rho\Big(\sum_{m\ge0}\frac{(\log x)^m}{m!}(s-\rho)^m\Big)\Big(\sum_{t\ge0}\frac{(-1)^t}{\rho^{t+1}}(s-\rho)^t\Big),
\]
since $\displaystyle \frac{1}{s}=\frac{1}{\rho+(s-\rho)}=\sum_{t\ge0}(-1)^t\frac{(s-\rho)^t}{\rho^{t+1}}$.

The residue is the coefficient of $(s-\rho)^{-1}$ in $-k!\,x^\rho\sum_{m,t\ge0}\frac{(\log x)^m}{m!}(-1)^t\rho^{-(t+1)}(s-\rho)^{m+t-(k+1)}$.
Set $m+t-(k+1)=-1$, i.e. $m+t=k$. Summing over $m=0,\dots,k$ gives

\[
\boxed{\;
\operatorname{Res}_{s=\rho} I_k(s)
= -k!\,x^\rho\sum_{m=0}^k \frac{(\log x)^m}{m!}\,(-1)^{\,k-m}\,\rho^{-(k-m+1)}
\;=\; x^\rho\;Q_{k,\rho}(\log x)
;}

where $Q_{k,\rho}$ is an explicit polynomial of degree $k$ in $\log x$.

Equivalently (reindex $j=k-m$),
\[
\boxed{\;
\operatorname{Res}_{s=\rho} I_k(s)
= x^\rho \sum_{j=0}^k (-1)^{j+1}\frac{k!}{(k-j)!}\,\frac{(\log x)^{\,k-j}}{\rho^{\,j+1}}.
\;}
\]

This provides the explicit closed form for the polynomial factor:
\[
P_k(\rho,\log x)=\sum_{j=0}^k (-1)^{j+1}\frac{k!}{(k-j)!}\,\frac{(\log x)^{\,k-j}}{\rho^{\,j+1}}.
\]

**Low‑k examples (useful for students):**
- $k=0$ (classical term):
  \[
  P_0(\rho)=-\frac{1}{\rho}\qquad\Rightarrow\qquad \text{contribution } -\frac{x^\rho}{\rho}.
  \]
- $k=1$:
  \[
  P_1(\rho,\log x)=-\frac{\log x}{\rho}+\frac{1}{\rho^2}\qquad\Rightarrow\qquad x^\rho\!\left(-\frac{\log x}{\rho}+\frac{1}{\rho^2}\right).
  \]
- $k=2$:
  \[
  P_2(\rho,\log x)
  = -\frac{2(\log x)^2}{\rho} + \frac{2\log x}{\rho^2} - \frac{2}{\rho^3},
  \]
  so the zero-term is $x^\rho P_2(\rho,\log x)$.

(Students can verify these by direct substitution into the residue-sum formula.)

*Derivation note.* The key sign and factorial factors above come from the identity for derivatives of a simple pole:
\[
\frac{d^k}{ds^k}\frac{1}{s-\rho}=(-1)^k\frac{k!}{(s-\rho)^{k+1}}.
\]
Careful tracking of the overall $(-1)^k$ factor in the definition of $\Lambda_k$ yields the negative sign in the residue above (and recovers the classical $k=0$ term $-x^\rho/\rho$).

### C. Improved proof sketch (explicit steps for the student)
1. Start from the Mellin inversion integral for $\Psi_k(x)$ (displayed in Section 3).
2. Justify moving the contour to $\Re(s)=\sigma$ with $\sigma<0$ using standard bounds on $(-1)^k d^k(-\zeta'/\zeta)$ and the $x^s/s$ kernel (briefly mention standard zero-free regions and growth bounds).
3. The pole at $s=1$ produces the polynomial main-term; compute its Laurent coefficients via the expansion of $\zeta(s)$ at 1 (Stieltjes constants appear here).
4. Each simple zero $\rho$ contributes by the residue computed in section B; for multiple zeros one must compute higher-order residues (student exercise).
5. Collect terms and bound the remaining integral on the left vertical contour; under RH move contour to $\Re(s)=1/2$ and apply standard zero-density / explicit zero bounds to get the conditional error term noted in the draft.

### D. Numerical guidance (fill-in for Section 4)
- For computing $\gamma_m$: use zeta evaluation near $s=1$ with high precision (mpmath or Arb). Two practical approaches:
  - Direct acceleration of the defining limit with Euler–Maclaurin smoothing.
  - Use precomputed high-precision tables for $\gamma_m$ for m up to, say, 10.
- For computing finite sums $\Psi_k(x)$: efficient method is to loop over prime powers $p^r\le x$ and add $(\log p)^{k+1} r^k$. This is far faster than summing over all integers.
- For the zero-sum: use a table of first 100 nontrivial zeros (e.g., Odlyzko tables or mpmath zeros). Compute $x^\rho P_k(\rho,\log x)$ and sum conjugate pairs for real values to get real oscillatory corrections.
- Precision notes: when $x$ is large, $x^\rho$ becomes highly oscillatory; use arbitrary precision and sum zeros in pairs to reduce cancellation error.

### E. Suggested student exercises (concrete)
1. Derive $P_1(\rho,\log x)$ and verify numerically for $k=1$ and the first zero $\rho\approx 1/2+14.1347 i$ at moderate $x$ (e.g., $x=10^3$).
2. Implement a routine that computes $\Psi_k(x)$ via prime-power enumeration and compare with $M_k(x)$ for $k=0,1,2$ up to $x=10^5$; plot the difference and overlay the contribution from the first 10 zeros.
3. Show how multiple zero multiplicity changes the residue computation (exercise in higher-order residues).

---

## Minor editorial suggestions (style / pedagogy)
- Move the canonical notation table (Appendix A) earlier (immediately after Introduction) so students are never confused by overloaded symbols.
- Add a one‑paragraph "intuition" box about why differentiation of $-\zeta'/\zeta$ produces $(\log n)^k$ weights (connect to Dirichlet series termwise differentiation).
- For presentation: separate the analytic derivation (Section 3) from computational implementation (Section 4) with a small "bridging" paragraph that explains how residues translate into computable finite sums over zeros.

---

## 6. References & resources

- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford, 1986.
- H. Davenport, *Multiplicative Number Theory*, 3rd ed., Springer, 2000.
- H. Iwaniec & E. Kowalski, *Analytic Number Theory*, AMS, 2004.
- C. Knessl & M. Coffey, “An effective asymptotic formula for the Stieltjes constants,” Math. Comp. 80 (2011).
- D. England, *Notes on von Mangoldt hierarchies and cumulant structures*, 2025 (in preparation).

---

## Appendix A — quick formula summary (canonical notation)

- Completed zeta (analytic factor): denote $\Lambda^*(s):=\pi^{-s/2}\Gamma(s/2)\zeta(s)$ (avoid clash with von Mangoldt $\Lambda(n)$).
- Digamma: $\psi(s)=\Gamma'(s)/\Gamma(s)$.
- Chebyshev (prime sum): use $\Psi(x)=\sum_{n\le x}\Lambda(n)$ to avoid symbol clash with digamma.

---

## Explicit polynomials $P_k(\rho,\log x)$ — corrected table and general formula

Recall from the residue computation (Section 3, Peer‑review notes) the general closed form for a simple zero $\rho$:
$$
P_k(\rho,\log x)
= \sum_{j=0}^k (-1)^{\,j+1}\frac{k!}{(k-j)!}\,\frac{(\log x)^{\,k-j}}{\rho^{\,j+1}}.
\tag{★}
$$

Below is a ready‑to‑use table of $P_k$ for small $k$ (useful for exercises and numeric checks). These follow from (★) and assume $\rho$ is a simple zero.

| k | $P_k(\rho,\log x)$ |
|---:|:---|
| 0 | $-\dfrac{1}{\rho}$ |
| 1 | $-\dfrac{\log x}{\rho}+\dfrac{1}{\rho^2}$ |
| 2 | $-\dfrac{(\log x)^2}{\rho}+\dfrac{2\log x}{\rho^2}-\dfrac{2}{\rho^3}$ |
| 3 | $-\dfrac{(\log x)^3}{\rho}+\dfrac{3(\log x)^2}{\rho^2}-\dfrac{6\log x}{\rho^3}+\dfrac{6}{\rho^4}$ |
| 4 | $-\dfrac{(\log x)^4}{\rho}+\dfrac{4(\log x)^3}{\rho^2}-\dfrac{12(\log x)^2}{\rho^3}+\dfrac{24\log x}{\rho^4}-\dfrac{24}{\rho^5}$ |
| 5 | $-\dfrac{(\log x)^5}{\rho}+\dfrac{5(\log x)^4}{\rho^2}-\dfrac{20(\log x)^3}{\rho^3}+\dfrac{60(\log x)^2}{\rho^4}-\dfrac{120\log x}{\rho^5}+\dfrac{120}{\rho^6}$ |

Notes and usage
- Each residue contribution for a simple zero is $x^\rho P_k(\rho,\log x)$. Sum conjugate pairs to obtain real corrections when $x$ is real.
- For multiple zeros of multiplicity $m>1$, higher‑order residues are required; the polynomial degree in $\log x$ increases accordingly (exercise for the student).
- The general formula (★) gives the coefficient of $(\log x)^{k-j}$ as $(-1)^{j+1} k!/(k-j)! \cdot \rho^{-(j+1)}$; implement directly in code to avoid algebra mistakes.

Numeric/implementation tip
- Compute $P_k$ symbolically once (or generate coefficients programmatically via factorials) and reuse for each $\rho$.
- When summing $x^\rho P_k(\rho,\log x)$ numerically, sum conjugate pairs $x^\rho P_k+\overline{x^\rho P_k}$ to reduce cancellation error and keep results real.

---

*Instructor note:* this file is now Markdown + KaTeX friendly. For lecture slides and notebooks, extract Sections 3 and 4 as exercises.