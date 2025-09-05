# The Weierstrass formulation for the reciprocal factorial function

## Abstract

We present a concise derivation of the Weierstrass product for the reciprocal factorial function \(1/s!\), viewed as the entire function \(1/\Gamma(s+1)\). Using the Weierstrass factorization theorem and the known zero set at the negative integers, we obtain
\[
\frac{1}{\Gamma(s+1)} \;=\; e^{\gamma s} \prod_{n=1}^{\infty} \left(1+\frac{s}{n}\right) e^{-s/n},
\]
where \(\gamma\) is the Euler–Mascheroni constant. Taking logarithmic derivatives yields an identity linking this product to the digamma function: \(\frac{d}{ds}\log(1/\Gamma(s+1))=-\psi(s+1)\). We briefly discuss convergence, growth (order and genus), and several natural extensions.

---

## Introduction

The factorial function extends to the complex plane via \(\Gamma(s+1)\), and its reciprocal \(1/\Gamma(s+1)\) is an entire function whose zeros encode the poles of \(\Gamma\). Since entire functions are determined (up to an exponential factor) by their zeros, the Weierstrass factorization theorem gives a canonical infinite product for \(1/\Gamma(s+1)\). This product reveals both the zero structure and the growth of the function and leads, upon logarithmic differentiation, to a clean expression for the digamma function.

---

## Preliminaries

- **Gamma and reciprocal factorial:**
  \[
  s! = \Gamma(s+1)\quad\text{for}\quad s\in\mathbb{N}_0,\qquad \frac{1}{s!}=\frac{1}{\Gamma(s+1)}.
  \]

- **Zeros of \(1/\Gamma(s+1)\):**
  \[
  \Gamma(s+1) \text{ has simple poles at } s=-n\ (n\in\mathbb{N}),\quad\Rightarrow\quad \frac{1}{\Gamma(s+1)} \text{ has simple zeros at } s=-n,
  \]
  and no zero at \(s=0\) since \(1/\Gamma(1)=1\).

- **Weierstrass primary factors:**
  For genus \(p=1\),
  \[
  E_1(z)=(1-z)e^{z}.
  \]
  Genus \(1\) is appropriate here because \(\sum_{n=1}^{\infty} \frac{1}{n}\) diverges while \(\sum_{n=1}^{\infty} \frac{1}{n^2}\) converges, ensuring convergence of the product with \(E_1\)-factors.

---

## Weierstrass product and constant determination

### Product representation

By the Weierstrass factorization theorem, an entire function with zeros at \(\{-n\}_{n\ge 1}\) and no zero at \(0\) admits a product of the form
\[
\frac{1}{\Gamma(s+1)} \;=\; e^{g(s)} \prod_{n=1}^{\infty} E_1\!\left(\frac{s}{-n}\right)
\;=\; e^{g(s)} \prod_{n=1}^{\infty} \left(1+\frac{s}{n}\right) e^{-s/n},
\]
for some entire function \(g(s)\) of degree at most \(1\) (Hadamard factorization). Hence \(g(s)=\alpha s + \beta\).

### Determining \(\alpha,\beta\)

- **Normalization at \(s=0\):**
  \[
  \frac{1}{\Gamma(1)}=1 \quad\Rightarrow\quad e^{g(0)}=1 \quad\Rightarrow\quad \beta=0.
  \]

- **Coefficient of \(s\):**
  Comparing the standard Hadamard form for \(1/\Gamma\) (or differentiating at \(s=0\)) yields \(\alpha=\gamma\), the Euler–Mascheroni constant. Consequently,
  \[
  \frac{1}{\Gamma(s+1)} \;=\; e^{\gamma s} \prod_{n=1}^{\infty} \left(1+\frac{s}{n}\right) e^{-s/n}.
  \]

---

## Logarithmic derivative and the digamma function

Taking logarithms,
\[
\log\!\left(\frac{1}{\Gamma(s+1)}\right)
= \gamma s + \sum_{n=1}^{\infty} \left[\log\!\left(1+\frac{s}{n}\right) - \frac{s}{n}\right].
\]
Differentiating termwise in the natural domain of uniform convergence:
\[
\frac{d}{ds}\log\!\left(\frac{1}{\Gamma(s+1)}\right)
= \gamma + \sum_{n=1}^{\infty}\left(\frac{1}{n+s}-\frac{1}{n}\right)
= \gamma - \sum_{n=1}^{\infty} \frac{s}{n(n+s)}.
\]
Since \(\psi(s)=\frac{d}{ds}\log\Gamma(s)\), we have
\[
\frac{d}{ds}\log\!\left(\frac{1}{\Gamma(s+1)}\right)
= -\frac{d}{ds}\log\Gamma(s+1)
= -\psi(s+1).
\]
Thus the Weierstrass product directly recovers the classical series representation for the digamma function.

---

## Convergence, growth, and asymptotics

- **Convergence and genus:**
  The zero sequence \(\{-n\}\) has exponent of convergence \(1\). Therefore, genus \(1\) primary factors \(E_1\) are necessary and sufficient for uniform convergence on compacta. The resulting entire function has order \(1\).

- **Growth and the role of \(\gamma\):**
  The exponential factor \(e^{\gamma s}\) adjusts the linear term in the exponent so that the product matches the local behavior at the origin and ensures the correct normalization. It also aligns the logarithmic derivative with \(-\psi(s+1)\).

- **Asymptotics via Stirling:**
  Stirling’s formula,
  \[
  \log\Gamma(s+1) \sim \left(s+\tfrac{1}{2}\right)\log s - s + \tfrac{1}{2}\log(2\pi) \quad (|s|\to\infty,\ |\arg s|<\pi),
  \]
  implies
  \[
  \log\!\left(\frac{1}{\Gamma(s+1)}\right) \sim -\left(s+\tfrac{1}{2}\right)\log s + s - \tfrac{1}{2}\log(2\pi),
  \]
  consistent with the order and genus indicated by the Weierstrass product.

---

## Extensions and related structures

- **Shifted products:**
  The classical Hadamard product for \(1/\Gamma(s)\) is
  \[
  \frac{1}{\Gamma(s)} = s\, e^{\gamma s} \prod_{n=1}^{\infty} \left(1+\frac{s}{n}\right) e^{-s/n},
  \]
  and shifting \(s\mapsto s\!+\!1\) yields the result for \(1/\Gamma(s+1)\).

- **Polygamma relations:**
  Higher derivatives of the logarithm of the Weierstrass product produce the polygamma functions:
  \[
  \frac{d^m}{ds^m}\log\Gamma(s+1) = \psi^{(m-1)}(s+1),\qquad m\ge 1.
  \]

- **Hypergeometric and Pochhammer symbols:**
  Similar products arise for reciprocal Pochhammer symbols \((a)_s^{-1}\) and, more generally, in the theory of hypergeometric functions, where gamma ratios and their zeros/poles control analytic structure.

---

## References

- Abramowitz, M., and Stegun, I. A. (eds.). Handbook of Mathematical Functions. Dover.
- Remmert, R. Classical Topics in Complex Function Theory. Springer.
- Titchmarsh, E. C. The Theory of Functions. Oxford University Press.
- Whittaker, E. T., and Watson, G. N. A Course of Modern Analysis. Cambridge University Press.
- Artin, E. The Gamma Function. Holt, Rinehart and Winston.