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

## Summary Table

| Matrix         | $(i,j)$ entry                                 | Inverse $(i,j)$ entry                        |
|---------------|-----------------------------------------------|----------------------------------------------|
| $S$           | $\left[ i \atop j \right] a^{i-j}$           | $\left\{ i \atop j \right\} (-a)^{i-j}$    |

## Interpretation

The matrix of signed Stirling numbers of the first kind, scaled by $a^{i-j}$, is inverted by the matrix of Stirling numbers of the second kind, scaled by $(-a)^{i-j}$.
