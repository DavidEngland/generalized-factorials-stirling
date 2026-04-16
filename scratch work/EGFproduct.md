# Logarithmic Derivatives of Exponential Generating Functions

This note began with the product of two exponential generating functions, but the more useful organizing theme is narrower and cleaner: how EGF products interact with differentiation, and how this leads naturally to logarithmic derivatives, formal logarithms, Bell-polynomial coefficient formulas, and the first polylogarithm.

The point of view throughout is this:

$$
f(x)g(x)=f'(x)
\qquad \Longleftrightarrow \qquad
g(x)=\frac{f'(x)}{f(x)}=(\operatorname{Log} f(x))'.
$$

That single identity connects binomial convolution, coefficient recurrences, function composition, and polylogarithmic expansions.

## Scope and Notation

We work with exponential generating functions of the form

$$
f(x)=\sum_{m\ge 0} a_m\frac{x^m}{m!},
\qquad
g(x)=\sum_{m\ge 0} b_m\frac{x^m}{m!},
\qquad
h(x)=\sum_{m\ge 0} c_m\frac{x^m}{m!}.
$$

All identities may be read in either of two ways:

- As formal power-series identities.
- As analytic identities in a neighborhood of $x=0$ when the series converge.

For notation, it is often convenient to use Greek letters for OGF coefficient sequences, such as $\alpha_m,\beta_m,\gamma_m$, and Latin letters for EGF coefficient sequences, such as $a_m,b_m,c_m$.

When $a_0=f(0)=1$, the formal logarithm $\operatorname{Log} f(x)$ is well defined as a power series.

## 1. Product Rules for OGFs and EGFs

For ordinary generating functions,

$$
F(x)=\sum_{m\ge 0} \alpha_m x^m,
\qquad
G(x)=\sum_{m\ge 0} \beta_m x^m,
\qquad
H(x)=F(x)G(x)=\sum_{m\ge 0} \gamma_m x^m,
$$

the coefficients satisfy the Cauchy product formula

$$
\gamma_m=\sum_{n=0}^m \alpha_n \beta_{m-n}.
$$

A particularly useful special case is multiplication by

$$
\frac{1}{1-x}=\sum_{m\ge 0} x^m.
$$

If

$$
F(x)=\sum_{m\ge 0} \alpha_m x^m,
$$

then

$$
\frac{F(x)}{1-x}=\sum_{m\ge 0}\left(\sum_{k=0}^m \alpha_k\right)x^m.
$$

So multiplying an OGF by $1/(1-x)$ replaces the coefficient sequence by its sequence of partial sums:

$$
(\alpha_0,\alpha_1,\alpha_2,\ldots)
\mapsto
\left(\alpha_0,\,\alpha_0+\alpha_1,\,\alpha_0+\alpha_1+\alpha_2,\ldots\right).
$$

The same phenomenon appears at infinity. For $|x|>1$ one has

$$
\frac{1}{x-1}=\frac{1}{x}\frac{1}{1-1/x}=\sum_{m\ge 1}\frac{1}{x^m}.
$$

If

$$
F(t)=\sum_{m\ge 0} \alpha_m t^m,
$$

then

$$
F\!\left(\frac{1}{x}\right)=\sum_{m\ge 0}\frac{\alpha_m}{x^m},
$$

and therefore

$$
\frac{F(1/x)}{x-1} =
\left(\sum_{m\ge 0}\frac{\alpha_m}{x^m}\right)
\left(\sum_{j\ge 1}\frac{1}{x^j}\right) =
\sum_{n\ge 1}\frac{1}{x^n}\sum_{k=0}^{n-1}\alpha_k.
$$

So the coefficient of $x^{-n}$ is again a partial sum, now taken from the beginning of the OGF coefficient sequence:

$$
\left[x^{-n}\right]\frac{F(1/x)}{x-1}=\sum_{k=0}^{n-1}\alpha_k,
\qquad n\ge 1.
$$

Equivalently,

$$
\frac{F(1/x)}{x-1} =
\frac{\alpha_0}{x}
+\frac{\alpha_0+\alpha_1}{x^2}
+\frac{\alpha_0+\alpha_1+\alpha_2}{x^3}
+\cdots.
$$

If the special case $\alpha_0=0$ holds, then the leading $x^{-1}$ term vanishes and the expansion begins one order later:

$$
\frac{F(1/x)}{x-1} =
\frac{\alpha_1}{x^2}
+\frac{\alpha_1+\alpha_2}{x^3}
+\frac{\alpha_1+\alpha_2+\alpha_3}{x^4}
+\cdots,
$$

so in particular

$$
\alpha_0=0
\qquad \Longrightarrow \qquad
\frac{F(1/x)}{x-1}=O\!\left(\frac{1}{x^2}\right)
\quad (x\to\infty).
$$

This may be read either as a convergent Laurent expansion for $|x|>1$ when $F$ is analytic at the origin, or more generally as an asymptotic expansion at infinity:

$$
F\!\left(\frac{1}{x}\right)\sim\sum_{m\ge 0}\frac{\alpha_m}{x^m}
\quad \Longrightarrow \quad
\frac{F(1/x)}{x-1}\sim\sum_{n\ge 1}\frac{1}{x^n}\sum_{k=0}^{n-1}\alpha_k
\qquad (x\to\infty).
$$

So yes: the same coefficient-summing rule can be cast naturally as an asymptotic expansion statement.

For exponential generating functions,

$$
h(x)=f(x)g(x),
$$

the factorial normalization introduces binomial coefficients:

$$
c_m=\sum_{n=0}^m \binom{m}{n} a_n b_{m-n}.
$$

This is the basic EGF product rule. It is the analogue of ordinary convolution, but weighted by the combinatorial factor

$$
\binom{m}{n}=\frac{m!}{n!(m-n)!}.
$$

Equivalently,

$$
c_m=\sum_{n=0}^m \binom{m}{m-n} a_{m-n} b_n.
$$

## 2. Differentiation of an EGF

If

$$
f(x)=\sum_{m\ge 0} a_m\frac{x^m}{m!},
$$

then termwise differentiation gives

$$
f'(x)=\sum_{m\ge 0} a_{m+1}\frac{x^m}{m!}.
$$

More generally, repeated differentiation shifts by $k$ places:

$$
f^{(k)}(x)=\sum_{m\ge 0} a_{m+k}\frac{x^m}{m!},
\qquad k\ge 0.
$$

So the $k$-th derivative of an EGF is again an EGF, now with coefficient sequence

$$
(a_k,a_{k+1},a_{k+2},\ldots).
$$

Thus differentiation shifts the coefficient sequence to the left:

$$
(a_0,a_1,a_2,a_3,\ldots)
\mapsto
(a_1,a_2,a_3,a_4,\ldots).
$$

This shift is one of the main reasons EGFs are convenient in differential and recursive settings.

## 3. Solving $f g = f'$

Suppose

$$
f(x)=\sum_{m\ge 0} a_m\frac{x^m}{m!},
\qquad
g(x)=\sum_{m\ge 0} b_m\frac{x^m}{m!},
$$

and assume

$$
f(x)g(x)=f'(x).
$$

The coefficient sequence of $f'(x)$ is $a_{m+1}$, so the EGF product rule yields

$$
\sum_{n=0}^m \binom{m}{n} a_n b_{m-n}=a_{m+1},
\qquad m\ge 0.
$$

If $a_0\neq 0$, this determines $b_m$ recursively:

$$
b_m=\frac{1}{a_0}\left(a_{m+1}-\sum_{n=1}^m \binom{m}{n} a_n b_{m-n}\right),
\qquad m\ge 0.
$$

The first few values are

$$
b_0=\frac{a_1}{a_0},
$$

$$
b_1=\frac{a_2-a_1 b_0}{a_0},
$$

$$
b_2=\frac{a_3-2a_1 b_1-a_2 b_0}{a_0},
$$

$$
b_3=\frac{a_4-3a_1 b_2-3a_2 b_1-a_3 b_0}{a_0}.
$$

Formally this is just the logarithmic derivative:

$$
g(x)=\frac{f'(x)}{f(x)}=(\operatorname{Log} f(x))'.
$$

## 4. Normalized Case: $f(0)=1$

When $a_0=1$, the formulas simplify substantially. The recurrence becomes

$$
b_m=a_{m+1}-\sum_{n=1}^m \binom{m}{n} a_n b_{m-n},
\qquad m\ge 0.
$$

The first logarithmic-derivative coefficients are then

$$
b_0=a_1,
$$

$$
b_1=a_2-a_1^2,
$$

$$
b_2=a_3-3a_1a_2+2a_1^3,
$$

$$
b_3=a_4-4a_1a_3-3a_2^2+12a_1^2a_2-6a_1^4.
$$

These are the EGF analogues of the standard polynomial relations between a function and the coefficients of its logarithmic derivative.

## 5. Expanding $\operatorname{Log} f(x)$

Write

$$
f(x)=1+u(x),
\qquad
u(x)=\sum_{m\ge 1} a_m\frac{x^m}{m!}.
$$

Then the formal logarithm is

$$
\operatorname{Log} f(x)=\operatorname{Log}(1+u(x))
=\sum_{k\ge 1} (-1)^{k+1}\frac{u(x)^k}{k}.
$$

If

$$
\operatorname{Log} f(x)=\sum_{m\ge 1} \lambda_m\frac{x^m}{m!},
$$

then

$$
g(x)=(\operatorname{Log} f(x))'=
\sum_{m\ge 0} \lambda_{m+1}\frac{x^m}{m!},
$$

so

$$
b_m=\lambda_{m+1}.
$$

This gives a second route to the same coefficients: first expand $\operatorname{Log} f$, then differentiate.

## 6. Bell-Polynomial Formula

The clean closed form comes from exponential Bell polynomials. If

$$
\frac{u(x)^k}{k!} = \sum_{n\ge k} B_{n,k}(a_1,a_2,\ldots)\frac{x^n}{n!},
$$

then substituting into the logarithm series gives

$$
\operatorname{Log} f(x) =
\sum_{k\ge 1} (-1)^{k+1}(k-1)!
\sum_{n\ge k} B_{n,k}(a_1,a_2,\ldots)\frac{x^n}{n!}.
$$

Hence

$$
\lambda_n =
\sum_{k=1}^n (-1)^{k+1}(k-1)!\,B_{n,k}(a_1,a_2,\ldots,a_{n-k+1}),
$$

and therefore

$$
b_m =
\sum_{k=1}^{m+1} (-1)^{k+1}(k-1)!\,B_{m+1,k}(a_1,a_2,\ldots,a_{m-k+2}).
$$

This is often the most compact symbolic formula for the logarithmic-derivative coefficients.

The same Bell-polynomial language gives a convenient formula for higher derivatives whenever

$$
f'(x)=g(x)f(x).
$$

Define the complete exponential Bell polynomial by

$$
Y_m(x_1,\ldots,x_m)=\sum_{n=1}^m B_{m,n}(x_1,\ldots,x_{m-n+1}),
$$

with $Y_0=1$.

### Lemma: higher derivatives when $f'=g f$

If $f$ and $g$ satisfy

$$
f'(x)=g(x)f(x),
$$

then for every $m\ge 0$,

$$
f^{(m)}(x)=f(x)\,Y_m\bigl(g(x),g'(x),\ldots,g^{(m-1)}(x)\bigr).
$$

Equivalently,

$$
f^{(m)}(x)=f(x)\sum_{n=1}^m B_{m,n}\bigl(g(x),g'(x),\ldots,g^{(m-n)}(x)\bigr),
\qquad m\ge 1.
$$

The first cases are

$$
f'=g f,
$$

$$
f''=(g'+g^2)f,
$$

$$
f^{(3)}=(g''+3g g'+g^3)f,
$$

$$
f^{(4)}=(g'''+4g g''+3(g')^2+6g^2 g'+g^4)f.
$$

Proof.
Write $h(x)=\operatorname{Log} f(x)$. Then $h'(x)=g(x)$, so locally

$$
f(x)=e^{h(x)}.
$$

Applying the standard derivative formula for an exponential composite gives

$$
\frac{d^m}{dx^m}e^{h(x)} =
e^{h(x)}\,Y_m\bigl(h'(x),h''(x),\ldots,h^{(m)}(x)\bigr).
$$

Since $h^{(j)}(x)=g^{(j-1)}(x)$ for $j\ge 1$, this becomes exactly

$$
f^{(m)}(x)=f(x)\,Y_m\bigl(g(x),g'(x),\ldots,g^{(m-1)}(x)\bigr).
$$

So the complete Bell polynomial packages all higher derivatives generated by the single first-order relation $f'=g f$.

## 7. Polylogarithm Viewpoint

The first polylogarithm satisfies

$$
\operatorname{Li}_1(z)=\sum_{k\ge 1}\frac{z^k}{k}=-\operatorname{Log}(1-z),
\qquad |z|<1.
$$

Therefore

$$
\operatorname{Log}(1+u)=-\operatorname{Li}_1(-u).
$$

Applied to a normalized EGF,

$$
\operatorname{Log} f(x)=-\operatorname{Li}_1\bigl(-(f(x)-1)\bigr).
$$

As a formal identity this is always valid, because $f(x)-1$ has zero constant term. Analytically it is valid wherever the chosen branch of the logarithm is valid.

Differentiating gives

$$
(\operatorname{Log} f(x))'=-\frac{d}{dx}\operatorname{Li}_1\bigl(-(f(x)-1)\bigr),
$$

and since

$$
\frac{d}{dz}\operatorname{Li}_1(z)=\frac{1}{1-z},
$$

the chain rule recovers

$$
\frac{d}{dx}\operatorname{Log} f(x)=\frac{f'(x)}{f(x)}.
$$

So the polylogarithm viewpoint is not a different theory. It is simply the logarithm series written in the standard special-function language.

## 8. Analytic Continuation of $\operatorname{Li}_1$ and the Region $|z|>1$

For analytic continuation, one keeps the logarithmic form

$$
\operatorname{Li}_1(z) = - \operatorname{Log}(1-z),
$$

where $\operatorname{Log}$ is a chosen branch of the complex logarithm, usually the principal branch. Thus $\operatorname{Li}_1$ has a branch point at $z=1$ and a branch cut usually taken along $[1,\infty)$.

For $|z|>1$, factor

$$
1-z=-z\left(1-\frac{1}{z}\right),
$$

so that

$$
\operatorname{Li}_1(z)=-\operatorname{Log}(-z)-\operatorname{Log}\!\left(1-\frac{1}{z}\right).
$$

Now the second logarithm has a convergent expansion in powers of $1/z$:

$$
-\operatorname{Log}\!\left(1-\frac{1}{z}\right)=\sum_{n\ge 1}\frac{1}{n z^n},
\qquad |z|>1.
$$

Hence the exact large-$z$ expansion is

$$
\operatorname{Li}_1(z)=-\operatorname{Log}(-z)+\sum_{n\ge 1}\frac{1}{n z^n},
\qquad |z|>1,
$$

which is also the asymptotic expansion at infinity.

On the principal branch, for real $x>1$ one has boundary values

$$
\operatorname{Li}_1(x\pm i0)=-\operatorname{Log}(x-1)\mp i\pi.
$$

## 9. Quick Reference

For a normalized EGF

$$
f(x)=1+\sum_{m\ge 1} a_m\frac{x^m}{m!},
\qquad
g(x)=\frac{f'(x)}{f(x)}=\sum_{m\ge 0} b_m\frac{x^m}{m!},
$$

the most useful formulas are:

- Product rule:

$$
[x^m]_{\mathrm{EGF}}\,(f g) =
\sum_{n=0}^m \binom{m}{n} a_n b_{m-n}.
$$

- OGF partial-sum rule:

$$
\left[x^m\right]\frac{F(x)}{1-x}=\sum_{k=0}^m \alpha_k.
$$

- Exterior OGF partial-sum rule:

$$
\left[x^{-n}\right]\frac{F(1/x)}{x-1}=\sum_{k=0}^{n-1}\alpha_k,
\qquad n\ge 1.
$$

- Recurrence for the logarithmic derivative:

$$
b_m=a_{m+1}-\sum_{n=1}^m \binom{m}{n} a_n b_{m-n}.
$$

- Logarithm expansion:

$$
\operatorname{Log} f(x)=\sum_{k\ge 1} (-1)^{k+1}\frac{(f(x)-1)^k}{k}.
$$

- Bell-polynomial coefficient formula:

$$
b_m =
\sum_{k=1}^{m+1} (-1)^{k+1}(k-1)!\,B_{m+1,k}(a_1,a_2,\ldots,a_{m-k+2}).
$$

- Higher-derivative Bell formula when $f'=g f$:

$$
f^{(m)}(x)=f(x)\,Y_m\bigl(g(x),g'(x),\ldots,g^{(m-1)}(x)\bigr)
=f(x)\sum_{n=1}^m B_{m,n}\bigl(g,g',\ldots,g^{(m-n)}\bigr).
$$

- Polylogarithm form:

$$
\operatorname{Log} f(x)=-\operatorname{Li}_1\bigl(-(f(x)-1)\bigr).
$$

## 10. Worked Examples

### Example 1: $f(x)=e^{a x}$

Here

$$
f'(x)=a e^{a x},
\qquad
\frac{f'(x)}{f(x)}=a.
$$

So

$$
g(x)=a,
\qquad
b_0=a,
\qquad
b_m=0 \text{ for } m\ge 1.
$$

This is the simplest case: the logarithmic derivative is constant.

### Example 2: $f(x)=e^{a x+b x^2/2}$

Then

$$
\operatorname{Log} f(x)=a x+\frac{b x^2}{2},
$$

so immediately

$$
\frac{f'(x)}{f(x)}=a+b x.
$$

Thus the EGF coefficients of $g$ are

$$
b_0=a,
\qquad
b_1=b,
\qquad
b_m=0 \text{ for } m\ge 2.
$$

This example shows why it is often easier to expand $\operatorname{Log} f$ first and differentiate afterward.

### Example 3: $f(x)=\dfrac{1}{1-x}$

Although this function is usually treated as an ordinary generating function, it is also a perfectly good normalized analytic function at $x=0$, so the logarithmic-derivative machinery still applies.

We have

$$
\operatorname{Log} f(x)=-\operatorname{Log}(1-x)=\operatorname{Li}_1(x),
$$

As an ordinary generating function, multiplication by $1/(1-x)$ accumulates coefficients. If

$$
F(x)=\sum_{m\ge 0} \alpha_m x^m,
$$

then

$$
\frac{F(x)}{1-x}=\sum_{m\ge 0}\left(\sum_{k=0}^m \alpha_k\right)x^m.
$$

and therefore

$$
\frac{f'(x)}{f(x)}=\frac{1}{1-x}.
$$

As an EGF,

$$
\frac{1}{1-x}=\sum_{m\ge 0} m!\,\frac{x^m}{m!},
$$

so in this case

$$
b_m=m!.
$$

This example is useful because it ties together the logarithm, the first polylogarithm, and a familiar rational function.

### Example 3a: exterior expansion of an OGF

Let

$$
F(t)=\sum_{m\ge 0} \alpha_m t^m.
$$

Then for $|x|>1$,

$$
\frac{F(1/x)}{x-1} =
\sum_{n\ge 1}\frac{1}{x^n}\sum_{k=0}^{n-1}\alpha_k.
$$

For example, if

$$
F(t)=\frac{t}{1-t}=t+t^2+t^3+\cdots,
$$

then $\alpha_0=0$ and $\alpha_m=1$ for $m\ge 1$, so

$$
\frac{F(1/x)}{x-1} =
\frac{1}{x^2}+\frac{2}{x^3}+\frac{3}{x^4}+\frac{4}{x^5}+\cdots.
$$

Indeed,

$$
F(1/x)=\frac{1}{x-1},
\qquad
\frac{F(1/x)}{x-1}=\frac{1}{(x-1)^2},
$$

and the displayed series is exactly the large-$x$ expansion of $(x-1)^{-2}$.

### Example 3b: the logarithm of the golden ratio

Let
$$
\varphi=\frac{1+\sqrt5}{2}.
$$
Then
$$
\log(1+\sqrt5)=\log 2+\log\varphi.
$$
It is better to expand $\log\varphi$ than $\log(1+\sqrt5)$ directly, because the naive series
$$
\log(1+u)=\sum_{n\ge 1}(-1)^{n+1}\frac{u^n}{n}
$$
only converges for $|u|<1$, whereas $\sqrt5>1$.

Using
$$
\varphi=1+\frac{1}{\varphi}=1+\frac{\sqrt5-1}{2},
$$
one obtains the convergent expansion
$$
\log\varphi
=\sum_{n\ge 1}(-1)^{n+1}\frac{1}{n\varphi^n}
=\sum_{n\ge 1}(-1)^{n+1}\frac{1}{n}\left(\frac{\sqrt5-1}{2}\right)^n.
$$
Therefore
$$
\log(1+\sqrt5)
=\log 2+\sum_{n\ge 1}(-1)^{n+1}\frac{1}{n}\left(\frac{\sqrt5-1}{2}\right)^n.
$$

There is also a particularly clean odd-power expansion. Since
$$
\log\varphi=\operatorname{artanh}\!\left(\frac{1}{\sqrt5}\right)
=\frac12\log\!\left(\frac{1+1/\sqrt5}{1-1/\sqrt5}\right),
$$
the standard series for $\operatorname{artanh}$ gives
$$
\log\varphi
=\sum_{k\ge 0}\frac{1}{(2k+1)5^{k+1/2}}
=\frac{1}{\sqrt5}\sum_{k\ge 0}\frac{1}{(2k+1)5^k}.
$$
Hence
$$
\log(1+\sqrt5)=\log 2+\frac{1}{\sqrt5}\sum_{k\ge 0}\frac{1}{(2k+1)5^k}.
$$

In polylogarithm language this may be written as
$$
\log\varphi=-\operatorname{Li}_1\!\left(-\frac{1}{\varphi}\right),
$$
so
$$
\log(1+\sqrt5)=\log 2-\operatorname{Li}_1\!\left(-\frac{1}{\varphi}\right).
$$
This is a useful model case: before applying the logarithm series, one often rewrites the argument into a form with modulus $<1$.

### Example 4: $\operatorname{Log}\!\left(\dfrac{\sin(\pi t)}{\pi t}\right)$

The Weierstrass product

$$
\frac{\sin(\pi t)}{\pi t}=\prod_{n\ge 1}\left(1-\frac{t^2}{n^2}\right)
$$

immediately gives, for $|t|<1$,

$$
\operatorname{Log}\!\left(\frac{\sin(\pi t)}{\pi t}\right)
=\sum_{n\ge 1}\operatorname{Log}\!\left(1-\frac{t^2}{n^2}\right).
$$

Expanding $\operatorname{Log}(1-u)=-\sum_{m\ge 1} u^m/m$ and interchanging sums yields

$$
\operatorname{Log}\!\left(\frac{\sin(\pi t)}{\pi t}\right)
=-\sum_{m\ge 1}\frac{\zeta(2m)}{m}t^{2m}.
$$

So the Taylor series at $t=0$ is

$$
\operatorname{Log}\!\left(\frac{\sin(\pi t)}{\pi t}\right)
=-\frac{\pi^2}{6}t^2-\frac{\pi^4}{180}t^4-\frac{\pi^6}{2835}t^6-\frac{\pi^8}{37800}t^8-\cdots.
$$

Using

$$
\zeta(2m)=(-1)^{m+1}\frac{B_{2m}(2\pi)^{2m}}{2(2m)!},
$$

the same expansion becomes

$$
\operatorname{Log}\!\left(\frac{\sin(\pi t)}{\pi t}\right)
=\sum_{m\ge 1} (-1)^m\frac{2^{2m-1}B_{2m}}{m(2m)!}\,\pi^{2m}t^{2m}.
$$

Differentiating gives the odd-power companion series

$$
\frac{d}{dt}\operatorname{Log}\!\left(\frac{\sin(\pi t)}{\pi t}\right)
=\pi\cot(\pi t)-\frac{1}{t}
=-2\sum_{m\ge 1}\zeta(2m)t^{2m-1}.
$$

This is not singled out by an EGF normalization, but it is an instructive example of the same formal mechanism: first take a logarithm, then differentiate, and the coefficients simplify dramatically.

## 11. Closing Remarks

The product rule for EGFs is the entry point, but the central object is really the logarithmic derivative of a normalized power series. Once $f(0)=1$, three equivalent descriptions are available:

- Recurrence from the EGF product rule.
- Expansion of $\operatorname{Log} f(x)$ as a formal series.
- Bell-polynomial coefficient formulas.

The polylogarithm notation $\operatorname{Li}_1$ is simply a convenient way to package the same logarithm expansion, and the sinc example shows how naturally zeta values appear when the logarithm is applied to an infinite product.
