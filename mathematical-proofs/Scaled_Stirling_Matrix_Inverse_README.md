# Invertibility of Scaled Stirling Matrices

Let S be the lower-triangular matrix with entries:

    S_{i,j} = [i \atop j] a^{i-j}

where [i \atop j] is the signed Stirling number of the first kind.

The inverse matrix T has entries:

    T_{i,j} = {i \atop j} (-a)^{i-j}

where {i \atop j} is the Stirling number of the second kind.

## Matrix Identity

    sum_{k=j}^i [i \atop k] a^{i-k} * {k \atop j} (-a)^{k-j} = delta_{i,j}

## Summary Table

| Matrix | (i,j) entry | Inverse (i,j) entry |
|--------|-------------------------------|-------------------------------|
| S      | [i \atop j] a^{i-j}           | {i \atop j} (-a)^{i-j}        |

## Interpretation

The matrix of signed Stirling numbers of the first kind, scaled by a^{i-j}, is inverted by the matrix of Stirling numbers of the second kind, scaled by (-a)^{i-j}.
