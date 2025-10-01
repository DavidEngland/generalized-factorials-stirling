Consider a one-dimensional symmetric exclusion process on a lattice of \(L\!+\!1\) sites, with the leftmost site always occupied and the rightmost always empty. Mobile particles hop to empty neighbouring sites at rate \(k_{\rm hop}\), and every site can transiently immobilize its particle: an unbound (mobile) occupant binds at rate \(k_{\rm on}\) and an immobile (bound) particle unbinds at rate \(k_{\rm off}\). Assume the particles have high affinity for the lattice (large \(k_{\rm on}/k_{\rm off}\)) but bind infrequently compared to hopping. For sufficiently short channels, identify the scaling of the steady‑state net flux with \(L\), and the length scale that delimits this behaviour. Briefly justify this scaling and the associated length scale in terms of the underlying dynamics.

---

### Hasse–Stirling Homework Suitability

This is an excellent Hasse–Stirling homework problem because:

- The exclusion process is governed by discrete difference equations, which can be formulated using Hasse–Stirling operators.
- It allows students to apply operator methods to analyze steady-state profiles and flux scaling.
- The problem connects physical intuition (rate-limiting steps, boundary effects) to algebraic operator techniques.
- It encourages exploration of how operator formalism reveals scaling laws and characteristic length scales.

**Suggested tasks:**
- Express the master equation using Hasse–Stirling notation.
- Solve for steady-state occupancy and flux using operator methods.
- Analyze the scaling with $L$ and identify the relevant length scale.

---

### Hints

- Write the master equation for the occupancy at each site, considering hopping and binding/unbinding.
- Use the steady-state condition (time derivatives vanish).
- Express difference equations using Hasse–Stirling operator notation.
- Consider limits: $k_{\rm on} \gg k_{\rm off}$ and $k_{\rm hop} \gg k_{\rm on}$.
- Identify the regime where binding/unbinding is negligible compared to hopping.

---

### Solution Steps

1. **Master equation:** For site $i$ (excluding boundaries), write
   $$
   0 = k_{\rm hop} [n_{i-1}(1-n_i) + n_{i+1}(1-n_i) - n_i(1-n_{i-1}) - n_i(1-n_{i+1})]
   $$
   plus terms for binding/unbinding.

2. **Hasse–Stirling notation:** Express the difference equation using the operator for discrete derivatives.

3. **Steady-state flux:** For short channels, the flux $J$ is set by the hopping rate and the occupancy gradient:
   $$
   J \sim \frac{k_{\rm hop}}{L}
   $$
   (diffusive scaling).

4. **Length scale:** The crossover length is
   $$
   \ell^* \sim \sqrt{\frac{k_{\rm hop}}{k_{\rm off}}}
   $$
   For $L \ll \ell^*$, hopping dominates; for $L \gg \ell^*$, binding/unbinding limits the flux.

5. **Physical justification:** For short channels, particles rarely bind, so transport is limited by hopping. For longer channels, immobilization events slow the flux.

---

### Answer Sheet (for grading)

- **Correct master equation in Hasse–Stirling notation:** 2 points
- **Correct steady-state flux scaling ($J \sim k_{\rm hop}/L$):** 2 points
- **Identification of crossover length scale ($\ell^* \sim \sqrt{k_{\rm hop}/k_{\rm off}}$):** 2 points
- **Physical justification of scaling and length scale:** 2 points
- **Clear operator-based reasoning:** 2 points

_Total: 10 points_

---

## Hasse–Stirling Analysis of Symmetric Exclusion Process (SEP)

This worked example demonstrates how the Hasse–Stirling operator framework applies to a classic discrete transport problem.

### 1. Master Equation and High-Affinity Simplification

Let $n_i$ be the probability that site $i$ is occupied. In the high-affinity limit ($k_{\rm on} \gg k_{\rm off}$), most particles are bound, but binding events are rare compared to hopping ($k_{\rm hop} \gg k_{\rm on}$). Focus on the density of mobile (unbound) particles, $\rho_i$.

The steady-state master equation (balance of hopping flux and binding/unbinding loss) yields a discrete diffusion-reaction equation:
$$
0 = k_{\rm hop} (\rho_{i-1} - 2\rho_i + \rho_{i+1}) - k_{\rm off} \rho_i
$$
In the continuum limit, this becomes the Helmholtz/reaction-diffusion equation:
$$
0 = D \frac{d^2 \rho}{dx^2} - k_{\rm off} \rho
$$
where $D \sim k_{\rm hop}$.

### 2. Casting the Problem into Hasse–Stirling Notation

