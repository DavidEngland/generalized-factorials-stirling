Course title

Lambert series, divisor sums and arithmetic functions — theory and modern research directions

Course goals & prerequisites

Goals. Students will master Lambert series and divisor–sum identities, Möbius inversion and Dirichlet convolution, connections to Dirichlet series and L-functions, the von Mangoldt function and explicit formulas, and modern analytic/combinatorial and modular-form applications. They’ll see classical theorems and current research directions and get practice computing, proving, and formulating research problems.

Prerequisites. Graduate real & complex analysis, basic analytic number theory (Dirichlet series, Riemann zeta), algebraic number theory helpful but not required, comfort with generating functions and asymptotics.

⸻

Course schedule (12 weeks — one lecture/week ~ 2–3 hr or two 75-min lectures)

Week 1 — Introduction, arithmetic functions, Dirichlet convolution
Week 2 — Möbius function, Möbius inversion and elementary consequences
Week 3 — Lambert series: definitions, basic identities, examples (including \sigma_s)
Week 4 — Lambert ↔ Dirichlet ↔ q-series relations; Eisenstein series & \sigma_{k-1}
Week 5 — Von Mangoldt \Lambda(n): definitions, generating functions, -\zeta’/\zeta
Week 6 — Explicit formula (sketch): contour shifts, residues, prime counting functions \psi(x) and \vartheta(x)
Week 7 — Tauberian theorems, Ikehara theorem and the link to the Prime Number Theorem (PNT)
Week 8 — Advanced Lambert examples: Ramanujan identities, partition connections, mock/modular objects
Week 9 — Correlations of arithmetic functions: Möbius randomness, Liouville, multiplicative chaos
Week 10 — Voronoi & summation formulas, divisor problem asymptotics, moments of \sigma_s(n)
Week 11 — Modern analytic techniques: pretentious approach (Granville–Soundararajan), Sarnak–Möbius disjointness, function field analogues
Week 12 — Student presentations, thesis ideas, open problems & directions

(Stretch option: split weeks into two lectures to add hands-on computational labs, proofs of deeper theorems, or guest lectures on modular forms.)

⸻

Lecture notes & core content (condensed, but rigorous)

1. Basic definitions (reference sheet)
	•	Arithmetic function: f:\mathbb{N}\to\mathbb{C}.
	•	Dirichlet convolution: (f*g)(n)=\sum_{d|n} f(d)g(n/d).
	•	Identity: \delta(n)=1 iff n=1, else 0. \delta * f = f.
	•	Multiplicative and completely multiplicative functions.
	•	Important functions:
	•	Constant 1(n)\equiv1.
	•	Identity \mathrm{id}_s(n)=n^s (commonly s real/complex).
	•	Divisor sum: \sigma_s(n)=\sum_{d\mid n} d^s.
	•	Möbius \mu(n): \mu(1)=1,\ \mu(n)=(-1)^k if n product of k distinct primes, else 0.
	•	von Mangoldt \Lambda(n)=\begin{cases}\log p & n=p^k\\0&\text{otherwise}\end{cases}.

2. Möbius inversion (full proof)

Theorem (Möbius inversion). If F(n)=\sum_{d|n} f(d) for all n, then
f(n)=\sum_{d|n} \mu(d)F(n/d).

Proof. This is the standard convolution statement: F=f1. Convolving both sides with \mu gives \( \muF = \mu*(f1) = (\mu1)f = \delta * f = f\) since \mu1=\delta. Writing out coefficients yields the formula. ∎

Immediate corollary. Since \sigma_s = \mathrm{id}_s * 1, by inversion
\mathrm{id}s(n)=n^s=\sum{d|n} \mu(d)\,\sigma_s(n/d).
(This is the identity you requested — derived directly from Möbius inversion.)

3. Lambert series: definition and basic manipulations

