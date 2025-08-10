{{Short description|Mathematical sequences in combinatorics}}
{{Use American English|date = March 2019}}
In [[mathematics]], '''Stirling numbers''' arise in a variety of [[Analysis (mathematics)|analytic]] and [[combinatorics|combinatorial]] problems. They are named after [[James Stirling (mathematician)|James Stirling]], who introduced them in a purely algebraic setting in his book ''Methodus differentialis'' (1730).{{sfn|Mansour|Schork|2015|p=5}} They were rediscovered and given a combinatorial meaning by Masanobu Saka in his 1782 ''Sanpō-Gakkai'' ''(The Sea of Learning on Mathematics)''.{{sfn|Mansour|Schork|2015|p=4}}<ref>{{Cite book |title=Combinatorics: Ancient & Modern. |publisher=Oxford University Press |year=2013 |isbn=978-0-19-965659-2 |editor-last=Wilson, R., & Watkins, J. J. |pages=26}}</ref>

Two different sets of numbers bear this name: the [[Stirling numbers of the first kind]] and the [[Stirling numbers of the second kind]]. Additionally, [[Lah numbers]] are sometimes referred to as Stirling numbers of the third kind.  Each kind is detailed in its respective article, this one serving as a description of relations between them.

A common property of all three kinds is that they describe coefficients relating three different sequences of polynomials that frequently arise in combinatorics.  Moreover, all three can be defined as the number of partitions of ''n'' elements into ''k'' non-empty subsets, where each subset is endowed with a certain kind of order (no order, cyclical, or linear).

==Notation==
{{main|Stirling numbers of the first kind|Stirling numbers of the second kind}}
Several different notations for Stirling numbers are in use. Ordinary (signed) '''Stirling numbers of the first kind''' are commonly denoted:

: <math> s(n,k)\,.</math>
'''Unsigned Stirling numbers of the first kind''', which count the number of [[permutation]]s of ''n'' elements with ''k'' disjoint [[cyclic permutation|cycle]]s, are denoted:

: <math> \biggl[{n \atop k}\biggr] =c(n,k)=|s(n,k)|=(-1)^{n-k} s(n,k)\,</math>
'''Stirling numbers of the second kind''', which count the number of ways to partition a set of ''n'' elements into ''k'' nonempty subsets:<ref>Ronald L. Graham, Donald E. Knuth, Oren Patashnik (1988) ''[[Concrete Mathematics]]'', Addison-Wesley, Reading MA. {{isbn|0-201-14236-8}}, p.&nbsp;244.</ref>

: <math> \biggl\{{\!n\! \atop \!k\!}\biggr\} = S(n,k) = S_n^{(k)} \,</math>

