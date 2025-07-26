# Rising and Falling Factorials (Wikipedia Article)

{{Short description|Mathematical functions}}
{{Use American English|date = March 2019}}
{{Redirect|Rising power|the description of a sovereign state or union of states with significant rising influence in global affairs|emerging power}}

In [[mathematics]], the '''falling factorial''' (sometimes called the '''descending factorial''',<ref name=Steffensen/> '''falling sequential product''', or '''lower factorial''') is defined as the polynomial

$$\begin{align}
(x)_n = x^\underline{n} &= \overbrace{x(x-1)(x-2)\cdots(x-n+1)}^{n\text{ factors}} \\
&= \prod_{k=1}^n(x-k+1) = \prod_{k=0}^{n-1}(x-k) .
\end{align}$$

The '''rising factorial''' (sometimes called the '''Pochhammer function''', '''Pochhammer polynomial''', '''ascending factorial''',<ref name=Steffensen>
{{cite book
 | last = Steffensen | first = J.F. | author-link = Johan Frederik Steffensen
 | date = 17 March 2006
 | title = Interpolation
 | publisher = Dover Publications | edition = 2nd
 | isbn = 0-486-45009-0
 | page = 8
}} — A reprint of the 1950 edition by Chelsea Publishing.
</ref> '''rising sequential product''', or '''upper factorial''') is defined as

$$\begin{align}
x^{(n)} = x^\overline{n} &= \overbrace{x(x+1)(x+2)\cdots(x+n-1)}^{n\text{ factors}} \\
&= \prod_{k=1}^n(x+k-1) = \prod_{k=0}^{n-1}(x+k) .
\end{align}$$

The value of each is taken to be 1 (an [[empty product]]) when $n=0$. These symbols are collectively called '''factorial powers'''.<ref name="The Art of Computer Programming">
{{cite book
 |last=Knuth |first=D.E. |author-link=Donald Knuth
 |title=[[The Art of Computer Programming]] |edition=3rd
 |volume=1 |page=50
}}
</ref>

## Unified Framework

Both rising and falling factorials are special cases of '''[[generalized factorial polynomials]]''' denoted $P(x,a,m)$, defined as:

$$P(x,a,m) = x(x+a)(x+2a)\cdots(x+(m-1)a)$$

The traditional forms correspond to specific parameter values:
* '''Rising factorial''': $x^{(n)} = P(x,1,n)$ (increment parameter $a = 1$)
* '''Falling factorial''': $(x)_n = P(x,-1,n)$ (increment parameter $a = -1$)  
* '''Monomials''': $x^n = P(x,0,n)$ (increment parameter $a = 0$)

This unified notation resolves the historical notational inconsistencies between different mathematical fields and provides a systematic framework for [[generalized Stirling transfer coefficients]].

## Notational Conventions

The '''Pochhammer symbol''', introduced by [[Leo August Pochhammer]], is the notation $(x)_n$, where $n$ is a [[non-negative integer]]. It may represent ''either'' the rising or the falling factorial, with different articles and authors using different conventions. Pochhammer himself actually used $(x)_n$ with yet another meaning, namely to denote the [[binomial coefficient]] $\tbinom{x}{n}$.<ref name=Knuth>
{{cite journal
 |last=Knuth |first=D.E.  |author-link=Donald Knuth
 |year=1992
 |title=Two notes on notation
 |journal=[[American Mathematical Monthly]]
 |volume=99 |issue=5 |pages=403–422
 |arxiv=math/9205211 |doi=10.2307/2325085
 |jstor=2325085 |s2cid=119584305
}} The remark about the Pochhammer symbol is on page 414.
</ref>

In this article, the symbol $(x)_n$ is used to represent the falling factorial, and the symbol $x^{(n)}$ is used for the rising factorial. These conventions are used in [[combinatorics]],<ref>
{{cite book
 |last=Olver |first=P.J. |author-link=Peter J. Olver
 |year=1999
 |title=Classical Invariant Theory
 |publisher=Cambridge University Press
 |isbn=0-521-55821-2 |mr=1694364
 |page=101
}}
</ref>
although [[Donald Knuth|Knuth]]'s underline and overline notations $x^\underline{n}$ and $x^\overline{n}$ are increasingly popular.<ref name="The Art of Computer Programming"/><ref>
{{cite book
 |last1=Harris
 |last2=Hirst
 |last3=Mossinghoff
 |year=2008
 |title=Combinatorics and Graph Theory 
 |publisher=Springer
 |isbn=978-0-387-79710-6
 |at=ch.&nbsp;2
}}
</ref>

