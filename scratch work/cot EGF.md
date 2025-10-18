Nice — let’s look at the inverses. I’ll give the clean power-series facts, show how those coefficients are built from the same Bernoulli / odd-reciprocal structure that gives the ζ-values for cot/coth, and point out the places (Lagrange inversion, Mellin integrals) where ζ(odd) can appear.

⸻

Quick expansions (the basics)

Arccot.
For real x>0,
\[
\arccot x=\frac{\pi}{2}-\arctan x
\]
and the small-x expansion (around x=0) is
\[
\arccot x=\frac{\pi}{2}-\sum_{n=0}^\infty (-1)^n\frac{x^{2n+1}}{2n+1}
=\frac{\pi}{2}-x+\frac{x^3}{3}-\frac{x^5}{5}+\cdots.
\]

More useful in the inverse/cot context is the large-argument expansion (asymptotic series for |w|\to\infty) for the inverse of \cot(z). If w=\cot z and we invert to get \(z=\arccot w\), one gets a Laurent series in powers of 1/w:
\[
\boxed{\arccot w
=\frac{1}{w}-\frac{1}{3w^3}-\frac{1}{45w^5}-\frac{2}{945w^7}-\frac{1}{4725w^9}+\cdots}
\]
(Those coefficients are the same numerical coefficients that appear in the Laurent expansion of \cot z about z=0, now reinterpreted as coefficients of the inverse series in powers of 1/w.)

⸻

Arccoth.
\displaystyle \operatorname{arccoth} x=\tfrac12\log\frac{x+1}{x-1} for |x|>1. Write it as \operatorname{arccoth}x=\operatorname{arctanh}(1/x) and use the standard arctanh series to get, for |x|>1,
\boxed{\operatorname{arccoth}x=\frac{1}{x}+\frac{1}{3x^3}+\frac{1}{5x^5}+\frac{1}{7x^7}+\cdots
=\sum_{n=0}^\infty \frac{1}{(2n+1)\,x^{2n+1}}.}

So arccoth has very simple coefficients (reciprocals of odd integers) when expanded in inverse powers of x.

⸻

How these inverses connect to ζ (where your original cot/coth–ζ connection lives)
	1.	Cot / coth → Bernoulli numbers → ζ(2n).
\cot z and z\cot z have expansions whose coefficients are Bernoulli numbers, and the Bernoulli numbers are directly proportional to \zeta(2n). That gives the well-known generation of even zeta values from cot/coth.
	2.	Inverting the series (arccot as inverse of cot):
When you compute the compositional inverse power series (i.e. the series for \(\arccot w\) as w\to\infty), the coefficients of that inverse are universal polynomials in the original series coefficients. Concretely: because
\cot z = \frac{1}{z} + \sum_{k\ge1} a_k z^{2k-1}
with a_k expressed via Bernoulli numbers (hence \zeta(2k)), the Lagrange inversion / series reversion formula gives
\[
z=\arccot w=\sum_{n\ge0} b_n w^{-2n-1},
\]
where each b_n is a (universal) polynomial in the a_1,a_2,\dots,a_n. Thus the b_n — the coefficients in the arccot series — are ultimately expressible in terms of Bernoulli numbers and therefore in terms of the even zeta values \zeta(2k). (So the inverse inherits the cot/coth → ζ(2k) information algebraically.)
In practice, the first few b_n coincide (up to sign) with the same small integers that appeared in the cot expansion, e.g.
b_0=1,\quad b_1=-\tfrac13,\quad b_2=-\tfrac{1}{45},\quad b_3=-\tfrac{2}{945},\dots
as shown above.
	3.	Arccoth is simpler but different:
Because \operatorname{arccoth}x=\operatorname{arctanh}(1/x), its inverse series coefficients are elementary \frac{1}{2n+1}. So arccoth’s coefficients do not directly encode Bernoulli numbers or ζ(2n) in the same way — they’re simpler. However, compositions or integrals involving arccoth can still produce ζ-values (especially odd ζ values) when combined with appropriate algebraic or integral transforms.

⸻

Where odd ζ values show up

The odd zeta values, \zeta(2n+1), are more subtle and do not appear as simple polynomial consequences of the Bernoulli numbers. They commonly appear in:
   •   Mellin / integral transforms of arctan/arcot-type kernels. For example integrals of the form
