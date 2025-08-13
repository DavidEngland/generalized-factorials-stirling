# Beginner Problem Set: Foundations

## Problem Set A: Basic Calculations

**A1.** Calculate the following by hand, then verify with code:
1. $P(2,3,2)$
2. $P(4,1,3)$
3. $P(3,0,4)$  
4. $P(5,-1,2)$

**A2.** Fill in the missing values:
1. $P(?,2,3) = 60$ (find the value of $x$)
2. $P(3,?,2) = 15$ (find the value of $a$)
3. $P(2,1,?) = 120$ (find the value of $m$)

**A3.** True or False (explain your reasoning):
1. $P(0,a,m) = 0$ for all $a \neq 0$ and $m > 0$
2. $P(x,0,m) = x^m$ for all $x$ and $m$
3. $P(x,a,0) = 1$ for all $x$ and $a$
4. $P(-a,a,2) = 0$ for all $a \neq 0$

## Problem Set B: Classical Stirling Numbers

**B1.** Compute the first few Stirling numbers of the second kind:
1. $\left\{\begin{array}{c}3\\1\end{array}\right\}$, $\left\{\begin{array}{c}3\\2\end{array}\right\}$, $\left\{\begin{array}{c}3\\3\end{array}\right\}$
2. $\left\{\begin{array}{c}4\\1\end{array}\right\}$, $\left\{\begin{array}{c}4\\2\end{array}\right\}$, $\left\{\begin{array}{c}4\\3\end{array}\right\}$, $\left\{\begin{array}{c}4\\4\end{array}\right\}$

**B2.** Verify the expansion $x^3 = ? \cdot x + ? \cdot x(x+1) + ? \cdot x(x+1)(x+2)$
Find the coefficients and verify by expanding both sides.

**B3.** Use the recurrence relation:
$\left\{\begin{array}{c}m+1\\n\end{array}\right\} = n\left\{\begin{array}{c}m\\n\end{array}\right\} + \left\{\begin{array}{c}m\\n-1\end{array}\right\}$

Calculate $\left\{\begin{array}{c}5\\3\end{array}\right\}$ step by step.

## Problem Set C: Matrix Relationships

**C1.** Write out the 4×4 matrix of Stirling numbers of the second kind:
$$\mathbf{S}_2 = \begin{pmatrix}
? & ? & ? & ? \\
? & ? & ? & ? \\
? & ? & ? & ? \\
? & ? & ? & ?
\end{pmatrix}$$

**C2.** Verify one entry of the orthogonality relationship:
$\sum_{k=0}^{3} s(3,k) \cdot \left\{\begin{array}{c}k\\2\end{array}\right\} = [3=2]$

Calculate each term and verify the sum equals 0.

**C3.** Matrix multiplication practice:
If $\mathbf{A} = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}$ and $\mathbf{B} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$, 
verify that $\mathbf{A} \cdot \mathbf{B} = \mathbf{I}$.

## Problem Set D: Generalized Coefficients

**D1.** Using the definition $P(x,a,m) = \sum_{n=0}^{m} S_{m,n}(a,b) \cdot P(x,b,n)$:

Find $S_{2,1}(2,1)$ by solving:
$P(x,2,2) = S_{2,0}(2,1) \cdot 1 + S_{2,1}(2,1) \cdot x + S_{2,2}(2,1) \cdot x(x+1)$

**Hint:** Expand both sides and equate coefficients.

**D2.** Verify the identity property:
$S_{m,n}(a,a) = [m=n]$ for the cases:
1. $S_{2,2}(3,3)$ 
2. $S_{2,1}(5,5)$
3. $S_{3,3}(-1,-1)$

**D3.** Pattern recognition:
Calculate $S_{m,n}(1,0)$ for small values and compare with your answer from Problem B1.
What do you notice?

## Coding Challenges

**Code Challenge 1:** Implement a function to compute Stirling numbers of the second kind using the recurrence relation.

**Code Challenge 2:** Write a verification function that checks if two polynomial expressions are equal by evaluating them at several test points.

**Code Challenge 3:** Create a function that converts between different factorial polynomial representations (e.g., from rising factorials to monomials).

## Reflection Questions

1. **Patterns:** What patterns do you notice in the Stirling number tables?

2. **Connections:** How do the generalized factorial polynomials $P(x,a,m)$ connect to things you already know (like regular polynomials or factorials)?

3. **Intuition:** Why do you think the coefficients $S_{m,n}(a,b)$ exist and are unique?

4. **Applications:** Where might these polynomial transformations be useful in mathematics or other fields?

## Before Moving On

Make sure you can:
- [ ] Calculate basic examples by hand
- [ ] Use recurrence relations for Stirling numbers
- [ ] Verify simple matrix relationships
- [ ] Find coefficients by expanding and equating
- [ ] Implement basic computations in code

**Next:** Move to `intermediate-problems.md` for more challenging matrix work and general patterns.
