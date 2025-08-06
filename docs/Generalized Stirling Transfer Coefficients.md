### Generalized Stirling Transfer Coefficients

**Abstract:** Generalized Stirling Transfer Coefficients provide a unified framework for expressing linear transformations between generalized factorial polynomials with different increment parameters. These coefficients generalize the classical Stirling numbers of both kinds, allowing for seamless transitions between various polynomial bases such as monomials, rising factorials, and falling factorials. Their applications span combinatorics, special function theory, and numerical analysis, where they enable the translation of results and identities across different polynomial representations.

The **Generalized Stirling Transfer Coefficients**, denoted as $S_{m,n}(a,b)$, are mathematical coefficients that express the linear transformation between generalized factorial polynomials with different increment parameters. These coefficients generalize the classical Stirling numbers and provide a unified framework for understanding polynomial transformations in combinatorics and special function theory.

## Definition

### Primary Definition

The **Generalized Stirling Transfer Coefficients** $S_{m,n}(a,b)$ are defined by the linear expansion:

$$P(x,a,m) = \sum_{n=0}^{m} S_{m,n}(a,b) \cdot P(x,b,n) \tag{1}$$

where:

* $P(x,a,m)$ and $P(x,b,n)$ are generalized factorial polynomials,
* $a$ and $b$ are increment parameters (constants),
* $m$ and $n$ are non-negative integers,
* $S_{m,n}(a,b)$ represents the coefficient for transforming from increment $b$ to increment $a$.

### Interpretation

The coefficients $S_{m,n}(a,b)$ capture how a generalized factorial polynomial with increment parameter $a$ can be expressed as a linear combination of generalized factorial polynomials with increment parameter $b$. This transformation is fundamental in connecting different factorial representations.

## Relationship to Classical Stirling Numbers

### Stirling Numbers of the First Kind

When $a = 0$ and $b = 1$, the generalized coefficients reduce to the **signed Stirling numbers of the first kind**, $s(m,n)$:

$$x^m = \sum_{n=0}^{m} s(m,n) \cdot P(x,1,n) \tag{2}$$

This is because $P(x,0,m) = x^m$ and $P(x,1,n) = x(x+1)\cdots(x+n-1)$ is the rising factorial.

### Stirling Numbers of the Second Kind

When $a = 1$ and $b = 0$, the generalized coefficients relate to the **Stirling numbers of the second kind**, $S(m,n)$. The transformation from a rising factorial to a monomial is given by:

$$P(x,1,m) = \sum_{n=0}^{m} S(m,n) \cdot x^n \tag{3}$$

This directly relates the generalized coefficients to the combinatorial interpretation of $S(m,n)$.

---

## Matrix Representations

The relationships between classical and generalized Stirling numbers are best understood through their matrix representations. Each matrix below corresponds to a specific transformation between polynomial bases. For clarity, this section is divided into two parts: **Classical Stirling Numbers** and **Generalized Stirling Transfer Coefficients**.

**Note on Matrix Structure:** All Stirling number matrices have trivial first row and column entries due to boundary conditions, which reflect the degree-preserving nature of polynomial transformations. The matrices below show only the non-trivial entries starting from the $(1,1)$ position.

### Classical Stirling Numbers

#### Stirling Numbers of the First Kind (Signed): $s(m,n)$

The signed Stirling numbers of the first kind, $s(m,n)$, correspond to the transformation from monomials to rising factorials. The matrix $\mathbf{S}_1^{(-)}$ (showing entries for $m,n \ge 1$) is:

$$
\mathbf{S}_1^{(-)} = \begin{pmatrix}
1 & 0 & 0 & 0 & 0 & \cdots \\
-1 & 1 & 0 & 0 & 0 & \cdots \\
2 & -3 & 1 & 0 & 0 & \cdots \\
-6 & 11 & -6 & 1 & 0 & \cdots \\
24 & -50 & 35 & -10 & 1 & \cdots \\
-120 & 274 & -225 & 85 & -15 & \cdots \\
\vdots & \vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

**Combinatorial interpretation:** $|s(m,n)|$ counts the number of permutations of $m$ elements with exactly $n$ cycles. The sign is $(-1)^{m-n}$.

