### A Clean Explanation of the Sokhotski–Plemelj Jump Formula

This document provides a clear explanation of the **Sokhotski–Plemelj (SP) jump formula** applied to a simple case, connecting it to the well-known geometric series identity. We'll show how the difference between the inside and outside boundary values of the geometric series kernel is a direct consequence of this powerful theorem.

---

### 1. Statement of the Sokhotski–Plemelj Formula

Let $\gamma$ be a smooth, simple, closed contour, such as the unit circle. For a function $\varphi(\zeta)$ on this contour, the Cauchy integral is defined as:

$$C\varphi = \frac{1}{2\pi i}\int_\gamma \frac{\varphi(\zeta)}{\zeta-z}\,d\zeta, \qquad z\notin\gamma$$

The SP formulas describe the non-tangential boundary values of this integral as you approach a point $t$ on the contour. The boundary value from the interior side (denoted with a '+') and the exterior side (denoted with a '-') are given by:

$$C[\varphi]\pm(t) = \pm\frac{1}{2}\varphi(t) + \frac{1}{2\pi i}\operatorname{PV}\!\int\gamma\frac{\varphi(\zeta)}{\zeta-t}\,d\zeta$$

The term $\operatorname{PV}$ denotes the **Cauchy principal value** of the integral. A key result from this is the **SP jump identity**, which states that the difference between the two boundary values is equal to the value of the density function at that point:

$$C[\varphi]+(t)-C[\varphi]-(t) = \varphi(t)$$

This is a fundamental result: the **jump across the contour equals the density at the point**.

---

### 2. Application to the Unit Circle with Constant Density

Let's apply this formula to the unit circle $|\zeta|=1$ with a constant density function $\varphi(\zeta) \equiv 1$.

The Cauchy integral becomes:

$$C1=\frac{1}{2\pi i}\int_{|\zeta|=1}\frac{1}{\zeta-z}\,d\zeta$$

Using the residue theorem, this integral equals **1** for $z$ inside the circle and **0** for $z$ outside.

Now, consider the SP boundary value formula for this case:

$$C[1]\pm(t) = \pm\frac{1}{2}\cdot 1 + \frac{1}{2\pi i}\operatorname{PV}\int_{|\zeta|=1}\frac{1}{\zeta-t}\,d\zeta$$

Due to the symmetry of the integrand (it's an odd function around the point $t$), the principal value integral on the unit circle vanishes. This simplifies the boundary values to:

$$C[1]+(t) = +\frac12 \quad \text{and} \quad C[1]-(t) = -\frac12$$

The jump is therefore:

$$C[1]+(t)-C[1]-(t)=1$$

This result perfectly matches the SP identity, since our density function $\varphi(t) = 1$. This simple case visually demonstrates the **jump** caused by the contour.

---

### 3. Connection to the Geometric Series Kernel

The identity for the geometric series kernel, $1/(1-z)$, can be expressed in terms of its boundary values on the unit circle. For a point $t=e^{it}$ on the circle, the "inside" geometric series $\sum_{n\ge0} z^n$ has a principal-value boundary representation given by:

$$\frac{1}{1-e^{it}} = \frac{1}{2} + \frac{i}{2}\cot\!\frac{t}{2}$$

Similarly, the "outside" series $-\sum_{n\ge1} z^{-n}$ has a principal-value boundary representation:

$$-\frac{1}{2} + \frac{i}{2}\cot\!\frac{t}{2}$$

Notice that the **$\frac{i}{2}\cot(t/2)$ term is common to both expressions**. This term represents the **shared singular behavior** or the Cauchy principal value part of the integral.

The difference between these two boundary values is:

$$\left(\frac{1}{2}+\frac{i}{2}\cot\frac{t}{2}\right) - \left(-\frac{1}{2}+\frac{i}{2}\cot\frac{t}{2}\right) = 1$$

This difference of **1** is precisely the jump predicted by the SP formula for a density of $\varphi(t)=1$. The geometric series kernel, with its simple pole at $z=1$, effectively **realizes the Sokhotski–Plemelj jump**. The discontinuity is encapsulated in the constant $\pm \frac{1}{2}$ terms, while the symmetric singular behavior is contained in the cotangent part.

This can be understood as an analog to the well-known distributional identity for a simple pole on the real line:

$$\frac{1}{x \pm i0} = \operatorname{PV}\frac{1}{x} \mp i\pi\delta(x)$$

The $\operatorname{PV}(1/x)$ term corresponds to our cotangent term, and the $\mp i\pi\delta(x)$ term encodes the jump, which is proportional to the residue of the pole.