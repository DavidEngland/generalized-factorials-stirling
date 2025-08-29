# Sheffer Sequences and Generalized Stirling Numbers

## 1. Defining Sheffer Sequences

A polynomial sequence $\{s_n(x)\}_{n\geq 0}$ is called a **Sheffer sequence** if its exponential generating function (EGF) has the form:

$$\sum_{n=0}^{\infty} s_n(x) \frac{t^n}{n!} = A(t) e^{x B(t)}$$

where:
- $A(t)$ and $B(t)$ are formal power series
- $A(0) \neq 0$
- $B(0) = 0$ and $B'(0) \neq 0$

The pair $(A(t), B(t))$ is called the **Sheffer pair** for the sequence.

## 2. Key Conditions and Classification

Sheffer sequences can be classified by additional conditions:

1. **Basic Sheffer Sequences**: When $A(t) = 1$, we get an Appell sequence
2. **Appell Sequences**: When $B(t) = t$, giving EGF of form $A(t)e^{xt}$
3. **Associated Sequences**: When $A(t) = 1$, giving EGF of form $e^{xB(t)}$

The most important characterizing condition is the **delta operator** $Q$, which acts on polynomials such that:
- $Q$ is linear
- $Q$ reduces degree by exactly 1
- $Q(s_n(x)) = n\cdot s_{n-1}(x)$ for all $n \geq 1$

A sequence is Sheffer if and only if it is the sequence of basic polynomials for some delta operator.

## 3. Connection to Generalized Stirling Numbers

The generalized Stirling numbers $S_{n,k}(a,b)$ are intimately connected to Sheffer sequences through:

1. **Transformation Perspective**: The generalized Stirling numbers serve as connection coefficients between different Sheffer sequences.

2. **Sheffer Pairs**: For parameters $(a,b)$, we can define the Sheffer pair:
   $$\left(g_{a,b}(t), f_{a,b}(t)\right)$$
   where $f_{a,b}(t)$ encodes the $(a,b)$-factorial basis and $g_{a,b}(t)$ modifies the weights.

3. **Operator Form**: The operator 
   $$U_{a,b}[A](t) = g_{a,b}(t)A(f_{a,b}(t))$$
   maps between different Sheffer sequences, with $S_{n,k}(a,b)$ as the connection coefficients.

## 4. Explicit Examples

### Classical Cases

1. **Hermite Polynomials**: Sheffer for $(e^{t^2/2}, t)$
2. **Laguerre Polynomials**: Sheffer for $((1-t)^{-\alpha-1}, t/(t-1))$
3. **Bernoulli Polynomials**: Sheffer for $(t/(e^t-1), e^t-1)$

### Generalized Stirling Cases

1. **Second Kind $(0,1)$**: Associated with the Sheffer pair $(1, e^t-1)$
2. **First Kind $(1,0)$**: Related to the Sheffer pair involving $\log(1+t)$
3. **Lah Numbers $(1,1)$**: Connected to the Sheffer pair involving $t/(1-t)$
4. **Hyperbolic Strip $(0,\pm 1/2)$**: Associated with hyperbolic factorizations

## 5. Implications of the Sheffer Property

The Sheffer property for generalized Stirling numbers has profound implications:

1. **Recurrence Relations**: The Sheffer property guarantees the existence of the triangular recurrence:
   $$S_{n,k}(a,b) = S_{n-1,k-1}(a,b) + (a(n-1) + bk)S_{n-1,k}(a,b)$$

2. **Generating Functions**: The EGF structure is directly derived from the Sheffer property:
   $$\sum_{n\geq k} S_{n,k}(a,b)\frac{t^n}{n!} = \frac{1}{k!}\left(\frac{e^{a t}-1}{a}\right)^k e^{bkt}$$
   (For $a=0$, appropriate limits are taken)

3. **Binomial-Type Identity**: Sheffer sequences satisfy:
   $$s_n(x+y) = \sum_{k=0}^n \binom{n}{k} s_k(x) q_{n-k}(y)$$
   where $\{q_n(x)\}$ is the associated sequence.

4. **Umbral Composition**: The composition property:
   $$s_n(q_m(x)) = \sum_{k=0}^{\min(n,m)} c_{n,m,k} s_k(x)$$
   for certain coefficients $c_{n,m,k}$ expressible via generalized Stirling numbers.

## 6. Combinatorial Implications

The Sheffer property provides deep insights into the combinatorial structure:

1. **Partition-based Interpretation**: The generalized Stirling numbers count weighted partitions, with:
   - Parameter $a$ controlling interior weighting (affinity)
   - Parameter $b$ controlling boundary weighting (barrier)

2. **Operator Calculus**: Sheffer sequences enable an operator calculus where differential operators have clear combinatorial interpretations.

3. **Bell Polynomial Connection**: The Sheffer property establishes the identity:
   $$B_n(1!x_1^{(a,b)}, 2!x_2^{(a,b)}, \ldots, n!x_n^{(a,b)}) = n!\sum_{k=0}^n S_{n,k}(a,b)\frac{a_k}{k!}$$
   connecting Bell polynomials to generalized Stirling numbers.

## 7. Summary of Key Conditions

For a sequence to be Sheffer in the generalized Stirling context:

1. It must have an EGF of the form $A(t)e^{xB(t)}$
2. The connection coefficients between the sequence and the standard basis must satisfy the generalized Stirling recurrence
3. The sequence must be the eigenfunctions of a suitable delta operator

These conditions ensure that generalized Stirling numbers have their rich algebraic, combinatorial, and analytical properties, making them fundamental to understanding partition-based combinatorial structures.

## References

1. Roman, S. (1984). *The Umbral Calculus*. Academic Press.
2. Hsu, L.C., & Shiue, P.J.-S. (1998). A unified approach to generalized Stirling numbers. *Adv. in Appl. Math.*, 20(3), 366-384.
3. Belbachir, H., et al. (Various papers on generalized Stirling numbers and their properties).
