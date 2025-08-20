# Appendix B: Generating Functions for Generalized Factorial Polynomials

This appendix develops the theory of generating functions for generalized factorial polynomials, culminating in a unified framework that encompasses ordinary generating functions (OGFs), exponential generating functions (EGFs), and more general forms involving ratios of factorial polynomials.

## Classical Generating Functions

### Ordinary Generating Functions (OGF)

The ordinary generating function for a sequence $\{a_n\}$ is defined as:
$$F(z) = \sum_{n=0}^{\infty} a_n z^n$$

For generalized factorial polynomials with fixed parameters $x$ and $a$:
$$G_{x,a}(z) = \sum_{m=0}^{\infty} P(x,a,m) z^m$$

**Connection to Factorial Polynomials:** The OGF has a natural interpretation:
- $z^m = P(z,0,m)$ (monomials as factorial polynomials)
- $P(x,a,m)$ (sequence coefficients)

This gives us:
$$G_{x,a}(z) = \sum_{m=0}^{\infty} P(x,a,m) \cdot P(z,0,m)$$

**Special Cases:**
- When $a = 0$: $G_{x,0}(z) = \frac{1}{1-xz}$
- When $a = 1$: $G_{x,1}(z) = \frac{1}{(1-xz)^2}$

### Exponential Generating Functions (EGF)

The exponential generating function for a sequence $\{a_n\}$ is defined as:
$$F(z) = \sum_{n=0}^{\infty} a_n \frac{z^n}{n!}$$

For generalized factorial polynomials with fixed parameters $x$ and $a$:
$$G_{x,a}(z) = \sum_{m=0}^{\infty} P(x,a,m) \frac{z^m}{m!}$$

**Connection to Factorial Polynomials:** The EGF relates to factorials as follows:
- $\frac{z^m}{m!} = P(z,1,m)$ (normalized monomials)
- $P(x,a,m)$ (sequence coefficients)

Thus:
$$G_{x,a}(z) = \sum_{m=0}^{\infty} P(x,a,m) \cdot P(z,1,m)$$

**Special Cases:**
- When $a = 0$: $G_{x,0}(z) = e^{-xz}$
- When $a = 1$: $G_{x,1}(z) = \frac{1}{1-xz}$

**Negative Increment Case:** When $a$ is replaced with $-a$:
$$E_{x,-a}(z) = (1-az)^{-x/a}$$

**This corrects the formula error from the previous version.**

**Theorem B.1 (EGF for Negative Increment).** The exponential generating function for $P(x,-a,m)$ is:
$$\sum_{m=0}^{\infty} P(x,-a,m) \frac{z^m}{m!} = (1-az)^{-x/a}$$

*Proof.* For $a \neq 0$, using the gamma function representation:
$$P(x,-a,m) = (-a)^m \frac{\Gamma(x/(-a) + m)}{\Gamma(x/(-a))} = (-a)^m \frac{\Gamma(-x/a + m)}{\Gamma(-x/a)}$$

The exponential generating function becomes:
$$\sum_{m=0}^{\infty} P(x,-a,m) \frac{z^m}{m!} = \sum_{m=0}^{\infty} (-a)^m \frac{\Gamma(-x/a + m)}{\Gamma(-x/a)} \frac{z^m}{m!}$$

Using the binomial series identity:
$$(1+w)^{\alpha} = \sum_{m=0}^{\infty} \frac{\Gamma(\alpha + m)}{\Gamma(\alpha)} \frac{w^m}{m!}$$

Setting $w = -az$ and $\alpha = -x/a$:
$$\sum_{m=0}^{\infty} (-a)^m \frac{\Gamma(-x/a + m)}{\Gamma(-x/a)} \frac{z^m}{m!} = (1 + (-az))^{-x/a} = (1-az)^{-x/a}$$

**Limit verification as $a \to 0$:** Using L'Hôpital's rule:
$$\lim_{a \to 0} (1-az)^{-x/a} = \lim_{a \to 0} \exp\left(\frac{-x}{a} \ln(1-az)\right) = e^{xz}$$
which matches the monomial case. □

### Graded Bell Polynomials in OGF Theory

**Definition:** The graded Bell polynomial $B_g(m,n)$ represents the sum of all possible products of $n$ different parts that add up to $m$, with each part weighted by the number of times it appears.

**OGF Relation:** The ordinary generating function for the graded Bell polynomial is given by:
$$\sum_{m=0}^{\infty} \sum_{n=0}^{m} B_g(m,n) \frac{z^m}{m!} = \frac{1}{1 - z - e^{-xz}}$$

