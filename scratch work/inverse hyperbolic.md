{{short description|Mathematical functions}}
{{anchor|asinh|acosh|atanh|asech|acsch|acoth}}
[[File:Graphs of the inverse hyperbolic functions.png|thumb|upright=1.25|Graphs of the inverse hyperbolic functions]]
[[File:Hyperbolic functions sinh, cosh, tanh.png|thumb|upright=1.25|right|The hyperbolic functions {{math|sinh}}, {{math|cosh}}, and {{math|tanh}} with respect to a unit hyperbola are analogous to circular functions {{math|sin}}, {{math|cos}}, {{math|tan}} with respect to a unit circle. The argument to the hyperbolic functions is a hyperbolic angle measure.]]
In [[mathematics]], the '''inverse hyperbolic functions''' are [[inverse function|inverses]] of the [[hyperbolic functions]], analogous to the [[inverse trigonometric functions|inverse circular functions]]. There are six in common use: inverse hyperbolic sine, inverse hyperbolic cosine, inverse hyperbolic tangent, inverse hyperbolic cosecant, inverse hyperbolic secant, and inverse hyperbolic cotangent. They are commonly denoted by the symbols for the hyperbolic functions, prefixed with ''arc-'' or ''ar-'' or with a superscript <math>{-1}</math> (for example {{math|arcsinh}}, {{math|arsinh}}, or <math>\sinh^{-1}</math>).

For a given value of a hyperbolic function, the inverse hyperbolic function provides the corresponding [[hyperbolic angle|hyperbolic angle measure]], for example <math>\operatorname{arsinh}(\sinh a) = a</math> and <math>\sinh(\operatorname{arsinh} x) = x.</math> Hyperbolic angle measure is the [[arc length|length of an arc]] of a [[unit hyperbola]] <math>x^2 - y^2 = 1</math> as measured in the Lorentzian plane ({{em|not}} the length of a hyperbolic arc in the [[Euclidean plane]]), and twice the [[area]] of the corresponding [[hyperbolic sector]]. This is analogous to the way [[angle|circular angle measure]] is the arc length of an arc of the [[unit circle]] in the Euclidean plane or twice the area of the corresponding [[circular sector]]. Alternately hyperbolic angle is the area of a sector of the hyperbola <math>xy = 1.</math> Some authors call the inverse hyperbolic functions ''hyperbolic area functions''.<ref>For example:{{pb}} {{cite book  |last1=Weltner |first1=Klaus |last2=John |first2=Sebastian |last3=Weber |first3=Wolfgang J. |last4=Schuster |first4=Peter |last5=Grosjean |first5=Jean |display-authors=1 |title=Mathematics for Physicists and Engineers |publisher=Springer |year=2014 |orig-year=2009 |edition=2nd |isbn=978-364254124-7 }} {{pb}} {{cite book |last=Durán |first=Mario |year=2012 |title=Mathematical methods for wave propagation in science and engineering |volume=1 |publisher=Ediciones UC |isbn=9789561413146 |page=89}}</ref>

