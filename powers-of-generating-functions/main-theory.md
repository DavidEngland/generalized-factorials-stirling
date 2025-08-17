# The Power of an Ordinary Generating Function: Complete Theory

## Abstract

We investigate the expansion of $[f(x)]^z$ where $f(x) = \sum_{m=0}^{\infty} \alpha_m x^m$ is an ordinary generating function with $f(0) = \alpha_0 \neq 0$. This expansion yields a fundamental connection between falling factorial polynomials $P(z,-1,m)$, normalized graded Bell polynomials $\beta_{m,k}$, and generating function coefficients, providing a unified framework for coefficient extraction and combinatorial interpretation.

## 1. Setup and Motivation

### 1.1 The Central Problem

Given an ordinary generating function:
$$f(x) = \sum_{m=0}^{\infty} \alpha_m x^m \quad \text{with } \alpha_0 \neq 0$$

we seek to understand the expansion of its $z$-th power:
$$[f(x)]^z = \sum_{n=0}^{\infty} c_n(z) x^n$$

The coefficients $c_n(z)$ encode rich combinatorial and analytical information, and our goal is to express them in terms of fundamental mathematical objects.

### 1.2 Key Insight: Normalization

Without loss of generality, we can factor out the constant term:
$$f(x) = \alpha_0 \left(1 + \sum_{m=1}^{\infty} \frac{\alpha_m}{\alpha_0} x^m\right) = \alpha_0 g(x)$$

where $g(x) = 1 + \sum_{m=1}^{\infty} a_m x^m$ with $a_m = \alpha_m/\alpha_0$.

Therefore:
$$[f(x)]^z = \alpha_0^z [g(x)]^z$$

This normalization is crucial because it separates the scaling factor $\alpha_0^z$ from the structural information contained in $[g(x)]^z$.

## 2. The Main Theorem: Power Expansion Formula

### 2.1 Statement of the Main Result

**Theorem 2.1 (OGF Power Expansion).** Let $f(x) = \sum_{m=0}^{\infty} \alpha_m x^m$ with $\alpha_0 \neq 0$. Then:

$$\boxed{[x^m] [f(x)]^z = \alpha_0^z \sum_{k=0}^{m} P(z,-1,k) \beta_{m,k}\left(\frac{\alpha_1}{\alpha_0^2}, \frac{\alpha_2}{\alpha_0^3}, \frac{\alpha_3}{\alpha_0^4}, \ldots\right)}$$

where:
- $P(z,-1,k) = z(z-1)(z-2)\cdots(z-k+1)$ is the falling factorial polynomial
- $\beta_{m,k}$ are the normalized graded Bell polynomials

**Alternative Form using Scalar Factorization:**
Using the property $\beta_{m,k}(ca_1, ca_2, \ldots) = c^m \beta_{m,k}(a_1, a_2, \ldots)$:

$$\boxed{[x^m] [f(x)]^z = \alpha_0^{z-m} \sum_{k=0}^{m} P(z,-1,k) \beta_{m,k}\left(\frac{\alpha_1}{\alpha_0}, \frac{\alpha_2}{\alpha_0}, \frac{\alpha_3}{\alpha_0}, \ldots\right)}$$

### 2.2 Derivation via Multinomial Theorem

The expansion follows from the generalized multinomial theorem applied to:
$$[g(x)]^z = \left(1 + \sum_{j=1}^{\infty} a_j x^j\right)^z$$

Using the multinomial expansion:
$$[g(x)]^z = \sum_{k=0}^{\infty} \binom{z}{k} \left(\sum_{j=1}^{\infty} a_j x^j\right)^k$$

The term $\left(\sum_{j=1}^{\infty} a_j x^j\right)^k$ generates all ways to select $k$ terms from the infinite sum, which corresponds exactly to partitions counted by Bell polynomials.

### 2.3 Coefficient Extraction

