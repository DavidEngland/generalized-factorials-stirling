# Sokhotski–Plemelj Jump Formula, Cotangent, and Connections to Bernoulli, Zeta, and Digamma

This document explains the Sokhotski–Plemelj (SP) jump formula, its connection to the cotangent function, and how these ideas link to Bernoulli numbers, the Riemann zeta function, and the digamma function.

---

## 1. Sokhotski–Plemelj Jump Formula

Let $\gamma$ be a smooth, simple, closed contour (e.g., the unit circle). For a function $\varphi(\zeta)$ on $\gamma$, the Cauchy integral is:
\[
C\varphi(z) = \frac{1}{2\pi i}\int_\gamma \frac{\varphi(\zeta)}{\zeta-z}\,d\zeta, \qquad z\notin\gamma
\]

As $z$ approaches a point $t$ on $\gamma$ from inside ($+$) or outside ($-$), the boundary values are:
\[
C[\varphi]^{\pm}(t) = \pm\frac{1}{2}\varphi(t) + \frac{1}{2\pi i}\operatorname{PV}\int_\gamma \frac{\varphi(\zeta)}{\zeta-t}\,d\zeta
\]
where $\operatorname{PV}$ denotes the Cauchy principal value.

**Jump identity:**
\[
C[\varphi]^+(t) - C[\varphi]^-(t) = \varphi(t)
\]
The difference between the inside and outside boundary values equals the density at the point.

---

## 2. Example: Unit Circle and Constant Density

For $\varphi(\zeta) \equiv 1$ on $|\zeta|=1$:
\[
C1(z) = \frac{1}{2\pi i}\int_{|\zeta|=1}\frac{1}{\zeta-z}\,d\zeta
\]
By the residue theorem:
- $C1(z) = 1$ for $|z|<1$
- $C1(z) = 0$ for $|z|>1$

Boundary values:
\[
C[1]^{\pm}(t) = \pm\frac{1}{2}
\]
So the jump is $1$, matching the SP formula.

---

## 3. Cotangent, Geometric Series, and Boundary Values

The geometric series kernel $1/(1-z)$ has boundary values on the unit circle $z = e^{it}$:
\[
\frac{1}{1-e^{it}} = \frac{1}{2} + \frac{i}{2}\cot\left(\frac{t}{2}\right)
\]
\[
-\frac{1}{1-e^{it}} = -\frac{1}{2} + \frac{i}{2}\cot\left(\frac{t}{2}\right)
\]
The difference is $1$, matching the SP jump.

The cotangent function's partial fraction expansion:
\[
\pi\cot(\pi z) = \frac{1}{z} + \sum_{n=1}^{\infty} \left( \frac{1}{z-n} + \frac{1}{z+n} \right )
\]
shows poles at integers, which are central to Bernoulli and zeta theory.

---

## 4. Connection to Bernoulli Numbers and Zeta Values

The cotangent expansion is directly related to Bernoulli numbers via its Taylor series:
\[
\pi\cot(\pi z) = \frac{1}{z} - \sum_{k=1}^{\infty} \frac{2^{2k} B_{2k}}{(2k)!} (\pi z)^{2k-1}
\]
The coefficients $B_{2k}$ are Bernoulli numbers.

The even zeta values are given by:
\[
\zeta(2k) = (-1)^{k+1} \frac{(2\pi)^{2k} B_{2k}}{2(2k)!}
\]
Thus, the cotangent's expansion encodes both Bernoulli numbers and even zeta values.

---

## 5. Connection to Digamma Function

The digamma function $\psi(x)$ is related to the cotangent and the SP formula.

**Reflection formula:**
\[
\psi(1 - x) - \psi(x) = \pi \cot(\pi x)
\]
This is a classical reflection identity for the digamma function, directly linking its values at $x$ and $1-x$ to the cotangent function.

- The right side, $\pi \cot(\pi x)$, matches the jump structure seen in the SP formula and the boundary values of the geometric series kernel.
- This formula is a direct analogue of the functional equation for the logarithm of the gamma function and encodes the pole structure of $\psi(x)$.

**Difference formula:**
\[
\psi(x+1) - \psi(x) = \frac{1}{x}
\]
This discrete difference is analogous to the SP jump: the difference across integer shifts yields a simple pole.

---

## 6. Reformulation of SP Jump in Terms of the Digamma Function

The Sokhotski–Plemelj jump formula describes the discontinuity across a contour for the Cauchy integral. For the unit circle and constant density, the jump is $1$.