Definition. For an arithmetic function a(n),
L_a(q)=\sum_{n\ge1}\frac{a(n)q^n}{1-q^n} \qquad(|q|<1).
Expand:
L_a(q)=\sum_{n\ge1} a(n)\sum_{k\ge1} q^{kn} = \sum_{m\ge1}\Big(\sum_{d\mid m} a(d)\Big) q^m.
Hence the coefficient of q^m is b(m)=\sum_{d\mid m} a(d)=(a*1)(m).

Inversion formula for Lambert series. If L_a(q)=\sum_{m\ge1} b(m) q^m then
b(m)=\sum_{d\mid m} a(d)\quad\Longrightarrow\quad a(n)=\sum_{d\mid n} \mu(d)\, b(n/d).
This is just Möbius inversion on coefficients.

Example. Take a(n)=n^s. Then
\sum_{n\ge1}\frac{n^s q^n}{1-q^n}=\sum_{m\ge1} \sigma_s(m)\,q^m,
since the coefficient of q^m is \sum_{d|m} d^s=\sigma_s(m).

4. Lambert series ↔ Dirichlet series / Mellin transforms (sketch of relations)
	•	Important philosophy: Lambert series encode divisor sums in q-variable; analyzing q\to1^{-} or q=e^{-t} small t connects to Dirichlet series by Mellin transforms.
	•	Heuristic transform. Set q=e^{-t}. Then
\sum_{n\ge1}\frac{a(n)q^n}{1-q^n}=\sum_{n\ge1} a(n)\sum_{k\ge1} e^{-knt}=\sum_{m\ge1}\Big(\sum_{d|m} a(d)\Big)e^{-mt}.
Applying Mellin transform \int_0^\infty t^{s-1}(\cdot)\,dt (with convergence caveats) relates to Dirichlet series A(s)=\sum a(n)n^{-s} multiplied by zeta factors. (In course, do a careful derivation for classes of a(n) with known growth.)

5. von Mangoldt and logarithmic derivative of \zeta
	•	Euler product: for \Re(s)>1,
\zeta(s)=\prod_p (1-p^{-s})^{-1}.
	•	Logarithmic derivative:
-\frac{\zeta’(s)}{\zeta(s)}=\sum_{p}\sum_{k\ge1} \log p\; p^{-ks} = \sum_{n\ge1}\frac{\Lambda(n)}{n^s},\qquad \Re(s)>1.
Proof. Take \log of Euler product and differentiate; rewrite double sum as Dirichlet series.

This identity is fundamental: -\zeta’/\zeta is the Dirichlet generating function of \Lambda.

6. Explicit formula for prime counting (sketch)

Start from the inverse Mellin transform for \sum_{n\le x}\Lambda(n) using -\zeta’/\zeta:
\Psi(x):=\sum_{n\le x}\Lambda(n)=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty} -\frac{\zeta’(s)}{\zeta(s)}\frac{x^s}{s}\,ds\quad (c>1).
Shift contour left, picking residues at:
	•	s=1 (simple pole) → main term x,
	•	Nontrivial zeros s=\rho → contributions -x^{\rho}/\rho,
	•	Trivial zeros at negative even integers → smaller contributions,
	•	Possibly pole at s=0 etc.

Thus one gets the explicit formula of the form
\Psi(x)=x-\sum_{\rho}\frac{x^{\rho}}{\rho} + \text{(known smaller terms)}.
Careful treatment (bounds, convergence) is required; class will derive the full formula with error terms in lecture 6.

7. Tauberian theorems and PNT
	•	Ikehara’s theorem: If F(s)=\sum_{n\ge1} a_n n^{-s} converges for \Re(s)>1 and has a simple pole at s=1 with residue A and is analytic in \Re(s)\ge1 except pole, then \sum_{n\le x} a_n \sim A x.
	•	Apply with a_n=\Lambda(n) and -\zeta’/\zeta to deduce PNT. We’ll present full statement and proof sketch.