[[Abramowitz and Stegun]] use an uppercase <math>S</math> and a [[blackletter]] <math>\mathfrak S</math>, respectively, for the first and second kinds of Stirling number.  The notation of brackets and braces, in analogy to [[binomial coefficients]], was introduced in 1935 by [[Jovan Karamata]] and promoted later by [[Donald Knuth]], though the bracket notation conflicts with a common notation for [[Gaussian coefficient]]s.<ref>{{Cite journal |last=Knuth |first=Donald E. |date=1992 |title=Two Notes on Notation |url=https://www.jstor.org/stable/2325085 |journal=American Mathematical Monthly |volume=99 |issue=5 |pages=403–422 |doi=10.2307/2325085 |jstor=2325085 }}</ref> The mathematical motivation for this type of notation, as well as additional Stirling number formulae, may be found on the page for [[Stirling numbers and exponential generating functions]].

Another infrequent notation is <math>s_1(n,k)</math> and <math>s_2(n,k)</math>.

==Expansions of falling and rising factorials<span class="anchor" id="falling_and_rising_anchor"></span>==
Stirling numbers express coefficients in expansions of [[falling and rising factorials]] (also known as the Pochhammer symbol) as polynomials.

That is, the '''falling factorial''', defined as <math>\ (x)_{n} = x(x-1)\ \cdots(x-n+1)\ ,</math> is a polynomial in {{mvar|x}} of degree {{mvar|n}} whose expansion is

:<math>(x)_{n}\ =\ \sum_{k=0}^n\ s(n,k)\ x^k\ </math>

with (signed) Stirling numbers of the first kind as coefficients.

Note that <math>\ (x)_0 \equiv 1\ ,</math> by convention, because it is an [[empty product]]. The notations <math style="vertical-align:baseline;">\ x^{\underline{n}}\ </math> for the falling factorial and <math style="vertical-align:baseline;">\ x^{\overline{n}}\ </math> for the rising factorial are also often used.<ref>{{cite book |last=Aigner |first=Martin |title=A Course in Enumeration |url=https://archive.org/details/courseenumeratio00aign_007 |url-access=limited |publisher=Springer |year=2007 |pages=[https://archive.org/details/courseenumeratio00aign_007/page/n563 561] |chapter=Section 1.2 – Subsets and binomial coefficients |isbn=978-3-540-39032-9}}</ref> (Confusingly, the Pochhammer symbol that many use for ''falling'' factorials is used in [[special function]]s for ''rising'' factorials.)

Similarly, the '''rising factorial''', defined as <math>\ x^{(n)}\ =\ x(x+1)\ \cdots(x+n-1)\ ,</math> is a polynomial in {{mvar|x}} of degree {{mvar|n}} whose expansion is

:<math> x^{(n)}\ =\ \sum_{k=0}^n\ \biggl[{n \atop k}\biggr]\ x^k\ =\ \sum_{k=0}^n\ (-1)^{n-k}\ s(n,k)\ x^k\ ,</math>

with unsigned Stirling numbers of the first kind as coefficients.
One of these expansions can be derived from the other by observing that <math>\ x^{(n)} = (-1)^n (-x)_{n} ~.</math>

Stirling numbers of the second kind express the reverse relations:

:<math>\ x^n\ =\ \sum_{k=0}^n\ S(n,k)\ (x)_k\ </math>

and

:<math>\ x^n\ =\ \sum_{k=0}^n\ (-1)^{n-k}\ S(n,k)\ x^{(k)} ~.</math>

==As change of basis coefficients==
Considering the set of [[polynomial]]s in the (indeterminate) variable ''x'' as a vector space,
each of the three sequences
:<math>x^0,x^1,x^2,x^3,\dots \quad (x)_0,(x)_1,(x)_2,\dots \quad x^{(0)},x^{(1)},x^{(2)},\dots</math>
is a [[Basis (linear algebra)|basis]].
That is, every polynomial in ''x'' can be written as a sum <math>a_0 x^{(0)} + a_1 x^{(1)} + \dots + a_n x^{(n)}</math> for some unique coefficients <math>a_i</math> (similarly for the other two bases).
The above relations then express the [[change of basis]] between them, as summarized in the following [[commutative diagram]]:
: {{Dark mode invert|[[File:Stirling numbers as polynomial basis change.svg|center|500x500px|A diagram of how different Stirling numbers give coefficients for changing one basis of polynomials to another]]}}
The coefficients for the two bottom changes are described by the [[#Lah numbers|Lah numbers]] below.
Since coefficients in any basis are unique, one can define Stirling numbers this way, as the coefficients expressing polynomials of one basis in terms of another, that is, the unique numbers relating <math>x^n</math> with falling and rising factorials as above.

Falling factorials define, up to scaling, the same polynomials as [[Binomial coefficient#Binomial coefficients as polynomials|binomial coefficients]]: <math display="inline">\binom{x}{k} = (x)_k/k!</math>. The changes between the standard basis <math>\textstyle x^0, x^1, x^2, \dots</math> and the basis <math display="inline">\binom{x}{0}, \binom{x}{1}, \binom{x}{2}, \dots</math> are thus described by similar formulas:
: <math>x^n=\sum_{k=0}^n \biggl\{{\!n\! \atop \!k\!}\biggr\} k! \binom{x}{k} \quad \text{and} \quad \binom{x}{n}=\sum_{k=0}^n \frac{s(n,k)}{n!} x^k</math>.

===Example===
Expressing a polynomial in the basis of falling factorials is useful for calculating sums of the polynomial evaluated at consecutive integers.
Indeed, the sum of falling factorials with fixed ''k'' can expressed as another falling factorial (for <math>k\ne-1</math>)

:<math>\sum_{0\leq i < n} (i)_k = \frac{(n)_{k+1}}{k+1} </math>

This can be proved by [[mathematical induction|induction]].

For example, the sum of fourth powers of integers up to ''n'' (this time with ''n'' included), is:

:<math>\begin{align}
\sum_{i=0}^{n} i^4 & = \sum_{i=0}^n \sum_{k=0}^4 \biggl\{{\!4\! \atop \!k\!}\biggr\} (i)_k = \sum_{k=0}^4 \biggl\{{\!4\! \atop \!k\!}\biggr\} \sum_{i=0}^n (i)_k =  \sum_{k=0}^4 \biggl\{{\!4\! \atop \!k\!}\biggr\} \frac{(n{+}1)_{k+1}}{k{+}1} \\[10mu]
& = \biggl\{{\!4\! \atop \!1\!}\biggr\} \frac{(n{+}1)_{2}}2
  + \biggl\{{\!4\! \atop \!2\!}\biggr\} \frac{(n{+}1)_{3}}3
  + \biggl\{{\!4\! \atop \!3\!}\biggr\} \frac{(n{+}1)_{4}}4
  + \biggl\{{\!4\! \atop \!4\!}\biggr\} \frac{(n{+}1)_{5}}5 \\[8mu]
& = \frac12 (n{+}1)_{2} + \frac73 (n{+}1)_{3} + \frac64 (n{+}1)_{4} + \frac15 (n{+}1)_{5}\,.
\end{align}</math>

Here the Stirling numbers can be computed from their definition as the number of partitions of 4 elements into ''k'' non-empty unlabeled subsets.

In contrast, the sum <math display="inline">\sum_{i=0}^n i^k</math> in the standard basis is given by [[Faulhaber's formula]], which in general is more complicated.

==As inverse matrices==
The Stirling numbers of the first and second kinds can be considered inverses of one another:

:<math>\sum_{j=k}^n s(n,j) S(j,k) = \sum_{j=k}^n (-1)^{n-j} \biggl[{n \atop j}\biggr] \biggl\{{\!j\! \atop \!k\!}\biggr\} = \delta_{n,k}</math>

and

:<math>\sum_{j=k}^n  S(n,j) s(j,k) = \sum_{j=k}^n (-1)^{j-k} \biggl\{{\!n\! \atop \!j\!}\biggr\} \biggl[{j \atop k}\biggr]= \delta_{n,k},</math>

where <math>\delta_{nk}</math> is the [[Kronecker delta]]. These two relationships may be understood to be matrix inverse relationships. That is, let ''s'' be the [[lower triangular matrix]] of Stirling numbers of the first kind, whose matrix elements
<math>s_{nk}=s(n,k).\,</math>
The [[matrix inverse|inverse]] of this matrix is ''S'', the [[lower triangular matrix]] of Stirling numbers of the second kind, whose entries are <math>S_{nk}=S(n,k).</math>  Symbolically, this is written

:<math>s^{-1} = S\,</math>

Although ''s'' and ''S'' are infinite, so calculating a product entry involves an infinite sum, the matrix multiplications work because these matrices are lower triangular, so only a finite number of terms in the sum are nonzero.

==Lah numbers==
{{main|Lah numbers}}

The Lah numbers <math>L(n,k) = {n-1 \choose k-1} \frac{n!}{k!}</math> are sometimes called Stirling numbers of the third kind.<ref>{{cite book
 | last1=Sándor | first1=Jozsef | last2=Crstici | first2=Borislav
 | title=Handbook of Number Theory II  | publisher=[[Kluwer Academic Publishers]] | year=2004
 | url=https://books.google.com/books?id=B2WZkvmFKk8C&dq=%22Stirling+numbers+of+the+third+kind%22&pg=PA464 | isbn=9781402025464 | page=464}}</ref>
By convention, <math>L(0,0)=1</math> and <math>L(n,k)=0</math> if <math>n<k</math> or <math>k = 0 < n</math>.

These numbers are coefficients expressing falling factorials in terms of rising factorials and vice versa:
:<math>x^{(n)} = \sum_{k=0}^n L(n,k) (x)_k\quad</math> and <math>\quad(x)_n = \sum_{k=0}^n (-1)^{n-k} L(n,k)x^{(k)}.</math>

As above, this means they express the change of basis between the bases <math>(x)_0,(x)_1,(x)_2,\cdots</math> and <math>x^{(0)},x^{(1)},x^{(2)},\cdots</math>, completing the diagram.
In particular, one formula is the inverse of the other, thus:

: <math>\sum_{j=k}^n (-1)^{j-k} L(n,j) L(j,k) = \delta_{n,k}.</math>

Similarly, composing the change of basis from <math>x^{(n)}</math> to <math>x^n</math> with the change of basis from <math>x^n</math> to <math>(x)_{n}</math> gives the change of basis directly from <math>x^{(n)}</math> to <math>(x)_{n}</math>:

:<math> L(n,k) = \sum_{j=k}^n \biggl[{n \atop j}\biggr]  \biggl\{{\!j\! \atop \!k\!}\biggr\} ,</math>

and similarly for other compositions. In terms of matrices, if <math>L</math> denotes the matrix with entries <math>L_{nk}=L(n,k)</math> and <math>L^{-}</math> denotes the matrix with entries  <math>L^{-}_{nk}=(-1)^{n-k}L(n,k)</math>, then one is the inverse of the other: <math> L^{-} = L^{-1}</math>.
Composing the matrix of unsigned Stirling numbers of the first kind with the matrix of Stirling numbers of the second kind gives the Lah numbers: <math>L = |s| \cdot S</math>.

[[Enumerative combinatorics|Enumeratively]], <math display="inline">\left\{{\!n\! \atop \!k\!}\right\}, \left[{n \atop k}\right] , L(n,k)</math> can be defined as the number of partitions of ''n'' elements into ''k'' non-empty unlabeled subsets, where each subset is endowed with no order, a [[cyclic order]], or a linear order, respectively. In particular, this implies the inequalities:
: <math>\biggl\{{\!n\! \atop \!k\!}\biggr\} \leq \biggl[{n \atop k}\biggr] \leq L(n,k).</math>

==Inversion relations and the Stirling transform==

For any pair of sequences, <math>\{f_n\}</math> and <math>\{g_n\}</math>, related by a finite sum Stirling number formula given by

:<math>g_n = \sum_{k=0}^{n} \left\{\begin{matrix} n \\ k \end{matrix} \right\} f_k, </math>

for all integers <math>n \geq 0</math>, we have a corresponding [[generating function transformation#Inversion relations and generating function identities|inversion formula]] for <math>f_n</math> given by

:<math>f_n = \sum_{k=0}^{n} \left[\begin{matrix} n \\ k \end{matrix} \right] (-1)^{n-k} g_k. </math>

The lower indices could be any integer between <math display="inline">0</math> and <math display="inline">n</math>.

These inversion relations between the two sequences translate into functional equations between the sequence [[generating function|exponential generating functions]] given by the [[Stirling transform|Stirling (generating function) transform]] as

:<math>\widehat{G}(z) = \widehat{F}\left(e^z-1\right)</math>

and

:<math>\widehat{F}(z) = \widehat{G}\left(\log(1+z)\right). </math>

For <math>D = d/dx</math>, the [[differential operators]] <math>x^nD^n</math> and <math>(xD)^n</math> are related by the following formulas for all integers <math>n \geq 0</math>:<ref>''Concrete Mathematics'' exercise 13 of section 6. Note that this formula immediately implies the first positive-order Stirling number transformation given in the main article on [[generating function transformation#Derivative transformations|generating function transformations]].</ref>

:<math>
\begin{align}
(xD)^n &= \sum_{k=0}^n S(n, k) x^k D^k \\
x^n D^n &= \sum_{k=0}^n s(n, k) (xD)^k = (xD)_n = xD(xD - 1)\ldots (xD - n + 1)
\end{align}
</math>

Another pair of "''inversion''" relations involving the [[Stirling numbers]] relate the [[finite difference|forward differences]] and the ordinary <math>n^{th}</math> [[derivative]]s of a function, <math>f(x)</math>, which is analytic for all <math>x</math> by the formulas<ref>{{cite journal|last1=Olver|first1=Frank|first2=Daniel|last2=Lozier|first3=Ronald|last3=Boisvert|first4=Charles|last4=Clark|title=NIST Handbook of Mathematical Functions|journal=NIST Handbook of Mathematical Functions|date=2010|url=https://www.nist.gov/publications/nist-handbook-mathematical-functions}} (Section 26.8)</ref>

:<math>\frac{1}{k!} \frac{d^k}{dx^k} f(x) = \sum_{n=k}^{\infty} \frac{s(n, k)}{n!} \Delta^n f(x)</math>

:<math>\frac{1}{k!} \Delta^k f(x) = \sum_{n=k}^{\infty} \frac{S(n, k)}{n!} \frac{d^n}{dx^n} f(x). </math>

== Similar properties ==
{| class="wikitable"
|+Table of similarities
![[Stirling numbers of the first kind]]
![[Stirling numbers of the second kind]]
|-
|<math> \left[{n+1\atop k}\right] = n \left[{n\atop k}\right] + \left[{n\atop k-1}\right]</math>
|<math>\left\{{n+1\atop k}\right\} = k \left\{{ n \atop k }\right\} + \left\{{n\atop k-1}\right\} </math>
|-
|<math>\sum_{k=0}^n \left[{n\atop k}\right] = n!</math>
|<math>\sum_{k=0}^n \left\{ {n \atop k} \right\} = B_n</math>, where <math>B_n</math> is the <math>n</math>th [[Bell number]]
|-
|<math>\sum_{k=0}^n \left[{n\atop k}\right] x^k = x^{(n)}</math>, where <math>\{x^{(n)}\}_{n\in\N} </math> are the [[Falling and rising factorials|rising factorials]]
|<math>\sum_{k=0}^n \left\{ {n \atop k} \right\} x^k = T_n(x)</math>, where <math>\{T_n\}_{n\in\N} </math> are the [[Touchard polynomials]]
|-
|<math> \left[{n\atop 0}\right] = \delta_n,\ \left[{n\atop n-1}\right] = \binom{n}{2},\ \left[{n\atop n}\right] = 1</math>
|<math> \left\{{n\atop 0}\right\} = \delta_n,\ \left\{{n\atop n-1}\right\} = \binom{n}{2},\ \left\{{n\atop n}\right\} = 1</math>
|-
|<math>\left[{n+1\atop k+1}\right] = \sum_{j=k}^n \left[{n\atop j}\right] \binom{j}{k}  </math>
|<math>\left\{{n+1\atop k+1}\right\} = \sum_{j=k}^n \binom{n}{j} \left\{{ j \atop k }\right\} </math>
|-
|<math>\left[\begin{matrix} n+1 \\ k+1 \end{matrix} \right] = \sum_{j=k}^n \frac{n!}{j!} \left[{j \atop k} \right]</math>
|<math>
\left\{{n+1\atop k+1}\right\} = \sum_{j=k}^n (k+1)^{n-j} \left\{{j \atop k}\right\} </math>
|-
|<math>\left[{ n+k+1 \atop n }\right] = \sum_{j=0}^k (n+j) \left[{n+j \atop j}\right]</math>
|<math>\left\{{n+k+1 \atop k}\right\} = \sum_{j=0}^k j \left\{{ n+j \atop j }\right\}</math>
|-
|<math>\left[{n \atop l+m } \right] \binom{l+m}{l} = \sum_k \left[{k \atop l} \right] \left[{n-k \atop m } \right] \binom{n}{k} </math>
|<math>\left\{{n \atop l+m } \right\} \binom{l+m}{l} = \sum_k \left\{{k \atop l} \right\} \left\{{n-k \atop m } \right\} \binom{n}{k} </math>
|-
|<math>\left[{n+k \atop n} \right] \underset{n \to \infty}{\sim} \frac{n^{2k}}{2^k k!}. </math>
|<math> \left\{{n+k \atop n}\right\} \underset{n \to \infty}{\sim} \frac{n^{2k}}{2^k k!}.</math>
|-
|<math>\sum_{n=k}^\infty\left[{n\atop k}\right] \frac{x^n}{n!} = \frac{(-\log(1-x))^k}{k!}.</math>
|<math> \sum_{n=k}^\infty \left\{ {n \atop k} \right\} \frac{x^n}{n!} = \frac{(e^x-1)^k}{k!}.</math>
|-
|<math> \left[{n \atop k} \right] = \sum_{0 \leq i_1 < \ldots < i_{n-k} < n} i_1 i_2 \cdots i_{n-k}.</math>
|<math>
\left\{ {n \atop k} \right\} = \sum_{
\begin{array}{c}
c_1 + \ldots + c_k = n-k\\
c_1, \ldots,\ c_k\ \geq\ 0
\end{array}
} 1^{c_1} 2^{c_2} \cdots k^{c_k}
</math>
|}
See the specific articles for details.

==Symmetric formulae==

Abramowitz and Stegun give the following symmetric formulae that relate the Stirling numbers of the first and second kind.<ref>{{Citation |last1=Goldberg |first1=K. |title=Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables|edition=10th  |pages=824–825 |year=1972 |editor-last1=Abramowitz |editor-first1=Milton |contribution=Stirling Numbers of the First Kind, Stirling Numbers of the Second Kind |location=New York |publisher=Dover |last2=Newman |first2=M |last3=Haynsworth |first3=E. |editor-last2=Stegun |editor-first2=Irene A.}}</ref>

:<math> \left[{ n \atop k } \right] = \sum_{j=n}^{2n-k}  (-1)^{j-k} \binom{j-1}{k-1} \binom{2n-k}{j} \left\{{ j-k \atop j-n} \right\} </math>

and

:<math>
\left\{{n \atop k}\right\} = \sum_{j=n}^{2n-k} (-1)^{j-k} \binom{j-1}{k-1} \binom{2n-k}{j} \left[{j-k \atop j-n } \right]
</math>

==Stirling numbers with negative integral values==
The Stirling numbers can be extended to negative integral values, but not all authors do so in the same way.<ref name="Loeb">{{cite journal |last1=Loeb |first1=Daniel E.|orig-year=Received 3 Nov 1989|title=A generalization of the Stirling numbers |journal=Discrete Mathematics |volume=103 |issue= 3|pages=259–269 |doi= 10.1016/0012-365X(92)90318-A|year=1992 |doi-access=free }}</ref><ref name=":0">{{cite web |url=http://www.fq.math.ca/Scanned/34-3/branson.pdf |archive-url=https://web.archive.org/web/20110827132927/http://www.fq.math.ca/Scanned/34-3/branson.pdf |archive-date=2011-08-27 |url-status=live |title=An extension of Stirling numbers |last=Branson |first=David |date=August 1994 |website=The Fibonacci Quarterly |access-date=Dec 6, 2017 }}</ref><ref name=":1">D.E. Knuth, 1992.</ref> Regardless of the approach taken, it is worth noting that Stirling numbers of first and second kind are connected by the relations:

: <math>\biggl[{n \atop k}\biggr] = \biggl\{{\!-k\! \atop \!-n\!}\biggr\} \quad \text{and} \quad
\biggl\{{\!n\! \atop \!k\!}\biggr\} = \biggl[{-k \atop -n}\biggr]</math>

when ''n'' and ''k'' are nonnegative integers.  So we have the following table for <math>\left[{-n \atop -k}\right]</math>:
{| cellspacing="0" cellpadding="5" style="text-align:right;" class="wikitable"
|-
| {{diagonal split header|''n''|''k''}}
! {{rh|align=right}} | −1
! {{rh|align=right}} | −2
! {{rh|align=right}} | −3
! {{rh|align=right}} | −4
! {{rh|align=right}} | −5
|-
! {{rh|align=right}} | −1
| 1
| 1
| 1
| 1
| 1
|-
! {{rh|align=right}} | −2
| 0
| 1
| 3
| 7
| 15
|-
! {{rh|align=right}} | −3
| 0
| 0
| 1
| 6
| 25
|-
! {{rh|align=right}} | −4
| 0
| 0
| 0
| 1
| 10
|-
! {{rh|align=right}} | −5
| 0
| 0
| 0
| 0
| 1
|}

Donald Knuth<ref name=":1" /> defined the more general Stirling numbers by extending a [[Stirling numbers of the second kind#Recurrence relation|recurrence relation]] to all integers.  In this approach, <math display=inline> \left[{n \atop k}\right]</math> and <math display=inline>\left\{{\!n\! \atop \!k\!}\right\}</math> are zero if ''n'' is negative and ''k'' is nonnegative, or if ''n'' is nonnegative and ''k'' is negative, and so we have, for ''any'' integers ''n'' and ''k'',
: <math>\biggl[{n \atop k}\biggr] = \biggl\{{\!-k\! \atop \!-n\!}\biggr\} \quad \text{and} \quad
\biggl\{{\!n\! \atop \!k\!}\biggr\} = \biggl[{-k \atop -n}\biggr].</math>

On the other hand, for positive integers ''n'' and ''k'', David Branson<ref name=":0" /> defined <math display=inline> \left[{-n \atop -k}\right]\!,</math> <math display=inline>\left\{{\!-n\! \atop \!-k\!}\right\}\!,</math> <math display=inline> \left[{-n \atop k}\right]\!,</math> and <math display=inline>\left\{{\!-n\! \atop \!k\!}\right\}</math> (but not <math display=inline> \left[{n \atop -k}\right]</math> or <math display=inline>\left\{{\!n\! \atop \!-k\!}\right\}</math>). In this approach, one has the following extension of the [[Stirling numbers of the second kind#Recurrence relation|recurrence relation]] of the Stirling numbers of the first kind:

:<math> \biggl[{-n \atop k}\biggr]
= \frac{(-1)^{n+1}}{n!}\sum_{i=1}^{n}\frac{(-1)^{i+1}}{i^k} \binom ni </math>,

For example, <math display=inline>\left[{-5 \atop k}\right] = \frac1{120}\Bigl(5-\frac{10}{2^k}+\frac{10}{3^k}-\frac 5{4^k}+\frac 1{5^k}\Bigr).</math>  This leads to the following table of values of <math display=inline>\left[{n \atop k}\right]</math> for negative integral ''n''.
{| cellspacing="0" cellpadding="5" style="text-align:center;" class="wikitable"
|-
| {{diagonal split header|''n''|''k''}}
! 0
! 1
! 2
! 3
! 4
|-
! −1
| 1
| 1
| 1
| 1
| 1
|-
! −2
| {{sfrac|{{val|-1}}|{{val|2}}}}
| {{sfrac|{{val|-3}}|{{val|4}}}}
| {{sfrac|{{val|-7}}|{{val|8}}}}
| {{sfrac|{{val|-15}}|{{val|16}}}}
| {{sfrac|{{val|-31}}|{{val|32}}}}
|-
! −3
| {{sfrac|{{val|1}}|{{val|6}}}}
| {{sfrac|{{val|11}}|{{val|36}}}}
| {{sfrac|{{val|85}}|{{val|216}}}}
| {{sfrac|{{val|575}}|{{val|1296}}}}
| {{sfrac|{{val|3661}}|{{val|7776}}}}
|-
! −4
| {{sfrac|{{val|-1}}|{{val|24}}}}
| {{sfrac|{{val|-25}}|{{val|288}}}}
| {{sfrac|{{val|-415}}|{{val|3456}}}}
| {{sfrac|{{val|-5845}}|{{val|41472}}}}
| {{sfrac|{{val|-76111}}|{{val|497664}}}}
|-
! −5
| {{sfrac|{{val|1}}|{{val|120}}}}
| {{sfrac|{{val|137}}|{{val|7200}}}}
| {{sfrac|{{val|12019}}|{{val|432000}}}}
| {{sfrac|{{val|874853}}|{{val|25920000}}}}
| {{sfrac|{{val|58067611}}|{{val|1555200000}}}}
|}

In this case <math display=inline>\sum_{n=1}^{\infty}\left[{-n \atop -k}\right]=B_{k} </math> where <math>B_{k}</math> is a [[Bell number]], and so one may define the negative Bell numbers by <math display=inline>\sum_{n=1}^{\infty}\left[{-n \atop k}\right]=:B_{-k}</math>.

For example, this produces <math display=inline>\sum_{n=1}^{\infty}\left[{-n \atop 1}\right]=B_{-1}=\frac 1e\sum_{j=1}^\infty\frac1{j\cdot j!}=\frac 1e\int_0^1\frac{e^t-1}{t}dt=0.4848291\dots</math>, generally <math display=inline>B_{-k}=\frac 1e\sum_{j=1}^\infty\frac1{j^kj!} </math>.

==See also==
* [[Bell polynomials]]
* [[Catalan number]]
* [[Cycles and fixed points]]
* [[Pochhammer symbol]]
* [[Polynomial sequence]]
* [[Touchard polynomials]]
* [[Stirling permutation]]

==Citations==
{{Reflist}}

==References==
{{refbegin}}
*{{Citation
| editor-last  = Rosen
| editor-first = Kenneth H.
| title  = Handbook of Discrete and Combinatorial Mathematics
| publisher = CRC Press
| date = 2018
| isbn = 978-1-5848-8780-5
}}
*{{Citation
| author-last1  = Mansour
| author-first1 = Toufik
| author-last2  = Schork
| author-first2 = Mathias
| title  = Commutation Relations, Normal Ordering, and Stirling Numbers
| publisher = CRC Press
| date = 2015
| isbn = 978-1-4665-7989-7
}}
{{refend}}

==Further reading==
* {{cite journal|first=Victor|last=Adamchik|url=http://www-2.cs.cmu.edu/~adamchik/articles/stirling.pdf |archive-url=https://web.archive.org/web/20041214001155/http://www-2.cs.cmu.edu/~adamchik/articles/stirling.pdf |archive-date=2004-12-14 |url-status=live|title=On Stirling Numbers and Euler Sums|journal=Journal of Computational and Applied Mathematics|volume=79|year=1997|pages=119–130|doi=10.1016/s0377-0427(96)00167-7|doi-access=free}}
* {{cite journal|first1=Arthur T.|last1=Benjamin|first2=Gregory O.|last2=Preston|first3=Jennifer J.|last3=Quinn|url=https://math.hmc.edu/benjamin/wp-content/uploads/sites/5/2019/06/A-Stirling-EnCOUNTer.pdf |archive-url=https://web.archive.org/web/20200910121921/https://math.hmc.edu/benjamin/wp-content/uploads/sites/5/2019/06/A-Stirling-EnCOUNTer.pdf |archive-date=2020-09-10 |url-status=live|title=A Stirling Encounter with Harmonic Numbers|date=2002|journal=Mathematics Magazine|volume=75|number=2|pages=95–103|doi=10.2307/3219141|jstor=3219141|citeseerx=10.1.1.383.722}}
* {{cite journal|url=http://www.maa.org/sites/default/files/pdf/upload_library/2/Boyadzhiev-2013.pdf |archive-url=https://web.archive.org/web/20150905120358/http://www.maa.org/sites/default/files/pdf/upload_library/2/Boyadzhiev-2013.pdf |archive-date=2015-09-05 |url-status=live|first=Khristo N.|last=Boyadzhiev|title=Close encounters with the Stirling numbers of the second kind|date=2012|journal=Mathematics Magazine|volume=85|number=4|pages=252–266|doi=10.4169/math.mag.85.4.252|arxiv=1806.09468|s2cid=115176876}}
* {{cite journal|first=Louis|last=Comtet|url=http://www.techniques-ingenieur.fr/page/af202niv10002/permutations.html#2.2|title=Valeur de ''s''(''n'',&nbsp;''k'')|journal=Analyse Combinatoire, Tome Second|page=51|year=1970|language=fr|url-access=subscription}}
* {{cite book|first=Louis|last=Comtet|title=Advanced Combinatorics: The Art of Finite and Infinite Expansions|url=https://archive.org/details/Comtet_Louis_-_Advanced_Coatorics|publisher=Reidel Publishing Company|location=Dordrecht-Holland/Boston-U.S.A.|date=1974|isbn=9789027703804 }}
* {{cite journal| author=Hsien-Kuei Hwang |title=Asymptotic Expansions for the Stirling Numbers of the First Kind |journal=Journal of Combinatorial Theory, Series A |volume=71 |issue=2 |pages=343–351 |year=1995 |url=http://citeseer.ist.psu.edu/577040.html |doi=10.1016/0097-3165(95)90010-1|doi-access=free }}
* {{citation |author-link=Donald Knuth|first=D.E.|last=Knuth| journal = Amer. Math. Monthly | title=Two notes on notation| year=1992 | volume=99 |issue=5| pages=403–422 | arxiv=math/9205211 | doi=10.2307/2325085 | jstor= 2325085|s2cid=119584305}}
* {{cite journal|first=Francis L.|last=Miksa|jstor=2002617|title=Stirling numbers of the first kind: 27 leaves reproduced from typewritten manuscript on deposit in the UMT File|journal=Mathematical Tables and Other Aids to Computation: Reviews and Descriptions of Tables and Books|volume=10|number=53|date=January 1956|pages=37–38}}
* {{cite book|editor1-first=Milton|editor1-last=Abramowitz|editor2-first=Irene A.|editor2-last=Stegun|chapter-url=http://www.convertit.com/Go/ConvertIt/Reference/AMS55.ASP|title=Handbook of Mathematical Functions (with Formulas, Graphs and Mathematical Tables)|publisher=U.S. Dept. of Commerce, National Bureau of Standards, Applied Math.|series=55|orig-year=1964|year=1972|chapter=Combinatorial Analysis, Table 24.4, Stirling Numbers of the Second Kind|first=Francis L.|last=Miksa|page=835}}
* {{cite journal|first=Dragoslav S.|last=Mitrinović|url=http://pefmath2.etf.bg.ac.rs/files/23/23.pdf |archive-url=https://web.archive.org/web/20090617034106/http://pefmath2.etf.bg.ac.rs/files/23/23.pdf |archive-date=2009-06-17 |url-status=live|title=Sur les nombres de Stirling de première espèce et les polynômes de Stirling|journal=Publications de la Faculté d'Electrotechnique de l'Université de Belgrade, Série Mathématiques et Physique|language=fr|issn=0522-8441|number=23|date=1959|pages=1–20}}
* {{cite web|first1=John J.|last1=O'Connor|first2=Edmund F.|last2=Robertson|url=https://mathshistory.st-andrews.ac.uk/Biographies/Stirling/|title=James Stirling (1692&ndash;1770)|date=September 1998}}
* {{cite journal| first1=J. M. |last1=Sixdeniers |first2= K. A. |last2=Penson
|first3=A. I. |last3= Solomon | url = http://www.cs.uwaterloo.ca/journals/JIS/VOL4/SIXDENIERS/bell.pdf
|title= Extended Bell and Stirling Numbers From Hypergeometric Exponentiation
|year=2001
|journal = Journal of Integer Sequences | volume= 4 | pages=01.1.4|arxiv=math/0106123 |bibcode=2001JIntS...4...14S }}
* {{cite journal| first1=Michael Z. | last1=Spivey | title=Combinatorial sums and finite differences
|doi=10.1016/j.disc.2007.03.052 | journal=Discrete Math.
|year=2007 | volume=307 | number=24 | pages=3130–3146| doi-access=free | citeseerx=10.1.1.134.8665 }}
* {{Cite OEIS|sequencenumber=A008275|name=Stirling numbers of first kind}}
* {{Cite OEIS|sequencenumber=A008277|name=Stirling numbers of 2nd kind}}

{{Classes of natural numbers}}

[[Category:Permutations]]
[[Category:Q-analogs]]
[[Category:Factorial and binomial topics]]
[[Category:Integer sequences]]