In the theory of [[special functions]] (in particular the [[hypergeometric function]]) and in the standard reference work ''[[Abramowitz and Stegun]]'', the Pochhammer symbol $(x)_n$ is used to represent the rising factorial.<ref>
{{cite book
 |editor1=Abramowitz, Milton
 |editor2=Stegun, Irene A.
 |date=December 1972  |orig-date=June 1964
 |title=Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables
 |title-link=Abramowitz and Stegun
 |place=Washington, DC
 |publisher=[[United States Department of Commerce]]
 |series=[[National Bureau of Standards]] [[Applied Mathematics]] Series
 |volume=55
 |lccn=64-60036
 |at=p.&nbsp;256 eqn.&nbsp;6.1.22
}}
</ref><ref>
{{cite book
 |last=Slater |first=Lucy J.
 |year=1966
 |title=Generalized Hypergeometric Functions
 |publisher=Cambridge University Press
 |mr=0201688 |at=Appendix&nbsp;I
}} — Gives a useful list of formulas for manipulating the rising factorial in $(x)_n$ notation.
</ref>

## Examples and Combinatorial Interpretation

The first few falling factorials are as follows:

$$\begin{alignat}{2}
(x)_0 & &&= 1 \\
(x)_1 & &&= x \\
(x)_2 &= x(x-1) &&= x^2-x \\
(x)_3 &= x(x-1)(x-2) &&= x^3-3x^2+2x \\
(x)_4 &= x(x-1)(x-2)(x-3) &&= x^4-6x^3+11x^2-6x
\end{alignat}$$

The first few rising factorials are as follows:

$$\begin{alignat}{2}
x^{(0)} & &&= 1 \\
x^{(1)} & &&= x \\
x^{(2)} &= x(x+1) &&=x^2+x \\
x^{(3)} &= x(x+1)(x+2) &&=x^3+3x^2+2x \\
x^{(4)} &= x(x+1)(x+2)(x+3) &&=x^4+6x^3+11x^2+6x
\end{alignat}$$

The coefficients that appear in the expansions are [[Stirling numbers of the first kind]] (see below).

When the variable $x$ is a positive integer, the number $(x)_n$ is equal to the number of [[k-permutation|$n$-permutations from a set of $x$ items]], that is, the number of ways of choosing an ordered list of length $n$ consisting of distinct elements drawn from a collection of size $x$. For example, $(8)_3 = 8\times7\times6 = 336$ is the number of different podiums—assignments of gold, silver, and bronze medals—possible in an eight-person race. 

On the other hand, $x^{(n)}$ is "the number of ways to arrange $n$ flags on $x$ flagpoles",<ref name=Feller>
{{cite book
 |first=William |last=Feller
 |title=An Introduction to Probability Theory and Its Applications
 |volume=1 |at=Ch. 2
}}
</ref>
where all flags must be used and each flagpole can have any number of flags. Equivalently, this is the number of ways to partition a set of size $n$ (the flags) into $x$ distinguishable parts (the poles), with a linear order on the elements assigned to each part (the order of the flags on a given pole).

## Properties

The rising and falling factorials are simply related to one another:

$$\begin{alignat}{2}
{(x)}_n &= {(x-n+1)}^{(n)} &&= (-1)^n (-x)^{(n)},\\
x^{(n)} &= {(x+n-1)}_{n} &&= (-1)^n (-x)_n.
\end{alignat}$$

In the unified $P(x,a,m)$ framework, this relationship becomes:
$$P(x,-1,n) = (-1)^n P(-x,1,n)$$

Falling and rising factorials of integers are directly related to the ordinary [[factorial]]:

$$\begin{align}
n! &= 1^{(n)} = (n)_n,\\[6pt]
(m)_n &= \frac{m!}{(m-n)!},\\[6pt]
m^{(n)} &= \frac{(m+n-1)!}{(m-1)!}.
\end{align}$$

### Real Numbers and Negative n

The falling factorial can be extended to [[real number|real]] values of $x$ using the [[gamma function]] provided $x$ and $x+n$ are real numbers that are not negative integers:

$$(x)_n = \frac{\Gamma(x+1)}{\Gamma(x-n+1)}$$