**Special Cases:**
- $B_g(0,0) = 1$
- $B_g(m,0) = 0$ for $m > 0$
- $B_g(m,n) = 0$ for $m < n$

**Recurrence Relation:**
$$B_g(m,n) = \frac{1}{n} \sum_{j=n-1}^{m-1} B_g(j,n-1) a_{m-j}$$

**Connection to Factorial Polynomials:** The graded Bell polynomial can be expressed in terms of factorial polynomials as:
$$B_g(m,n) = \sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} P(m,k)$$

**Example Values:**
- $B_g(1,1) = 1$
- $B_g(2,1) = 2$, $B_g(2,2) = 1$
- $B_g(3,1) = 6$, $B_g(3,2) = 3$, $B_g(3,3) = 1$

Computational note (Maxima). A practical graded partial Bell polynomial (without multinomial factors) recursion matching the text is:
- Base: B_g(0,0)=1; B_g(m,0)=0 for m>0; B_g(m,n)=0 for m<n
- Recurrence: B_g(m,n) = (1/n) ∑_{j=n-1}^{m-1} B_g(j,n−1) a_{m−j}

The following Maxima code accepts either a list a=[a1,a2,…] (1-based) or a function a(k):

```maxima
/* graded Bell polynomials B_g(m,n; a): ordinary (no multinomial weights) */
bellg(m,n,a) := block(
  /* Guards and bases */
  if m = 0 and n = 0 then return(1)
  elseif n = 0 or m < 0 or n < 0 then return(0)
  elseif m < n then return(0),
  /* Accessor for a_{k}: list or function */
  a_k : lambda([k], if listp(a) then a[k] else a(k)),
  /* Recurrence: (1/n) * sum_{j=n-1}^{m-1} B_g(j,n-1) * a_{m-j} */
  (1/n) * sum( bellg(j,n-1,a) * a_k(m - j), j, n-1, m-1 )
)$

/* Example: with a = [a1,a2,a3,a4], B_g(4,3)=a1^2*a2 */
example_bg_4_3 : bellg(4,3,[a1,a2,a3,a4]);
/* => a1^2*a2 */
```

This implementation matches the graded (unweighted) definition used in the OGF context and is convenient for symbolic checks (e.g., a_j ≡ 1, alternating signs, factorial inputs).

### Notation Convention (Index Domains)

We write sums with bare indices and state the index domain afterward in set notation. For example:
\[
\sum_m c_m\,x^m,\quad \text{where } m\in\mathbb{N}_0.
\]

### Unified View: Same Function as OGF and EGF

A function can be viewed with either ordinary or exponential normalization:
\[
f(x) \;=\; \sum_m \alpha_m\,x^m \;=\; \sum_m \frac{a_m}{m!}\,x^m,\quad \text{where } m\in\mathbb{N}_0,
\]
with the coefficient relation
\[
\alpha_m \;=\; \frac{a_m}{m!}\quad\Longleftrightarrow\quad a_m \;=\; m!\,\alpha_m,\quad \text{where } m\in\mathbb{N}_0.
\]

Corresponding generating functions:
\[
G_f(z) \;=\; \sum_m \alpha_m\,z^m,\quad \text{where } m\in\mathbb{N}_0,
\]
\[
E_f(z) \;=\; \sum_m \frac{a_m}{m!}\,z^m,\quad \text{where } m\in\mathbb{N}_0.
\]

Remarks:
- OGF and EGF differ only by factorial normalization of coefficients.
- Transformations are immediate via \(a_m=m!\alpha_m\) and \(\alpha_m=a_m/m!\).

## Appendix C: Bell Polynomials and Their Generating Functions

This appendix explores Bell polynomials, their properties, and their generating functions, building upon the foundations laid in Appendix B.

### Bell Polynomials Overview

**Bell Polynomial \(B(m,n)\):** Counts partitions of \(m\) labeled objects into \(n\) non-empty unlabeled subsets.

**Exponential Generating Function (EGF):**
$$\sum_{m=n}^{\infty} B(m,n) \frac{z^m}{m!} = \frac{1}{n!} \left( e^z - \sum_{k=0}^{n-1} \frac{z^k}{k!} \right)$$

**Special Cases:**
- \(B(0,0) = 1\)
- \(B(m,0) = 0\) for \(m > 0\)
- \(B(m,1) = 1\) for \(m \geq 1\)

**Recurrence Relation:**
$$B(m,n) = \sum_{k=0}^{n-1} \binom{n-1}{k} B(m-1,k)$$

