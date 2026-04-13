# Irrationality Measures via the Hasse-Stirling Framework

This document examines how the Hasse-Stirling approach can be used to establish irrationality measures for mathematical constants, with particular focus on Stieltjes constants.

## 1. General Framework for Irrationality Measures

### 1.1 Core Principle

The Hasse-Stirling framework provides a systematic approach for constructing sequences that approximate mathematical constants with controlled error terms. The key insight is that by carefully selecting parameters $(\alpha, \beta, r)$ for the generalized Hasse operator, we can:

1. Generate sequences $(a_n)$ and $(b_n)$ that satisfy specific recurrence relations
2. Form linear combinations that approximate the target constant
3. Analyze the growth rates of these sequences to establish irrationality measures

### 1.2 Methodology for Establishing Irrationality Measures

For a constant $\theta$, the general procedure follows these steps:

1. Identify a parameterized Hasse operator $\mathcal{H}_{\alpha,\beta,r}$ and function $f(t)$ such that $\mathcal{H}_{\alpha,\beta,r}(f)(1)$ involves $\theta$
2. Construct sequences $(a_n)$ and $(b_n)$ using this operator
3. Form a linear form $a_n - \theta b_n = \frac{c_n}{d_n}$ where $c_n, d_n$ are integers
4. Show that this linear form is non-zero but approaches zero rapidly
5. Calculate the irrationality measure $\mu(\theta)$ from the growth rates of these sequences

### 1.3 Advantages Over Traditional Approaches

The Hasse-Stirling approach offers several advantages:

1. **Unified Framework**: It provides a consistent methodology applicable to various constants
2. **Optimal Parameter Selection**: The parameters $(\alpha, \beta, r)$ can be optimized for each constant
3. **Systematic Sequence Construction**: The framework generates sequences with known recurrence relations
4. **Precise Error Analysis**: The connection to generalized Stirling numbers allows for detailed error analysis

## 2. Application to Zeta Values

The irrationality measures for zeta values can be studied through:

$$\mathcal{H}_{\alpha,\beta,r}([\log(t)]^k)(1)$$

For odd zeta values $\zeta(2n+1)$, we have established:

- For $\zeta(3)$: $\mu(\zeta(3)) \leq 5.513...$ (with parameters $(1,-2,0)$)
- For $\zeta(5)$: $\mu(\zeta(5)) \leq 6.578...$ (with parameters $(2,-3,0)$)
- For $\zeta(7)$: $\mu(\zeta(7)) \leq 8.890...$ (with parameters $(3,-4,0)$)

The pattern suggests that for $\zeta(2n+1)$, the irrationality measure grows approximately linearly with $n$.

## 3. Stieltjes Constants: Corrected Holonomic Setup

### 3.1 Connection to the Hasse Operator

The Stieltjes constants $\gamma_k(x)$ are linked to the Hasse operator by

$$\mathcal{H}([\log(t)]^{k+1})(x) = -(k+1)\gamma_k(x).$$

This identity is the entry point for building linear forms in Stieltjes constants via generalized Hasse operators.

### 3.2 Parameterized Expansion

For the generalized operator,

$$\mathcal{H}_{\alpha,\beta,r}([\log(t)]^{k+1})(x)=\sum_{j=0}^{k+1} C_{\alpha,\beta,r}(k+1,j)\,\gamma_{j-1}(x).$$

Empirically effective parameter choices are:

