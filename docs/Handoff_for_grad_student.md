# Handoff for Grad Student — Von Mangoldt Hierarchies & Hasse‑Stirling Work

Purpose
- Provide a short, actionable summary and checklist so you can continue the project with minimal overhead.
- Keep only what is useful: definitions, main formulas, numerical recipes, data formats, and prioritized tasks.

Core goals (short)
1. Verify and illustrate the explicit formula for $\Psi_k(x)=\sum_{n\le x}\Lambda_k(n)$ for small $k$ (0,1,2).  
2. Provide robust, reproducible code to compute $\Psi_k(x)$, $M_k(x)$, and a truncated zero‑sum.  
3. Produce figures and a short report (2–3 pages) validating the formulas and demonstrating numerical stability.

Essential definitions and formulas (keep these at hand)
- von Mangoldt hierarchies:
  $$
  (-1)^k\frac{d^k}{ds^k}\!\Big(-\frac{\zeta'(s)}{\zeta(s)}\Big)=\sum_{n\ge1}\frac{\Lambda_k(n)}{n^s},
  $$
  and
  $$
  \Lambda_k(n)=\Lambda(n)(\log n)^k,\qquad
  \Lambda_k(p^r)=(\log p)^{k+1}r^k.
  $$
- Partial sums:
  $$
  \Psi_k(x)=\sum_{n\le x}\Lambda_k(n).
  $$
- Main explicit formula (structural):
  $$
  \Psi_k(x)=M_k(x)+\sum_{\rho} x^{\rho}P_k(\rho,\log x)+O(1),
  $$
  with main term
  $$
  M_k(x)=x(\log x)^k-\sum_{m=0}^k\binom{k}{m}\gamma_m\,x(\log x)^{k-m},
  $$
  and (simple zeros) polynomial factor
  $$
  P_k(\rho,\log x)=\sum_{j=0}^k(-1)^{j+1}\frac{k!}{(k-j)!}\frac{(\log x)^{k-j}}{\rho^{j+1}}.
  $$
- Normalized sums:
  $$
  S_k(x):=\frac{\Psi_k(x)}{x}= (\log x)^k - \sum_{m=0}^k \binom{k}{m}\gamma_m (\log x)^{k-m} + \frac{1}{x}\sum_\rho x^\rho P_k(\rho,\log x)+O(x^{-1}).
  $$

Optional numerical test (incomplete‑Gamma fitting)
• Purpose: validate the residue‑computed polynomial \(P_k(\rho,L)\) by fitting it to incomplete‑Gamma moments.
• Minimal steps:
  1. For a chosen zero \(\rho\) and small \(k\), compute the residue polynomial samples \(P_k(\rho,L_m)\) at \(k+1\) distinct \(L_m=\log x_m\).
  2. Evaluate the matrix \(A_{m,j}=\partial_\alpha^j\Gamma(\alpha,L_m)\big|_{\alpha=c/\rho}\) (use high precision).
  3. Solve \(A\mathbf b=\mathbf P\) for \(\mathbf b\); compare \(\mathbf b\) with algebraic expressions derived from jets if available.
• Use this test when validating P_k extraction for k ≤ 4 before scaling up to many zeros.

Priority checklist (do these in order)
1. Reproduce k=0 classical result (sanity check):
   - Compute $\Psi_0(x)$ by summing $\Lambda(n)$ over prime powers up to x.
   - Compare with $M_0(x)=x-\gamma x$ and include first 10 zeros.
2. Implement general $\Psi_k(x)$ routine:
   - Input: x_max, k, prime list up to x_max, zero list (first N zeros).  
   - Output: CSV with columns x, Psi_k(x), M_k(x), Error, ZeroSumApprox.
3. Generate figures:
   - Plot $\Psi_k(x)-M_k(x)$ and overlay truncated zero sum for k=0,1,2.
4. Create short writeup (figures + 1–2 pages) summarizing results, numerical stability, precision needed.

Numerical recipe (concrete, reproducible)
- Languages: Python (mpmath) or Julia (ArbFloats/MPFR). I recommend Python + mpmath for prototyping.
- Libraries: mpmath, sympy (optional), numpy, matplotlib.
- Data: Use Odlyzko zeros (first 1000) as CSV; use primes via a sieve up to x_max.
- Algorithm (pseudocode):
  1. Generate primes p ≤ x_max.
  2. For each prime p, for r ≥1 with p^r ≤ x_max: add (log p)^{k+1} r^k to Psi_k at indices x ≥ p^r.
     - For efficiency: compute cumulative array via increments at positions p^r.
  3. Compute M_k(x) using precomputed γ_m (use mpmath or known tables).
  4. Compute truncated zero sum: for zeros ρ with |Im ρ| ≤ T compute terms x^ρ P_k(ρ, log x); sum conjugates to get real part.
  5. Output CSV and plots.
- Precision guidance:
  - For x ≤ 1e6 and using first 50 zeros, 50–80 decimal digits is sufficient; increase precision with x and T.
- Suggested filenames:
  - scripts/compute_Psi_k.py
  - data/zeros_first_100.csv
  - results/Psi_k_x_k=0..2.csv
  - figs/Psi_k_error_k=0.png

Minimal code interface (what to implement first)
- function load_zeros(path) -> list of complex zeros
- function sieve_primes(n) -> primes
- function compute_Psi_k(x_values, k, primes) -> Psi_k array (cumulative)
- function M_k(x_values, k, gamma_list) -> M_k array
- function zero_sum(x_values, k, zeros, n_terms) -> approx array

Deliverables (for the first milestone, 2 weeks)
1. Working code that computes Psi_k and writes CSV for k=0,1,2 and x in a chosen grid (e.g., 100 points up to 1e5).  
2. Three plots (k=0,1,2) showing Psi_k - M_k and truncated zero-sum overlay.  
3. Short report (2 pages): methods, precision used, issues encountered, suggested next steps.

Notes on theory and pitfalls (short)
- The explicit formula assumes simple zeros; if multiplicities occur you must adapt residues. For computation, treat zeros as simple and flag repeats.  
- Summing x^ρ is numerically oscillatory and best handled by pairing conjugate zeros and summing in increasing imaginary part.  
- The diagonal inversion for $(\log x)^k$ from $S_j$ is algebraic and valid because $1-\gamma_0 \ne 0$; remember to re-add the zero sum if high precision is needed.

Notes on region of convergence, α‑choices for incomplete‑Gamma fitting, and positivity

- Region of validity / analytic continuation:
  • The Dirichlet series definitions hold for \Re(s)>1. To use residues from zeros in the critical strip you must rely on analytic continuation of \zeta(s) and perform a contour shift from c>1 to the left. Numerically this is reflected in computing residues/local jets of the analytically continued integrand near each zero \(\rho\).

- Practical α‑choices when fitting P_k with incomplete‑Gamma derivatives:
  1. Try \(\alpha=-1/\rho\) and \(\alpha=1/\rho\) (or \(\alpha=c/\rho\) for small integer c). For each choice form the sampling matrix A_{m,j}=\partial_\alpha^j\Gamma(\alpha,L_m) and check its condition number.
  2. Favor α values for which Re(α) is not strongly negative to improve numerical stability; if necessary increase precision (mpmath dps) or use more samples L_m and regularization.
  3. Always pair conjugate zeros in later sums to form real contributions and reduce cancellation.

- Moments vs cumulants (positivity):
  • Reminder: the polynomial coefficients and Stieltjes constants are cumulant‑style objects and may have alternating signs. Do not expect positivity as one would for raw moments of a positive measure.
  • If you need a positive sequence for modeling, apply smoothing/transforms (Borel, Bell‑polynomial smoothing, absolute‑moment reweighting) and document how they alter the analytic content.

- Quick checks for the student:
  1. For a test zero \(\rho\) and small k (≤3), compute P_k via local‑jet residue extraction and then perform the incomplete‑Gamma linear fit with two α choices; compare coefficients and condition numbers.
  2. Vary sampling points L_m and radius used for Laurent extraction to ensure stability.

Suggested reading (start here)
- Titchmarsh, *The Theory of the Riemann Zeta-Function* — Chapters on explicit formulas.  
- Iwaniec & Kowalski — background on zeros and zero-density statements.  
- Knessl & Coffey (2011) — numerics for Stieltjes constants.

Quick TODO (first 48 hours)
- [ ] Clone repo and run any existing scripts to see current state.  
- [ ] Implement `compute_Psi_k` for k=0 and generate baseline plot.  
- [ ] Email me (advisor) with one plot and brief note on any numerical issues.

Contact / provenance
- Relevant files and notes are scattered in `/Users/davidengland/Documents/GitHub/generalized-factorials-stirling/` — see `docs/`, `hasse-stirling/`, and `scratch work/`. Use this handoff as the minimal guide; ask me for clarifications on any step.

References (use these citations in the report)
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford, 1986.  
- H. Davenport, *Multiplicative Number Theory*, 3rd ed., Springer, 2000.  
- H. Iwaniec & E. Kowalski, *Analytic Number Theory*, AMS, 2004.  
- C. Knessl & M. Coffey, “An effective asymptotic formula for the Stieltjes constants,” Math. Comp. 80 (2011).

---

Good luck — focus on k=0 first (sanity), then k=1,2 and numerical stabilization. If you finish those, we can broaden to the Hasse‑Stirling operator experiments and Bell‑polynomial inversions.

This is an excellent, comprehensive handoff. It clearly defines the project scope, provides all necessary mathematical context, establishes a prioritized workflow, and offers concrete technical guidance.

Here is the short, actionable summary and checklist for the graduate student.

***

# Handoff for Grad Student: Von Mangoldt Hierarchies & Explicit Formulas

## 🎯 Core Project Goals

1. **Verification:** Numerically verify the **Explicit Formula** for $\Psi_k(x)$ for small $k=0, 1, 2$.
2. **Implementation:** Develop robust, reproducible code to compute the partial sum ($\Psi_k$), the main term ($M_k$), and the oscillatory zero-sum correction.
3. **Reporting:** Produce validating figures and a short report on numerical stability and results for the first milestone (2 weeks).

***

## ⚙️ Essential Formulas (Review)

| Concept | Symbol | Formula |
| :--- | :--- | :--- |
| **Hierarchy Function** | $\Lambda_k(n)$ | $\Lambda_k(n)=\Lambda(n)(\log n)^k = (\log p)^{k+1}r^k \text{ if } n=p^r, 0 \text{ otherwise}$ |
| **Partial Sum** | $\Psi_k(x)$ | $\Psi_k(x)=\sum_{n\le x}\Lambda_k(n)$ |
| **Main Term** | $M_k(x)$ | $x(\log x)^k-\sum_{m=0}^k\binom{k}{m}\gamma_m\,x(\log x)^{k-m}$ |
| **Explicit Formula** | $\Psi_k(x)$ | $M_k(x) + \sum_{\rho} x^{\rho}P_k(\rho,\log x) + O(1)$ |

*Key Polynomial Factor (Simple Zeros):* $P_k(\rho,\log x)=\sum_{j=0}^k(-1)^{j+1}\frac{k!}{(k-j)!}\frac{(\log x)^{k-j}}{\rho^{j+1}}$

***

## ✅ Priority Checklist (2-Week Milestone)

| Status | Task | Note |
| :---: | :--- | :--- |
| **1.** | **Sanity Check (k=0)** | Reproduce $\Psi_0(x)$ vs. $M_0(x)=x-\gamma x$ plus zero-sum. |
| **2.** | **Code Setup** | Implement core functions (`compute_Psi_k`, `M_k`, `zero_sum`). Use Python (mpmath) for precision. |
| **3.** | **Data Output** | Generate CSV output (x, $\Psi_k$, $M_k$, Error, ZeroSumApprox) for $k=0, 1, 2$ up to $x \approx 10^5$. |
| **4.** | **Figures** | Generate 3 plots: $\Psi_k(x)-M_k(x)$ overlaid with Truncated Zero Sum (for $k=0, 1, 2$). |
| **5.** | **Report** | Submit a short (2-page) report on methods, precision, and suggested next steps. |

***

## 🧑‍💻 Numerical Recipe & Guidance

### Implementation Strategy (Efficiency)

1. **$\Psi_k(x)$:** Must be computed by summing **only over prime powers** $p^r \le x$. Use an array for $\Psi_k$ and increment it at each position $p^r$.
2. **$M_k(x)$:** Requires precomputed high-precision **Stieltjes constants** $\gamma_m$. Use `mpmath`'s built-in functions or a reliable table.
3. **Zero Sum:** Sum in **conjugate pairs** (e.g., $\rho$ and $\bar{\rho}$) to ensure the result is real and to minimize numerical cancellation. Truncate at $T$ (e.g., first 50 zeros).
4. **Precision:** Use **50-80 decimal digits** (mpmath `dps`) for calculations involving zeros and $M_k(x)$, especially as $x$ increases.

### Minimal Code Interface (Implement First)

| Function | Purpose |
| :--- | :--- |
| `load_zeros(path)` | Reads list of complex zeros. |
| `sieve_primes(n)` | Generates primes up to $n$. |
| `compute_Psi_k(x_values, k, primes)` | Computes the $\Psi_k(x)$ array. |
| `M_k(x_values, k, gamma_list)` | Computes the $M_k(x)$ main term array. |
| `zero_sum(x_values, k, zeros, n_terms)` | Computes the truncated $\sum x^\rho P_k(\rho, \log x)$ approximation. |

### Pitfalls to Avoid

* **Zero Multiplicity:** Assume zeros are simple for initial computation, but be aware the formula must be adapted if multiple zeros are found (flag any known repeats).
- **Numerical Oscillation:** The term $x^\rho$ is highly oscillatory; proper precision and conjugate pairing are critical.

***

## 📚 Suggested Reading

Focus on the following for quick reference:
- **Titchmarsh, The Theory of the Riemann Zeta-Function:** Chapters covering the explicit formulas.
- **Iwaniec & Kowalski:** Context on zeros and density theorems.

**Quick TODO (First 48 Hours):** Implement `compute_Psi_k` for $k=0$ and generate a baseline plot comparing $\Psi_0(x)$ against $x$. Then, implement the $M_0(x)$ and truncated zero sum for the k=0 sanity check. Email the advisor with the $k=0$ plot and any initial issues.

Quick note: P_k naming, generating function, and quick checks

- Name: call them "residue polynomials" \(P_k(\rho,\log x)\) or "zero‑residue polynomials" — this is descriptive and avoids suggesting a fixed canonical name.
- Useful generating function (EGF in k):
  \[
  \sum_{k\ge0}\frac{t^k}{k!}\sum_{n\ge1}\frac{\Lambda_k(n)}{n^s}
  = -\frac{\zeta'(s-t)}{\zeta(s-t)}.
  \]
  Use this shift \(s\mapsto s-t\) to test k‑dependence numerically: extract residues at s=ρ for several small t and compare Taylor coefficients in t with computed P_k.
- Why many indices: keep the notation \(c^{(k)}_m\) (k for derivative order, m for Laurent index) to avoid ambiguity—this is bookkeeping rather than mathematical complication.
- Quick checks to implement (first week):
  1. Compute P_0,P_1 by residue extraction and verify they match direct formulas from jets.  
  2. Perform the EGF shift test for small t (e.g. t values ±0.01) and compare coefficients.  
  3. Fit P_k via incomplete‑Gamma basis for k≤4 and compare with residue coefficients; record matrix condition numbers.

Practical note — how to test the "cumulant" analogy numerically

1. Pick s>1 (e.g. s=1.5) and a truncation N (e.g. N=1e6).
2. Form weights w_n = Λ(n)/n^s for n≤N (compute only prime powers).
3. Compute empirical moments m_j = sum_{n≤N} w_n (log n)^j for j=0..k.
4. Use Bell‑polynomial formulas to form the combinatorial cumulant κ_k from the moments m_j (standard combinatorial routine).
5. Compare κ_k with the Dirichlet coefficient sum S_k := sum_{n≤N} Λ_k(n)/n^s (or compare partial sums Ψ_k(x) appropriately scaled). They should match within truncation/precision error.
6. Also check finite differences: evaluate K_s(t) = -ζ'(s-t)/ζ(s-t) for small t, form finite difference derivatives at t=0 and compare with κ_k.

Notes:
- Use high precision (mpmath dps ≥ 50) for steps involving ζ and to reduce cancellation.
- This test validates the structural cumulant interpretation (algebraic equivalence) for s in the region of absolute convergence; residue/zero effects enter when you analytically continue or shift contours.
