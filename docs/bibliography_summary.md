# Bibliography Overview for Generalized Stirling Numbers

This document provides a brief overview of the key references used in our implementation of generalized Stirling numbers.

## Primary References

### Belbachir, Belkhir, and Bousbaa (2014)
**"Combinatorial approach of certain generalized Stirling numbers"**

This is the primary paper our implementation is based on. It introduces the generalized Stirling numbers L{n,k}^{α,β} with a combinatorial interpretation as weighted distributions of elements into ordered lists. The paper provides explicit formulas, recurrence relations, and connections to symmetric functions.

### Hsu and Shiue (1998)
**"A unified approach to generalized Stirling numbers"**

This paper introduces a broader framework S(n,k;α,β,r) that includes our L{n,k}^{α,β} as the special case S(n,k;-α,β,0). It provides a comprehensive theoretical foundation connecting various generalizations of Stirling numbers.

## Extensions and Special Cases

### Broder (1984)
**"The r-Stirling numbers"**

Introduces r-Stirling numbers, which count permutations with k cycles (or partitions into k subsets) where the elements 1,2,...,r are in different cycles (or subsets). These correspond to S(n,k;-1,0,r) and S(n,k;0,1,r) in the Hsu-Shiue framework.

### Benoumhani (1996)
**"On Whitney numbers of Dowling lattices"**

Studies Whitney numbers, which can be expressed using our framework as w_m(n,k) = (-1)^{n-k}S(n,k;-m,0,0) and W_m(n,k) = S(n,k;0,m,0).

### Carlitz (1979, 1980)
**"Degenerate Stirling, Bernoulli and Eulerian numbers"** and **"Weighted Stirling numbers of the first and second kind"**

Carlitz studied various generalizations of Stirling numbers, including weighted and degenerate versions that overlap with our framework.

## Applications and Further Generalizations

### Belbachir and Bousbaa (2012-2014)
**"Convolution identities for the r-Stirling numbers"** and **"Combinatorial identities for the r-Lah numbers"**

These papers explore convolution identities for r-Stirling and r-Lah numbers, providing additional properties and applications of our framework.

### Howard (1980)
**"Associated Stirling numbers"**

Presents another generalization that fits within the unified approach and has connections to our framework.

## Implementation Notes

Our implementation follows the combinatorial approach of Belbachir et al. while incorporating numerical stability techniques and optimizations for practical computation of large values.