and so can the rising factorial:

$$x^{(n)} = \frac{\Gamma(x+n)}{\Gamma(x)}$$

In the unified framework, this becomes:

$$P(x,a,m) = \begin{cases} 
x^m & \text{if } a = 0 \\
a^m \frac{\Gamma(x/a + m)}{\Gamma(x/a)} & \text{if } a \neq 0
\end{cases}$$

## Connection Coefficients and Stirling Numbers

Falling and rising factorials are closely related to [[Stirling number|Stirling numbers]]. The expansions in terms of monomials reveal [[Stirling numbers of the first kind]]:

$$\begin{align}
(x)_n & = \sum_{k=0}^n s(n,k) x^k \\
      &= \sum_{k=0}^n \begin{bmatrix}n \\ k \end{bmatrix} (-1)^{n-k}x^k \\
x^{(n)} & = \sum_{k=0}^n \begin{bmatrix} n \\ k \end{bmatrix} x^k \\
\end{align}$$

The inverse relations use [[Stirling numbers of the second kind]]:

$$\begin{align}
x^n & = \sum_{k=0}^{n} \begin{Bmatrix} n \\ k \end{Bmatrix} (x)_{k} \\
    & = \sum_{k=0}^n \begin{Bmatrix} n \\ k \end{Bmatrix} (-1)^{n-k} x^{(k)} .
\end{align}$$

### Generalized Stirling Transfer Coefficients

In the unified framework, these relationships are generalized through '''[[generalized Stirling transfer coefficients]]''' $S_{m,n}(a,b)$, defined by:

$$P(x,a,m) = \sum_{n=0}^{m} S_{m,n}(a,b) \cdot P(x,b,n)$$

The classical Stirling numbers emerge as special cases:
* $S_{m,n}(0,-1) = s(m,n)$ (Stirling numbers of the first kind)
* $S_{m,n}(-1,0) = \begin{Bmatrix} m \\ n \end{Bmatrix}$ (Stirling numbers of the second kind, with appropriate scaling)

### Lah Numbers Connection

The falling and rising factorials are related to one another through the [[Lah numbers]] $L(n, k) = \binom{n-1}{k-1} \frac{n!}{k!}$:

$$\begin{align}
x^{(n)} & = \sum_{k=0}^n L(n,k) (x)_k \\
(x)_n & = \sum_{k=0}^n L(n,k) (-1)^{n-k} x^{(k)}
\end{align}$$

In the unified framework, this corresponds to:
$$S_{n,k}(1,-1) = (-1)^{n-k} L(n,k)$$

showing that '''Lah numbers are special cases of generalized Stirling transfer coefficients'''.

## Applications

### Finite Difference Calculus

The falling factorial occurs in [[umbral calculus]] and serves as the discrete analog of $x^n$ in finite difference theory:

$$\Delta (x)_n = n(x)_{n-1}$$

Compare with the continuous case: $\frac{d}{dx} x^n = nx^{n-1}$

### Hypergeometric Functions

The rising factorial is integral to the definition of the [[hypergeometric function]]:

$${}_2F_1(a,b;c;z) = \sum_{n=0}^\infty \frac{a^{(n)} b^{(n)}}{c^{(n)}} \frac{z^n}{n!}$$

### Generating Functions

The exponential generating functions are:

$$\sum_{n=0}^\infty (x)_n \frac{t^n}{n!} = (1+t)^x$$

$$\sum_{n=0}^\infty x^{(n)} \frac{t^n}{n!} = (1-t)^{-x}$$

## See Also

* [[Generalized factorial polynomials]] - The unified P(x,a,m) framework
* [[Generalized Stirling transfer coefficients]] - Unified transformation theory
* [[Pochhammer symbol]] - Traditional notation
* [[Stirling numbers]] - Connection coefficients
* [[Lah numbers]] - Rising-to-falling transformations
* [[Hypergeometric function]] - Applications in special functions
* [[Umbral calculus]] - Finite difference applications

## References

<references/>

## External Links

* {{MathWorld |title=Pochhammer Symbol |urlname=PochhammerSymbol}}

{{DEFAULTSORT:Pochhammer Symbol}}
[[Category:Gamma and related functions]]
[[Category:Factorial and binomial topics]]
[[Category:Finite differences]]
[[Category:Operations on numbers]]