Hyperbolic functions occur in the calculation of angles and distances in [[hyperbolic geometry]]. They also occur in the solutions of many linear [[differential equation]]s (such as the equation defining a [[catenary]]), [[Cubic function#Hyperbolic solution for one real root|cubic equations]], and [[Laplace's equation]] in [[Cartesian coordinates]]. [[Laplace's equation]]s are important in many areas of [[physics]], including [[electromagnetic theory]], [[heat transfer]], [[fluid dynamics]], and [[special relativity]].

==Notation==
[[Image:Hyperbolic functions-2.svg|thumb|300px|right|A ray through the [[unit hyperbola]] {{math|1= ''x''{{sup|2}} − ''y''{{sup|2}} = 1}} in the point {{math|(cosh ''a'', sinh ''a'')}}, where {{mvar|a}} is twice the area between the ray, the hyperbola, and the {{mvar|x}}-axis]]

The earliest and most widely adopted symbols use the prefix ''arc-'' (that is: {{math|arcsinh}}, {{math|arccosh}}, {{math|arctanh}}, {{math|arcsech}}, {{math|arccsch}}, {{math|arccoth}}), by analogy with the [[inverse trigonometric functions|inverse circular functions]] ({{math|arcsin}}, etc.). For a [[unit hyperbola]] ("Lorentzian circle") in the Lorentzian plane ([[pseudo-Euclidean space|pseudo-Euclidean plane]] of [[metric signature|signature]] {{math|(1, 1)}})<ref>{{cite journal |title=Trigonometry in Lorentzian Geometry |last1=Birman |first1=Graciela S. |last2=Nomizu |first2=Katsumi |journal=American Mathematical Monthly |year=1984 |volume=91 |number=9 |pages=543–549 |doi=10.1080/00029890.1984.11971490 |jstor=2323737 }}</ref> or in the [[hyperbolic number]] plane,<ref>{{cite journal |last=Sobczyk |first=Garret |title=The hyperbolic number plane |journal=College Mathematics Journal |volume=26 |number=4 |year=1995 |pages=268–280|doi=10.1080/07468342.1995.11973712 }}</ref> the [[hyperbolic angle|hyperbolic angle measure]] (argument to the hyperbolic functions) is indeed the [[arc length]] of a hyperbolic arc.

Also common is the notation <math>\sinh^{-1},</math> <math>\cosh^{-1},</math> etc.,<ref name=onlinesources>{{Cite web |last=Weisstein |first=Eric W.|title=Inverse Hyperbolic Functions |url=https://mathworld.wolfram.com/InverseHyperbolicFunctions.html |access-date=2020-08-30 |website=Wolfram Mathworld }} {{pb}} {{Cite web |title=Inverse hyperbolic functions |url=https://encyclopediaofmath.org/wiki/Inverse_hyperbolic_functions |access-date=2020-08-30 |website= Encyclopedia of Mathematics}}</ref><ref>{{cite book |last1=Press |first1=W.H. |last2=Teukolsky |first2=S.A. |last3=Vetterling |first3=WT |last4=Flannery |first4=B.P. |year=1992 |title=Numerical Recipes in FORTRAN |edition=2nd |publisher=Cambridge University Press |isbn=0-521-43064-X |chapter=§ 5.6. Quadratic and Cubic Equations}} {{pb}} {{cite book |last=Woodhouse |first=N.M.J. |author-link=N. M. J. Woodhouse |title=Special Relativity |publisher=Springer |date=2003 |page=71 |isbn=1-85233-426-6}}</ref> although care must be taken to avoid misinterpretations of the superscript −1 as an exponent. The standard convention is that <math>\sinh^{-1} x</math> or <math>\sinh^{-1}(x)</math> means the inverse function while <math>(\sinh x)^{-1}</math> or <math>\sinh(x)^{-1}</math> means the [[multiplicative inverse|reciprocal]] <math>1 / \sinh x.</math> Especially inconsistent is the conventional use of positive [[integer]] superscripts to indicate an exponent rather than function composition, e.g. <math>\sinh^{2} x</math> conventionally means <math>(\sinh x)^2</math> and {{em|not}} <math>\sinh(\sinh x).</math>

Because the argument of hyperbolic functions is {{em|not}} the arc length of a hyperbolic arc in the [[Euclidean plane]], some authors have condemned the prefix ''arc-'', arguing that the prefix ''ar-'' (for {{gloss|area}}) or ''arg-'' (for {{gloss|argument}}) should be preferred.<ref>{{cite book |last=Gullberg |first=Jan |author-link=Jan Gullberg |title=Mathematics: From the Birth of Numbers |publisher=W. W. Norton |year=1997 |isbn=039304002X |page=539 |quote=Another form of notation, {{math|arcsinh ''x''}}, {{math|arccosh ''x''}}, etc., is a practice to be condemned as these functions have nothing whatever to do with '''arc''', but with '''ar'''ea, as is demonstrated by their full Latin names, {{math|arsinh}} {{lang|la|area sinus hyperbolicus}}, {{math|arcosh}} {{lang|la|area cosinus hyperbolicus}}, etc.}} {{pb}} {{cite book |last1=Zeidler |first1=Eberhard |author1-link=Eberhard Zeidler (mathematician) |last2=Hackbusch |first2=Wolfgang |author2-link=Wolfgang Hackbusch |last3=Schwarz |first3=Hans Rudolf  |translator-last=Hunt |translator-first=Bruce |title=[[Oxford Users' Guide to Mathematics]] |publisher=Oxford University Press |year=2004 |isbn=0198507631 |chapter=§ 0.2.13 The inverse hyperbolic functions |page=68 |quote=The Latin names for the inverse hyperbolic functions are {{lang|la|area sinus hyperbolicus}}, {{lang|la|area cosinus hyperbolicus}}, {{lang|la|area tangens hyperbolicus}} and {{lang|la|area cotangens hyperbolicus}} (of {{mvar|x}})....}}. {{pb}} Zeidler & al. use the notations {{math|arsinh}}, etc.; note that the quoted Latin names are [[back-formation]]s, invented long after [[Neo-Latin]] ceased to be in common use in mathematical literature. {{pb}} {{cite book |last1=Bronshtein |first1=Ilja N. |author1-link=Ilja N. Bronshtein |last2=Semendyayev |first2=Konstantin A. |author2-link=Konstantin A. Semendyayev |last3=Musiol |first3=Gerhard |last4=Heiner |first4=Mühlig |title=[[Handbook of Mathematics]] |publisher=Springer |edition=5th |year=2007 |isbn=978-3540721215 |doi=10.1007/978-3-540-72122-2 |chapter=§ 2.10: Area Functions |page=91 |quote=The ''area functions'' are the inverse functions of the hyperbolic functions, i.e., the ''inverse hyperbolic functions''. The functions {{math|sinh ''x''}}, {{math|tanh ''x''}}, and {{math|coth ''x''}} are strictly monotone, so they have unique inverses without any restriction; the function {{math|cosh ''x''}} has two monotonic intervals so we can consider two inverse functions. The name ''area'' refers to the fact that the geometric definition of the functions is the area of certain hyperbolic sectors ...}} {{pb}} {{cite book |last=Bacon |first=Harold Maile |year=1942 |title=Differential and Integral Calculus |publisher=McGraw-Hill |page=203 |url=https://books.google.com/books?id=3shEAAAAIAAJ }}</ref> Following this recommendation, the [[ISO 80000-2]] standard abbreviations use the prefix ''ar-'' (that is: {{math|arsinh}}, {{math|arcosh}}, {{math|artanh}}, {{math|arsech}}, {{math|arcsch}}, {{math|arcoth}}).

In computer programming languages, inverse circular and hyperbolic functions are often named with the shorter prefix ''a-'' ({{code|asinh}}, etc.).

This article will consistently adopt the prefix ''ar-'' for convenience.

==Definitions in terms of logarithms==

Since the [[hyperbolic functions]] are quadratic [[rational function]]s of the exponential function <math>\exp x,</math> they may be solved using the [[quadratic formula]] and then written in terms of the [[natural logarithm]].

<math display=block>\begin{align}
\operatorname{arsinh} x &= \ln \left(x + \sqrt{x^2 + 1}\right)               & -\infty &< x < \infty, \\[10mu]
\operatorname{arcosh} x &= \ln \left(x + \sqrt{x^2 - 1}\right)               & 1 &\leq x < \infty, \\[10mu]
\operatorname{artanh} x &= \frac12\ln\frac{1+x}{1-x}                         & -1 &< x < 1, \\[10mu]
\operatorname{arcsch} x &= \ln \left(\frac1x + \sqrt{\frac1{x^2} + 1}\right) & -\infty &< x < \infty, \ x \neq 0, \\[10mu]
\operatorname{arsech} x &= \ln \left(\frac1x + \sqrt{\frac1{x^2} - 1}\right) & 0 &< x \leq 1, \\[10mu]
\operatorname{arcoth} x &= \frac12\ln\frac{x+1}{x-1}                         & -\infty &< x < -1\ \ \text{or}\ \ 1 < x < \infty.
\end{align}</math>

For [[complex number|complex]] arguments, the inverse circular and hyperbolic functions, the [[square root]], and the natural logarithm are all [[multi-valued function]]s.

==Addition formulae==

<!-- are these valid for the complex arguments??-->

<math display=block>\operatorname{arsinh} u \pm \operatorname{arsinh} v = \operatorname{arsinh} \left(u \sqrt{1 + v^2} \pm v \sqrt{1 + u^2}\right)</math>
<math display=block>\operatorname{arcosh} u \pm \operatorname{arcosh} v = \operatorname{arcosh} \left(u v \pm \sqrt{(u^2 - 1) (v^2 - 1)}\right)</math>
<math display=block>\operatorname{artanh} u \pm \operatorname{artanh} v = \operatorname{artanh} \left( \frac{u \pm v}{1 \pm uv} \right)</math>
<math display=block>\operatorname{arcoth} u \pm \operatorname{arcoth} v = \operatorname{arcoth} \left( \frac{1 \pm uv}{u \pm v} \right)</math>
<math display=block>\begin{align}\operatorname{arsinh} u + \operatorname{arcosh} v & = \operatorname{arsinh} \left(u v + \sqrt{(1 + u^2) (v^2 - 1)}\right) \\
                                                                      & = \operatorname{arcosh} \left(v \sqrt{1 + u^2} + u \sqrt{v^2 - 1}\right) \end{align}</math>

==Other identities==

<!-- are these valid for the complex arguments??-->

<math display=block>
\begin{align}
2\operatorname{arcosh}x&=\operatorname{arcosh}(2x^2-1)      &\quad \hbox{ for }x\geq 1 \\
4\operatorname{arcosh}x&=\operatorname{arcosh}(8x^4-8x^2+1) &\quad \hbox{ for }x\geq 1 \\
2\operatorname{arsinh}x&=\pm\operatorname{arcosh}(2x^2+1) \\
4\operatorname{arsinh}x&=\operatorname{arcosh}(8x^4+8x^2+1) &\quad \hbox{ for }x\geq 0
\end{align}
</math>

<math display=block>
\ln(x) = \operatorname{arcosh} \left( \frac{x^2 + 1}{2x}\right)  = \operatorname{arsinh} \left( \frac{x^2 - 1}{2x}\right)
= \operatorname{artanh} \left( \frac{x^2 - 1}{x^2 + 1}\right)
</math>

==Composition of hyperbolic and inverse hyperbolic functions==

<!-- are these valid for the complex arguments??-->

<math display=block>\begin{align}
 &\sinh(\operatorname{arcosh}x) = \sqrt{x^{2} - 1}  \quad \text{for} \quad |x| > 1 \\
 &\sinh(\operatorname{artanh}x) = \frac{x}{\sqrt{1-x^{2}}} \quad \text{for} \quad -1 < x < 1 \\
 &\cosh(\operatorname{arsinh}x) = \sqrt{1+x^{2}} \\
 &\cosh(\operatorname{artanh}x) = \frac{1}{\sqrt{1-x^{2}}} \quad \text{for} \quad -1 < x < 1 \\
 &\tanh(\operatorname{arsinh}x) = \frac{x}{\sqrt{1+x^{2}}} \\
 &\tanh(\operatorname{arcosh}x) = \frac{\sqrt{x^{2} - 1}}{x} \quad \text{for} \quad |x| > 1
\end{align}</math>

==Composition of inverse hyperbolic and circular functions==

<math display=block>
  \operatorname{arsinh} \left( \tan  \alpha \right)
= \operatorname{artanh} \left( \sin  \alpha  \right)
= \ln\left( \frac{ 1 + \sin  \alpha }{ \cos  \alpha } \right)
= \pm \operatorname{arcosh} \left( \frac {1} {\cos \alpha  }\right)
</math>

<div style="display:block; margin-left:1.6em;">
<math>
  \ln \left( \left| \tan  \alpha \right|\right)
= -\operatorname{artanh} \left( \cos  2 \alpha  \right)
</math><ref>{{cite web|title=Identities with inverse hyperbolic and trigonometric functions|url=https://math.stackexchange.com/q/1878399 |website=math stackexchange|publisher=[[stackexchange]]|access-date=3 November 2016}}{{User-generated source|date=October 2025}}</ref>
</div>

==Conversions==

<math display=block>
  \ln x = \operatorname{artanh} \left( \frac{x^2-1}{x^2+1}\right)
= \operatorname{arsinh} \left( \frac{x^2-1}{2 x}\right)
= \pm \operatorname{arcosh} \left( \frac{x^2+1}{2 x}\right)
</math>

<math display=block>
  \operatorname{artanh} x
= \operatorname{arsinh} \left( \frac{x}{\sqrt{1-x^2}}\right)
= \pm \operatorname{arcosh} \left( \frac{1}{\sqrt{1-x^2}}\right)
</math>

<math display=block>
  \operatorname{arsinh} x
= \operatorname{artanh} \left( \frac{x}{\sqrt{1+x^2}}\right)
= \pm \operatorname{arcosh} \left( \sqrt{1+x^2}\right)
</math>

<math display=block>
  \operatorname{arcosh} x
= \left| \operatorname{arsinh} \left( \sqrt{x^2-1}\right) \right|
=  \left| \operatorname{artanh} \left(  \frac{\sqrt{x^2-1}}{x}
\right) \right|
</math>

==Derivatives==

<math display=block>
\begin{align}
\frac{d}{dx} \operatorname{arsinh} x & {}= \frac{1}{\sqrt{x^2+1}}, \text{ for all real } x\\
\frac{d}{dx} \operatorname{arcosh} x & {}= \frac{1}{\sqrt{x^2-1}}, \text{ for all real } x>1\\
\frac{d}{dx} \operatorname{artanh} x & {}= \frac{1}{1-x^2}, \text{ for all real } |x|<1\\
\frac{d}{dx} \operatorname{arcoth} x & {}= \frac{1}{1-x^2}, \text{ for all real } |x|>1\\
\frac{d}{dx} \operatorname{arsech} x & {}= \frac{-1}{x\sqrt{1-x^2}}, \text{ for all real } x \in (0,1)\\
\frac{d}{dx} \operatorname{arcsch} x & {}= \frac{-1}{|x|\sqrt{1+x^2}}, \text{ for all real } x\text{, except } 0\\
\end{align}</math>

These formulas can be derived in terms of the derivatives of hyperbolic functions. For example, if <math>x = \sinh \theta</math>, then <math display=inline>dx/d\theta = \cosh \theta = \sqrt{1+x^2},</math> so
<math display=block>\frac{d}{dx}\operatorname{arsinh}(x) = \frac{d \theta}{dx} = \frac{1}{dx/d\theta} = \frac{1}{\sqrt{1+x^2}}.</math>

==Series expansions==

Expansion series can be obtained for the above functions:

<math display=block>\begin{align}\operatorname{arsinh} x & = x - \left( \frac {1} {2} \right) \frac {x^3} {3} + \left( \frac {1 \cdot 3} {2 \cdot 4} \right) \frac {x^5} {5} - \left( \frac {1 \cdot 3 \cdot 5} {2 \cdot 4 \cdot 6} \right) \frac {x^7} {7} \pm\cdots \\
                       & = \sum_{n=0}^\infty \left( \frac {(-1)^n(2n)!} {2^{2n}(n!)^2} \right) \frac {x^{2n+1}} {2n+1} , \qquad \left| x \right| < 1  \end{align} </math>

<math display=block>\begin{align}\operatorname{arcosh} x & = \ln(2x) - \left( \left( \frac {1} {2} \right) \frac {x^{-2}} {2} + \left( \frac {1 \cdot 3} {2 \cdot 4} \right) \frac {x^{-4}} {4} + \left( \frac {1 \cdot 3 \cdot 5} {2 \cdot 4 \cdot 6} \right) \frac {x^{-6}} {6} +\cdots \right) \\
                      & = \ln(2x) - \sum_{n=1}^\infty \left( \frac {(2n)!} {2^{2n}(n!)^2} \right) \frac {x^{-2n}} {2n} , \qquad \left| x \right| > 1 \end{align} </math>

<math display=block>\begin{align}\operatorname{artanh} x & = x + \frac {x^3} {3} + \frac {x^5} {5} + \frac {x^7} {7} +\cdots \\
                      & = \sum_{n=0}^\infty \frac {x^{2n+1}} {2n+1} , \qquad \left| x \right| < 1 \end{align} </math>

<math display=block>\begin{align}\operatorname{arcsch} x = \operatorname{arsinh} \frac1x & = x^{-1} - \left( \frac {1} {2} \right) \frac {x^{-3}} {3} + \left( \frac {1 \cdot 3} {2 \cdot 4} \right) \frac {x^{-5}} {5} - \left( \frac {1 \cdot 3 \cdot 5} {2 \cdot 4 \cdot 6} \right) \frac {x^{-7}} {7} \pm\cdots \\
                      & = \sum_{n=0}^\infty \left( \frac {(-1)^n(2n)!} {2^{2n}(n!)^2} \right) \frac {x^{-(2n+1)}} {2n+1} , \qquad \left| x \right| > 1 \end{align} </math>

<math display=block>\begin{align}\operatorname{arsech} x = \operatorname{arcosh} \frac1x & = \ln \frac{2}{x} - \left( \left( \frac {1} {2} \right) \frac {x^{2}} {2} + \left( \frac {1 \cdot 3} {2 \cdot 4} \right) \frac {x^{4}} {4} + \left( \frac {1 \cdot 3 \cdot 5} {2 \cdot 4 \cdot 6} \right) \frac {x^{6}} {6} +\cdots \right) \\
                      & = \ln \frac{2}{x} - \sum_{n=1}^\infty \left( \frac {(2n)!} {2^{2n}(n!)^2} \right) \frac {x^{2n}} {2n} , \qquad 0 < x \le 1 \end{align} </math>

<math display=block>\begin{align}\operatorname{arcoth} x = \operatorname{artanh} \frac1x & = x^{-1} + \frac {x^{-3}} {3} + \frac {x^{-5}} {5} + \frac {x^{-7}} {7} +\cdots \\
                      & = \sum_{n=0}^\infty \frac {x^{-(2n+1)}} {2n+1} , \qquad \left| x \right| > 1 \end{align} </math>
An [[asymptotic expansion]] for arsinh is given by

<math display=block>\operatorname{arsinh} x = \ln(2x) + \sum\limits_{n = 1}^\infty  {\left( { - 1} \right)^{n - 1} \frac{{\left( {2n - 1} \right)!!}}{{2n\left( {2n} \right)!!}}} \frac{1}{{x^{2n} }}</math>

<!--- planning to simplify old version of this section -->

==Principal values in the complex plane==

As [[functions of a complex variable]], inverse hyperbolic functions are [[multivalued function]]s that are [[analytic function|analytic]] except at a finite number of points. For such a function, it is common to define a [[principal value]], which is a single valued analytic function which coincides with one specific branch of the multivalued function, over a domain consisting of the [[complex plane]] in which a finite number of [[arc (geometry)|arcs]] (usually [[half line]]s or [[line segment]]s) have been removed. These arcs are called [[branch cut]]s. The principal value of the multifunction is chosen at a particular point and values elsewhere in the domain of definition are defined to agree with those found by [[analytic continuation]].

For example, for the square root, the principal value is defined as the square root that has a positive [[real part]]. This defines a single valued analytic function, which is defined everywhere, except for non-positive real values of the variables (where the two square roots have a zero real part). This principal value of the square root function is denoted <math>\sqrt x</math> in what follows. Similarly, the principal value of the logarithm, denoted <math>\operatorname{Log}</math> in what follows, is defined as the value for which the [[imaginary part]] has the smallest absolute value. It is defined everywhere except for non-positive real values of the variable, for which two different values of the logarithm reach the minimum.

For all inverse hyperbolic functions, the principal value may be defined in terms of principal values of the square root and the logarithm function. However, in some cases, the formulas of {{section link||Definitions in terms of logarithms}} do not give a correct principal value, as giving a domain of definition which is too small and, in one case [[connected space|non-connected]].

===Principal value of the inverse hyperbolic sine===

The principal value of the inverse hyperbolic sine is given by
<math display=block>\operatorname{arsinh} z = \operatorname{Log}(z + \sqrt{z^2 + 1} \,)\,.</math>

The argument of the square root is a non-positive [[real number]], [[if and only if]] {{math|''z''}} belongs to one of the intervals {{math|[''i'', +''i''∞)}} and {{math|(−''i''∞, −''i'']}} of the imaginary axis. If the argument of the logarithm is real, then it is positive. Thus this formula defines a principal value for arsinh, with branch cuts {{math|[''i'', +''i''∞)}} and {{math|(−''i''∞, −''i'']}}. This is optimal, as the branch cuts must connect the singular points {{math|''i''}} and {{math|−''i''}} to infinity.

===Principal value of the inverse hyperbolic cosine===
The formula for the inverse hyperbolic cosine given in {{section link||Inverse hyperbolic cosine}} is not convenient, since similar to the principal values of the logarithm and the square root, the principal value of arcosh would not be defined for imaginary {{math|''z''}}. Thus the square root has to be factorized, leading to
<math display=block>\operatorname{arcosh}  z = \operatorname{Log}(z + \sqrt{z+1} \sqrt{z-1} \,)\,.</math>

The principal values of the square roots are both defined, except if {{math|''z''}} belongs to the real interval {{math|(−∞, 1]}}. If the argument of the logarithm is real, then {{math|''z''}} is real and has the same sign. Thus, the above formula defines a principal value of arcosh outside the real interval {{math|(−∞, 1]}}, which is thus the unique branch cut.

===Principal values of the inverse hyperbolic tangent and cotangent===

The formulas given in {{section link||Definitions in terms of logarithms}} suggests
<math display=block>
\begin{align}
\operatorname{artanh} z  &=\frac12\operatorname{Log}\left(\frac{1+z}{1-z}\right)
    \\
 \operatorname{arcoth} z &=  \frac12\operatorname{Log}\left(\frac{z+1}{z-1}\right)
  \end{align}
</math>
for the definition of the principal values of the inverse hyperbolic tangent and cotangent. In these formulas, the argument of the logarithm is real if and only if {{math|''z''}} is real. For artanh, this argument is in the real interval {{math|(−∞, 0]}}, if {{math|''z''}} belongs either to {{math|(−∞, −1]}} or to {{math|[1, ∞)}}. For arcoth, the argument of the logarithm is in {{math|(−∞, 0]}}, if and only if {{math|''z''}} belongs to the real interval {{math|[−1, 1]}}.

Therefore, these formulas define convenient principal values, for which the branch cuts are {{math|(−∞, −1]}} and {{math|[1, ∞)}} for the inverse hyperbolic tangent, and {{math|[−1, 1]}} for the inverse hyperbolic cotangent.

In view of a better numerical evaluation near the branch cuts, some authors{{citation needed|date=December 2015}} use the following definitions of the principal values, although the second one introduces a [[removable singularity]] at {{math|1=''z'' = 0}}. The two definitions of <math> \operatorname {artanh} </math> differ for real values of {{mvar|z}} with {{math|1=''z'' > 1}}. The ones of <math> \operatorname {arcoth} </math> differ for real values of {{mvar|z}} with {{math|1=''z'' ∈ [0, 1)}}.
<math display=block>
  \begin{align}
    \operatorname{artanh} z &= \tfrac12\operatorname{Log}\left({1+z}\right) -  \tfrac12\operatorname{Log}\left({1-z}\right)
    \\
    \operatorname{arcoth} z &= \tfrac12\operatorname{Log}\left({1+\frac{1}{z} }\right) -   \tfrac12\operatorname{Log}\left({1-\frac{1}{z}}\right)
 \end{align}
</math>

===Principal value of the inverse hyperbolic cosecant===

For the inverse hyperbolic cosecant, the principal value is defined as
<math display=block>\operatorname{arcsch} z = \operatorname{Log}\left( \frac{1}{z} + \sqrt{ \frac{1}{z^2} +1 } \,\right).</math>

It is defined except when the arguments of the logarithm and the square root are non-positive real numbers. The principal value of the square root is thus defined outside the interval {{math|[−''i'', ''i'']}} of the imaginary line. If the argument of the logarithm is real, then {{math|''z''}} is a non-zero real number, and this implies that the argument of the logarithm is positive.

Thus, the principal value is defined by the above formula outside the [[branch cut]], consisting of the interval {{math|[−''i'', ''i'']}} of the imaginary line.

(At {{math|1=''z'' = 0}}, there is a singular point that is included in the branch cut.)

===Principal value of the inverse hyperbolic secant===

Here, as in the case of the inverse hyperbolic cosine, we have to factorize the square root. This gives the principal value
<math display=block>
    \operatorname{arsech} z = \operatorname{Log}\left( \frac{1}{z} + \sqrt{ \frac{1}{z} + 1 } \, \sqrt{ \frac{1}{z} -1 } \right).
</math>

If the argument of a square root is real, then {{math|''z''}} is real, and it follows that both principal values of square roots are defined, except if {{math|''z''}} is real and belongs to one of the intervals {{math|(−∞, 0]}} and {{math|[1, +∞)}}. If the argument of the logarithm is real and negative, then {{math|''z''}} is also real and negative. It follows that the principal value of arsech is well defined, by the above formula outside two [[branch cut]]s, the real intervals {{math|(−∞, 0]}} and {{math|[1, +∞)}}.

For {{math|1=''z'' = 0}}, there is a singular point that is included in one of the branch cuts.

===Graphical representation===

In the following graphical representation of the principal values of the inverse hyperbolic functions, the branch cuts appear as discontinuities of the color. The fact that the whole branch cuts appear as discontinuities, shows that these principal values may not be extended into analytic functions defined over larger domains. In other words, the above defined [[branch cut]]s are minimal.

{{multiple image
 | perrow = 3
 | align = center
 | width = 200
 | footer = Inverse hyperbolic functions in the complex {{mvar|z}}-plane: the colour at each point in the plane [[domain coloring|represents the complex value]] of the respective function at that point
 | image1 = Complex ArcSinh.jpg
 | image2 = Complex ArcCosh.jpg
 | image3 = Complex ArcTanh.jpg
 | image4 = Complex ArcCoth.jpg
 | image5 = Complex ArcSech.jpg
 | image6 = Complex ArcCsch.jpg
 | alt1 = Square representing central portion of the complex z-plane painted in psychedelic colours
 | alt2 = Square representing central portion of the complex z-plane painted in psychedelic colours
 | alt3 = Square representing central portion of the complex z-plane painted in psychedelic colours
 | alt4 = Square representing central portion of the complex z-plane painted in psychedelic colours
 | alt5 = Square representing central portion of the complex z-plane painted in psychedelic colours
 | alt6 = Square representing central portion of the complex z-plane painted in psychedelic colours
 | caption1 = {{math|arsinh(''z'')}}
 | caption2 = {{math|arcosh(''z'')}}
 | caption3 = {{math|artanh(''z'')}}
 | caption4 = {{math|arcoth(''z'')}}
 | caption5 = {{math|arsech(''z'')}}
 | caption6 = {{math|arcsch(''z'')}}
 }}

==See also==
*[[Complex logarithm]]
*[[Hyperbolic secant distribution]]
*[[ISO 80000-2]]
*[[List of integrals of inverse hyperbolic functions]]

==References==
{{reflist|25em}}

== Bibliography ==
* [[Herbert Busemann]] and Paul J. Kelly (1953) ''Projective Geometry and Projective Metrics'', page 207, [[Academic Press]].

==External links==
* {{springer|title=Inverse hyperbolic functions|id=p/i052370}}

{{Trigonometric and hyperbolic functions}}

[[Category:Inverse hyperbolic functions| ]]
