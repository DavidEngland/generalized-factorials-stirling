# J(x) = ∑_{n≥1} π(x^{1/n})/n and its Mellin transform — detailed note

Goal: treat
\[
J(x)\;=\;\sum_{n\ge1}\frac{1}{n}\,\pi\!\big(x^{1/n}\big)
=\sum_{p^k\le x}\frac{1}{k}
=\sum_{n\le x}\frac{\Lambda(n)}{\log n},
\]
compute its Mellin transform, state domains of validity, give the inversion, and explain how explicit‑formula terms (main term, zero contributions) arise. Provide practical remarks and known/conjectural consequences.

## 1. Equivalent representations and basic identities

- By unfolding the definition of $\pi(y)$,
  \[
  J(x)=\sum_{n\ge1}\frac{1}{n}\sum_{p\le x^{1/n}}1
  =\sum_{p}\sum_{k\ge1\ :\ p^k\le x}\frac{1}{k}
  =\sum_{p^k\le x}\frac{1}{k}.
  \]
- Using $\Lambda(n)$ (supported on prime powers) and $\log n=k\log p$ for $n=p^k$,
  \[
  \frac{\Lambda(n)}{\log n}=\frac{1}{k}\quad\text{when }n=p^k.
  \]
  Hence the compact identity
  \[
  \boxed{\,J(x)=\sum_{n\le x}\frac{\Lambda(n)}{\log n}\, }.
  \]

## 2. Mellin transform (direct computation)

Consider
\[
I(s):=\int_{0}^{\infty} J(x)\,x^{-s-1}\,dx.
\]
For $\Re(s)>1$ we may interchange sum and integral (absolute convergence justified below):

\[
\begin{aligned}
I(s)
&=\sum_{n\ge1}\frac{\Lambda(n)}{\log n}\int_{n}^{\infty} x^{-s-1}\,dx
= \sum_{n\ge1}\frac{\Lambda(n)}{\log n}\,\frac{n^{-s}}{s} \\
&=\frac{1}{s}\sum_{n\ge1}\frac{\Lambda(n)}{\log n}\,n^{-s}.
\end{aligned}
\]

But for $\Re(s)>1$ the Dirichlet series satisfies
\[
\log\zeta(s)=\sum_{p}\sum_{k\ge1}\frac{1}{k}p^{-ks}
=\sum_{n\ge2}\frac{\Lambda(n)}{\log n}\,n^{-s},
\]
so (including $n=1$ harmlessly)
\[
\boxed{\,I(s)=\frac{1}{s}\log\zeta(s),\qquad \Re(s)>1.\,}
\]

Convergence remarks:
- Small $x$: $J(x)=0$ for $x<2$, so no singularity at $0$.
- Large $x$: $J(x)\asymp\pi(x)\sim x/\log x$ heuristically, forcing $\Re(s)>1$ for convergence of the Mellin integral.
- The identity above is valid in the half‑plane of absolute convergence $\Re(s)>1$ and extends by analytic continuation of $\log\zeta(s)$ (with branch choices).

## 3. Mellin inversion and the explicit‑formula viewpoint

Mellin inversion (for $c>1$) gives
\[
J(x)=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}\frac{1}{s}\log\zeta(s)\,x^{s}\,ds.
\]

Deforming the contour left (standard explicit‑formula technique) picks up contributions from the singularities of the integrand:

- The pole of $\zeta(s)$ at $s=1$ makes $\log\zeta(s)$ have a logarithmic singularity near $s=1$; careful local analysis yields the main term of prime counting (the logarithmic integral $\operatorname{li}(x)$ appears naturally after handling the $1/s$ factor).
- Nontrivial zeros $\rho$ of $\zeta(s)$ cause zeros of $\zeta$ and hence branch points for $\log\zeta$; passing the contour over these produces oscillatory contributions of the form (heuristically)
  \[
  -\sum_{\rho} \operatorname{Li}(x^{\rho}) + \text{(conjugate pairing gives real oscillations)},
  \]
  where $\operatorname{Li}$ denotes the logarithmic integral (analytically continued).
- Trivial zeros and poles at negative integers contribute smaller explicit correction terms.

Thus one recovers the classical Riemann‑type explicit formula for prime counting functions; for $J(x)$ the formula is the logarithmic analogue of the explicit formula for $\pi(x)$:
\[
\boxed{\,J(x)=\operatorname{li}(x)-\sum_{\rho}\operatorname{li}(x^{\rho}) + \text{(known elementary corrections)}\,}
\]
(valid once branch choices and principal values are fixed). Precise constant terms (e.g. $-\log 2$ or contributions from $s=0$) appear in the full, carefully derived formula.