The coefficient of $x^m$ in $[g(x)]^z$ is:
$$[x^m] [g(x)]^z = \sum_{k=0}^{m} \binom{z}{k} \beta_{m,k}(a_1, a_2, \ldots)$$

Using the identity $\binom{z}{k} = \frac{P(z,-1,k)}{k!}$:
$$[x^m] [g(x)]^z = \sum_{k=0}^{m} \frac{P(z,-1,k)}{k!} \beta_{m,k}(a_1, a_2, \ldots)$$

## 3. Foundation: Bell Polynomials and Falling Factorials

### 3.1 Normalized Graded Bell Polynomials

The normalized graded Bell polynomials $\beta_{m,k}$ are defined by the recurrence:
$$\beta_{m,k}(a_1, a_2, \ldots) = \frac{1}{k} \sum_{j=1}^{m-k+1} a_j \beta_{m-j, k-1}(a_1, a_2, \ldots)$$

with boundary conditions:
- $\beta_{0,0} = 1$
- $\beta_{m,0} = 0$ for $m > 0$ 
- $\beta_{m,k} = 0$ for $k > m$

**Combinatorial Interpretation:** Each term $\beta_{m,k}(a_1, a_2, \ldots)$ counts weighted partitions of the integer $m$ into exactly $k$ parts, where parts of size $j$ have weight $a_j$ and the normalization factor $1/k$ accounts for the unlabeled nature of the parts.

### 3.2 Falling Factorial Polynomials

The falling factorial polynomial is defined as:
$$P(z,-1,m) = z(z-1)(z-2)\cdots(z-m+1)$$

**Key Properties:**
- $P(z,-1,0) = 1$ (empty product)
- $P(z,-1,m+1) = P(z,-1,m) \cdot (z-m)$
- $P(z,-1,m) = (-1)^m P(-z,1,m)$ (connection to rising factorials)

**Binomial Coefficient Connection:**
$$\binom{z}{k} = \frac{P(z,-1,k)}{k!}$$

This identity is crucial for connecting the multinomial expansion to our Bell polynomial formulation.

## 4. Explicit Formula and Computational Framework

### 4.1 The Complete Expansion

The coefficient of $x^m$ in $[f(x)]^z$ can be expressed in two equivalent forms:

**Form 1 (Direct):**
$$[x^m] [f(x)]^z = \alpha_0^z \sum_{k=0}^{m} P(z,-1,k) \beta_{m,k}\left(\frac{\alpha_1}{\alpha_0^2}, \frac{\alpha_2}{\alpha_0^3}, \frac{\alpha_3}{\alpha_0^4}, \ldots\right)$$

**Form 2 (Using Scalar Factorization):**
$$\boxed{[x^m] [f(x)]^z = \alpha_0^{z-m} \sum_{k=0}^{m} P(z,-1,k) \beta_{m,k}\left(\frac{\alpha_1}{\alpha_0}, \frac{\alpha_2}{\alpha_0}, \frac{\alpha_3}{\alpha_0}, \ldots\right)}$$

The equivalence follows from the Bell polynomial scalar factorization:
$$\beta_{m,k}\left(\frac{\alpha_1}{\alpha_0^2}, \frac{\alpha_2}{\alpha_0^3}, \ldots\right) = \left(\frac{1}{\alpha_0}\right)^m \beta_{m,k}\left(\frac{\alpha_1}{\alpha_0}, \frac{\alpha_2}{\alpha_0}, \ldots\right)$$

### 4.2 Special Cases and Verification

**Case 1: Geometric Series**
For $f(x) = \frac{1}{1-ax} = \sum_{m=0}^{\infty} a^m x^m$:
- $\alpha_0 = 1$ and $\alpha_m/\alpha_0 = a$ for all $m \geq 1$
- Using scalar factorization: $\beta_{m,k}(a, a, a, \ldots) = a^m \beta_{m,k}(1, 1, 1, \ldots) = a^m [k = m]$

