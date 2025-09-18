# Sokhotski–Plemelj Formula: Boundary Values and the Geometric Series Kernel

This note provides a clean summary of the Sokhotski–Plemelj (SP) boundary-value/jump formula for the Cauchy integral, specializes it to the unit circle with constant density, and connects it to the geometric series kernel $1/(1-z)$ and its cotangent expansion.

---

## 1. Sokhotski–Plemelj (Cauchy Integral) — Statement

Let $\gamma$ be a smooth, simple, closed, oriented contour (e.g., the unit circle $|z|=1$, oriented counterclockwise). For a sufficiently regular density $\varphi(\zeta)$ on $\gamma$, define the Cauchy integral:
$$
C\varphi(z) = \frac{1}{2\pi i} \int_\gamma \frac{\varphi(\zeta)}{\zeta - z}\, d\zeta, \qquad z \notin \gamma.
$$

For $t$ a point on $\gamma$, the non-tangential boundary values (approaching from inside $+$ and outside $-$) satisfy:
$$
C[\varphi]_\pm(t) = \pm \frac{1}{2} \varphi(t) + \frac{1}{2\pi i} \operatorname{PV} \int_\gamma \frac{\varphi(\zeta)}{\zeta - t}\, d\zeta,
$$
where $\operatorname{PV}$ denotes the Cauchy principal value.

**Jump formula:**  
The difference of the two boundary values is
$$
C[\varphi]_+(t) - C[\varphi]_-(t) = \varphi(t).
$$

---

## 2. Specialization: Unit Circle and Constant Density

Let $\gamma = \{ e^{i\tau} : \tau \in [0, 2\pi) \}$ and $\varphi(\zeta) \equiv 1$. Then
$$
C1(z) = \frac{1}{2\pi i} \int_{|\zeta|=1} \frac{1}{\zeta - z}\, d\zeta.
$$

- For $z$ inside the unit circle, $C1(z) = 1$ (by the residue theorem).
- For $z$ outside, $C1(z) = 0$.

On the boundary $t = e^{i t_0}$:
$$
C[1]_\pm(t) = \pm \frac{1}{2} + \frac{1}{2\pi i} \operatorname{PV} \int_{|\zeta|=1} \frac{1}{\zeta - t}\, d\zeta.
$$

For constant density, the principal value integral vanishes (by symmetry), so:
$$
C[1]_+(t) = +\frac{1}{2}, \qquad C[1]_-