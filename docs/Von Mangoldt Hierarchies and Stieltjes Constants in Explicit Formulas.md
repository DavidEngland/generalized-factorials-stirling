📘 Draft Preprint: Von Mangoldt Hierarchies and Stieltjes Constants in Explicit Formulas

Author: [Student Name]
Advisor: David England
Date: October 2025

⸻

Abstract

We develop and formalize higher-order generalizations of the von Mangoldt function arising from derivatives of the logarithmic derivative of the Riemann zeta function. These “von Mangoldt hierarchies” \Lambda_k(n) admit Dirichlet series
(-1)^k\frac{d^k}{ds^k}\!\Big(-\frac{\zeta’(s)}{\zeta(s)}\Big)=\sum_{n\ge1}\frac{\Lambda_k(n)}{n^s},
and satisfy explicit prime-power formulas \Lambda_k(p^r)=(\log p)^{k+1}r^k.
We derive residue expansions for
\Psi_k(x)=\sum_{n\le x}\Lambda_k(n),
obtaining main terms involving Stieltjes constants \gamma_m and polynomial corrections in \log x. We present both conditional (under the Riemann Hypothesis) and unconditional estimates for the error terms. Connections with the cumulant interpretation of Stieltjes constants and their relation to the prime number distribution are discussed.

⸻

1. Introduction

The classical von Mangoldt function \Lambda(n) encodes prime powers via
-\frac{\zeta’(s)}{\zeta(s)}=\sum_{n\ge1}\frac{\Lambda(n)}{n^s},\qquad \Re(s)>1.
Its partial sums \Psi(x)=\sum_{n\le x}\Lambda(n) lie at the heart of the explicit formula relating primes and zeros of the Riemann zeta function.

Differentiating the logarithmic derivative of \zeta(s) introduces powers of \log n:
\frac{d^k}{ds^k}\,n^{-s}=(-\log n)^k n^{-s}.
Thus each successive derivative yields a weighted von Mangoldt function emphasizing logarithmic moments of prime powers. These “von Mangoldt hierarchies” provide a natural framework to study higher-order interactions between zeros, logarithmic derivatives, and the Laurent expansion coefficients of \zeta(s).

The Stieltjes constants \gamma_m, defined by the Laurent expansion
\zeta(1+u)=\frac{1}{u}+\sum_{m\ge0}\frac{(-1)^m\gamma_m}{m!}u^m,
emerge naturally in the residue computations of \Psi_k(x). This establishes a hierarchy linking the analytic structure of \zeta(s) at s=1 with logarithmic weighting in the prime domain.

⸻

2. Preliminaries

2.1. Definitions

For integer k\ge0, define
\Lambda_k(n)\quad\text{by}\quad (-1)^k\frac{d^k}{ds^k}\!\left(-\frac{\zeta’(s)}{\zeta(s)}\right)=\sum_{n\ge1}\frac{\Lambda_k(n)}{n^s}.

By differentiating the Euler product,
-\frac{\zeta’(s)}{\zeta(s)}=\sum_{p}\frac{\log p}{p^s-1},
one obtains the explicit form:
\boxed{\Lambda_k(p^r)=(\log p)^{k+1}r^k,\quad r\ge1,}
and \Lambda_k(n)=0 otherwise.

2.2. Dirichlet series relations

Note that \Lambda_0(n)=\Lambda(n), and for all k,
\Lambda_k(n)=(\log n)^k(\Lambda*\log^{k})(n),
where  denotes Dirichlet convolution and \log^{*k} is the k-fold convolution power of the logarithm sequence.

2.3. Stieltjes constants

The Stieltjes constants satisfy
\gamma_m=\lim_{N\to\infty}\Bigg(\sum_{n=1}^N\frac{(\log n)^m}{n}-\frac{(\log N)^{m+1}}{m+1}\Bigg).
Their exponential generating function is
G(t)=\sum_{m\ge0}\frac{\gamma_m}{m!}t^m=\zeta(1-t)+\frac{1}{t}.