Result: $\left(\frac{1}{1-ax}\right)^z = \sum_{m=0}^{\infty} P(z,-1,m) a^m x^m = (1-ax)^{-z}$ ✓

**Case 2: Exponential-Type Series**
For $f(x) = \sum_{m=0}^{\infty} \frac{a^m}{m!} x^m$:
- $\alpha_0 = 1$ and $\alpha_m/\alpha_0 = a^m/m!$
- The scalar factorization reveals the exponential structure more clearly

**Case 3: Polynomial $f(x) = 1 + cx$**
For the simple case where only $\alpha_0 = 1$ and $\alpha_1 = c$ are non-zero:
- Using scalar factorization: $\beta_{m,k}(c, 0, 0, \ldots) = c^m \beta_{m,k}(1, 0, 0, \ldots)$
- Only $\beta_{1,1}(1, 0, 0, \ldots) = 1$ contributes, giving the binomial expansion

## 5. Advanced Topics and Extensions

### 5.1 Asymptotic Analysis

For large $m$, the dominant terms can be analyzed using:
- Saddle-point methods for the falling factorials
- Asymptotic expansions of Bell polynomials
- Hayman's method for coefficient extraction

### 5.2 q-Analogues

The framework extends to q-generating functions:
$$[f_q(x)]^z = \sum_{m=0}^{\infty} \alpha_0^{z-m} P_q(z,-1,m) \beta_{m,k}^{(q)}(a_1, a_2, \ldots) x^m$$

where $P_q$ are q-falling factorials and $\beta^{(q)}$ are q-Bell polynomials.

### 5.3 Multivariate Extensions

For multivariate OGFs $f(\mathbf{x}) = f(x_1, x_2, \ldots)$, the power expansion involves:
- Multivariate Bell polynomials
- Multi-index falling factorials
- Tensor products of partition structures

## 6. Connections to Other Mathematical Areas

### 6.1 Symmetric Functions

The Bell polynomials relate to:
- Elementary symmetric polynomials (for specific weight choices)
- Complete homogeneous symmetric polynomials
- Power sum symmetric polynomials

### 6.2 Representation Theory

The combinatorial structures connect to:
- Representations of the symmetric group
- Plethysm operations in representation theory
- Character theory of wreath products

### 6.3 Statistical Physics

Applications include:
- Partition functions of statistical mechanical models
- Virial expansions in gas theory
- Phase transition analysis

## 7. Conclusion

The power expansion of ordinary generating functions provides a unifying framework that connects:

1. **Falling factorial polynomials** - encoding the algebraic structure
2. **Normalized graded Bell polynomials** - capturing combinatorial constraints  
3. **Generating function coefficients** - providing the weights

This trinity reveals deep connections between combinatorics, special functions, and generating function theory. The explicit formula serves as both a computational tool and a theoretical bridge between discrete and continuous mathematics.

The framework's power lies not just in coefficient calculation, but in revealing the underlying mathematical structures that govern generating function behavior. Applications span probability theory, combinatorics, mathematical physics, and analytic number theory.

## References

1. Comtet, L. (1974). *Advanced Combinatorics: The Art of Finite and Infinite Expansions*. D. Reidel Publishing Company.
2. Stanley, R. P. (2012). *Enumerative Combinatorics* (2nd ed.). Cambridge University Press.
3. Riordan, J. (1968). *Combinatorial Identities*. John Wiley & Sons.
4. Bergeron, F., Labelle, G., & Leroux, P. (1998). *Combinatorial Species and Tree-like Structures*. Cambridge University Press.
5. Andrews, G. E., Askey, R., & Roy, R. (1999). *Special Functions*. Cambridge University Press.
6. Flajolet, P., & Sedgewick, R. (2009). *Analytic Combinatorics*. Cambridge University Press.

---

**Mathematical Subject Classification:** 05A15, 05A19, 33B15, 33C05  
**Keywords:** generating functions, Bell polynomials, falling factorials, coefficient extraction, combinatorial enumeration