8. Connections to modular forms & Eisenstein series
	•	Classical relation: for even k\ge4, the Eisenstein series E_k(q) has Fourier expansion
E_k(q)=1 - \frac{2k}{B_k}\sum_{n\ge1}\sigma_{k-1}(n) q^n,
where B_k are Bernoulli numbers. This identifies divisor sums as Fourier coefficients of modular forms. Explore consequences: modular transformation gives deep identities and growth control for \sigma_{k-1}(n).

9. Advanced tools & topics (overview)
	•	Voronoi summation for \sigma_{s}(n) and applications to divisor problems.
	•	Circle method and partitions (Lambert series appear naturally).
	•	Ramanujan’s identities and mock modular forms — many Lambert series from Ramanujan connect to mock theta functions.
	•	Pretentious analytic number theory (Granville & Soundararajan) — approach to Möbius randomness.
	•	Sarnak’s Möbius disjointness conjecture and dynamical systems ties.
	•	Function field analogues: many problems have cleaner proofs in \mathbb{F}_q[T] world.
	•	Computational aspects: effective algorithms for computing \sigma_s(n), \Lambda(n) sums and verifying conjectured correlations.

⸻

Worked examples (short)

Example 1. Show \sum_{n\ge1}\frac{n^s q^n}{1-q^n} = \sum_{m\ge1} \sigma_s(m) q^m.
Proof: Expand LHS as \sum_{n,k\ge1} n^s q^{kn}. Let m=kn. For fixed m, contributions come from divisors n\mid m with k=m/n. So coefficient of q^m is \sum_{n\mid m} n^s=\sigma_s(m).

Example 2 (Möbius inversion to recover n^s). From previous identity \sigma_s = \mathrm{id}_s * 1. Convolving with \mu gives \mathrm{id}s = \sigma_s * \mu, i.e.
n^s = \sum{d\mid n} \mu(d)\,\sigma_s(n/d).

Example 3 (von Mangoldt from -\zeta’/\zeta). Differentiate Euler product:
\log \zeta(s) = -\sum_p\log(1-p^{-s}) = \sum_p\sum_{k\ge1}\frac{1}{k}p^{-ks}.
Differentiate: \zeta’(s)/\zeta(s) = -\sum_p\sum_{k\ge1} (\log p)\,p^{-ks}. Multiply by -1 and rearrange to get \sum_{n\ge1}\Lambda(n)n^{-s}.

⸻

Assignments & homework (sample problems by week)

Week 1–2 (foundations)
	1.	Prove basic properties of Dirichlet convolution: associativity, commutativity, identity, inverses for multiplicative functions.
	2.	Prove Möbius inversion and compute \mu * \log for small n.
	3.	Compute \sigma_0(n),\ \sigma_1(n),\ \sigma_{-1}(n) for n\le 30.

Week 3–4 (Lambert & examples)
4. Show expansions: \sum_{n\ge1} \frac{q^n}{(1-q^n)^2} = \sum_{m\ge1} \sigma_1(m) q^m (differentiate standard Lambert series as needed).
5. Prove the Eisenstein expansion for E_4 and E_6 up to constant factors (exercise in modular forms).
6. Given a coefficient sequence b(n) (small data provided), recover a(n) so that \sum a(n)q^n/(1-q^n)=\sum b(n)q^n.

Week 5–7 (zeta and primes)
7. Show -\zeta’/\zeta=\sum \Lambda(n)n^{-s} for \Re(s)>1.
8. Evaluate contour integral for \Psi(x) in a toy model where zeta has no zeros (illustrative).
9. Apply partial summation to convert Dirichlet series results into asymptotics for arithmetic sums.

Week 8–12 (advanced & research-oriented)
10. Prove a basic Voronoi summation identity for the divisor function d(n)=\sigma_0(n).
11. Numerical exercise: compute \sum_{n\le X}\mu(n) for X up to 10^6 and examine behavior; plot scaled sums. (Computational project)
12. Read a short paper or chapter on Ramanujan’s mock theta functions and present how a Lambert series appears in the identities.