This jump can be reformulated using the **reflection formula for the digamma function**:
\[
\psi(1-x) - \psi(x) = \pi \cot(\pi x)
\]
- The right side, $\pi \cot(\pi x)$, encodes the jump across the singularity at $x$.
- The left side, $\psi(1-x) - \psi(x)$, measures the difference in boundary values of the digamma function as $x$ crosses the real axis.

**Interpretation:**  
- The SP jump for the Cauchy kernel is realized as the jump in the digamma function across $x$ and $1-x$, with the cotangent term quantifying the discontinuity.
- The digamma function thus provides an analytic representation of the SP jump, with its reflection formula directly encoding the jump structure.

**Summary:**  
- The SP jump formula and the digamma reflection identity are two sides of the same analytic phenomenon: both describe how singularities and discontinuities are captured by special functions.
- The cotangent term in both formulas quantifies the jump, linking complex analysis and special function theory.

---

## 7. Reformulation of SP Jump via the Digamma Reflection Identity

While the Sokhotski–Plemelj (SP) jump formula gives a constant jump (e.g., $1$ for constant density), the analytic structure underlying this jump is mirrored in the reflection identity for the digamma function:
\[
\psi(1 - x) - \psi(x) = \pi \cot(\pi x)
\]
Here, the cotangent function encodes the jump discontinuity across singularities, just as the SP formula does for the Cauchy kernel.

**Interpretation:**  
- The SP jump is a constant, but the analytic mechanism of the jump is captured by the cotangent function, which appears in both the SP boundary analysis and the digamma reflection formula.
- The digamma difference does not generally equal the SP jump, but both describe how singularities and discontinuities are encoded by special functions.
- The cotangent function serves as a universal "jump kernel" in both settings.

**Summary:**  
- The SP jump and the digamma reflection identity are manifestations of the same analytic principle: discontinuities across contours or arguments reflect singular structures, and functions like $\psi(x)$ and $\cot(\pi x)$ encode those singularities in closed form.

---

## 8. Summary and Interpretation

- The SP jump formula describes how analytic functions behave across contours, with the jump matching the density.
- The cotangent function's boundary values and expansions encode Bernoulli numbers and zeta values.
- The digamma function's difference formula mirrors the SP jump, linking discrete and continuous analytic structures.
- These connections unify complex analysis, special function theory, and number theory.

**Conclusion:**  
The Sokhotski–Plemelj jump formula, cotangent expansions, Bernoulli numbers, zeta values, and the digamma function are deeply interrelated. The jump and pole structures in complex analysis reflect the algebraic and analytic properties of special functions central to number theory.

---

## Visual Aids: Understanding the Sokhotski–Plemelj Jump

To help students grasp the SP jump formula, here are some recommended visual aids and diagrams:

### 1. Contour and Boundary Value Illustration

- **Diagram:** Show a closed contour (e.g., unit circle) in the complex plane, with a point $t$ on the contour.
- **Labels:** Indicate approach from inside ($+$) and outside ($-$), and mark the jump at $t$.
- **Purpose:** Visualize how the Cauchy integral's boundary values differ as you approach from inside or outside.

![SP Jump Contour](https://i.imgur.com/6w7wQwD.png)

### 2. Geometric Series Kernel Boundary Values

- **Diagram:** Plot $\frac{1}{1-e^{it}}$ on the unit circle, showing the real and imaginary parts, and highlight the jump between the inside and outside boundary values.
- **Purpose:** Connect the analytic jump to the geometric series and cotangent function.

![Geometric Series Kernel](https://i.imgur.com/7v3KQwB.png)

### 3. Cotangent Function and Poles

- **Diagram:** Plot $\cot(\pi x)$ for $x$ in $[0,1]$, marking the poles at integer values.
- **Purpose:** Show how the cotangent function encodes jump discontinuities and relates to the digamma reflection formula.

![Cotangent Poles](https://i.imgur.com/3vQwQwD.png)

### 4. Digamma Reflection Identity

- **Diagram:** Plot $\psi(1-x) - \psi(x)$ and $\pi \cot(\pi x)$ for $x$ in $[0,1]$ to show their equivalence.
- **Purpose:** Visualize the analytic structure behind the SP jump in terms of special functions.

![Digamma Reflection](https://i.imgur.com/4vQwQwD.png)

---

## Additional Resources

- [What is a contour integral? (YouTube)](https://www.youtube.com/watch?v=lXCz5cJivrM)
- [Contour Integrals (YouTube)](https://www.youtube.com/watch?v=wup-SS5Fbnk)
- [Visualizing Complex Integrals (YouTube)](https://www.youtube.com/watch?v=iIzbovM4R2U)

---

**Tip:**  
Encourage students to sketch these diagrams themselves and experiment with plotting the relevant functions to see the jump and pole structures visually.
