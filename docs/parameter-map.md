# Parameter Map for Generalized Stirling Numbers

This diagram maps the important families of generalized Stirling numbers in the $(a,b)$ parameter space, showing landmark points, axes, and regions of special behavior.

```
                         b (barrier/separation)
                             ↑
                             │
                   Laguerre  │  Touchard/Bell
         (-1,1) ●───────────●───────────● (0,1) Second Kind
                │            │            │
                │            │            │
                │            │            │
                │   Double   │   Classical│
         (-1,0) ●───────────●───────────● (0,0)
                │  Barriers  │    Forms   │
                │            │            │
                │            │            │
                │            │            │
         (-1,-1)●───────────●───────────● (0,-1)
                             │  ● (0,-1/2) Hyperbolic Strip
                             │  ● (0,1/2)
                             │
←────────────────────────────┼────────────────────────────→
                             │            a (affinity/cohesion)
                             │
                 Signed      │
         (1,-1) ●───────────●───────────● (2,-1)
                │  First Kind│            │
                │            │            │
                │            │            │
                │            │            │
         (1,0)  ●───────────●───────────● (2,0)
                │            │            │
                │            │            │
                │            │            │
                │            │            │
         (1,1)  ●───────────●───────────● (2,1) Lah Numbers
                             │
                             │
                             ↓
```

## Legend
- ● Landmark basis pair (specific parameter values with known interpretations)
- ─ Axis or boundary between parameter regions
- Region labels indicate families with similar characteristics

## Mathematical Characterization of Regions

### The Hyperbolic Strip
**Set definition**: $\mathcal{H} = \{(a,b) \in \mathbb{R}^2 \mid a = 0, b = \pm\frac{1}{2}\}$

**Properties**:
- **Explicit formula**: $S_{n,k}(0,\frac{1}{2}) = 2^{k-n}S(n,k)$ and $S_{n,k}(0,-\frac{1}{2}) = (-1)^{n-k}2^{k-n}S(n,k)$
- **Fixed-k EGF**: $\sum_{n\geq k} S_{n,k}(0,\pm\frac{1}{2})\frac{t^n}{n!} = \frac{4^k}{k!}e^{\pm kt/4}\sinh(t/4)^k$
- **Parity structure**: The coefficient pattern follows strict even/odd separation due to $\sinh(t/4)^k$
- **Convergence**: Better conditioning for asymptotic expansions when $b = -\frac{1}{2}$ versus $b = \frac{1}{2}$
- **Hyperbolic identity**: $\frac{e^{\pm t/2}-1}{\pm\frac{1}{2}} = 4e^{\pm t/4}\sinh(t/4)$

### Classical Stirling Triangle
**Set definition**: $\mathcal{C} = \{(a,b) \in \mathbb{R}^2 \mid (a,b) \in \{(0,1), (1,0), (1,1)\}\}$

**Properties for each landmark point**:
- **(0,1)**: $S_{n,k}(0,1) = S(n,k)$ (Stirling numbers of the second kind)
  - EGF: $\frac{(e^t-1)^k}{k!}$
  - Triangular recurrence: $S(n,k) = S(n-1,k-1) + k·S(n-1,k)$
  - Combinatorial interpretation: Partitions of $n$ elements into $k$ non-empty subsets

- **(1,0)**: $S_{n,k}(1,0) = s(n,k)$ (Stirling numbers of the first kind)
  - EGF: $\frac{(\ln(1+t))^k}{k!}$
  - Triangular recurrence: $s(n,k) = s(n-1,k-1) - (n-1)s(n-1,k)$
  - Combinatorial interpretation: Permutations of $n$ elements with $k$ cycles

- **(1,1)**: $S_{n,k}(1,1) = L(n,k)$ (Lah numbers)
  - EGF: $\frac{1}{k!}(1-t)^{-k}(\frac{t}{1-t})^k$
  - Explicit formula: $L(n,k) = \binom{n-1}{k-1}\frac{n!}{k!}$
  - Combinatorial interpretation: Number of ways to partition $n$ elements into $k$ ordered lists

### Touchard/Bell Region
**Set definition**: $\mathcal{T} = \{(a,b) \in \mathbb{R}^2 \mid a = 0, b > 0\}$