#### Stirling Numbers of the First Kind (Unsigned): $|s(m,n)|$

The unsigned Stirling numbers of the first kind, $|s(m,n)|$, correspond to the transformation from monomials to falling factorials. The matrix $\mathbf{S}_1^{(+)}$ (for $m,n \ge 1$) is:

$$
\mathbf{S}_1^{(+)} = \begin{pmatrix}
1 & 0 & 0 & 0 & 0 & \cdots \\
1 & 1 & 0 & 0 & 0 & \cdots \\
2 & 3 & 1 & 0 & 0 & \cdots \\
6 & 11 & 6 & 1 & 0 & \cdots \\
24 & 50 & 35 & 10 & 1 & \cdots \\
120 & 274 & 225 & 85 & 15 & \cdots \\
\vdots & \vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

The relationship is: $|s(m,n)| = (-1)^{m-n} s(m,n)$.

#### Stirling Numbers of the Second Kind: $S(m,n)$

The Stirling numbers of the second kind, $S(m,n)$, correspond to the transformation from rising factorials to monomials. The matrix $\mathbf{S}_2$ (for $m,n \ge 1$) is:

$$
\mathbf{S}_2 = \begin{pmatrix}
1 & 0 & 0 & 0 & 0 & \cdots \\
1 & 1 & 0 & 0 & 0 & \cdots \\
1 & 3 & 1 & 0 & 0 & \cdots \\
1 & 7 & 6 & 1 & 0 & \cdots \\
1 & 15 & 25 & 10 & 1 & \cdots \\
1 & 31 & 90 & 65 & 15 & \cdots \\
\vdots & \vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

**Combinatorial interpretation:** $S(m,n)$ counts the number of ways to partition a set of $m$ labeled elements into $n$ non-empty, unlabeled subsets.

#### Orthogonality Relationship

The matrices $\mathbf{S}_1^{(-)}$ and $\mathbf{S}_2$ are **inverses** of each other:

$$\mathbf{S}_1^{(-)} \cdot \mathbf{S}_2 = \mathbf{I} \tag{4}$$

In summation notation:
$$\sum_{k=0}^m s(m, k) \, S(k, n) = [m = n]$$
This reflects that the transformation from monomials to rising factorials and back is the identity.

### Generalized Stirling Transfer Coefficient Matrices

The following matrices generalize the classical cases to arbitrary increment parameters, unifying transformations between various factorial polynomial bases.

#### Case 1: $S_{m,n}(0,1)$ - Monomial to Rising Factorial

This matrix is identical to the signed Stirling numbers of the first kind: $\mathbf{S}(0,1) = \mathbf{S}_1^{(-)}$.

#### Case 2: $S_{m,n}(1,0)$ - Rising Factorial to Monomial

This matrix is identical to the Stirling numbers of the second kind: $\mathbf{S}(1,0) = \mathbf{S}_2$.

#### Case 3: $S_{m,n}(1,-1)$ - Rising to Falling Factorial (Lah Numbers)

The coefficients for this transformation are related to the **Lah numbers**, $L(m,n)$. The matrix is:

$$
\mathbf{S}(1,-1) = \begin{pmatrix}
1 & 0 & 0 & 0 & 0 & \cdots \\
2 & 1 & 0 & 0 & 0 & \cdots \\
6 & 6 & 1 & 0 & 0 & \cdots \\
24 & 36 & 12 & 1 & 0 & \cdots \\
120 & 240 & 120 & 20 & 1 & \cdots \\
\vdots & \vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

The relationship is: $S_{m,n}(1,-1) = (-1)^{m-n} L(m,n)$, where $L(m,n)$ are the unsigned Lah numbers.

#### Case 4: $S_{m,n}(-1,1)$ - Falling to Rising Factorial

This is the inverse of the Lah transformation: $\mathbf{S}(-1,1) = \mathbf{S}(1,-1)^{-1}$.

#### Case 5: $S_{m,n}(0,-1)$ - Monomial to Falling Factorial

This matrix is identical to the unsigned Stirling numbers of the first kind: $\mathbf{S}(0,-1) = \mathbf{S}_1^{(+)}$.

