# Relationship Between Different Generalized Stirling Number Notations

## Introduction

This document explores the relationship between different notations for generalized Stirling numbers, particularly focusing on:
- The L_{n,k}^{α,β} notation used in our implementation (based on Belbachir, Belkhir, and Bousbaa)
- The S(n,k;α,β,r) notation introduced by Hsu and Shiue (1998)

Understanding these relationships allows us to connect different parameterizations and leverage the combinatorial insights from multiple approaches.

## Notation Equivalences

### Hsu-Shiue Generalized Stirling Numbers

Hsu and Shiue (1998) defined a unified approach to generalized Stirling numbers with the notation:

$$S(n,k;\alpha,\beta,r)$$

where α, β, and r are parameters that generalize various Stirling-type numbers.

They defined these numbers through the relation:

$$(x|\alpha)^{\underline{n}} = \sum_{k=0}^{n}S(n,k;\alpha,\beta,r)(x-r|\beta)^{\underline{k}}$$

where $(x|\theta)^{\underline{n}}$ is the generalized falling factorial:

$$(x|\theta)^{\underline{n}} = x(x-\theta)(x-2\theta)\cdots(x-(n-1)\theta)$$

### Relationship to L_{n,k}^{α,β} Notation

Our implementation uses L_{n,k}^{α,β} notation from Belbachir et al. The relationship between these notations is:

$$L_{n,k}^{\alpha,\beta} = S(n,k;-\alpha,\beta,0)$$

That is, the L_{n,k}^{α,β} notation corresponds to the special case of Hsu-Shiue's notation where:
- α in Hsu-Shiue is replaced with -α
- r = 0

## Recurrence Relations

### Hsu-Shiue Recurrence

The numbers S(n,k;α,β,r) satisfy the recurrence relation:

$$S(n,k;\alpha,\beta,r) = S(n-1,k-1;\alpha,\beta,r) + (\beta k - \alpha(n-1) + r)S(n-1,k;\alpha,\beta,r)$$

with initial conditions S(0,0;α,β,r) = 1 and S(n,0;α,β,r) = r^n for n > 0.

### L_{n,k}^{α,β} Recurrence

The L_{n,k}^{α,β} numbers satisfy:

$$L_{n,k}^{\alpha,\beta} = L_{n-1,k-1}^{\alpha,\beta} + (\alpha(n-1) + \beta k)L_{n-1,k}^{\alpha,\beta}$$

### Converting Between Recurrences

To convert from the Hsu-Shiue recurrence to our L_{n,k}^{α,β} recurrence, substitute:
- α from Hsu-Shiue with -α
- r = 0

This gives:

$$S(n,k;-\alpha,\beta,0) = S(n-1,k-1;-\alpha,\beta,0) + (\beta k + \alpha(n-1))S(n-1,k;-\alpha,\beta,0)$$

Which is precisely our recurrence for L_{n,k}^{α,β}.

## Combinatorial Interpretation

### L_{n,k}^{α,β} Interpretation

L_{n,k}^{α,β} represents the total weight of all possible ways to distribute n elements into k ordered non-empty lists, where:

1. The first element placed in each list has weight 1
2. Elements placed at the head of a list have weight β
3. Other elements in the lists have weight α

### Understanding the Recurrence Combinatorially

The recurrence relation:

$$L_{n,k}^{\alpha,\beta} = L_{n-1,k-1}^{\alpha,\beta} + (\alpha(n-1) + \beta k)L_{n-1,k}^{\alpha,\beta}$$

has a direct combinatorial interpretation:

1. **First term** (L_{n-1,k-1}^{α,β}): This represents placing element n in its own singleton list. The weight of this placement is 1 (as the first element in a list), and we now need to distribute the remaining n-1 elements into k-1 lists.

2. **Second term** ((\alpha(n-1) + \beta k)L_{n-1,k}^{α,β}): This represents placing element n into one of the existing k lists that already contain the n-1 other elements. We have two subcases:
   - Term \alpha(n-1): Element n can be placed after any of the n-1 elements, each with weight α
   - Term \beta k: Element n can be placed at the head of any of the k lists, each with weight β

This recurrence directly reflects the combinatorial construction process, building larger distributions from smaller ones by adding one element at a time.

## Special Cases

The generalized framework includes important special cases:

1. **Stirling Numbers of the First Kind** (L_{n,k}^{1,0} or S(n,k;-1,0,0)):
   - Combinatorial meaning: Counts permutations of n elements with exactly k cycles
   - Recurrence: L_{n,k}^{1,0} = L_{n-1,k-1}^{1,0} + (n-1)L_{n-1,k}^{1,0}