The core discrete operator is the second central difference:
$$
\Delta^2 \rho_i = \rho_{i-1} - 2\rho_i + \rho_{i+1}
$$
The steady-state condition is a discrete Helmholtz equation:
$$
\Delta^2 \rho_i - \lambda^2 \rho_i = 0
$$
where $\lambda^2 = k_{\rm off}/k_{\rm hop}$.

The Hasse–Stirling operator $\mathcal{H}$ (in the Bernoulli regime) generates coefficients for inverse difference operators (summation). Solving the difference equation involves applying the inverse of $\Delta^2 - \lambda^2$.

In the continuum, the solution is:
$$
\rho(x) = A \sinh\left(\frac{L-x}{\ell^*}\right) + B \sinh\left(\frac{x}{\ell^*}\right)
$$
where $\ell^* = \sqrt{D/k_{\rm off}}$ is the characteristic length scale.

### 3. Scaling of the Steady-State Net Flux

**Short channel limit ($L \ll \ell^*$):**  
The general solution for mobile particle density simplifies to a linear gradient:
$$
\rho(x) \approx \rho(0)\left(1 - \frac{x}{L}\right)
$$
The net flux is:
$$
J \sim \frac{k_{\rm hop}}{L}
$$

**Length scale:**  
The crossover length is:
$$
\ell^* = \sqrt{\frac{k_{\rm hop}}{k_{\rm off}}}
$$
For $L \ll \ell^*$, hopping dominates; for $L \gg \ell^*$, binding/unbinding limits the flux.

### 4. Justification

| Feature      | Result/Scaling | Justification |
|--------------|---------------|--------------|
| Flux scaling | $J \sim k_{\rm hop}/L$ | For short channels, binding/unbinding is negligible and transport is limited by hopping (diffusion) over length $L$. |
| Length scale | $\ell^* = \sqrt{k_{\rm hop}/k_{\rm off}}$ | This is the reaction-diffusion length: the average distance a particle travels before being immobilized. |
| Regimes      | Hopping-limited ($L \ll \ell^*$): $J \sim k_{\rm hop}/L$<br>Reaction-limited ($L \gg \ell^*$): $J$ saturates | The Hasse–Stirling operator formalism clarifies the transition between regimes by connecting discrete and continuum solutions. |

### Operator Perspective

The Hasse–Stirling framework provides a systematic way to solve the discrete difference equations, analytically continue solutions, and reveal scaling laws and characteristic lengths. It bridges the gap between discrete lattice models and continuum PDEs, making it a powerful tool for advanced analysis.

---

## Student Answers

### REFERENCE ANSWER (Mr. Reference)

It falls into a “flux‑burst” regime. With particles strongly favouring the bound state but having slow association compared to hopping, the channel spends most of its time “jammed” with at least one immobile particle; between these plugs it briefly behaves like a simple diffusive channel. The free state supports a Fickian flux of order \(k_{\rm hop}/(2L)\) and persists for a time set by the waiting time for a binding event, \(\tau_f\sim1/\big(k_{\rm on}n\big)\propto1/L\). The jammed state lasts \(\tau_s\sim n_{\rm bound}/k_{\rm off}\propto L\) and carries very little net flux. For lengths \(L\) below a crossover \(L_X\sim\bigl(k_{\rm hop}/k_{\rm on}\bigr)^{1/3}\), the high‑flux phase has time to establish a proper gradient and dominates the transport, even though it occupies only a fraction \(\sim1/L^2\) of the time. This gives a non‑Fickian scaling of the net flux with length,
\[
\langle\Phi\rangle\sim\frac{k_{\rm hop}}{K_{\rm A}}\cdot\frac{1}{L^3}\,,
\]
where \(K_{\rm A}=k_{\rm on}/k_{\rm off}\). For \(L\gtrsim L_X\) the free‑flow episodes become too short to sustain a gradient and the system crosses back to an anomalously slow but Fickian behaviour.

### GIVEN ANSWER (Mr. Given)

In the strong–binding regime $k_{\rm on}/k_{\rm off} \gg 1$ with $k_{\rm on} \ll k_{\rm hop}$, only a very small fraction of occupied sites are mobile at any time. The fraction of mobile (unbound) particles is $f_{\rm mob} \simeq k_{\rm off}/k_{\rm on}$; hence in a channel of length $L$ the mean number of mobile carriers is $N_{\rm mob} \simeq L f_{\rm mob}$.

