# Generalized Stirling Numbers: Combinatorial Approach

This document recasts the theorems and proofs using consistent notation and provides clear combinatorial explanations.

## Notation
* $S_{n,k}(a,b)$ represents the generalized Stirling number with parameters $a$ and $b$
* $\phi$ is the set of all distributions of $n$ elements into $k$ ordered, labeled lists
* $P(x,a,m)$ is the rising factorial $x(x+a)(x+2a)\cdots(x+(m-1)a)$

## Theorem 1: Explicit Formula

For any non-negative integers $n,k$, we have
$$S_{n,k}(a,b)=\frac{1}{b^{k}k!}\sum_{j=0}^{k}(-1)^{j}\binom{k}{j}P(b(k-j),a,n)$$

**Combinatorial Explanation:**
We want to find the total weight of distributing $n$ distinct elements into $k$ **ordered, non-empty, labeled** lists. The distribution rules are:
1. A newly started list (the first element in it) has a weight of $1$
2. The head of each list (the first element inserted) contributes a weight of $b$
3. All other elements contribute a weight of $a$

The total weight of a specific distribution is the product of the weights of all its elements.

## Proof of Theorem 1

Let $\phi$ be the set of all ways to distribute $n$ elements into $k$ ordered, labeled lists (which can be empty). The total weight of $\phi$ is the sum of the weights of all these distributions.

The total weight of distributing $n$ elements into $m$ ordered, labeled lists is given by the product of the weights assigned at each step. The correct total weight for distributing $n$ elements into $m$ lists is given by the generalized rising factorial $P(bm, a, n)$.

Now, we use the Principle of Inclusion-Exclusion to find the total weight of distributions where **no list is empty**.

Let $A_j$ be the set of distributions where the $j$-th list is empty. We want to find the total weight of the set $\bigcap_{j=1}^k \overline{A_j}$. By the inclusion-exclusion principle, this weight is given by:

$$\text{Total Weight} = \sum_{j=0}^k (-1)^j \sum_{1 \leq i_1 < \dots < i_j \leq k} \text{Weight of } \left( \bigcap_{l=1}^j A_{i_l} \right)$$

The term $\bigcap_{l=1}^j A_{i_l}$ represents the set of distributions where at least $j$ specific lists are empty. This is equivalent to distributing the $n$ elements into the remaining $k-j$ lists. The total weight for this is $P(b(k-j), a, n)$.

There are $\binom{k}{j}$ ways to choose which $j$ lists are empty. Therefore, the sum for a fixed $j$ is:

$$\binom{k}{j} P(b(k-j), a, n)$$

Substituting this back into the inclusion-exclusion formula, we get:

$$\sum_{j=0}^k (-1)^j \binom{k}{j} P(b(k-j), a, n)$$

This sum gives the total weight of distributions into **ordered, non-empty, labeled lists**. To get the desired number, we must account for:
1. The **k lists are not labeled**, so we must divide by $k!$
2. The **first element in each non-empty list has a weight of 1**, not $b$. Since there are $k$ non-empty lists, we have overcounted by a factor of $b^k$

Dividing the result of the inclusion-exclusion by $k!$ and $b^k$ gives the final formula.

## Theorem 2: Triangular Recurrence

The generalized Stirling numbers satisfy the following triangular recurrence relation:
$$S_{n+1,k}(a,b) = S_{n,k-1}(a,b) + (an + bk)S_{n,k}(a,b)$$

**Combinatorial Proof:**
We can derive this recurrence by considering the position of the element $n+1$. We are counting the total weight of distributing $n+1$ elements into $k$ ordered, non-empty lists.

There are two mutually exclusive cases for element $n+1$:

* **Case 1: Element $n+1$ forms a new, single-element list.**
    The total weight of distributing the remaining $n$ elements into $k-1$ lists is $S_{n,k-1}(a,b)$. The weight of element $n+1$ in this new list is $1$ (as it's the head). Thus, the total weight for this case is $S_{n,k-1}(a,b)$.

* **Case 2: Element $n+1$ is added to an existing list.**
    We start with a distribution of the $n$ elements into $k$ lists, which has a total weight of $S_{n,k}(a,b)$. Now we add element $n+1$ to one of these distributions. Where can it go?
    * It can be placed as the head of any of the $k$ lists. There are $k$ such positions, and the weight is $b$.
    * It can be placed after any of the other $n$ elements. There are $n$ such positions, and the weight is $a$.
    
    So, for each existing distribution of $n$ elements, there are $k$ positions with weight $b$ and $n$ positions with weight $a$ to insert element $n+1$. The total weight from these new insertions is $(bk + an)$. This gives a total weight of $(an + bk)S_{n,k}(a,b)$.

Since these two cases cover all possibilities, summing their weights gives the desired recurrence relation.

## Theorem 3: Vertical Recurrence

Let $n$ and $k$ be non-negative integers, we have
$$S_{n+1,k+1}(a,b)=\sum_{i=k}^{n}\binom{n}{i} P(a+b, a, n-i) S_{i,k}(a,b)$$

**Combinatorial Proof:**
We are distributing $n+1$ elements into $k+1$ ordered, non-empty lists. Let's focus on the list containing element $n+1$.

Assume element $n+1$ is in a list with $n-i$ other elements. We can choose these $n-i$ elements from the set $\{1, 2, \ldots, n\}$ in $\binom{n}{i}$ ways.

* The remaining $i$ elements must be distributed into the other $k$ lists. The total weight for this is $S_{i,k}(a,b)$.

* For the list containing element $n+1$ and the other $n-i$ elements, we need to determine its weight. Since element $n+1$ is already placed in this list (with weight 1 as it's the first element), we need to arrange the remaining $n-i$ elements around it.

When arranging the $n-i$ elements around element $n+1$:
1. The first element can be placed before $n+1$ (weight $b$) or after $n+1$ (weight $a$), giving total weight $a+b$.
2. The second element can be placed in 3 positions, giving weight $2a+b$ or $a+2b$ depending on existing arrangement.
3. And so on, with each new element having more positions with different weights.

This arrangement exactly corresponds to the rising factorial $P(a+b, a, n-i)$, which represents the weight of distributing $n-i$ additional elements into a list that already contains element $n+1$.

Combining all cases, we sum over all possible values of $i$ (from $k$ to $n$) to get the total weight:
$$S_{n+1,k+1}(a,b)=\sum_{i=k}^{n}\binom{n}{i} P(a+b, a, n-i) S_{i,k}(a,b)$$

## Theorem 4: Symmetric Function Expression

For non-negative integers $n$, $k$, $a$, and $b$, we have:
$$S_{n+k,n}(a,b) = \sum_{1\leq i_1\leq \cdots \leq i_k\leq n}\prod_{j=1}^{k}\left((a+b)i_j + a(j-1)\right)$$

**Combinatorial Explanation:**
This theorem expresses $S_{n+k,n}(a,b)$ as a symmetric function of the numbers $1,2,\ldots,n$. It shows that the generalized Stirling numbers can be viewed as weighted elementary symmetric functions.

## Theorem 5: Multinomial Convolution Identity

The generalized Stirling numbers satisfy:
$$\binom{k}{k_1,\ldots,k_p}S_{n,k}(a,b) = \sum_{l_1+\cdots+l_p=n}\binom{n}{l_1,\ldots,l_p}S_{l_1,k_1}(a,b)\cdots S_{l_p,k_p}(a,b)$$

**Combinatorial Explanation:**
This identity relates the generalized Stirling numbers to multinomial coefficients. It can be interpreted as follows:

1. The left side represents distributing $n$ elements into $k$ ordered, non-empty lists, and then coloring these $k$ lists using $p$ colors such that $k_i$ lists receive color $i$.

2. The right side represents first partitioning the $n$ elements into $p$ groups of sizes $l_1,\ldots,l_p$, and then distributing the elements of each group into $k_i$ ordered, non-empty lists.

## Special Cases

The generalized Stirling numbers provide a unified framework that includes several classical number sequences as special cases:

- Stirling numbers of the first kind: $S_{n,k}(1,0)$
- Stirling numbers of the second kind: $S_{n,k}(0,1)$
- Lah numbers: $S_{n,k}(1,1)$

These special cases demonstrate how this framework unifies several important combinatorial sequences under a single mathematical structure.