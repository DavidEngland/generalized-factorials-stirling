# Mathematical Background of Generalized Stirling Numbers

This document provides the mathematical theory behind the generalized Stirling numbers $L_{n,k}^{\alpha,\beta}$ as described in the paper "Combinatorial approach of certain generalized Stirling numbers" by Belbachir, Belkhir, and Bousbaa.

## 1. Introduction

### 1.1 Classical Stirling Numbers

The classical Stirling numbers have well-established combinatorial interpretations:

- **Stirling numbers of the first kind** $s(n,k)$ count permutations of $n$ elements with exactly $k$ cycles.
- **Stirling numbers of the second kind** $S(n,k)$ count partitions of a set of $n$ elements into exactly $k$ non-empty subsets.
- **Lah numbers** $L(n,k)$ count partitions of a set of $n$ elements into exactly $k$ non-empty ordered lists.

These numbers satisfy the following recurrence relations:
- $s(n,k) = s(n-1,k-1) + (n-1)s(n-1,k)$
- $S(n,k) = S(n-1,k-1) + kS(n-1,k)$
- $L(n,k) = L(n-1,k-1) + (n+k-1)L(n-1,k)$

### 1.2 Generalization Framework

The generalized Stirling numbers $L_{n,k}^{\alpha,\beta}$ unify these three sequences through parameters $\alpha$ and $\beta$, where:
- $L_{n,k}^{1,0} = s(n,k)$ (Stirling numbers of the first kind)
- $L_{n,k}^{0,1} = S(n,k)$ (Stirling numbers of the second kind)
- $L_{n,k}^{1,1} = L(n,k)$ (Lah numbers)

## 2. Combinatorial Interpretation

The generalized Stirling numbers $L_{n,k}^{\alpha,\beta}$ represent the total weight of all possible ways to distribute $n$ elements (labeled $1,2,\ldots,n$) into $k$ ordered non-empty lists, where:

1. The first element placed in each list has weight 1
2. Elements placed at the head of a list have weight $\beta$
3. Other elements in the lists have weight $\alpha$

The weight of a particular distribution is the product of the weights of all elements according to their positions.

### 2.1 Example: $L_{3,1}^{\alpha,\beta}$

For $n=3, k=1$ (distributing 3 elements into 1 ordered list):

| Distribution | Weight | Explanation |
|--------------|--------|-------------|
| $(1,2,3)$    | $\alpha^2$ | First element has weight 1, others have weight $\alpha$ |
| $(1,3,2)$    | $\alpha^2$ | First element has weight 1, others have weight $\alpha$ |
| $(3,1,2)$    | $\alpha\beta$ | First element has weight 1, head has weight $\beta$, other has weight $\alpha$ |
| $(2,1,3)$    | $\alpha\beta$ | First element has weight 1, head has weight $\beta$, other has weight $\alpha$ |
| $(2,3,1)$    | $\alpha\beta$ | First element has weight 1, head has weight $\beta$, other has weight $\alpha$ |
| $(3,2,1)$    | $\beta^2$ | First element has weight 1, both others are heads with weight $\beta$ |

Total weight = $2\alpha^2 + 3\alpha\beta + \beta^2 = (\alpha+\beta)(2\alpha+\beta)$

## 3. Mathematical Properties

### 3.1 Explicit Formula

Using the inclusion-exclusion principle:

$$L_{n,k}^{\alpha,\beta} = \frac{1}{\beta^k k!}\sum_{j=0}^{k}(-1)^j \binom{k}{j}(\beta(k-j)|\alpha)^{\overline{n}}$$

where $(\beta(k-j)|\alpha)^{\overline{n}}$ is the generalized rising factorial:

$$(\beta(k-j)|\alpha)^{\overline{n}} = \beta(k-j)(\beta(k-j)+\alpha)(\beta(k-j)+2\alpha)\cdots(\beta(k-j)+(n-1)\alpha)$$

### 3.2 Recurrence Relations

#### 3.2.1 Triangular Recurrence

$$L_{n,k}^{\alpha,\beta} = L_{n-1,k-1}^{\alpha,\beta} + (\alpha(n-1) + \beta k)L_{n-1,k}^{\alpha,\beta}$$

with base cases:
- $L_{n,0}^{\alpha,\beta} = \delta_{n,0}$ (1 if n=0, 0 otherwise)
- $L_{0,k}^{\alpha,\beta} = \delta_{0,k}$ (1 if k=0, 0 otherwise)
- $L_{n,k}^{\alpha,\beta} = 0$ for $k > n$
- $L_{n,n}^{\alpha,\beta} = 1$ for $n \geq 0$

#### 3.2.2 Horizontal Recurrence

$$L_{n,k}^{\alpha,\beta} = \sum_{j=0}^{n-k}(-1)^j((k+1)\beta + n\alpha|\alpha)^{\overline{j}}L_{n+1,k+j+1}^{\alpha,\beta}$$

#### 3.2.3 Vertical Recurrence

$$L_{n+1,k+1}^{\alpha,\beta} = \sum_{i=k}^{n}(\alpha+\beta|\alpha)^{\overline{n-i}}\binom{n}{i}L_{i,k}^{\alpha,\beta}$$

### 3.3 Special Case: k=1

For $k=1$, we have the simple product formula:

$$L_{n,1}^{\alpha,\beta} = \prod_{j=1}^{n-1}(j\alpha + \beta)$$

### 3.4 Symmetric Functions

The generalized Stirling numbers can be expressed in terms of elementary symmetric functions:

$$L_{n+k,n}^{\alpha,\beta} = \sum_{1 \leq i_1 \leq \cdots \leq i_k \leq n}\prod_{j=1}^{k}((\alpha+\beta)i_j + \alpha(j-1))$$

## 4. Applications

Generalized Stirling numbers have applications in:

1. **Combinatorial analysis**: Counting with weights and constraints
2. **Statistical physics**: Partition functions with weighted states
3. **Computer science**: Analysis of algorithms with weighted structures
4. **Number theory**: Generalizations of factorial-like sequences

## 5. Implementation Considerations

When implementing generalized Stirling numbers, consider:

1. **Numerical stability**: For large values, use logarithmic computations
2. **Memoization**: Cache computed values due to the recursive nature
3. **Asymptotic approximations**: For very large values, use approximation formulas
4. **Special case optimizations**: Use direct formulas for special cases like k=1 or n=k

## References

1. H. Belbachir, A. Belkhir, I.E. Bousbaa. "Combinatorial approach of certain generalized Stirling numbers." arXiv:1411.6271v1, 2014.
2. L.C. Hsu, P.J.-S. Shiue. "A unified approach to generalized Stirling numbers." Adv. in Appl. Math., 20(3):366-384, 1998.
3. A.Z. Broder. "The r-Stirling numbers." Discrete Math., 49(3):241-259, 1984.
4. L. Carlitz. "Weighted Stirling numbers of the first and second kind." Fibonacci Quart., 18(2):147-162, 1980.
