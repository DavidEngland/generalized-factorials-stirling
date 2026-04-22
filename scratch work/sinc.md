# Notes on the Sinc Function

This note collects standard identities for the two closely related functions
$$
\operatorname{sinc}(t) :=
\begin{cases}
\dfrac{\sin t}{t}, & t \ne 0,\\[4pt]
1, & t = 0,
\end{cases}
$$
and its normalized version
$$
\operatorname{sinc}_{\pi}(t) :=
\begin{cases}
\dfrac{\sin(\pi t)}{\pi t}, & t \ne 0,\\[4pt]
1, & t = 0.
\end{cases}
$$
They are related by the simple rescaling
$$
\operatorname{sinc}_{\pi}(t) = \operatorname{sinc}(\pi t).
$$

The normalized sinc also admits the generalized binomial form
$$
\binom{0}{t}
:= \frac{\Gamma(1)}{\Gamma(1+t)\Gamma(1-t)}
= \frac{1}{\Gamma(1+t)\Gamma(1-t)}
= \operatorname{sinc}_{\pi}(t).
$$
This follows from Euler's reflection formula in the form
$$
\Gamma(1+t)\Gamma(1-t) = \frac{\pi t}{\sin(\pi t)}
= \frac{1}{\operatorname{sinc}_{\pi}(t)}.
$$

Equivalently, the normalized sinc has the simple infinite product
$$
\operatorname{sinc}_{\pi}(t) = \prod_{n=1}^{\infty} \left(1-\frac{t^2}{n^2}\right),
$$
and hence the unnormalized form is
$$
\operatorname{sinc}(t) = \prod_{n=1}^{\infty} \left(1-\frac{t^2}{n^2 \pi^2}\right).
$$

The normalized form is the natural one for Fourier analysis with the convention
$$
\widehat{f}(\xi) = \int_{-\infty}^{\infty} f(t) e^{-2\pi i \xi t} \, dt,
\qquad
f(t) = \int_{-\infty}^{\infty} \widehat{f}(\xi) e^{2\pi i \xi t} \, d\xi.
$$

## Basic facts

- Both functions are even and entire after removing the removable singularity at $t=0$.
- Both satisfy $\operatorname{sinc}(0)=\operatorname{sinc}_{\pi}(0)=1$.
- Zeros:
  $$
  \operatorname{sinc}(t)=0 \iff t = n\pi, \quad n \in \mathbb{Z}\setminus\{0\},
  $$
  $$
  \operatorname{sinc}_{\pi}(t)=0 \iff t = n, \quad n \in \mathbb{Z}\setminus\{0\}.
  $$
- Decay:
  $$
  \operatorname{sinc}(t),\operatorname{sinc}_{\pi}(t) = O\!\left(\frac{1}{|t|}\right)
  \quad (|t|\to\infty).
  $$

## Power series

From the Taylor series for $\sin t$,
$$
\sin t = \sum_{n=0}^{\infty} (-1)^n \frac{t^{2n+1}}{(2n+1)!},
$$
we obtain
$$
\operatorname{sinc}(t) = \sum_{n=0}^{\infty} (-1)^n \frac{t^{2n}}{(2n+1)!}
= 1 - \frac{t^2}{3!} + \frac{t^4}{5!} - \frac{t^6}{7!} + \cdots,
$$
and therefore
$$
\operatorname{sinc}_{\pi}(t) = \sum_{n=0}^{\infty} (-1)^n \frac{\pi^{2n} t^{2n}}{(2n+1)!}
= 1 - \frac{\pi^2 t^2}{3!} + \frac{\pi^4 t^4}{5!} - \frac{\pi^6 t^6}{7!} + \cdots.
$$

In particular,
$$
\operatorname{sinc}'(0)=0,
\qquad
\operatorname{sinc}''(0)=-\frac{1}{3},
$$
and
$$
\operatorname{sinc}_{\pi}'(0)=0,
\qquad
\operatorname{sinc}_{\pi}''(0)=-\frac{\pi^2}{3}.
$$

More generally, only even derivatives survive at the origin:
$$
\operatorname{sinc}^{(2m)}(0) = (-1)^m \frac{(2m)!}{(2m+1)!} = \frac{(-1)^m}{2m+1},
$$
and similarly
$$
\operatorname{sinc}_{\pi}^{(2m)}(0) = (-1)^m \frac{\pi^{2m}}{2m+1}.
$$

## Derivatives

For $t \ne 0$,
$$
\operatorname{sinc}'(t) = \frac{t\cos t - \sin t}{t^2},
$$
$$
\operatorname{sinc}''(t) = \frac{2\sin t - 2t\cos t - t^2 \sin t}{t^3}.
$$

Using $\operatorname{sinc}_{\pi}(t)=\operatorname{sinc}(\pi t)$,
$$
\operatorname{sinc}_{\pi}'(t) = \frac{\pi t \cos(\pi t) - \sin(\pi t)}{\pi t^2},
$$
$$
\operatorname{sinc}_{\pi}''(t) = \pi^2 \operatorname{sinc}''(\pi t).
$$

