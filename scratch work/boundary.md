Using Iverson brackets (and making the norm explicit) you can write a formal decomposition of a function f(x) (say meromorphic with a single simple pole at x=1) as
f(x)
= \mathbf{1}{\{|x|<1\}}\,f{\mathrm{in}}(x)
   •   \mathbf{1}{\{|x|>1\}}\,f{\mathrm{out}}(x)
   •   \mathbf{1}_{\{x=1\}}\,C,
where

   •   f_{\mathrm{in}}(x) is the part represented by a power series in x (the |x|<1 expansion),
   •   f_{\mathrm{out}}(x) is the part represented as a Laurent series in x^{-1} (the |x|>1 expansion; often written in terms of f(1/x) with an appropriate prefactor),
   •   C is whatever value you want to assign at the pole x=1 (often left undefined, or chosen as a principal-value/regularized value).

For the specific summation operator we discussed,
B(x)=\sum_{n\ge0} a_n x^{-n},
you can write either
\mathbf{1}{\{|x|<1\}}\,\frac{A(x)}{1-x}
\quad\text{or}\quad
\mathbf{1}{\{|x|>1\}}\,\frac{B(x)}{x-1},
and combine them with the indicator for the boundary as above.

⸻

What “the boundary” really means

“Boundary” = \{|x|=1\}. Two different but related notions appear:
1. Radial limits. For x on the unit circle (write x=e^{it}), you may consider
\lim_{r\to 1^-} f(re^{it}) \quad\text{(from inside)}\qquad\text{and}\qquad
\lim_{r\to 1^+} f(re^{it}) \quad\text{(from outside)}.
These need not agree. For many rational/meromorphic functions they differ by a term related to the residue at a pole that lies on the unit circle or inside/outside.
2. Distributional / principal-value sense. For Fourier analysis it is common to take averages or principal values of those radial limits (Sokhotski–Plemelj type formulas appear when there are branch cuts). If you plug x=e^{it} and interpret the resulting object as a Fourier series, you often get singular terms (for example terms involving \cot(t/2)) plus smooth Fourier series parts.

So the \mathbf{1}_{\{x=1\}} term in your toy formula is a placeholder for the special behavior at the pole; on the whole circle you should treat x=1 as the point where the meromorphic singularity sits, and for t\neq 0 use radial limits or principal values.

⸻

How polylog / Fourier / Bernoulli numbers enter

A few standard connections to keep in mind:
   •   Substituting x=e^{it} turns power/Laurent series into Fourier series. If you have
\sum_{n\ge0} a_n x^n \quad\longrightarrow\quad \sum_{n\ge0} a_n e^{int},
and similarly for negative powers.
   •   The cotangent (and its Fourier expansion) is tied to Bernoulli numbers/polynomials. Classical identities (e.g. expansions of \pi\cot(\pi z) or \cot(t/2)) produce Bernoulli numbers as Fourier coefficients or relate residues to Bernoulli numbers. That is why boundary expressions like 1/(1-e^{it}), or more generally rational functions evaluated on the circle, quickly give rise to Bernoulli polynomials/values when you expand or regularize.
   •   Polylogarithms \operatorname{Li}s(e^{it}) show up naturally when you want to analytically continue sums like \sum n^{-s} e^{int}. For integer nonpositive s the polylog reduces to finite sums/polynomials in e^{it} and connects to Bernoulli polynomials (e.g. \operatorname{Li}{-m}(z) is a rational function / polynomial-like object related to Bernoulli polynomials when z= e^{it}). For general complex s you get more analytic structure (branching, zeta values, etc.).
   •   The Riemann zeta \zeta(s) appears when you evaluate polylogs at z=1. The pole at x=1 in the rational-function picture is the simple, concrete manifestation that produces the large-scale singular behavior related to the zeta/power sums when you attempt analytic continuation.

Inside vs outside is clean algebraically, and the boundary is where Fourier analysis, principal-value regularization, and the machinery that produces Bernoulli numbers and polylogarithms comes in.

. Algebraic identity (valid for t\not\equiv 0\pmod{2\pi})