2. **Stirling Numbers of the Second Kind** (L_{n,k}^{0,1} or S(n,k;0,1,0)):
   - Combinatorial meaning: Counts partitions of n elements into exactly k non-empty subsets
   - Recurrence: L_{n,k}^{0,1} = L_{n-1,k-1}^{0,1} + kL_{n-1,k}^{0,1}

3. **Lah Numbers** (L_{n,k}^{1,1} or S(n,k;-1,1,0)):
   - Combinatorial meaning: Counts partitions of n elements into exactly k ordered lists
   - Recurrence: L_{n,k}^{1,1} = L_{n-1,k-1}^{1,1} + (n+k-1)L_{n-1,k}^{1,1}

## Other Generalizations

### r-Stirling Numbers

The r-Stirling numbers introduced by Broder (1984) are another special case of the Hsu-Shiue framework:

- **r-Stirling numbers of the first kind**: S(n,k;-1,0,r)
- **r-Stirling numbers of the second kind**: S(n,k;0,1,r)

These count permutations with k cycles (or partitions into k subsets) where the elements 1,2,...,r are in different cycles (or subsets).

### Whitney Numbers

The Whitney numbers of Dowling lattices (Benoumhani, 1996) can also be related to this framework:

- **Whitney numbers of the first kind**: w_m(n,k) = (-1)^{n-k}S(n,k;-m,0,0)
- **Whitney numbers of the second kind**: W_m(n,k) = S(n,k;0,m,0)

Where m is a parameter related to the Dowling lattice structure.

## Recommendations for Implementation

### Option 1: Maintain Original Approach with Relation

If the focus is on the specific combinatorial interpretation from Belbachir et al., maintain the L_{n,k}^{α,β} notation but provide conversion functions to other frameworks:

```python
def convert_to_hsu_shiue(n, k, alpha, beta):
    """Convert L_{n,k}^{α,β} parameters to S(n,k;α,β,r) parameters"""
    return n, k, -alpha, beta, 0

def convert_from_hsu_shiue(n, k, alpha, beta, r):
    """Convert S(n,k;α,β,r) parameters to L_{n,k}^{α,β} parameters if possible"""
    if r != 0:
        raise ValueError("Cannot convert to L notation when r ≠ 0")
    return n, k, -alpha, beta
```

### Option 2: Rebuild Foundation with Hsu-Shiue Framework

If the goal is maximum generality, rebuild the foundation using the Hsu-Shiue notation:

```python
class GeneralizedStirlingHsuShiue:
    """Implementation of generalized Stirling numbers S(n,k;α,β,r)"""
    
    def __init__(self, alpha=0.0, beta=1.0, r=0.0):
        self.alpha = alpha
        self.beta = beta
        self.r = r
        # ...existing code...
    
    def triangular_recurrence(self, n, k):
        # Base cases
        if k == 0:
            if n == 0:
                return 1.0
            else:
                return self.r ** n
        if n == 0 or k > n:
            return 0.0
            
        # Recurrence relation
        term1 = self.triangular_recurrence(n-1, k-1)
        term2 = (self.beta * k - self.alpha * (n-1) + self.r) * self.triangular_recurrence(n-1, k)
        
        return term1 + term2
    
    # ...existing code...
```

Then provide the L_{n,k}^{α,β} notation as a special case:

```python
def generalized_stirling_L(n, k, alpha, beta):
    """Compute L_{n,k}^{α,β} using Hsu-Shiue framework"""
    gs = GeneralizedStirlingHsuShiue(alpha=-alpha, beta=beta, r=0)
    return gs.compute(n, k)
```

## Conclusion

The generalized Stirling numbers L_{n,k}^{α,β} and S(n,k;α,β,r) provide powerful frameworks for understanding various counting sequences. By understanding their relationship, we can leverage the combinatorial insights from both approaches and connect them to other generalizations in the literature.

For our implementation, we recommend:
1. Keep the current L_{n,k}^{α,β} implementation with its clear combinatorial interpretation
2. Add conversion functions to other notations for interoperability
3. Document the relationships between different frameworks
4. Consider implementing the full Hsu-Shiue framework as an extension for maximum generality

This approach maintains the clarity of the current implementation while providing pathways to other generalizations.

## References

1. H. Belbachir, A. Belkhir, I.E. Bousbaa. "Combinatorial approach of certain generalized Stirling numbers." arXiv:1411.6271v1, 2014.

2. L.C. Hsu, P.J.-S. Shiue. "A unified approach to generalized Stirling numbers." Adv. in Appl. Math., 20(3):366-384, 1998.

3. A.Z. Broder. "The r-Stirling numbers." Discrete Math., 49(3):241-259, 1984.

4. M. Benoumhani. "On Whitney numbers of Dowling lattices." Discrete Math., 159(1-3):13-33, 1996.