The differential equation viewpoint is also useful. Since $y(t)=\sin t / t$ satisfies
$$
t y''(t) + 2 y'(t) + t y(t) = 0,
$$
the normalized function satisfies the rescaled version
$$
t \operatorname{sinc}_{\pi}''(t) + 2 \operatorname{sinc}_{\pi}'(t) + \pi^2 t \, \operatorname{sinc}_{\pi}(t)=0.
$$

## Integrals and transforms

The classical Dirichlet integral is
$$
\int_0^{\infty} \frac{\sin t}{t} \, dt = \frac{\pi}{2},
$$
so over the whole line,
$$
\int_{-\infty}^{\infty} \operatorname{sinc}(t) \, dt = \pi,
\qquad
\int_{-\infty}^{\infty} \operatorname{sinc}_{\pi}(t) \, dt = 1.
$$

With the Fourier convention above, define the rectangle function by
$$
\operatorname{rect}(\xi) :=
\begin{cases}
1, & |\xi| < 1/2,\\[4pt]
1/2, & |\xi| = 1/2,\\[4pt]
0, & |\xi| > \tfrac12.
\end{cases}
$$
Then
$$
\widehat{\operatorname{sinc}_{\pi}}(\xi) = \operatorname{rect}(\xi),
\qquad
\widehat{\operatorname{rect}}(t) = \operatorname{sinc}_{\pi}(t).
$$

Equivalently, by rescaling,
$$
\widehat{\operatorname{sinc}}(\xi) = \operatorname{rect}(\xi / \pi).
$$

Since multiplication in frequency corresponds to convolution in time,
$$
\widehat{\operatorname{sinc}_{\pi}^2}(\xi)
= \operatorname{rect} * \operatorname{rect}(\xi)
= \operatorname{tri}(\xi),
$$
where
$$
\operatorname{tri}(\xi) := \max(1-|\xi|,0).
$$
Thus
$$
\widehat{\operatorname{tri}}(t) = \operatorname{sinc}_{\pi}(t)^2.
$$

This is one of the cleanest reasons the normalized sinc is preferred in signal processing and sampling theory.

## Extrema

The critical points of $\operatorname{sinc}(t)$ away from the origin satisfy
$$
\operatorname{sinc}'(t)=0
\iff t\cos t - \sin t = 0
\iff \tan t = t.
$$
Hence all nonzero extrema occur at the nonzero real roots of
$$
\operatorname{tan} t = t.
$$
The first few positive roots are approximately
$$
4.493409,
\qquad
7.725252,
\qquad
10.904122,
\ldots
$$

At such a root $t_*$, the extremal value simplifies because $\sin t_* = t_* \cos t_*$:
$$
\operatorname{sinc}(t_*) = \cos t_* = \pm \frac{1}{\sqrt{1+t_*^2}}.
$$
So the side-lobe heights decay like $1/|t_*|$.

For the normalized sinc, nonzero extrema occur at
$$
\operatorname{tan}(\pi t) = \pi t,
$$
or equivalently at $t = t_*/\pi$ where $t_*$ solves $\operatorname{tan} t_* = t_*$. The first positive extrema occur near
$$
1.430297,
\qquad
2.459024,
\qquad
3.470889,
\ldots
$$

The global maximum is at the origin:
$$
\operatorname{sinc}(0)=\operatorname{sinc}_{\pi}(0)=1.
$$
All other local extrema alternate in sign.

## Series expansions near the origin

For local approximation,
$$
\operatorname{sinc}(t) = 1 - \frac{t^2}{6} + \frac{t^4}{120} + O(t^6),
$$
$$
\operatorname{sinc}_{\pi}(t) = 1 - \frac{\pi^2 t^2}{6} + \frac{\pi^4 t^4}{120} + O(t^6).
$$

These are often enough for perturbative calculations or for matching asymptotics at low frequency.

## Product and convolution facts

- Since $\widehat{\operatorname{sinc}_{\pi}} = \operatorname{rect}$, repeated products of $\operatorname{sinc}_{\pi}$ correspond to repeated convolutions of $\operatorname{rect}$.
- Repeated convolutions of $\operatorname{rect}$ generate compactly supported spline kernels.
- This places powers of sinc naturally next to B-splines, bandlimited interpolation, and Shannon sampling.

## Sampling identity

The normalized sinc is the interpolation kernel for ideal bandlimited recovery. Formally, if a function $f$ is bandlimited to $[-\tfrac12,\tfrac12]$, then under standard hypotheses,
$$
f(t) = \sum_{n\in\mathbb{Z}} f(n) \, \operatorname{sinc}_{\pi}(t-n).
$$
This is the Shannon-Whittaker sampling formula.

## Summary

- $\operatorname{sinc}(t)=\sin t/t$ and $\operatorname{sinc}_{\pi}(t)=\sin(\pi t)/(\pi t)$ differ only by scaling.
- The normalized sinc is the Fourier transform of the rectangle function under the $2\pi$ convention.
- Its square corresponds to the triangular function.
- Nonzero extrema are governed by the transcendental equation $\operatorname{tan} t=t$.
- Near the origin, sinc is controlled by a simple even power series.

These identities make the sinc function one of the central bridges between elementary trigonometric analysis, Fourier transforms, compact frequency support, and exact interpolation.