#### Case 6: $S_{m,n}(-1,0)$ - Falling Factorial to Monomial

The transformation from falling factorials to monomials is:

$$
\mathbf{S}(-1,0) = \begin{pmatrix}
1 & 0 & 0 & 0 & 0 & \cdots \\
-1 & 1 & 0 & 0 & 0 & \cdots \\
1 & -3 & 1 & 0 & 0 & \cdots \\
-1 & 7 & -6 & 1 & 0 & \cdots \\
1 & -15 & 25 & -10 & 1 & \cdots \\
-1 & 31 & -90 & 65 & -15 & \cdots \\
\vdots & \vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

---

## Properties and Identities

### Fundamental Properties

#### Identity Transformation
$$S_{m,n}(a,a) = [m = n] \tag{5}$$
This means the coefficient matrix is the identity when the increment parameters are identical.

#### Triangular Structure
$$S_{m,n}(a,b) = 0 \quad \text{for } n > m \tag{6}$$
The coefficient matrix is upper triangular, as transformations do not increase the polynomial degree.

#### Inverse Transformation Property
For any parameters $a$ and $b$, the coefficients $S_{m,n}(a,b)$ and $S_{m,n}(b,a)$ form inverse transformations:

$$\sum_{k=0}^{m} S_{m,k}(a,b) \cdot S_{k,n}(b,a) = [m = n] \tag{7}$$

This ensures that transformations between any two parameter regimes are bijective and reversible.

### Recurrence Relations

The generalized coefficients satisfy recurrence relations derived from the properties of generalized factorial polynomials. These recurrences are generalizations of the well-known relationships for classical Stirling numbers.

For example, the recurrence for the unsigned Stirling numbers of the first kind (monomial to falling factorial) is:

\[
\left[ \begin{array}{c} m+1 \\ n \end{array} \right] = m \left[ \begin{array}{c} m \\ n \end{array} \right] + \left[ \begin{array}{c} m \\ n-1 \end{array} \right]
\]

And for the Stirling numbers of the second kind (rising factorial to monomial) is:

\[
\left\{ \begin{array}{c} m+1 \\ n \end{array} \right\} = n \left\{ \begin{array}{c} m \\ n \end{array} \right\} + \left\{ \begin{array}{c} m \\ n-1 \end{array} \right\}
\]

These classical recurrences are special cases of a more general recurrence for $S_{m,n}(a,b)$.

---

## Decomposition into Classical Stirling Numbers

### Scaling Property and Fundamental Decomposition

When both $a$ and $b$ are non-zero, the generalized Stirling transfer coefficients can be expressed as a combination of classical Stirling numbers. This is a result of the scaling property of the generalized factorial polynomials: $P(x,a,m) = a^m P(x/a, 1, m)$.

This property allows us to express any transformation $S_{m,n}(a,b)$ as a scaled composition of three simpler transformations: from base $a$ to base 1, from base 1 to base 0 (monomial), and then from base 0 back to base $b$. This decomposition leads to the key result that all generalized Stirling transfer coefficients are simply scaled combinations of the classical Stirling numbers.

### Lah Numbers as a Special Case

The **Lah numbers**, $L(m,n)$, are a particularly elegant special case that emerges when we consider specific parameter ratios. For the transformation between rising and falling factorials (with unit increments), we have:

$$S_{m,n}(1,-1) = (-1)^{m-n} L(m,n) \tag{8}$$

where $L(m,n)$ are the unsigned Lah numbers, defined by the formula $L(m,n) = \binom{m-1}{n-1} \frac{m!}{n!}$. This shows that Lah numbers are simply generalized Stirling transfer coefficients with a specific parameter choice, fitting perfectly into the unified framework.

---

## Conclusion and Future Work

The framework of generalized Stirling transfer coefficients unifies a wide range of combinatorial and analytical problems. They provide a powerful tool for understanding polynomial transformations, with applications in numerical analysis and special function theory.

Future work will focus on:
* Developing a concise combinatorial proof of the general nature of these coefficients.
* Deriving the full exponential generating functions for all parameter combinations.
* Creating a comprehensive historical survey of the field.

This framework represents a significant step in generalizing classical combinatorial ideas to a broader mathematical context.