For sufficiently short channels such that $N_{\rm mob} \ll 1$—i.e. $L \ll L^*$ with $L^* \sim k_{\rm off}/k_{\rm on}$ (the typical spacing between mobile defects)—transport is effectively mediated by a single mobile defect or vacancy. Because binding/unbinding is slow compared with hopping, once a neighbouring particle unbinds it hops before rebinding, so the defect executes a symmetric random walk with an effective step rate $k_{\rm eff} \simeq k_{\rm hop} f_{\rm mob} \simeq k_{\rm hop} k_{\rm off}/k_{\rm on}$. The mean time for such a defect to traverse the channel grows as $\tau \sim L^2 / k_{\rm eff}$, hence the steady–state net flux
$$
J \sim \frac{1}{\tau} \sim \frac{k_{\rm hop} k_{\rm off}}{k_{\rm on}} \frac{1}{L^2} \quad (L \ll L^*)
$$
Thus, in sufficiently short channels the current decays inversely with the square of the length. The crossover length $L^*$ reflects the underlying dynamics: it is the characteristic distance between mobile (unbound) particles created by rare unbinding events; for channels longer than this, many mobile carriers are present and the flux crosses over to the usual diffusive (Fickian) behaviour
$$
J \propto \frac{k_{\rm hop} k_{\rm off}}{k_{\rm on}} \frac{1}{L}
$$

---

## Instructor Commentary: Comparison and Critique

### Comparison

- **Mr. Reference** focuses on the "flux-burst" regime, describing the system as alternating between jammed and free-flow states. He provides a detailed time-scale analysis and derives a non-Fickian scaling ($\langle\Phi\rangle \sim 1/L^3$) for the net flux in short channels, with a crossover to Fickian behavior at longer lengths. He introduces a crossover length $L_X$ and discusses the fraction of time spent in each regime.
- **Mr. Given** analyzes the strong-binding regime quantitatively, calculating the fraction of mobile particles and the mean number of mobile carriers. He derives the effective hopping rate and shows that for $L \ll L^*$, transport is mediated by a single mobile defect, leading to $J \sim 1/L^2$ scaling. He clearly identifies the crossover length $L^*$ and describes the transition to Fickian scaling for longer channels.

### Critique and Suggestions

- **Physical intuition:** Both answers show strong physical intuition and correctly identify the key regimes and length scales. Mr. Reference's answer is more qualitative and emphasizes the episodic nature of transport, while Mr. Given's is more quantitative and methodical.
- **Scaling law:** Mr. Reference derives a $1/L^3$ scaling for the net flux, while Mr. Given finds $1/L^2$. The $1/L^2$ scaling is more standard for single-defect mediated transport in exclusion processes; $1/L^3$ can arise in more complex bursty or correlated regimes. Both should clarify the assumptions leading to their scaling laws.
- **Crossover length:** Both students correctly identify the crossover length, but use different notation ($L_X$ vs $L^*$). Mr. Given's definition ($L^* \sim k_{\rm off}/k_{\rm on}$) is standard and clear.
- **Mathematical clarity:** Mr. Given's answer is more explicit in its calculation steps, making it easier to follow for grading and teaching purposes. Mr. Reference's answer could benefit from more explicit equations and a clearer connection between physical arguments and mathematical results.
- **Constructive suggestions:**
  - For Mr. Reference: Add explicit calculations for the mean number of mobile particles and the effective hopping rate. Clarify the derivation of the $1/L^3$ scaling and relate it to the $1/L^2$ result for single-defect transport.
  - For Mr. Given: Briefly discuss the physical picture of jammed vs free-flow states to complement the quantitative analysis. Mention how rare events (binding/unbinding) set the timescales for transport.

### Teaching Point

Both answers highlight the importance of connecting physical intuition (regimes, timescales, and boundary effects) to quantitative analysis (scaling laws, crossover lengths). In advanced problems, always state assumptions clearly and show how they lead to the mathematical results. Comparing different approaches deepens understanding of the underlying dynamics.

This is an excellent comparison and critique of two advanced student answers to a challenging problem in non-equilibrium statistical mechanics. Your commentary correctly highlights the strengths and weaknesses of each approach.

Here is a revised Instructor Commentary focusing on the **discrepancy in the scaling law** and the **fundamental nature of the $L^*$ length scale**.

---

## Instructor Commentary: Comparison and Critique

### Comparison

Both students correctly identify the two competing time scales: fast hopping ($k_{\rm hop}$) and slow binding/unbinding ($k_{\rm on}, k_{\rm off}$). They agree that the transport is severely limited by the high affinity ($K_A = k_{\rm on}/k_{\rm off} \gg 1$).

