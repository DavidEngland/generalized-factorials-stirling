Good — let’s do it cleanly.

I’ll (1) state the Sokhotski–Plemelj (SP) boundary-value/jump formula for the Cauchy integral on a contour, (2) specialize it to the unit circle and the constant density \varphi\equiv1, and (3) show how that reproduces the difference between the inside/outside boundary values of the geometric-series kernel 1/(1-z) (equivalently the identity you already have with the \cot term). The upshot: the SP jump equals the value of the density at the contour point, and for our simple pole at z=1 this shows the inside and outside radial limits differ by exactly 1.

⸻

1 — Sokhotski–Plemelj (Cauchy integral) — statement

Let \gamma be a smooth simple closed oriented contour (take the unit circle |z|=1 oriented counterclockwise). For a (sufficiently regular) density \varphi(\zeta) on \gamma define the Cauchy integral
C\varphi\;=\;\frac{1}{2\pi i}\int_\gamma \frac{\varphi(\zeta)}{\zeta-z}\,d\zeta,\qquad z\notin\gamma.
For t a point on \gamma, the non-tangential boundary values (approach from the interior side denoted + and from the exterior side denoted -) satisfy the Sokhotski–Plemelj formulas
C[\varphi]\pm(t)
= \pm\frac{1}{2}\varphi(t)\;+\;\frac{1}{2\pi i}\operatorname{PV}\!\int\gamma\frac{\varphi(\zeta)}{\zeta-t}\,d\zeta,
where \operatorname{PV} is the Cauchy principal value. In particular the jump across the contour is
C[\varphi]+(t)-C[\varphi]-(t) \;=\; \varphi(t).
This is the canonical SP jump identity: the difference of the two boundary values equals the density at the point.

⸻

2 — Specialize to the unit circle and \varphi\equiv 1

Take \gamma=\{e^{i\tau}:\tau\in[0,2\pi)\} and \varphi(\zeta)\equiv 1. Then
C1=\frac{1}{2\pi i}\int_{|\zeta|=1}\frac{1}{\zeta-z}\,d\zeta.
By the residue theorem, for z strictly inside the unit circle the integral equals 1 (so C1=1) and for z strictly outside it equals 0 (so C1=0). The SP boundary formula then says that for a point t=e^{i t_0} on the circle
C[1]\pm(t) = \pm\frac{1}{2}\cdot 1 \;+\; \frac{1}{2\pi i}\operatorname{PV}\int{|\zeta|=1}\frac{1}{\zeta-t}\,d\zeta.
But by symmetry the principal-value integral vanishes in this constant-density case (the integrand is an odd-symmetric kernel around the point), so the PV term is zero. Thus
C[1]+(t) = +\frac12,\qquad C[1]-(t) = -\frac12,
and the jump
C[1]+(t)-C[1]-(t)=1
agrees with the general SP identity \varphi(t)=1.

(If you prefer the orientation/sign convention that yields the outside value 0 and inside value 1, the same jump conclusion holds; different textbooks use slightly different \pm sign conventions, but the difference is always \varphi(t).)

⸻

3 — Connect to the geometric series / 1/(1-e^{it}) representation

We previously wrote, for t\not\equiv0\pmod{2\pi},
\frac{1}{1-e^{it}} \;=\; \frac{1}{2} \;+\; \frac{i}{2}\cot\!\frac{t}{2},
as the distributional/principal-value boundary representation of the inside geometric series
\sum_{n\ge0} e^{int}. There is also an outside-series representation (Laurent in negative powers)
-\sum_{n\ge1} e^{-int},
whose principal-value boundary representation is
-\frac{1}{2} \;+\; \frac{i}{2}\cot\!\frac{t}{2}.
(You can check the cotangent part is common to both and encodes the symmetric principal-value singular behavior; the only difference is the \pm\frac12 constant.)

Therefore the inside minus outside boundary values give
\Big(\tfrac12+\tfrac{i}{2}\cot\tfrac{t}{2}\Big) - \Big(-\tfrac12+\tfrac{i}{2}\cot\tfrac{t}{2}\Big)
= 1.
That difference is exactly the SP jump, and equals the density value \varphi(t)=1 that we used in the Cauchy integral formulation.

⸻

4 — Interpretation in terms of the simple pole at z=1
   •   The cotangent term \tfrac{i}{2}\cot(t/2) is the shared principal-value part of the boundary values; it reflects the symmetric singular behavior coming from the kernel.
   •   The constant \pm\tfrac12 pieces are the discontinuous parts of the boundary values; their difference is the jump and matches the SP formula.
   •   Equivalently, thinking infinitesimally near the pole at t=0 with the local linearization 1-e^{it}\approx -i t, the well-known distributional identity on the real line
\frac{1}{x\pm i0} = \operatorname{PV}\frac{1}{x} \mp i\pi\delta(x)
is the real-line analogue: the PV part corresponds to the cotangent-like term and the \pm (or \delta) part encodes the jump / residue contribution. After pulling back via x\leftrightarrow t (and restoring circle geometry) you get the same structure: a shared PV-type term plus a jump equal to the residue/density.

⸻

Short summary
   •   SP for the Cauchy integral states C[\varphi]+ - C[\varphi]- = \varphi.
   •   For \varphi\equiv1 on the unit circle, the inside/outside boundary values of the Cauchy integral are \pm\tfrac12 (up to the PV part which vanishes here), so the jump equals 1.
   •   The identity \frac{1}{1-e^{it}}=\tfrac12+\tfrac{i}{2}\cot(t/2) (inside principal-value form) and the outside principal-value form -\tfrac12+\tfrac{i}{2}\cot(t/2) differ by exactly 1; that difference is the SP jump and matches the general theorem. Thus the geometric-series kernel and its cotangent expansion realize the SP jump for the simple pole on the contour.