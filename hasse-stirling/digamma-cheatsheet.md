# Digamma Function: Main Formulas and Identities (Reference Cheatsheet)

## Definition

- $\psi(x) = \frac{d}{dx} \log \Gamma(x) = \frac{\Gamma'(x)}{\Gamma(x)}$

---

## Recurrence Relation

- $\psi(x+1) = \psi(x) + \frac{1}{x}$

---

## Reflection Formula and Hypergeometric Series

- The reflection formula for the digamma function:
  $$
  \psi(1-x) - \psi(x) = \pi \cot(\pi x)
  $$
- There is also a hypergeometric series representation for $\psi(x)$ involving falling factorials:
  $$
  \psi(x) = -\gamma + \sum_{n=1}^\infty \frac{1}{n} - \frac{1}{n + x - 1}
  $$
  or equivalently,
  $$
  \psi(x) = -\gamma + \sum_{k=1}^\infty \frac{(x-1)_{k}}{k \cdot k!}
  $$
  where $(x-1)_k$ is the falling factorial: $(x-1)_k = (x-1)(x-2)\cdots(x-k)$.

- This series can be interpreted as a hypergeometric-type expansion, and is related to the Newton/Stern series for the digamma function.

**Summary:**  
- The reflection formula connects digamma to trigonometric functions.
- The hypergeometric series and falling factorial expansion provide alternative representations, useful for analytic continuation and series acceleration.

---

## Series Representations

- $\psi(x) = -\gamma + \sum_{n=0}^\infty \left( \frac{1}{n+1} - \frac{1}{n+x} \right )$
- $\psi(x+1) = -\gamma + \sum_{n=1}^\infty \left( \frac{1}{n} - \frac{1}{n+x} \right )$

---

## Asymptotic Expansion ($|x| \to \infty$)

- $\psi(x) \sim \log x - \frac{1}{2x} - \sum_{k=1}^\infty \frac{B_{2k}}{2k\,x^{2k}}$
  - $B_{2k}$: Bernoulli numbers

---

## Gauss's Digamma Theorem (Short Version)

For $x = \frac{r}{m}$, $r, m \in \mathbb{N}$, $r < m$:
$$
\psi\left(\frac{r}{m}\right) = -\gamma - \ln(2m) - \frac{\pi}{2} \cot\left(\frac{\pi r}{m}\right) + 2 \sum_{n=1}^{\left\lfloor \frac{m-1}{2} \right\rfloor} \cos\left(\frac{2\pi n r}{m}\right) \ln \sin\left(\frac{\pi n}{m}\right)
$$

- The sum only runs up to $\left\lfloor \frac{m-1}{2} \right\rfloor$, making it much shorter for large $m$.

---

## Special Values

- $\psi(1) = -\gamma$
- $\psi\left( \frac{1}{2} \right ) = -2 \log 2 - \gamma$
- $\psi\left( \frac{1}{3} \right ) = -\frac{\pi}{2\sqrt{3}} -\frac{3\log{3}}{2} - \gamma$
- $\psi\left( \frac{1}{4} \right ) = -\frac{\pi}{2} - 3\log{2} - \gamma$
- $\psi\left( \frac{1}{6} \right ) = -\frac{\pi\sqrt{3}}{2} -2\log{2} -\frac{3\log{3}}{2} - \gamma$
- $\psi\left( \frac{1}{8} \right ) = -\frac{\pi}{2} - 4\log{2} - \frac {\pi + \log \left (\sqrt{2} + 1 \right ) - \log \left (\sqrt{2} - 1 \right ) }{\sqrt{2}} - \gamma$.

Moreover, by taking the logarithmic derivative of $|\Gamma (bi)|^2$ or $|\Gamma (\tfrac{1}{2}+bi)|^2$ where $b$ is real-valued, it can easily be deduced that

- $\operatorname{Im} \psi(bi) = \frac{1}{2b}+\frac{\pi}{2}\coth (\pi b)$
- $\operatorname{Im} \psi(\tfrac{1}{2}+bi) = \frac{\pi}{2}\tanh (\pi b)$

Apart from Gauss's digamma theorem, no such closed formula is known for the real part in general. For example, at the imaginary unit:
- $\operatorname{Re} \psi(i) = -\gamma-\sum_{n=0}^\infty\frac{n-1}{n^3+n^2+n+1} \approx 0.09465$

---

## Integral Representations

- $\psi(x) = \int_0^\infty \left( \frac{e^{-t}}{t} - \frac{e^{-x t}}{1 - e^{-t}} \right ) dt$
- $\psi(x+1) = -\gamma + \int_0^1 \frac{1 - t^x}{1 - t} dt$

---

## Values for Complex and Imaginary Arguments

- $\operatorname{Im} \psi(bi) = \frac{1}{2b} + \frac{\pi}{2} \coth(\pi b)$
- $\operatorname{Im} \psi\left( \frac{1}{2} + bi \right ) = \frac{\pi}{2} \tanh(\pi b)$

---

## Relation to Harmonic Numbers

- $\psi(n) = H_{n-1} - \gamma$
- $H_n = \sum_{k=1}^n \frac{1}{k}$

---

## Relation to Trigonometric and Hyperbolic Functions

- Reflection formula involves $\cot(\pi x)$ (trigonometric)
- Imaginary arguments involve $\coth(\pi b)$ and $\tanh(\pi b)$ (hyperbolic)

---

## Useful Approximations

- For large $x$: $\psi(x) \approx \log x - \frac{1}{2x}$
- For $x \in (0,1)$: $\psi(x) \in \left( -\frac{1}{x} - \gamma, 1 - \frac{1}{x} - \gamma \right )$

---

## Adding $\gamma$ to Digamma (When Not a Difference)

- When using the digamma function $\psi(x)$ in formulas where it is not a difference of digammas, add the Euler-Mascheroni constant $\gamma$:
  - Use $\psi(x) + \gamma$ for normalization, e.g., in operator formulas or analytic continuations.
  - Example: $\mathcal{H}_{1,-1,0}(\log t)(x-1) = \psi(x) + \gamma$

---

## Entire Function and Infinite Product over Zeros

- The function $\frac{\psi(x)}{\Gamma(x)}$ is **entire** (analytic everywhere in the complex plane).
- It admits an infinite product representation over the zeros $x_k$ of the digamma function:
  $$
  \frac{\psi(x)}{\Gamma(x)} = -e^{2\gamma x} \prod_{k=0}^\infty \left(1 - \frac{x}{x_k}\right) e^{x/x_k}
  $$
  where $x_k$ are the zeros of $\psi(x)$ and $\gamma$ is the Euler-Mascheroni constant.

**Summary:**  
- $\frac{\psi(x)}{\Gamma(x)}$ is entire and its zeros coincide with the zeros of the digamma function.
- The infinite product formula expresses this function in terms of its zeros, similar to Weierstrass products for other entire functions.

---

## Summary Table

| Formula/Identity                | Expression                                                      |
|----------------------------------|-----------------------------------------------------------------|
| Definition                      | $\psi(x) = \frac{d}{dx} \log \Gamma(x)$                        |
| Recurrence                      | $\psi(x+1) = \psi(x) + \frac{1}{x}$                            |
| Reflection                      | $\psi(1-x) - \psi(x) = \pi \cot(\pi x)$                        |
| Series                          | $-\gamma + \sum_{n=0}^\infty \left( \frac{1}{n+1} - \frac{1}{n+x} \right )$ |
| Asymptotic                      | $\log x - \frac{1}{2x} - \sum_{k=1}^\infty \frac{B_{2k}}{2k\,x^{2k}}$ |
| Gauss's theorem                 | See above                                                      |
| Special values                  | See above                                                      |
| Integral                        | See above                                                      |
| Complex/imaginary               | See above                                                      |
| Add $\gamma$ if not a difference| Use $\psi(x) + \gamma$                                         |

---

**References:**  
- Abramowitz & Stegun, Handbook of Mathematical Functions
- NIST Digital Library of Mathematical Functions (DLMF)
- Wikipedia: Digamma function