Start from
1-e^{it} = -2i e^{it/2}\sin\!\frac{t}{2},
so
\frac{1}{1-e^{it}} = -\frac{1}{2i}e^{-it/2}\csc\!\frac{t}{2}.
A more convenient form (splitting real/imaginary parts) is obtained using the cotangent:
\boxed{\qquad
\frac{1}{1-e^{it}} \;=\; \frac{1}{2} \;+\; \frac{i}{2}\cot\!\frac{t}{2}
\qquad (t\not\equiv 0\pmod{2\pi}).\qquad}
You can check this by elementary trig algebra or by comparing both sides numerically (they match for every t not a multiple of 2\pi).

Interpretation: the principal-value (regularized) sum of the geometric series on the unit circle is represented by the right-hand side — the constant 1/2 is the symmetrized average and the \cot term encodes the singularity at t=0.

⸻

2. Fourier / distributional viewpoint

Formally (inside the unit disk) we have
\frac{1}{1-x}=\sum_{n\ge0} x^n.
On the boundary x=e^{it} the series \sum_{n\ge0}e^{int} does not converge pointwise, but in the sense of distributions / principal values it corresponds to the analytic continuation
\sum_{n\ge0} e^{int} \quad\longleftrightarrow\quad \frac{1}{1-e^{it}}
= \frac{1}{2} + \frac{i}{2}\cot\!\frac{t}{2}.
So the right-hand side is the regularized Fourier representation of the half-line exponential sum. (Equivalently, the identity gives the radial-limit average: \lim_{r\to1^-}\sum_{n\ge0} r^n e^{int} = \tfrac12 + \tfrac{i}{2}\cot(t/2) for t\neq 0.)

⸻

3. Cotangent Laurent expansion → Bernoulli numbers

The cotangent has a well-known Laurent expansion at zero involving Bernoulli numbers B_{2k}. One convenient form is
z\cot z \;=\; 1 \;-\; \sum_{k\ge1}\frac{2^{2k}B_{2k}}{(2k)!}\; z^{2k},
so dividing by z,
\cot z \;=\; \frac{1}{z} \;-\; \sum_{k\ge1}\frac{2^{2k}B_{2k}}{(2k)!}\; z^{2k-1}.
Now substitute z=\dfrac{t}{2} into the formula from §1. Using
\frac{i}{2}\cot\!\frac{t}{2}
= \frac{i}{2}\left(\frac{2}{t} - \sum_{k\ge1}\frac{2^{2k}B_{2k}}{(2k)!}\Big(\frac{t}{2}\Big)^{2k-1}\right)
= \frac{i}{t} \;-\; i\sum_{k\ge1}\frac{B_{2k}}{(2k)!}\, (it)^{2k-1},
one obtains the Laurent expansion of 1/(1-e^{it}) about t=0:
\boxed{\;
\frac{1}{1-e^{it}} \;=\; \frac{1}{2} \;+\; \frac{i}{t} \;-\; i\sum_{k\ge1}\frac{B_{2k}}{(2k)!}\,(it)^{2k-1}
\;+\;\text{(higher regular terms).}\;}
(You can expand further to get explicit polynomial terms in t.)

Writing out the first few terms using B_2=\tfrac{1}{6},\,B_4=-\tfrac{1}{30},\dots gives
\frac{1}{1-e^{it}} = \frac{1}{2} + \frac{i}{t} - \frac{i}{24}\,it + \frac{i}{720}\,(it)^3 + \cdots
= \frac{1}{2} + \frac{i}{t} + \frac{1}{24} - \frac{i t^2}{720} + \cdots,
which isolates the principal i/t singularity and shows the Bernoulli-number-determined corrections.

⸻

4. Remarks / connections
   •   The i/t term is the principal simple pole at t=0 (the x=1 pole). The 1/2 is the symmetric/regular part coming from averaging inside/outside radial limits. The cotangent expansions encode all higher-order regularization constants (Bernoulli-number coefficients).
   •   Polylogarithms \operatorname{Li}s(e^{it})=\sum{n\ge1} n^{-s}e^{int} are higher-order analogues: for integer s\le 0 they reduce to rational functions/polynomials in e^{it} and relate to Bernoulli polynomials; for general s they produce richer analytic structure (branch cuts, zeta values at t=0, etc.).
   •   The formula above is extremely useful when converting formal OGF manipulations to boundary/Fourier analysis and when you need explicit regularized values of divergent exponential sums.