\int_0^1 x^{s-1}\arctan x\,dx
or
\int_0^\infty \frac{x^{2n}}{e^{2\pi x}-1}\,dx
produce values involving \zeta(2n+1) (or Dirichlet β-values), so the inverse trigonometric kernels are a natural place for odd zeta values to appear.
   •   Polylogarithmic / Clausen function identities. Many identities that start from \arctan, \operatorname{arccot}, or logarithms lead (after integration or series manipulation) to polylogarithms evaluated at roots of unity; those evaluations typically contain odd ζs.
   •   Compositions and Lagrange inversion at higher depth. While the direct inverse coefficients b_n for arccot are algebraic combinations of ζ(even), more elaborate transforms of arccot (e.g. integrals of \(x^{m}\arccot(x)\), or combining with x\mapsto \frac{\pi x}{something}) can produce odd ζs.

⸻

## Exponential Generating Function for $x \cot x$ and Lagrange Inversion

---

### 1. Exponential Generating Function (EGF) for $x \cot x$

The function $x \cot x$ has a classical power series expansion involving Bernoulli numbers and even zeta values:

```math
x \cot x = 1 - 2 \sum_{n=1}^\infty \frac{(-1)^n B_{2n}}{(2n)!} (2x)^{2n}
```

Alternatively, in terms of even zeta values:

```math
x \cot x = 1 - 2 \sum_{n=1}^\infty \frac{2^{2n} |B_{2n}|}{(2n)!} x^{2n}
         = 1 - 2 \sum_{n=1}^\infty \frac{(-1)^{n-1} \zeta(2n)}{\pi^{2n}} x^{2n}
```

where $B_{2n}$ are Bernoulli numbers and $\zeta(2n)$ are Riemann zeta values at even integers.

---

### 2. Lagrange Inversion for $\cot z$ and $\arccot w$

Suppose $w = \cot z$, and we seek the inverse series $z = \arccot w$ as $w \to \infty$.

**Lagrange inversion formula:**
Given $w = f(z)$, the compositional inverse $z = f^{-1}(w)$ has the expansion:

```math
z = \sum_{n=1}^\infty \frac{w^{-n}}{n!} \left. \frac{d^{n-1}}{dz^{n-1}} \left[ (z f(z))^n \right] \right|_{z=0}
```

For $f(z) = \cot z$, the coefficients in the inverse series for $\arccot w$ are universal polynomials in the coefficients of the expansion of $\cot z$.

**Explicit inverse series:**

```math
\arccot w = \frac{1}{w} - \frac{1}{3 w^3} - \frac{1}{45 w^5} - \frac{2}{945 w^7} - \frac{1}{4725 w^9} + \cdots
```

These coefficients are algebraic combinations of Bernoulli numbers and thus encode even zeta values.

---

### 3. Summary Table

| Function         | Series Expansion / EGF                                 | Coefficient Structure           |
|------------------|-------------------------------------------------------|---------------------------------|
| $x \cot x$       | $1 - 2 \sum_{n=1}^\infty \frac{(-1)^n B_{2n}}{(2n)!} (2x)^{2n}$ | Bernoulli numbers, $\zeta(2n)$  |
| $\arccot w$      | $\sum_{n=0}^\infty b_n w^{-2n-1}$                     | $b_n$ from Lagrange inversion, Bernoulli numbers |

---

### 4. Next Steps

- **Lagrange inversion:** Compute explicit formulas for the coefficients $b_n$ in terms of Bernoulli numbers for the inverse series $\arccot w$.
- **Connection to zeta values:** Show how these coefficients relate to $\zeta(2n)$.
- **Further expansions:** Explore integrals or transforms involving $\arccot$ that produce odd zeta values.

---

**References:**
- Abramowitz & Stegun, Handbook of Mathematical Functions
- NIST Digital Library of Mathematical Functions (DLMF)
- Classical texts on Lagrange inversion and generating functions

---

**Markdown Tips for Displaying Math:**
- Use single dollar signs `$...$` for inline math.
- Use double dollar signs `$$...$$` or triple backticks with `math` for display math.
- Avoid using `\[` and `\]` for display math in GitHub markdown.
- For best compatibility, keep equations simple and avoid unsupported LaTeX environments.