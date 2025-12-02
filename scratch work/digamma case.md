## Digamma Function Half-Shift Identity

### The Identity

For the digamma function $\psi(x) = \frac{d}{dx}\ln\Gamma(x)$, we examine:

$$\psi\left(x + \frac{1}{2}\right) - \psi(x)$$

### Using the Duplication Formula

From the duplication formula for the digamma function:
$$\psi(2z) = \frac{1}{2}\psi(z) + \frac{1}{2}\psi\left(z + \frac{1}{2}\right) + \ln 2$$

Solving for $\psi(z + \frac{1}{2}) - \psi(z)$:
$$\psi\left(x + \frac{1}{2}\right) - \psi(x) = 2\psi(2x) - 2\psi(x) - 2\ln 2$$

### Series Representation

Using the series expansion:
$$\psi\left(x + \frac{1}{2}\right) - \psi(x) = -2\ln 2 + 2\sum_{k=0}^{\infty}\left(\frac{1}{2k+1} - \frac{1}{2x + 2k + 1}\right)$$

### Special Cases

For positive integers $n$:
$$\psi\left(n + \frac{1}{2}\right) - \psi(n) = -2\ln 2 + 2\left(1 + \frac{1}{3} + \frac{1}{5} + \cdots + \frac{1}{2n-1}\right) - 2H_n$$

where $H_n = \sum_{k=1}^{n}\frac{1}{k}$ is the $n$-th harmonic number.

### Connection to Previous Identity

Note that this is related to our earlier identity. For integer $n$:
$$\psi\left(\frac{n+1}{2}\right) - \psi\left(\frac{n}{2}\right) = \frac{2}{n}$$

which gives a simpler constant result for that specific shift pattern.

---

## The Pairing Result and the Power Pitfall

### A Critical Warning About Divergent Series

Define the sequence:
$$a_n = \psi\left(\frac{n+1}{2}\right) - \psi\left(\frac{n}{2}\right) - \frac{1}{n}$$

From our earlier identity, we know that $\psi\left(\frac{n+1}{2}\right) - \psi\left(\frac{n}{2}\right) = \frac{2}{n}$, so:
$$a_n = \frac{2}{n} - \frac{1}{n} = \frac{1}{n}$$

The sum $\sum_{n=1}^{\infty} a_n = \sum_{n=1}^{\infty} \frac{1}{n}$ **diverges** (harmonic series).

**WARNING:** Any manipulation of this divergent series requires careful justification. The "pairing result" that follows is only valid in the sense of **Cesàro summation** or similar regularization methods.

### The Pairing Interpretation (Cesàro Sum)

When we pair consecutive terms and consider partial sums:
$$S_N = \sum_{n=1}^{2N} a_n = \sum_{k=1}^{N}\left(a_{2k-1} + a_{2k}\right) = \sum_{k=1}^{N}\left(\frac{1}{2k-1} - \frac{1}{2k}\right)$$

This partial sum **does** converge to $\ln 2$ as $N \to \infty$:
$$\lim_{N \to \infty} S_{2N} = \ln 2$$

However, $\lim_{N \to \infty} S_N$ does not exist (the harmonic series diverges).

The value $\ln 2$ is obtained through a specific grouping (Cesàro-type regularization), not from the ordinary sum. This is a **conditional** or **regularized** sum, not an absolute convergence.

### Why Powering Changes Everything

Consider the powered series:
$$\sum_{n=1}^{\infty} a_n^{2014} = \sum_{n=1}^{\infty} \frac{1}{n^{2014}} = \zeta(2014)$$

Since $a_n = \frac{1}{n}$ exactly, and the exponent $2014 > 1$, this series **converges absolutely** to $\zeta(2014)$.

**Key distinction:**
- Original series: divergent, but regularizes to $\ln 2$ under specific pairing
- Powered series: absolutely convergent to $\zeta(2014)$
- No relationship: $\zeta(2014) \neq (\ln 2)^{2014}$

**Conclusion:** The powered sum equals $\zeta(2014)$, **not** $(\ln 2)^{2014}$. The regularized value from conditional summation is not preserved under nonlinear operations like powering. This illustrates a fundamental principle: **regularization methods are not compatible with nonlinear transformations**.

---
## Original Problem and Critique

### Problem Statement

Evaluate using only series manipulation:

$$\sum_{n=1}^{\infty} \left(\psi\left(\frac{n+1}{2}\right)-\psi\left(\frac{n}{2}\right)-\frac{1}{n}\right)$$

**Supplementary Questions:**

1. Alternating version:
$$\sum_{n=1}^{\infty} (-1)^{n+1} \left(\psi\left(\frac{n+1}{2}\right)-\psi\left(\frac{n}{2}\right)-\frac{1}{n}\right)$$

2. Powered version:
$$\sum_{n=1}^{\infty} \left(\psi\left(\frac{n+1}{2}\right)-\psi\left(\frac{n}{2}\right)-\frac{1}{n}\right)^{2014}$$

---

### Critical Analysis of the Reference Answer