**Properties**:
- **Touchard-type polynomial family**: $\mathcal{T}^{(b)}_n(x) = \sum_{k=0}^n S_{n,k}(0,b)x^k$
- **General EGF**: $\sum_{n\geq 0} \mathcal{T}^{(b)}_n(x)\frac{t^n}{n!} = \exp(x\frac{e^{bt}-1}{b})$
- **Scaling relation**: $S_{n,k}(0,b) = b^{n-k}S(n,k)$
- **Special case**: At $b=1$, recovers Bell polynomials/Touchard polynomials

### Laguerre Connection Region
**Set relation**: Near $\{(a,b) \in \mathbb{R}^2 \mid (a,b) \approx (-1,1)\}$

**Properties**:
- **EGF for Laguerre polynomials**: $\sum_{n=0}^{\infty} L_n^{(\alpha)}(x) \frac{t^n}{n!} = \frac{e^{-xt/(1-t)}}{(1-t)^{\alpha+1}}$
- **Expansion**: $L_n^{(\alpha)}(x) = \sum_{k=0}^{n} \binom{n+\alpha}{n-k} \frac{(-x)^k}{k!}$
- **Parameter relation**: The parameters $(a,b) = (-\frac{1}{\alpha+1},1)$ generate coefficients related to $L_n^{(\alpha)}(x)$

### First Kind Region
**Set definition**: $\mathcal{F} = \{(a,b) \in \mathbb{R}^2 \mid a > 0, b = 0\}$

**Properties**:
- **Generalized cycle-counting**: Extends permutation cycle structure with weighted internal connections
- **Logarithmic EGF pattern**: Related to $\ln(1+t)$ with adjustable parameters
- **Key point**: At $(a,b)=(1,0)$, recovers signed Stirling numbers of the first kind

### Negative Parameter Region
**Set definition**: $\mathcal{N} = \{(a,b) \in \mathbb{R}^2 \mid a < 0 \text{ or } b < 0\}$

**Properties**:
- **Sign alternation**: When $b < 0$, coefficients typically show sign alternation pattern $(-1)^{n-k}$
- **"Anti-clustering"**: Negative $b$ values represent repulsive forces between elements
- **Dual transformation**: The map $(a,b) \mapsto (-a,-b)$ relates each region to a "dual" with inverse properties

## Important Mappings Between Regions

### Duality Transformation
The mapping $(a,b) \mapsto (-a,-b)$ transforms:
- Stirling second kind $(0,1) \mapsto (0,-1)$ (alternating Stirling numbers)
- Stirling first kind $(1,0) \mapsto (-1,0)$ (related to unsigned Stirling numbers)
- Lah numbers $(1,1) \mapsto (-1,-1)$

### Inverse Relation
The relation between parameters $(a,b)$ and $(b,a)$ connects the generalized Stirling pairs:
- If $\{S_{n,k}(a,b,r)\}$ is one family, then $\{S_{n,k}(b,a,-r)\}$ forms its inverse relation

### Scaling Properties
For $b \neq 0$, scaling follows: $S_{n,k}(0,b) = b^{n-k}S_{n,k}(0,1) = b^{n-k}S(n,k)$

### Compositional Inverse Relation
For function pairs $f(x)$ and $g(x)$ where $g(f(x)) = x$:
- Their coefficient sequences are related through generalized Stirling numbers with specific $(a,b)$ parameters
- For example, $f(x)=e^x-1$ and $g(x)=\ln(1+x)$ relate through parameters $(a,b)=(1,-1)$

## Combinatorial Interpretations Across the Parameter Space

The parameters $(a,b,r)$ have consistent interpretations throughout the space:

- **a parameter**: Controls internal cohesion/affinity within clusters
  - $a > 0$: Elements prefer to group together
  - $a = 0$: No inherent grouping preference
  - $a < 0$: Elements prefer to separate

- **b parameter**: Controls boundary/barrier effects between clusters
  - $b > 0$: Barriers between clusters (partition-like)
  - $b = 0$: No boundary effects
  - $b < 0$: "Anti-barriers" encouraging cluster formation

- **r parameter**: Controls initial conditions/shifts in the recurrence

This parameter interpretation provides a unified framework for understanding the combinatorial meaning across different Stirling-type numbers.