⸻

3. Main Theorem (Conditional Explicit Formula)

Theorem 1 (Conditional explicit formula for \Psi_k(x)).
For k\ge0, define
\Psi_k(x)=\sum_{n\le x}\Lambda_k(n).
Then for any c>1,
\Psi_k(x)=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}(-1)^k\frac{d^k}{ds^k}\!\Big(-\frac{\zeta’(s)}{\zeta(s)}\Big)\frac{x^s}{s}\,ds.
Shifting the contour to the left and summing residues yields
\Psi_k(x)=x(\log x)^k-\sum_{m=0}^{k}\binom{k}{m}\gamma_m x(\log x)^{k-m}
+\sum_{\rho}x^{\rho}P_k(\rho,\log x)+O(1),
where the sum runs over nontrivial zeros \rho of \zeta(s), and P_k is an explicit polynomial of degree k with coefficients depending on \rho and \gamma_m.
Under the Riemann Hypothesis,
\Psi_k(x)=x(\log x)^k+O\!\big(x^{1/2}\log^{k+2}x\big).

Proof Sketch. Differentiating under the integral sign and applying Cauchy’s theorem isolates the residue at s=1, whose Laurent expansion coefficients involve the \gamma_m. Nontrivial zeros \rho contribute oscillatory secondary terms x^{\rho} times polynomials in \log x.

⸻

4. Computational Implementation
	•	Objective: Numerically verify the first few coefficients of the residue expansion and the oscillatory behavior of the zero terms.
	•	Method:
	1.	Compute \gamma_m using high-precision zeta evaluation near s=1.
	2.	Evaluate truncated sums \Psi_k(x) for k=0,1,2 up to x\le10^6.
	3.	Compare with main-term predictions:
M_k(x)=x(\log x)^k-\sum_{m=0}^{k}\binom{k}{m}\gamma_m x(\log x)^{k-m}.
	4.	Plot \Psi_k(x)-M_k(x) and observe oscillations at frequencies matching the first zeta zeros.

Expected outcomes: confirmation of the sign pattern and amplitude predicted by the first few nontrivial zeros.

⸻

5. Discussion and Future Work

5.1. Cumulant interpretation

Interpreting \gamma_m as cumulants of the prime-log distribution suggests that the moments of the corresponding random variable (if it exists) would be obtained via Bell polynomials:
\mu_n=B_n(\gamma_1,\gamma_2,\dots,\gamma_n).
Clarifying the probabilistic object behind this formalism remains open.

5.2. Open problems
	1.	Error term dependence on k: Obtain uniform bounds for \Psi_k(x) as k\to\infty.
	2.	Asymptotics of Stieltjes constants: rigorous estimates extending Knessl–Coffey results.
	3.	Functional field analogues: define and test \Lambda_k analogues in \mathbb{F}_q[T] for exact verification.
	4.	Spectral interpretation: explore whether the hierarchy corresponds to derivatives of the Selberg trace or spectral cumulants.

⸻

References
	1.	E.C. Titchmarsh, The Theory of the Riemann Zeta-Function, 2nd ed., Oxford Univ. Press, 1986.
	2.	H. Davenport, Multiplicative Number Theory, 3rd ed., Springer GT, 2000.
	3.	H. Iwaniec, E. Kowalski, Analytic Number Theory, AMS Coll. Publ., 2004.
	4.	C. Knessl, M. Coffey, “An effective asymptotic formula for the Stieltjes constants,” Math. Comp. 80 (2011).
	5.	A. Granville, Analytic number theory lectures, available notes (various sources).
	6.	D. England (ed.), Notes on von Mangoldt hierarchies and cumulant structures, 2025.

⸻

Advisor’s Note

The student is encouraged to focus first on completing Section 4 (numerical confirmation) and Section 3 (residue derivations for k=0,1,2). Section 5 and the probabilistic framing may be expanded once empirical results are validated.

⸻