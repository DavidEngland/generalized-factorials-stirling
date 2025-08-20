# Generalized Stirling Numbers

This document explains the theory of generalized Stirling numbers $L_{n,k}^{\alpha,\beta}$ based on the paper "Combinatorial approach of certain generalized Stirling numbers" by Belbachir, Belkhir, and Bousbaa.

## Introduction

Stirling numbers are important combinatorial quantities with well-known interpretations:

- **Stirling numbers of the first kind** $s(n,k)$ count permutations of $n$ elements with exactly $k$ cycles
- **Stirling numbers of the second kind** $S(n,k)$ count partitions of $n$ elements into exactly $k$ non-empty subsets
- **Lah numbers** $L(n,k)$ count partitions of $n$ elements into exactly $k$ non-empty ordered lists

The paper introduces a generalization, denoted $L_{n,k}^{\alpha,\beta}$, that unifies these and provides additional flexibility through parameters $\alpha$ and $\beta$.

## Combinatorial Interpretation

The generalized Stirling numbers $L_{n,k}^{\alpha,\beta}$ represent the total weight of all possible ways to distribute $n$ elements into $k$ ordered non-empty lists, where:

1. The first element placed in each list has weight 1
2. Elements placed at the head of a list have weight $\beta$
3. Other elements in the lists have weight $\alpha$

The weight of a distribution is the product of the weights of all elements.

### Example

For $n=3, k=1$ (distributing 3 elements into 1 ordered list):

- Distribution (1,2,3): Weight = $\alpha^2$
- Distribution (1,3,2): Weight = $\alpha^2$
- Distribution (3,1,2): Weight = $\alpha\beta$
- Distribution (2,1,3): Weight = $\alpha\beta$
- Distribution (2,3,1): Weight = $\alpha\beta$
- Distribution (3,2,1): Weight = $\beta^2$

Total weight = $2\alpha^2 + 3\alpha\beta + \beta^2 = (\alpha+\beta)(2\alpha+\beta)$

## Special Cases

Setting specific values for $\alpha$ and $\beta$ yields classical number sequences:

- $(\alpha,\beta) = (1,0)$: Unsigned Stirling numbers of the first kind
- $(\alpha,\beta) = (0,1)$: Stirling numbers of the second kind
- $(\alpha,\beta) = (1,1)$: Lah numbers

## Explicit Formula

Using the inclusion-exclusion principle, we get:

$$L_{n,k}^{\alpha,\beta} = \frac{1}{\beta^k k!}\sum_{j=0}^{k}(-1)^j \binom{k}{j}(\beta(k-j)|\alpha)^{\overline{n}}$$

where $(\beta(k-j)|\alpha)^{\overline{n}}$ is the generalized rising factorial:

$$(\beta(k-j)|\alpha)^{\overline{n}} = \beta(k-j)(\beta(k-j)+\alpha)(\beta(k-j)+2\alpha)\cdots(\beta(k-j)+(n-1)\alpha)$$

## Recurrence Relations

### Triangular Recurrence

$$L_{n,k}^{\alpha,\beta} = L_{n-1,k-1}^{\alpha,\beta} + (\alpha(n-1) + \beta k)L_{n-1,k}^{\alpha,\beta}$$

This generalizes the recurrence relations for the classical Stirling numbers and Lah numbers.

### Horizontal Recurrence

$$L_{n,k}^{\alpha,\beta} = \sum_{j=0}^{n-k}(-1)^j((k+1)\beta + n\alpha|\alpha)^{\overline{j}}L_{n+1,k+j+1}^{\alpha,\beta}$$

### Vertical Recurrence

$$L_{n+1,k+1}^{\alpha,\beta} = \sum_{i=k}^{n}(\alpha+\beta|\alpha)^{\overline{n-i}}\binom{n}{i}L_{i,k}^{\alpha,\beta}$$

## Special Case: k=1

For the special case where $k=1$, we have:

$$L_{n,1}^{\alpha,\beta} = \prod_{j=1}^{n-1}(j\alpha + \beta)$$

## Symmetric Functions

The generalized Stirling numbers can be expressed as symmetric functions:

$$L_{n+k,n}^{\alpha,\beta} = \sum_{1 \leq i_1 \leq \cdots \leq i_k \leq n}\prod_{j=1}^{k}((\alpha+\beta)i_j + \alpha(j-1))$$

## Convolution Identities

The generalized Stirling numbers satisfy various convolution identities, including:

$$\binom{k}{k_1,\ldots,k_p}L_{n,k}^{\alpha,\beta} = \sum_{l_1+\cdots+l_p=n}\binom{n}{l_1,\ldots,l_p}L_{l_1,k_1}^{\alpha,\beta}\cdots L_{l_p,k_p}^{\alpha,\beta}$$

## Implementation Notes

Our implementation uses several approaches to compute these numbers:

1. **Triangular recurrence** - Most efficient for building tables of values
2. **Explicit formula** - Good for theoretical analysis and verification
3. **Special cases** - Optimized calculations for specific parameter values
4. **Symmetric functions** - Alternative computation method

## References

1. H. Belbachir, A. Belkhir, I.E. Bousbaa. "Combinatorial approach of certain generalized Stirling numbers." arXiv:1411.6271v1, 2014.

2. L. Carlitz. "Weighted Stirling numbers of the first and second kind." Fibonacci Quart., 18(2):147-162, 1980.

3. L.C. Hsu, P.J.-S. Shiue. "A unified approach to generalized Stirling numbers." Adv. in Appl. Math., 20(3):366-384, 1998.

4. A.Z. Broder. "The r-Stirling numbers." Discrete Math., 49(3):241-259, 1984.