## 4. Relation to Ψ(x) and other summatory functions

- The Chebyshev sum $\Psi(x)=\sum_{n\le x}\Lambda(n)$ has Mellin transform
  \[
  \int_0^\infty \Psi(x)x^{-s-1}\,dx = -\frac{1}{s}\frac{\zeta'(s)}{\zeta(s)},\qquad \Re(s)>1.
  \]
- Differentiation relates $I(s)=(1/s)\log\zeta(s)$ and the $\Psi$ transform:
  \[
  \frac{d}{ds}\big(s I(s)\big)=\frac{d}{ds}\log\zeta(s)=\frac{\zeta'(s)}{\zeta(s)}.
  \]
  This shows the transforms of $J$ and $\Psi$ are tightly linked: roughly, $\Psi$ corresponds to the logarithmic derivative, while $J$ corresponds to the logarithm itself.

## 5. Analytic continuation, branch choices, and rigor

- $\log\zeta(s)$ must be defined with a chosen branch cut; zeros of $\zeta$ introduce branch points. For contour deformations one uses a consistent determination of $\arg\zeta(s)$ and principal value integrals; classical treatments use symmetric contours and pairing of conjugate zeros to obtain real results.
- The explicit formula derivation requires justifying:
  - (i) contour shifts (growth estimates for $\log\zeta(s)$ and $1/s$ on vertical lines),
  - (ii) handling of cuts near zeros,
  - (iii) contributions at infinity vanish (or are controlled).
  Standard references (Titchmarsh, Edwards) handle these technicalities.

## 6. Known results, asymptotics, and relations to RH

- Main term: under standard analytic methods one gets $J(x)\sim\operatorname{li}(x)$ as $x\to\infty$.
- Error terms: the Riemann Hypothesis (RH) is equivalent to strong error bounds in explicit formulas; for example, under RH the oscillatory sum is bounded to give classical strong estimates for prime counting. Concretely, one gets for $\pi(x)$ or related sums $O(x^{1/2}\log x)$ type remainders; analogous bounds hold for $J(x)$.
- Information content: because $I(s)=(1/s)\log\zeta(s)$, the zeros of $\zeta$ control oscillations in $J$ just as they do for $\pi$ and $\Psi$.

## 7. Practical / numerical considerations

- Numeric inversion: evaluate the truncated inverse Mellin integral; subtract main term and add finite zero sum (paired zeros) for accuracy. Use high precision and careful summation order.
- Regularization: near $s=1$ one can subtract the singular part (main term) analytically and invert the residual numerically.
- Computation of log ζ: use high‑precision zeta evaluation and continuous choice of argument along the contour; Odlyzko/Riemann zero tables are standard inputs.

## 8. What is known vs plausible conjectures

- Known: identity $I(s)=(1/s)\log\zeta(s)$ for $\Re(s)>1$; Mellin inversion and derivation of explicit formulas are classical and rigorous when handled with care.
- Known: asymptotics $J(x)\sim\operatorname{li}(x)$ and relation to prime distribution.
- Conjectural: fine cancellation in the zero‑sum is governed by RH; precise distribution of oscillations depends on zero statistics (random matrix heuristics predict fluctuations).
- Plausible research directions: use the $J\leftrightarrow\log\zeta$ viewpoint to study linear relations among Stieltjes constants (via expansions at $s=1$), or to design smoothed explicit formulas by modifying the Mellin kernel (weighting improves numerical convergence).

## 9. References and further reading

- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function* (2nd ed.), Oxford.
- H. Edwards, *Riemann's Zeta Function*, Dover.
- A. Odlyzko, tables of zeros (for numerical experiments).
- Expository sources on the explicit formula for $\pi(x)$ and $\Psi(x)$.

---

**Takeaway:** the weighted prime counting function $J(x)=\sum_{p^k\le x}1/k$ has Mellin transform $(1/s)\log\zeta(s)$ for $\Re(s)>1$. Mellin inversion and contour deformation produce the familiar explicit‑formula decomposition: a smooth main term (logarithmic integral) plus oscillatory contributions driven by zeta zeros. Analytical care (branch choice for $\log\zeta$, contour estimates) is required for full rigor; numerically, subtract the main term and add a truncated zero sum (paired conjugates) for accurate reconstructions.
