## Riemann Zeta Function at $s = 0 + ir$ and $s = 1 + ir$

### $\zeta(0 + ir)$

- The Riemann zeta function $\zeta(s)$ is defined for $\Re(s) > 1$ by
  $$
  \zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}
  $$
  and analytically continued elsewhere except $s=1$.
- At $s=0+ir$:
  $$
  \zeta(0+ir) = \frac{1}{2} - \frac{1}{2^{1+ir}}
  $$
  (from functional equation and analytic continuation).

### $\zeta(1 + ir)$

- At $s=1+ir$, $\zeta(s)$ has a simple pole at $s=1$, but for $s=1+ir$ ($r \neq 0$) it is finite:
  $$
  \zeta(1+ir) = \sum_{n=1}^\infty \frac{1}{n^{1+ir}}
  $$
  - This is a convergent Dirichlet series for $r \neq 0$.
  - Can also be written as:
    $$
    \zeta(1+ir) = \sum_{n=1}^\infty \frac{e^{-ir \log n}}{n}
    $$

### Analytic properties

- $\zeta(s)$ is analytic for $s \neq 1$.
- At $s=0+ir$, the value is always finite.
- At $s=1+ir$, the function is finite for $r \neq 0$.

### References

- Titchmarsh, "Theory of the Riemann Zeta Function"
- Abramowitz & Stegun, "Handbook of Mathematical Functions"
- [Wolfram MathWorld: Riemann Zeta Function](https://mathworld.wolfram.com/RiemannZetaFunction.html)

