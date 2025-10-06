# Multivariate Differential: What Is It?

The multivariate differential generalizes the concept of the derivative to functions of several variables.

## Function of Two Variables

For $f(x, y)$, the differential is:
$$
df = \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy
$$
This expresses how $f$ changes as both $x$ and $y$ change.

## Function of Three Variables

For $f(x, y, z)$:
$$
df = \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy + \frac{\partial f}{\partial z} dz
$$

## Function of Four Variables

For $f(x_1, x_2, x_3, x_4)$:
$$
df = \frac{\partial f}{\partial x_1} dx_1 + \frac{\partial f}{\partial x_2} dx_2 + \frac{\partial f}{\partial x_3} dx_3 + \frac{\partial f}{\partial x_4} dx_4
$$

## General Case: $n$ Variables

For $f(x_1, x_2, \ldots, x_n)$:
$$
df = \sum_{i=1}^n \frac{\partial f}{\partial x_i} dx_i
$$

---

## Physical Implications of the Differential

- **Rates of change:** The differential describes how a physical quantity changes as its variables change (e.g., temperature, pressure, position).
- **Tangent plane:** For functions of several variables, $df$ gives the best linear approximation (tangent plane) near a point.
- **Optimization:** Used in finding maxima/minima and in methods like Lagrange multipliers.
- **Physics:** Appears in thermodynamics (e.g., $dU = TdS - PdV$), mechanics, and electromagnetism.

---

## Extension to Complex Variables and Beyond

- **Complex differential:** For $f(z)$, $df = f'(z) dz$; in several complex variables, use $\partial/\partial z_i$ and $dz_i$.
- **Manifolds:** Differentials generalize to differential forms, allowing integration over curves, surfaces, and higher-dimensional spaces.
- **Applications:** Used in calculus on manifolds, differential geometry, and modern physics (e.g., general relativity).

**Summary:**  
The differential is a universal tool for describing change, approximation, and integration in mathematics, physics, and engineering, and extends naturally to complex variables and higher-dimensional spaces.