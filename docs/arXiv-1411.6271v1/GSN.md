# Generalized Stirling Numbers: Notation and Equivalence

## Introduction

Our approach and notation for generalized Stirling numbers, as presented here, is fundamentally equivalent to other frameworks in the literature, such as the $S_{m,n}(a,b)$ notation of Hsu and Shiue [Hsu & Shiue, 1998] and the $P(x,a,m)$ notation used in other works. The combinatorial interpretations, recurrence relations, and explicit formulas all correspond under suitable parameter substitutions. In particular, the generalized Stirling numbers and generalized Lah numbers are not fundamentally different objects, but rather different notational perspectives on the same combinatorial structure. This equivalence allows us to translate results and identities between frameworks without loss of generality.

## Explicit Formula for Generalized Lah Numbers

**Theorem:**  
For any non-negative integers $n,k$, we have
$$
L_{n,k}^{\alpha,\beta} = \frac{1}{\beta^k k!} \sum_{j=0}^{k} (-1)^j \binom{k}{j} (\beta(k-j)|\alpha)^{\overline{n}}
$$
where
$$
(\beta(k-j)|\alpha)^{\overline{n}} = \beta(k-j) \cdot (\beta(k-j) + \alpha) \cdots (\beta(k-j) + (n-1)\alpha)
$$

**Note:**  
The rising factorial $(\beta(k-j)|\alpha)^{\overline{n}}$ is equivalent to the notation $P(\beta(k-j), \alpha, n)$ used in other works. That is,
$$
P(x, a, n) = x \cdot (x + a) \cdots (x + (n-1)a)
$$
so $(\beta(k-j)|\alpha)^{\overline{n}} = P(\beta(k-j), \alpha, n)$.

## Notational Equivalence

The explicit formula above is directly analogous to the results obtained for $P(x,a,m)$ and $S_{m,n}(a,b)$ notations in other works. The combinatorial reasoning and inclusion-exclusion principle apply identically, and the resulting expressions are equivalent up to a change of parameters and notation. Thus, the generalized Stirling numbers and generalized Lah numbers presented here yield the same results as those frameworks.

## References

- Hsu, L.C., & Shiue, P.J.-S. (1998). A unified approach to generalized Stirling numbers. *Adv. in Appl. Math.*, 20(3), 366-384.
- Belbachir, H., & Belkhir, A. (2013). Cross recurrence relations for $r$-Lah numbers. *Ars Combin.*, 110, 199-203.
- Belbachir, H., & Bousbaa, I.E. (2014). Combinatorial identities for the $r$-Lah numbers. *Ars Combin.*, 110.
- Broder, A.Z. (1984). The $r$-Stirling numbers. *Discrete Math.*, 49(3), 241-259.
- Carlitz, L. (1980). Weighted Stirling numbers of the first and second kind. *Fibonacci Quart.*, 18(2), 147-162.