(Homework should contain both proofs and computational parts; encourage Sage/pari/gp or Python.)

⸻

Midterm & final projects (examples)

Midterm project (pair). Implement efficient computation of \sum_{n\le X}\sigma_s(n) and compare to the expected asymptotic (use known average results). Submit code, plots, and a 6–8 page writeup.

Final project / thesis seed ideas (see more below). Students present a short poster and 20-minute talk on one of the thesis topics; deliver a 15–25 page paper exploring background, partial results or computational experiments.

⸻

Suggested thesis / research topics (fruitful areas)
	•	Möbius disjointness and dynamics. Explore Sarnak’s conjecture in specific dynamical systems; either prove disjointness for new classes or provide computational experiments.
	•	Correlations of multiplicative functions. Study \sum_{n\le X}\mu(n)\mu(n+h) or analogous sums for \lambda(n) (Liouville) and search for patterns.
	•	Lambert series and mock modularity. Investigate Lambert series that generate mock modular forms (Ramanujan type) and their modern interpretation.
	•	Divisor function in short intervals. Bounds and asymptotics for \sum_{x<n\le x+H} d(n) when H=o(x).
	•	Moments of \sigma_s(n). Analytic estimation of \sum_{n\le X} \sigma_s(n)^k for fixed k — connections to multiple Dirichlet series.
	•	Pretentious method problems. Use the Granville–Soundararajan framework to study irregularities in divisor sums or Möbius behavior.
	•	Function field analogues. Prove analogues of classical Lambert/divisor identities over \mathbb{F}_q[T]; sometimes easier and illuminating.
	•	Computational exploration of zeros influence. Numerically study how specific zeros of \zeta affect \Psi(x) via explicit formula truncations.
	•	New Lambert identities. Search for Lambert expansions for nonstandard arithmetic functions and study modularity properties.

⸻

Assessment and grading
	•	Weekly problem sets (50%) — proof & computation mix.
	•	Midterm project (15%) — implementation + report.
	•	Final project/paper & presentation (25%).
	•	Participation (10%) — presentations, problem solutions in class.

⸻

Further reading (classics & modern directions)

(These are standard references students will easily find in a math library or online; assign selected chapters.)
	•	Apostol, Introduction to Analytic Number Theory — divisor sums, Dirichlet convolutions.
	•	Davenport, Multiplicative Number Theory — zeta, von Mangoldt, PNT and explicit formulas.
	•	Titchmarsh, The Theory of the Riemann Zeta-Function — deeper treatment of explicit formula and zeros.
	•	Iwaniec & Kowalski, Analytic Number Theory — Voronoi, modular forms, advanced tools.
	•	K. Soundararajan & A. Granville papers/notes — pretentious method and multiplicative function correlations.
	•	Papers by Ramanujan on q-series and modern expositions linking Lambert series to mock modular forms.

(If you want, I can assemble a week-by-week reading list with exact chapter/section references pulled from these books.)

⸻

Sample exam / oral questions
	1.	Prove Möbius inversion and use it to express n^s in terms of \sigma_s and \mu.
	2.	Derive -\zeta’/\zeta=\sum \Lambda(n)n^{-s} and outline how to obtain the explicit formula for \Psi(x).
	3.	Show how the Eisenstein series coefficient identity implies average order of \sigma_{k-1}(n).
	4.	State Ikehara’s theorem and show how it implies PNT from known analytic properties of \zeta.

⸻

Practical tips for running the course
	•	Mix peers’ computational projects with analytic proofs. Students learn both the “hands-on” behavior and rigorous theory.
	•	Invite a guest lecture on modular forms or computational number theory.
	•	Encourage students to use high-precision numerics when investigating explicit formulas (zeros effect is subtle!).
	•	Use the course to push one or two students toward publishable computations or partial results for thesis work.

⸻