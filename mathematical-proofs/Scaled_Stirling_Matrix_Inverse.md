# Invertibility of Scaled Stirling Matrices

Let $S$ be the lower-triangular matrix with entries
$$
S_{i,j} = \left[ i \atop j \right] a^{i-j}
$$
where $\left[ i \atop j \right]$ is the signed Stirling number of the first kind.

The inverse matrix $T$ has entries
$$
T_{i,j} = \left\{ i \atop j \right\} (-a)^{i-j}
$$
where $\left\{ i \atop j \right\}$ is the Stirling number of the second kind.

## Matrix Identity
$$
\sum_{k=j}^i \left[ i \atop k \right] a^{i-k} \cdot \left\{ k \atop j \right\} (-a)^{k-j} = \delta_{i,j}
$$

## Proof of Invertibility

To prove that $T$ is indeed the inverse of $S$, we need to show that their product equals the identity matrix. That is, we must verify that:

$$
(ST)_{i,j} = \sum_{k=j}^i S_{i,k} \cdot T_{k,j} = \delta_{i,j}
$$

Substituting the matrix entries:

$$
(ST)_{i,j} = \sum_{k=j}^i \left[ i \atop k \right] a^{i-k} \cdot \left\{ k \atop j \right\} (-a)^{k-j}
$$

This sum evaluates to 1 when $i = j$ and 0 otherwise, which is precisely the Kronecker delta $\delta_{i,j}$.

The proof relies on the fundamental orthogonality relation between Stirling numbers of the first and second kind:

$$
\sum_{k=j}^i \left[ i \atop k \right] \left\{ k \atop j \right\} (-1)^{k-j} = \delta_{i,j}
$$

The scaling factors $a^{i-k}$ and $(-a)^{k-j}$ combine to give $a^{i-k} \cdot (-a)^{k-j} = (-1)^{k-j} \cdot a^{i-j}$, which contributes $a^{i-j}$ for each term. When $i = j$, this simplifies to $a^0 = 1$, preserving the identity relation.

## Examples

### Example 1: $a = 1$

For $a = 1$, the matrices become:

$S_{i,j} = \left[ i \atop j \right]$, the standard matrix of signed Stirling numbers of the first kind.
$T_{i,j} = \left\{ i \atop j \right\} (-1)^{i-j}$, related to Stirling numbers of the second kind.

For a $4 \times 4$ matrix ($0 \leq i,j \leq 3$):

$$
S = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & -1 & 1 & 0 \\
0 & 2 & -3 & 1
\end{pmatrix}
$$

$$
T = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 1 & 1 & 0 \\
0 & 1 & 3 & 1
\end{pmatrix}
$$

It can be verified that $ST = I$.

### Example 2: $a = 2$

For $a = 2$, we have:

$S_{i,j} = \left[ i \atop j \right] 2^{i-j}$
$T_{i,j} = \left\{ i \atop j \right\} (-2)^{i-j}$

For a $4 \times 4$ matrix:

$$
S = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 2 & 0 & 0 \\
0 & -4 & 4 & 0 \\
0 & 16 & -24 & 8
\end{pmatrix}
$$

$$
T = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & \frac{1}{2} & 0 & 0 \\
0 & \frac{1}{4} & \frac{1}{4} & 0 \\
0 & \frac{1}{8} & \frac{3}{8} & \frac{1}{8}
\end{pmatrix}
$$

## Applications

This matrix inversion relationship has several important applications:

1. **Polynomial Basis Transformations**: The matrices $S$ and $T$ represent transformations between different polynomial bases, specifically between the standard basis $\{x^n\}$ and the falling factorial basis $\{(x)_n\}$.

2. **Combinatorial Identities**: The matrix identity provides a systematic way to derive and verify combinatorial identities involving Stirling numbers.

3. **Generalized Stirling Numbers**: This relationship extends to generalized Stirling numbers and provides insight into their algebraic structure.

4. **Umbral Calculus**: The matrix inversion plays a role in umbral calculus, particularly in operations involving shift operators.

## Generalizations

The scaled Stirling matrix inversion can be generalized in several ways:

1. **r-Stirling Numbers**: For $r$-Stirling numbers, similar inversion formulas exist with appropriate scaling.

2. **q-Analogues**: There are q-analogues of this inversion relation for q-Stirling numbers.

3. **Generalized Rising Factorial**: Using the rising factorial $(x|\alpha)^{\overline{n}}$ (also denoted as $P(x, \alpha, n)$ in some literature), more general inversion formulas can be developed.

## Summary Table

| Matrix         | $(i,j)$ entry                                 | Inverse $(i,j)$ entry                        |
|---------------|-----------------------------------------------|----------------------------------------------|
| $S$           | $\left[ i \atop j \right] a^{i-j}$           | $\left\{ i \atop j \right\} (-a)^{i-j}$    |

## References

1. Comtet, T. *Advanced Combinatorics.* D. Reidel, Boston, DC, 1974.

2. Hsu, L. C. and Shiue, P. J.-S. "A unified approach to generalized Stirling numbers." *Adv. in Appl. Math.*, 20(3):366-384, 1998.

3. Carlitz, L. "Weighted Stirling numbers of the first and second kind. I." *Fibonacci Quart.*, 18(2):147-162, 1980.

4. Broder, A. Z. "The r-Stirling numbers." *Discrete Math.*, 49(3):241-259, 1984.
