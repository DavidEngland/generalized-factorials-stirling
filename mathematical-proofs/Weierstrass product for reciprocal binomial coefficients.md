# Weierstrass Product for the Product of Reciprocal Factorials and Binomial Coefficients

## Abstract

We investigate the analytic properties of $\frac{1}{s!} \cdot \frac{1}{(s-t)!}$ and its relation to binomial coefficients $\binom{s}{t}$. Using the Weierstrass factorization theorem, we derive infinite product representations and analyze the pole structure of these functions. We also examine the partial derivatives with respect to parameters $s$ and $t$, revealing elegant connections to the digamma function that emerge when considering logarithmic derivatives.

## Introduction

The functions $\frac{1}{s!} \cdot \frac{1}{(s-t)!}$ and $\frac{s!}{t!(s-t)!} = \binom{s}{t}$ can be expressed in terms of gamma functions, allowing for analytic continuation to the complex plane. By determining their zeros and poles and deriving Weierstrass products, we gain insight into their analytic structure and relationships to special functions.

## Zero Structure of Reciprocal Factorials Product

To identify the zeros of $\frac{1}{s!} \cdot \frac{1}{(s-t)!}$, we examine each component separately:

1. $\frac{1}{\Gamma(s+1)}$ has simple zeros at $s = -n$ for all integers $n \geq 1$
2. $\frac{1}{\Gamma(s-t+1)}$ has simple zeros at $s = t-m$ for all integers $m \geq 1$

Therefore, $\frac{1}{s!} \cdot \frac{1}{(s-t)!}$ has simple zeros at:
- $s = -n$ for all integers $n \geq 1$
- $s = t-m$ for all integers $m \geq 1$

## Pole Structure of Binomial Coefficients

For the binomial coefficient $\binom{s}{t} = \frac{\Gamma(s+1)}{\Gamma(t+1)\Gamma(s-t+1)}$, the poles occur where the denominator has zeros that are not canceled by zeros in the numerator:

1. $\Gamma(t+1)$ has poles at $t = -k$ for integers $k \geq 1$
2. $\Gamma(s-t+1)$ has poles at $s-t = -l$ for integers $l \geq 1$, or equivalently, at $s = t-l$

However, the numerator $\Gamma(s+1)$ has poles at $s = -n$ for integers $n \geq 1$, which may cancel some poles in the denominator.

A careful analysis shows that $\binom{s}{t}$ has poles when:
- $t = -k$ for integers $k \geq 1$, except when $s$ is also a negative integer with $s \leq -k$
- $s = t-l$ for integers $l \geq 1$, except when $s$ is a negative integer

This complex pole structure highlights the rich analytic behavior of the binomial coefficient in the complex plane.

## Weierstrass Product Representation

Using the Weierstrass factorization theorem and the known product for reciprocal gamma functions, we can express the reciprocal factorial product as:

$$\frac{1}{s!} \cdot \frac{1}{(s-t)!} = \frac{1}{\Gamma(s+1)} \cdot \frac{1}{\Gamma(s-t+1)}$$

$$= e^{\gamma s} \prod_{n=1}^{\infty} \left(1+\frac{s}{n}\right) e^{-s/n} \cdot e^{\gamma (s-t)} \prod_{m=1}^{\infty} \left(1+\frac{s-t}{m}\right) e^{-(s-t)/m}$$

Simplifying:

$$\frac{1}{s!} \cdot \frac{1}{(s-t)!} = e^{\gamma(2s-t)} \prod_{n=1}^{\infty} \left(\frac{n+s}{n}\right) e^{-s/n} \prod_{m=1}^{\infty} \left(\frac{m+s-t}{m}\right) e^{-(s-t)/m}$$

This product clearly displays the zeros at $s = -n$ and $s = t-m$, confirming our earlier analysis.

## Partial Derivatives and Digamma Functions

### Derivatives of Reciprocal Factorial Product

The partial derivatives of this function with respect to parameters $s$ and $t$ reveal interesting connections to the digamma function $\psi(z) = \frac{d}{dz}\ln\Gamma(z)$.

For the derivative with respect to $s$:

$$\frac{\partial}{\partial s}\left(\frac{1}{s!} \cdot \frac{1}{(s-t)!}\right) = -[\psi(s+1) + \psi(s-t+1)]\frac{1}{s!}\frac{1}{(s-t)!}$$

For the derivative with respect to $t$:

$$\frac{\partial}{\partial t}\left(\frac{1}{s!} \cdot \frac{1}{(s-t)!}\right) = \psi(s-t+1)\frac{1}{s!}\frac{1}{(s-t)!}$$

### Derivatives of Binomial Coefficients

For the binomial coefficient $\binom{s}{t}$, the partial derivatives can be expressed as:

$$\frac{\partial}{\partial s}\binom{s}{t} = \binom{s}{t}[\psi(s+1) - \psi(s-t+1)]$$

$$\frac{\partial}{\partial t}\binom{s}{t} = \binom{s}{t}[\psi(s-t+1) - \psi(t+1)]$$

### Logarithmic Derivatives

The most elegant formulations emerge when considering the logarithmic derivatives:

$$\frac{\partial}{\partial s}\log\binom{s}{t} = \psi(s+1) - \psi(s-t+1)$$

$$\frac{\partial}{\partial t}\log\binom{s}{t} = \psi(s-t+1) - \psi(t+1)$$

These results directly relate the logarithmic derivatives of binomial coefficients to differences of digamma functions, providing a clean analytical expression that highlights the special nature of binomial coefficients in the theory of special functions.

## Connection between Products and Coefficients

The reciprocal factorial product and binomial coefficient are related by:

$$\frac{1}{s!} \cdot \frac{1}{(s-t)!} = \frac{1}{t!}\binom{s}{t}^{-1}$$

This relationship provides a path to derive the Weierstrass product for the reciprocal binomial coefficient:

$$\frac{1}{\binom{s}{t}} = \frac{t!}{s!}\frac{1}{(s-t)!} = t! \cdot e^{\gamma(2s-t)} \prod_{n=1}^{\infty} \left(\frac{n+s}{n}\right) e^{-s/n} \prod_{m=1}^{\infty} \left(\frac{m+s-t}{m}\right) e^{-(s-t)/m}$$

Further manipulation allows us to express this in terms of the zeros and poles of the reciprocal binomial coefficient, providing a complete characterization of its analytic structure.

## Applications and Extensions

These Weierstrass product representations and differential properties have applications in:

1. Complex analysis of hypergeometric functions
2. Asymptotic analysis of binomial coefficients
3. Generalized binomial series and their convergence properties
4. Combinatorial identities and generating functions

A natural extension is to consider generalized factorials and the corresponding Weierstrass products for $r$-Stirling numbers, which appear in combinatorial contexts as noted by Broder \cite{MR743795} and others.

## Conclusion

We have derived the Weierstrass product representations for $\frac{1}{s!} \cdot \frac{1}{(s-t)!}$ and related functions, while analyzing their analytic properties. The logarithmic derivatives with respect to $s$ and $t$ reveal elegant formulas involving differences of digamma functions, providing a beautiful connection between these special functions and combinatorial structures.

## References

1. Artin, E. The Gamma Function. Holt, Rinehart and Winston.
2. Whittaker, E. T., and Watson, G. N. A Course of Modern Analysis. Cambridge University Press.
3. Andrews, G. E., Askey, R., and Roy, R. Special Functions. Cambridge University Press.
4. \bibitem{MR743795} A.~Z. Broder. The {$r$}-{S}tirling numbers. {\em Discrete Math.}, 49(3):241--259, 1984.