**Grade: D+ (Conditionally passing, but with major issues)**

#### What the Reference Answer Gets Right:

The pairing calculation is algebraically correct:
$$a_{2k-1} + a_{2k} = \frac{1}{2k-1} - \frac{1}{2k}$$

And the limit of even partial sums is correct:
$$\lim_{N \to \infty} \sum_{k=1}^{N}\left(\frac{1}{2k-1} - \frac{1}{2k}\right) = \ln 2$$

#### Critical Flaws:

**1. The series DIVERGES**

Since $a_n = \frac{1}{n}$, the series $\sum_{n=1}^{\infty} a_n$ is the harmonic series, which **diverges to infinity**. The answer "$\ln 2$" is only valid under specific regularization.

**2. Unjustified Rearrangement**

The reference answer rearranges terms of a divergent series without justification. By the **Riemann Rearrangement Theorem**, divergent series can be rearranged to give any value or diverge. The pairing used is a specific grouping that gives a Cesàro-type sum.

**3. Missing Context**

The answer should explicitly state:
- The ordinary sum does not exist
- The value $\ln 2$ is a **regularized** or **conditionally summed** value
- This requires pairing consecutive terms specifically as $(a_1 + a_2) + (a_3 + a_4) + \cdots$

#### Correct Statement:

The series **diverges**, but admits the Cesàro sum:
$$\lim_{N \to \infty} \frac{1}{N}\sum_{n=1}^{N} S_n = \ln 2$$

or equivalently, the limit of even partial sums:
$$\lim_{N \to \infty} S_{2N} = \ln 2$$

---

## Evaluation of “GIVEN ANSWER”

### Exact identity
Using the digamma recurrence,
$$\psi\left(\frac{n+1}{2}\right)-\psi\left(\frac{n}{2}\right)=\frac{2}{n},$$
so
$$A_n=\psi\left(\frac{n+1}{2}\right)-\psi\left(\frac{n}{2}\right)-\frac{1}{n}=\frac{1}{n}.$$

### Issues in the given derivation
- Interchanging the order of summation on
  $$\sum_{n=1}^\infty A_n=\sum_{n=1}^\infty \frac{1}{n}$$
  is invalid: the series **diverges**. Rearrangement and telescoping without a regularization framework (e.g., Abel/Cesàro) is not permissible.
- The claimed alternating result
  $$\sum_{n=1}^\infty(-1)^{n+1}A_n=1-\ln 2$$
  is **incorrect**. Since $A_n=1/n$, one has
  $$\sum_{n=1}^\infty(-1)^{n+1}\frac{1}{n}=\ln 2.$$
- The power-series claim “essentially equal to $(2\ln 2-1)^{2014}$” is **incorrect**. With $A_n=1/n$,
  $$\sum_{n=1}^\infty A_n^{2014}=\sum_{n=1}^\infty \frac{1}{n^{2014}}=\zeta(2014),$$
  which converges absolutely and is not expressible via $(\ln 2)^{2014}$ or the first term.

### Correct conclusions
- Ordinary sum: $\sum_{n=1}^\infty A_n=\sum_{n=1}^\infty \frac{1}{n}$ diverges.
- Alternating sum: $\sum_{n=1}^\infty(-1)^{n+1}A_n=\ln 2$ (standard alternating harmonic series).
- Powered sum: $\sum_{n=1}^\infty A_n^{2014}=\zeta(2014)$.

### Note on regularization
If one groups as $(A_1+A_2)+(A_3+A_4)+\cdots$, the even partial sums tend to $\ln 2$. This is a **regularized** value (via specific pairing/Cesàro), not the ordinary sum of the divergent series.

---

### Answers to Supplementary Questions

#### 1. Alternating Version

$$\sum_{n=1}^{\infty} (-1)^{n+1} a_n = \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} = \ln 2$$

This series **converges absolutely** by the alternating series test. The value is genuinely $\ln 2$ without any regularization needed.

#### 2. Powered Version

$$\sum_{n=1}^{\infty} a_n^{2014} = \sum_{n=1}^{\infty} \frac{1}{n^{2014}} = \zeta(2014)$$

This series **converges absolutely** for any exponent $> 1$.

**Critical Point:** $\zeta(2014) \neq (\ln 2)^{2014}$

The regularized value from the divergent series is **not preserved** under nonlinear operations.

---

### Pedagogical Summary

**The Three Series:**

| Series | Convergence | Value |
|--------|-------------|-------|
| $\sum a_n$ | Divergent | $\ln 2$ (Cesàro/regularized) |
| $\sum (-1)^{n+1} a_n$ | Absolutely convergent | $\ln 2$ (ordinary sum) |
| $\sum a_n^{2014}$ | Absolutely convergent | $\zeta(2014)$ |

**Key Lesson:** Regularization methods (Cesàro, Abel, etc.) assign values to divergent series, but these values do not behave like ordinary limits under nonlinear transformations. The equality $\sum a_n = \ln 2$ is **conditional**, not absolute.