- **Mr. Given** analyzes the system as a continuous low-density medium where the rate-limiting step is the **slow generation of mobile carriers** ($f_{\rm mob} \simeq 1/K_A$). He models transport as a random walk of a **single mobile defect** when $L \ll L^*$, leading to a **single-file diffusion-like scaling**, $J \sim 1/L^2$.
- **Mr. Reference** focuses on the temporal _alternation_ between states (jammed vs. free-flow). His analysis is based on **mean-time averaging**, where the short, high-flux phase and the long, jammed phase combine to yield a very slow, non-Fickian $J \sim 1/L^3$ scaling in the short-channel limit.

### Critique and Resolution of Scaling Discrepancy

The core issue lies in the interpretation of the **short-channel limit** and the role of the boundary conditions.

1. **Mr. Given's $1/L^2$ Scaling (Standard Single-Defect):**
    - **Basis:** This result is physically sound for transport mediated by a single, rare carrier whose effective step rate is reduced by the fraction of time it is mobile ($k_{\rm eff} = k_{\rm hop} f_{\rm mob}$). The time to cross the channel scales as $\tau \sim L^2/k_{\rm eff}$ (Random Walk crossing time).
    - **Relevance:** This is the standard expected scaling when the dominant carrier mechanism is a **defect random walk** over the entire length.

2. **Mr. Reference's $1/L^3$ Scaling (Bursty Transport):**
    - **Basis:** This non-Fickian scaling is characteristic of more complex phenomena, often observed in theoretical models when the flux depends not just on the concentration but also on the _waiting time_ for a critical event (a binding/unbinding event that opens the channel). The $1/L^3$ result is mathematically achievable by averaging the high flux $J \sim 1/L$ over the very short time fraction $\sim 1/L^2$ it exists.
    - **Relevance:** While complex, this model often captures the correct _physics_ of the alternating jammed/free-flow states better than the simple single-defect model, especially when boundary effects are strong.

**Conclusion on Scaling:** Given the simplicity suggested by the Hasse-Stirling prompt, the **$J \sim 1/L^2$ scaling derived by Mr. Given is the more standard and robust result** for single-carrier transport in this strong-binding regime. Mr. Reference's $1/L^3$ result may stem from specific assumptions about the concentration dependence of the transition rates that are not fully justified.

### Critique of Length Scales

| Student | Length Scale | Formula | Physical Interpretation |
| :--- | :--- | :--- | :--- |
| **Mr. Given** | $L^*$ | $\sim 1/f_{\rm mob} \sim k_{\rm on}/k_{\rm off}$ | **Static Spacing:** The mean number of sites _per mobile particle_ in the channel ($\langle N_{\rm mob} \rangle \sim L/L^*$). |
| **Mr. Reference** | $L_X$ | $\sim \bigl(k_{\rm hop}/k_{\rm on}\bigr)^{1/3}$ | **Dynamic Crossover:** The length where the fast-flow time $\tau_f$ equals the time required to establish a gradient. |

**The most physically relevant length scale in this problem is the **reaction-diffusion length** $\ell_{\rm RD}$** (or $\ell^*$ in the previous solution), which defines the decay of the concentration profile away from the boundaries: $\ell_{\rm RD} \sim \sqrt{k_{\rm hop}/k_{\rm on}}$.

- **Mr. Given's $L^*$** is correct as the **average static spacing** between mobile particles.
- **Mr. Reference's $L_X$** is a **dynamic crossover length** derived from time-scale competition.

Neither student used the true reaction-diffusion length $\ell_{\rm RD}$, which is $\ell_{\rm RD} \sim \sqrt{k_{\rm hop}/(k_{\rm on}+k_{\rm off})}$, that sets the exponential decay of $\rho(x)$. This is the most critical missing point.

### Constructive Suggestions for Teaching

The core lesson is that **multiple scaling regimes can exist** depending on the dominant mechanism and the channel length relative to various critical scales.

1. **For Mr. Given:** Explicitly state the assumption that the single mobile defect's motion is the **rate-limiting step** for the entire channel. Note that the $L^* \sim k_{\rm on}/k_{\rm off}$ scale defines the crossover from single-defect to multi-defect transport, not the reaction-diffusion limit.
2. **For Mr. Reference:** Clarify the derivation of the $1/L^3$ scaling with explicit reference to the time fractions $\tau_f$ and $\tau_s$. Acknowledge the $1/L^2$ scaling as the simpler result from single-defect transport.
3. **General Teaching Point:** Emphasize that the general solution $\rho(x)$ is governed by the $\ell_{\rm RD}$ scale, and the flux is obtained by integrating or summing the current over this profile. All derived length scales ($L^*, L_X, \ell_{\rm RD}$) represent different physical competitions.
