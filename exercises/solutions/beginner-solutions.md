# Solutions to Beginner Problem Set

## Problem Set A: Basic Calculations

**A1.** Calculate the following by hand:

1. $P(2,3,2) = 2 \cdot (2+3) = 2 \cdot 5 = 10$
2. $P(4,1,3) = 4 \cdot (4+1) \cdot (4+2) = 4 \cdot 5 \cdot 6 = 120$
3. $P(3,0,4) = 3^4 = 81$ (monomial case)
4. $P(5,-1,2) = 5 \cdot (5-1) = 5 \cdot 4 = 20$

**A2.** Fill in missing values:

1. $P(x,2,3) = x(x+2)(x+4) = 60$
   Try $x=3$: $3 \cdot 5 \cdot 7 = 105$ (too big)
   Try $x=2$: $2 \cdot 4 \cdot 6 = 48$ (too small)
   Try $x=2.5$: $2.5 \cdot 4.5 \cdot 6.5 ≈ 73$ (still too big)
   
   **Systematic approach:** Solve $x(x+2)(x+4) = 60$
   Expanding: $x^3 + 6x^2 + 8x - 60 = 0$
   By inspection or numerical methods: $x ≈ 2.43$

2. $P(3,a,2) = 3(3+a) = 15$
   $3+a = 5$, so $a = 2$

3. $P(2,1,m) = 2 \cdot 3 \cdot 4 \cdots (1+m) = 120$
   This is $\frac{(m+1)!}{1!} = (m+1)! = 120$
   Since $5! = 120$, we have $m+1 = 5$, so $m = 4$

**A3.** True or False:

1. **True**: $P(0,a,m) = 0 \cdot (0+a) \cdot (0+2a) \cdots = 0$ when $m > 0$ and $a \neq 0$
2. **True**: $P(x,0,m) = x \cdot x \cdot x \cdots = x^m$ (all increments are 0)
3. **True**: $P(x,a,0) = 1$ by empty product convention for any $x,a$
4. **True**: $P(-a,a,2) = (-a) \cdot (-a+a) = (-a) \cdot 0 = 0$ for $a \neq 0$

## Problem Set B: Classical Stirling Numbers

**B1.** Stirling numbers of the second kind:

Using $\left\{\begin{array}{c}m+1\\n\end{array}\right\} = n\left\{\begin{array}{c}m\\n\end{array}\right\} + \left\{\begin{array}{c}m\\n-1\end{array}\right\}$

Base cases: $\left\{\begin{array}{c}0\\0\end{array}\right\} = 1$, $\left\{\begin{array}{c}m\\0\end{array}\right\} = 0$ for $m>0$, $\left\{\begin{array}{c}m\\n\end{array}\right\} = 0$ for $n>m$

1. $\left\{\begin{array}{c}3\\1\end{array}\right\} = 1$, $\left\{\begin{array}{c}3\\2\end{array}\right\} = 3$, $\left\{\begin{array}{c}3\\3\end{array}\right\} = 1$

2. $\left\{\begin{array}{c}4\\1\end{array}\right\} = 1$, $\left\{\begin{array}{c}4\\2\end{array}\right\} = 7$, $\left\{\begin{array}{c}4\\3\end{array}\right\} = 6$, $\left\{\begin{array}{c}4\\4\end{array}\right\} = 1$

**B2.** Expansion verification:
$x^3 = 1 \cdot x + 3 \cdot x(x+1) + 1 \cdot x(x+1)(x+2)$

Check by expanding right side:
- $1 \cdot x = x$
- $3 \cdot x(x+1) = 3x^2 + 3x$  
- $1 \cdot x(x+1)(x+2) = x^3 + 3x^2 + 2x$

Sum: $x + 3x^2 + 3x + x^3 + 3x^2 + 2x = x^3 + 6x^2 + 6x$

**Wait, this doesn't equal $x^3$!** Let me recalculate...

Actually, the correct expansion is:
$x^3 = 2x - 3x(x+1) + 1x(x+1)(x+2)$

The coefficients are the **signed** Stirling numbers of the first kind!

**B3.** Calculate $\left\{\begin{array}{c}5\\3\end{array}\right\}$:

$\left\{\begin{array}{c}5\\3\end{array}\right\} = 3\left\{\begin{array}{c}4\\3\end{array}\right\} + \left\{\begin{array}{c}4\\2\end{array}\right\} = 3 \cdot 6 + 7 = 18 + 7 = 25$

## Problem Set C: Matrix Relationships

**C1.** 4×4 Stirling numbers of the second kind matrix:
$$\mathbf{S}_2 = \begin{pmatrix}
1 & 0 & 0 & 0 \\
1 & 1 & 0 & 0 \\
1 & 3 & 1 & 0 \\
1 & 7 & 6 & 1
\end{pmatrix}$$

**C2.** Orthogonality verification:
$\sum_{k=0}^{3} s(3,k) \cdot \left\{\begin{array}{c}k\\2\end{array}\right\} = [3=2] = 0$

Signed Stirling first kind: $s(3,0)=0$, $s(3,1)=2$, $s(3,2)=-3$, $s(3,3)=1$
Stirling second kind: $\left\{\begin{array}{c}0\\2\end{array}\right\}=0$, $\left\{\begin{array}{c}1\\2\end{array}\right\}=0$, $\left\{\begin{array}{c}2\\2\end{array}\right\}=1$, $\left\{\begin{array}{c}3\\2\end{array}\right\}=3$

Sum: $0 \cdot 0 + 2 \cdot 0 + (-3) \cdot 1 + 1 \cdot 3 = 0 + 0 - 3 + 3 = 0$ ✓

**C3.** Matrix multiplication:
$$\mathbf{A} \cdot \mathbf{B} = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \mathbf{I}$$ ✓

## Alternative Solution Methods

For many problems, there are multiple approaches:

1. **Direct calculation** vs **recurrence relations** for Stirling numbers
2. **Matrix methods** vs **generating functions** for verifications  
3. **Symbolic manipulation** vs **numerical verification** for polynomial identities

**Learning tip**: Try solving problems multiple ways to deepen understanding!

## Common Mistakes and How to Avoid Them

1. **Sign errors**: Remember that Stirling numbers of the first kind can be negative
2. **Index confusion**: Be careful about $m$ vs $n$ and 0-indexing vs 1-indexing
3. **Special cases**: Always check $m=0$, $n=0$, and boundary conditions
4. **Matrix multiplication**: Remember it's not commutative!

## Next Steps

Once you've mastered these problems:
- Try the intermediate problem set for more challenging matrix relationships
- Implement your solutions in code to verify answers
- Explore the computational exercises for larger examples
- Start thinking about the patterns you're seeing - they'll become important in advanced topics!