**Connection to Factorial Polynomials:**
$$B(m,n) = \sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} P(m,k)$$

**Example Values:**
- \(B(1,1) = 1\)
- \(B(2,1) = 1\), \(B(2,2) = 1\)
- \(B(3,1) = 1\), \(B(3,2) = 3\), \(B(3,3) = 1\)

**Computational Note (Maxima):** For unweighted Bell polynomials:
```maxima
/* Bell polynomials B(m,n): ordinary (no multinomial weights) */
bell(m,n) := block(
  /* Guards and bases */
  if m = 0 and n = 0 then return(1)
  elseif n = 0 or m < 0 or n < 0 then return(0)
  elseif m < n then return(0),
  /* Recurrence: sum_{k=0}^{n-1} B(m-1,k) */
  sum( bell(m-1,k) , k, 0, n-1 )
)$

/* Example: bell(4,3) */
example_bell_4_3 : bell(4,3);
/* => 6 */
```

### Bell Polynomial Properties

- **Symmetry:** \(B(m,n) = B(m,m-n)\)
- **Stirling Numbers Relation:
  - First kind: \(c(m,n) = \sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} B(m,k)\)
  - Second kind: \(S(m,n) = \frac{1}{n!} \sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} k^m\)

### Corrected Subdiagonal Pattern

For all $m \geq 2$:
$$\boxed{\beta_{m,m-1}(\alpha) = \alpha_2 \frac{\alpha_1^{m-2}}{(m-2}!}$$

**Combinatorial proof:** The only partition of $m$ into $m-1$ parts is $2+1+\cdots+1$ (one part of size 2 and $m-2$ parts of size 1). The graded weight without multinomial factors is:
$$\frac{1}{(m_2)!(m_1)!} \alpha_2^{m_2} \alpha_1^{m_1} = \frac{1}{1!(m-2)!} \alpha_2 \alpha_1^{m-2} = \alpha_2 \frac{\alpha_1^{m-2}}{(m-2)!}$$

**Verification by recurrence:** Using $\beta_{m,m-1} = \frac{1}{m-1}(\alpha_1 \beta_{m-1,m-2} + \alpha_2 \beta_{m-2,m-2})$ with inductive hypotheses:
- $\beta_{m-1,m-2} = \alpha_2 \alpha_1^{m-3}/(m-3)!$
- $\beta_{m-2,m-2} = \alpha_1^{m-2}/(m-2)!$

This yields:
$$\beta_{m,m-1} = \frac{\alpha_2 \alpha_1^{m-2}}{m-1} \left(\frac{1}{(m-3)!} + \frac{1}{(m-2)!}\right) = \alpha_2 \frac{\alpha_1^{m-2}}{(m-2)!}$$

## Special Case: P(-1,-1,n) and OGF Reciprocals

### Definition and Basic Properties

The special case P(-1,-1,n) represents a falling factorial starting at -1:

$$P(-1,-1,n) = (-1)(-2)(-3)\cdots(-n) = (-1)^n \cdot n!$$

**Key Properties:**
- **Sign alternation**: Even n gives positive values, odd n gives negative values
- **Magnitude**: $|P(-1,-1,n)| = n!$ 
- **Recurrence**: $P(-1,-1,n+1) = -(n+1) \cdot P(-1,-1,n)$

### Connection to OGF Reciprocals

This case provides coefficients for the "power rule" in OGF reciprocal expansions. For the basic geometric series:

$$\frac{1}{1+x} = \sum_{n=0}^{\infty} (-1)^n x^n = \sum_{n=0}^{\infty} \frac{P(-1,-1,n)}{n!} x^n$$

**Verification:**
- $P(-1,-1,0) = 1 \Rightarrow$ coefficient of $x^0$ is $1/0! = 1$ ✓
- $P(-1,-1,1) = -1 \Rightarrow$ coefficient of $x^1$ is $-1/1! = -1$ ✓  
- $P(-1,-1,2) = 2 \Rightarrow$ coefficient of $x^2$ is $2/2! = 1$ ✓

### Exponential Generating Function

$$\sum_{n=0}^{\infty} P(-1,-1,n) \frac{x^n}{n!} = \sum_{n=0}^{\infty} (-1)^n x^n = \frac{1}{1+x}$$

This is the key connection showing how alternating factorials encode OGF reciprocal structure.

### Computational Notes

For large n, use logarithmic computation:
- $\log|P(-1,-1,n)| = \log(n!)$
- $\text{sign}(P(-1,-1,n)) = (-1)^n$

Direct computation becomes numerically challenging around n = 20 due to factorial growth.