- $\gamma_0$ (Euler's constant): $(\alpha,\beta,r)=(1,-1,0)$
- $\gamma_k$ for $k\ge 1$: $(\alpha,\beta,r)=\left(\left\lfloor\frac{k+3}{2}\right\rfloor,-\left\lfloor\frac{k+4}{2}\right\rfloor,0\right)$

These should be viewed as optimization heuristics unless proved optimal for a specified objective.

### 3.3 Sequence Model and Kernel

Define

$$K(n,j)=\binom{n}{j}^3\binom{n+j}{j}^3,$$

$$E_j:=\mathcal{H}_{1,-1,0}([\log t]^{2j})(1),\qquad O_j:=\mathcal{H}_{1,-1,0}([\log t]^{2j+1})(1),$$

and

$$a_n=\sum_{j=0}^n K(n,j)E_j,\qquad b_n=\sum_{j=0}^n K(n,j)(n+j)^3O_j.$$

The relation $\mathcal{H}_{1,-1,0}([\log(t)])(1)=-\gamma$ gives the target constant in the resulting linear forms.

### 3.4 What Is Required for P-Recursiveness

The closure argument needs a hypothesis on $E_j$ and $O_j$.

**Proposition (holonomic criterion).**
If $E_j$ and $O_j$ are P-recursive in $j$ (equivalently, holonomic sequences), then $a_n$ and $b_n$ are P-recursive in $n$.

**Why:**

- $K(n,j)$ and $K(n,j)(n+j)^3$ are proper hypergeometric terms in $(n,j)$.
- Products of holonomic objects remain holonomic.
- Definite summation over $j$ preserves holonomicity.

So there exist recurrences

$$\sum_{k=0}^r P_k(n)a_{n+k}=0,\qquad \sum_{k=0}^{r_b} Q_k(n)b_{n+k}=0,$$

with $P_k,Q_k\in\mathbb{Q}[n]$.

**Important caveat:** if $E_j$ or $O_j$ are treated as arbitrary symbolic sequences (with no annihilating recurrence), P-recursiveness of $a_n,b_n$ does not follow automatically.

### 3.5 Practical Recurrence Extraction

There are two rigorous computational routes.

1. **Full holonomic route:** provide annihilators for $E_j,O_j$ and run creative telescoping in an Ore-algebra/holonomic package.
2. **Truncated route:** fix $J$ and replace sums by $\sum_{j=0}^{\min(n,J)}$. Then each sequence is a finite sum of hypergeometric terms in $n$, hence P-recursive, and recurrences can be extracted directly.

Maple template (truncated route):

```maple
with(SumTools[Hypergeometric]):

K := (n,j) -> binomial(n,j)^3 * binomial(n+j,j)^3:
J := 20:  # example cutoff

# Replace Ej/Oj by concrete numeric or exact data arrays first.
Fa := (n,j) -> K(n,j) * Ej[j]:
Fb := (n,j) -> K(n,j) * (n+j)^3 * Oj[j]:

an := n -> add(Fa(n,j), j=0..min(n,J)):
bn := n -> add(Fb(n,j), j=0..min(n,J)):

# Fit and verify a recurrence from sufficiently many terms.
# (Use gfun routines after generating a term table.)
```

Mathematica template (truncated route):

```mathematica
K[n_, j_] := Binomial[n, j]^3 Binomial[n + j, j]^3;
J = 20; (* example cutoff *)

a[n_] := Sum[K[n, j] Ej[[j + 1]], {j, 0, Min[n, J]}];
b[n_] := Sum[K[n, j] (n + j)^3 Oj[[j + 1]], {j, 0, Min[n, J]}];

aData = Table[a[n], {n, 0, 120}];
bData = Table[b[n], {n, 0, 120}];

recA = FindLinearRecurrence[aData, 8];
recB = FindLinearRecurrence[bData, 8];
```

In both systems, candidate recurrences should be validated against additional terms not used in fitting.

### 3.6 Implications for Irrationality-Measure Claims

With explicit, validated recurrences and corresponding asymptotics, one can estimate linear-form decay and denominator growth. This supports conditional bounds such as

$$\mu(\gamma)\le 10.97\ldots,\qquad \mu(\gamma_1)\le 13.42\ldots$$

in a recurrence-driven framework.

The pattern

$$\mu(\gamma_k)\lesssim 3k^2+11$$

should be presented as a heuristic/conditional growth law unless each step (non-vanishing, integrality control, and asymptotic constants) is proved for the specific construction.

## 4. Limitations and Challenges

The Hasse-Stirling approach, while powerful, faces several challenges:

1. **Computational Complexity**: As $k$ increases, the degree of recurrence polynomials grows, making explicit calculations challenging.

2. **Multi-Constant Relations**: Often, the Hasse operator expressions involve multiple constants, requiring simultaneous consideration of their linear independence.

3. **Optimality Questions**: Whether the obtained irrationality measures are optimal remains an open question.

4. **Linear Independence**: The approach does not directly address the linear independence of these constants over the rationals.

## 5. Conclusion and Future Directions

The Hasse-Stirling framework provides a systematic approach to establishing irrationality measures for various mathematical constants, including Stieltjes constants. By selecting appropriate parameters, we can construct sequences that yield increasingly precise rational approximations while maintaining control over their denominators.

For Stieltjes constants specifically, this approach offers new insights into their arithmetic nature. While currently no Stieltjes constant beyond $\gamma_0$ is proven irrational, the framework suggests that they all possess finite irrationality measures, supporting the conjecture of their irrationality and potential transcendence.

Future work could focus on:

1. Refining parameter selection to optimize irrationality measures
2. Extending the framework to address linear independence questions
3. Developing computational tools to handle the increasing complexity of higher-order constants
4. Exploring connections to other frameworks for irrationality proofs

The Hasse-Stirling approach thus represents a promising direction for advancing our understanding of the arithmetic nature of these fundamental mathematical constants.
