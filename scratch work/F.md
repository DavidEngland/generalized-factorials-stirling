Let
$$
F(z):=\frac{\psi\!\left(\frac{z+1}{2z}\right)-\psi\!\left(\frac{1}{2z}\right)}{2z}
=\frac{\psi\!\left(\frac12+\frac{1}{2z}\right)-\psi\!\left(\frac{1}{2z}\right)}{2z},
$$
where $\psi$ denotes the Gauss digamma function.

**Further useful digamma identities.** For later manipulations, especially rational specializations, alternating filters, and parity-splitting, the following identities are the most structurally relevant.

1. **Shift relation.**
$$
\psi(z+1)=\psi(z)+\frac{1}{z}.
$$
This is the basic reduction tool: it peels off rational terms and moves arguments into a preferred strip.

2. **Reflection formula.**
$$
\psi(1-z)-\psi(z)=\pi\cot(\pi z).
$$
This is essential when arguments appear in complementary pairs. It converts digamma differences into trigonometric constants, often the fastest route to explicit evaluations.

3. **Multiplication formula.**
$$
\sum_{k=0}^{m-1}\psi\!\left(z+\frac{k}{m}\right)=m\,\psi(mz)-m\log m.
$$
The case $m=2$ is duplication; larger $m$ packages sums over evenly spaced rational shifts.

4. **Gauss's digamma theorem at rational arguments.** For $1\le a<q$ with $(a,q)=1$,
$$
\psi\!\left(\frac{a}{q}\right)
=-\gamma-\log(2q)-\frac{\pi}{2}\cot\!\left(\frac{\pi a}{q}\right)
+2\sum_{n=1}^{\lfloor (q-1)/2\rfloor}
\cos\!\left(\frac{2\pi an}{q}\right)\log\sin\!\left(\frac{\pi n}{q}\right).
$$
This is the main tool for turning rational digamma values into explicit $\pi$- and log-combinations. In particular, it applies directly to
$$
F(m)=\frac1m\left[\psi\!\left(\frac1m\right)-\psi\!\left(\frac1{2m}\right)-\log 2\right].
$$

5. **Series difference identity.**
$$
\psi(a)-\psi(b)=\sum_{n=0}^{\infty}\left(\frac{1}{n+b}-\frac{1}{n+a}\right).
$$
This is the cleanest way to recognize filtered harmonic progressions and alternating decompositions.

6. **Integral representation.**
$$
\psi(z)+\gamma=\int_0^1 \frac{1-t^{z-1}}{1-t}\,dt,
\qquad \Re z>0.
$$
Together with the $1+t$ denominator variant used below, this gives the two basic kernels for ordinary and alternating harmonic filters.

7. **Parity-split identity.**
$$
\psi\!\left(z+\frac12\right)-\psi(z)
=2\sum_{n=0}^{\infty}
\left(\frac{1}{2n+2z}-\frac{1}{2n+2z+1}\right).
$$
This is the structural decomposition behind the present kernel $F(z)$, isolating the alternating component.

8. **First polygamma reflection.**
$$
\psi_1(1-z)+\psi_1(z)=\pi^2\csc^2(\pi z),
$$
where $\psi_1=\psi'$. This is useful for monotonicity, convexity, and weighted sums such as $\sum_{n\ge 0}(-1)^n/(1+nz)^2$.

**Lemma.** For $z\neq 0$, the function $F$ admits the equivalent representations
$$
F(z)=\frac1z\left[\psi\!\left(\frac1z\right)-\psi\!\left(\frac1{2z}\right)-\log 2\right],
$$
and, for $\Re(1/z)>0$,
$$
F(z)=\frac1z\int_0^1 \frac{u^{1/z-1}}{1+u}\,du
=\sum_{n=0}^{\infty}\frac{(-1)^n}{1+nz}.
$$
Consequently, $F$ extends meromorphically to the complex plane with simple poles at
$$
z=-\frac1n,\qquad n=1,2,3,\dots,
$$
and residues
$$
\operatorname{Res}_{z=-1/n}F(z)=\frac{(-1)^n}{n}.
$$

**Proof.** Apply the digamma duplication formula
$$
\psi(2w)=\frac12\psi(w)+\frac12\psi\!\left(w+\frac12\right)+\log 2
$$
with $w=\frac{1}{2z}$. This gives
$$
\psi\!\left(\frac12+\frac{1}{2z}\right)-\psi\!\left(\frac{1}{2z}\right)
=2\psi\!\left(\frac1z\right)-2\psi\!\left(\frac{1}{2z}\right)-2\log 2,
$$
hence
$$
F(z)=\frac1z\left[\psi\!\left(\frac1z\right)-\psi\!\left(\frac1{2z}\right)-\log 2\right].
$$
For the integral form, use the standard identity
$$
\psi\!\left(a+\frac12\right)-\psi(a)=2\int_0^1\frac{u^{2a-1}}{1+u}\,du,
\qquad \Re(a)>0,
$$
and substitute $a=\frac{1}{2z}$ to obtain
$$
F(z)=\frac1z\int_0^1\frac{u^{1/z-1}}{1+u}\,du.
$$
If $\Re(1/z)>0$, expand
$$
\frac{1}{1+u}=\sum_{n=0}^{\infty}(-1)^n u^n,
\qquad 0\le u<1,
$$
and integrate termwise:
$$
F(z)=\frac1z\sum_{n=0}^{\infty}(-1)^n\int_0^1 u^{n+1/z-1}\,du
=\frac1z\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1/z}
=\sum_{n=0}^{\infty}\frac{(-1)^n}{1+nz}.
$$
The meromorphic continuation and the pole data now follow immediately from the partial-fraction expansion. $\square$

Two asymptotic regimes are especially useful:
$$
F(z)=\frac12+\frac z4+O(z^2)\qquad (z\to 0),
$$
and
$$
F(z)=1-\frac{\log 2}{z}+\frac{\pi^2}{12z^2}+O(z^{-3})\qquad (z\to\infty).
$$
Thus $F$ may be viewed as an alternating Stieltjes-type kernel, with both an integral representation and an explicit partial-fraction expansion.

**Corollary (positive integer parameters).** For $m\in\mathbb{N}$,
$$
F(m)=\sum_{n=0}^{\infty}\frac{(-1)^n}{1+mn}=\int_0^1\frac{dx}{1+x^m}.
$$
In particular,
$$
F(1)=\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}=\log 2,
$$
$$
F(2)=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}=\frac{\pi}{4},
$$
$$
F(3)=\sum_{n=0}^{\infty}\frac{(-1)^n}{3n+1}=\frac{\log 2}{3}+\frac{\pi}{3\sqrt{3}},
$$
and
$$
F(4)=\sum_{n=0}^{\infty}\frac{(-1)^n}{4n+1}=\frac{\pi}{4\sqrt{2}}+\frac{\log(1+\sqrt{2})}{2\sqrt{2}}.
$$
and
$$
F(5)=\sum_{n=0}^{\infty}\frac{(-1)^n}{5n+1}
=\frac{\log 2}{5}+\frac{\sqrt{5}}{5}\log\!\left(\frac{1+\sqrt{5}}{2}\right)
+\frac{\pi}{50}\sqrt{50+10\sqrt{5}}.
$$

**Proof.** Starting from
$$
F(m)=\frac1m\int_0^1\frac{u^{1/m-1}}{1+u}\,du,
$$
set $u=x^m$. Then $du=mx^{m-1}\,dx$, and therefore
$$
\frac1m u^{1/m-1}\,du=\frac1m x^{1-m}\cdot mx^{m-1}\,dx=dx,
$$
which yields
$$
F(m)=\int_0^1\frac{dx}{1+x^m}.
$$
The evaluations for $m=1,2,3,4$ follow from elementary partial fractions:
$$
\int_0^1\frac{dx}{1+x}=\log 2,
\qquad
\int_0^1\frac{dx}{1+x^2}=\arctan(1)=\frac{\pi}{4},
$$
$$
\frac{1}{1+x^3}=\frac{1}{3}\frac{1}{x+1}+\frac{-x+2}{3(x^2-x+1)},
$$
and
$$
\frac{1}{1+x^4}=\frac{\frac{x}{2\sqrt2}+\frac12}{x^2+\sqrt2 x+1}+\frac{-\frac{x}{2\sqrt2}+\frac12}{x^2-\sqrt2 x+1}.
$$
After integration over $[0,1]$, these give the stated constants. The case $m=5$ is still elementary, but it is cleaner to obtain it from the root-pair decomposition below; equivalently, one may factor $1+x^5$ over the reals and integrate the resulting quadratic pieces. $\square$

**Proposition (decomposition by the $m$-th roots of $-1$).** Let
$$
\omega_r:=e^{(2r+1)\pi i/m},\qquad r=0,1,\dots,m-1,
$$
so that $\omega_r^m=-1$. Then
$$
\frac{1}{1+x^m}=-\frac1m\sum_{r=0}^{m-1}\frac{\omega_r}{x-\omega_r},
$$
and therefore
$$
F(m)=-\frac1m\sum_{r=0}^{m-1}\omega_r\int_0^1\frac{dx}{x-\omega_r}
=-\frac1m\sum_{r=0}^{m-1}\omega_r\Bigl(\log(1-\omega_r)-\log(-\omega_r)\Bigr).
$$
In particular, after pairing conjugate roots, $F(m)$ becomes a real linear combination of logarithms and arctangents of algebraic numbers.

**Proof.** Since the roots of $1+x^m$ are simple, the partial-fraction coefficients are the residues at $x=\omega_r$:
$$
\operatorname*{Res}_{x=\omega_r}\frac{1}{1+x^m}=\frac{1}{m\omega_r^{m-1}}=-\frac{\omega_r}{m},
$$
because $\omega_r^m=-1$. This proves the partial-fraction expansion. Integrating termwise from $0$ to $1$ gives the logarithmic formula. Pairing $\omega_r$ with $\overline{\omega_r}$ then yields a real expression in logarithms and arctangents. $\square$

More explicitly, let
$$
	heta_r:=\frac{(2r+1)\pi}{m},\qquad 0<\theta_r<\pi,
$$
and write $\omega_r=e^{i\theta_r}$. For such a root,
$$
1-\omega_r=2\sin\!\left(\frac{\theta_r}{2}\right)e^{i(\theta_r/2-\pi/2)},
$$
while
$$
-\omega_r=e^{i(\theta_r-\pi)}.
$$
Using the principal branch of the logarithm,
$$
\log(1-\omega_r)-\log(-\omega_r)
=\log\!\left(2\sin\!\left(\frac{\theta_r}{2}\right)\right)
+i\frac{\pi-\theta_r}{2}.
$$
Hence the combined contribution of the conjugate pair $\omega_r,\overline{\omega_r}$ is
$$
-\frac1m\Bigl(\omega_r\bigl(\log(1-\omega_r)-\log(-\omega_r)\bigr)
+\overline{\omega_r}\bigl(\log(1-\overline{\omega_r})-\log(-\overline{\omega_r})\bigr)\Bigr)
$$
$$
=\frac{1}{m}\Bigl((\pi-\theta_r)\sin\theta_r
-2\cos\theta_r\log\!\left(2\sin\!\left(\frac{\theta_r}{2}\right)\right)\Bigr).
$$
Therefore,
$$
F(m)=\frac{\mathbf{1}_{m\text{ odd}}}{m}\log 2
+\frac{1}{m}\sum_{0<\theta_r<\pi}
\Bigl((\pi-\theta_r)\sin\theta_r
-2\cos\theta_r\log\!\left(2\sin\!\left(\frac{\theta_r}{2}\right)\right)\Bigr),
$$
where the indicator term comes from the unpaired root $\omega=-1$ when $m$ is odd.

This makes the structure transparent. The quantities
$$
\cos\theta_r,\qquad \sin\theta_r,\qquad 2\sin\!\left(\frac{\theta_r}{2}\right)
$$
are algebraic because they are obtained from roots of unity. Moreover,
$$
\frac{\pi-\theta_r}{2}=\arctan\!\left(\cot\!\left(\frac{\theta_r}{2}\right)\right),
\qquad 0<\theta_r<\pi,
$$
and $\cot(\theta_r/2)$ is also algebraic. So each paired term is literally a real linear combination of a logarithm of an algebraic number and an arctangent of an algebraic number, with algebraic coefficients.

**Remark (gentle Dirichlet-character viewpoint).** The same sum may be rewritten as
$$
F(m)=\sum_{k=0}^{\infty}\frac{1}{2mk+1}-\sum_{k=0}^{\infty}\frac{1}{2mk+m+1}.
$$
Thus $F(m)$ is a difference of harmonic sums over two residue classes modulo $2m$. This is the right starting point for a character decomposition.

A Dirichlet character modulo $q$ is a periodic arithmetic weight $\chi(n)$ of period $q$ that is multiplicative and vanishes when $(n,q)\ne 1$. The associated Dirichlet $L$-series is
$$
L(s,\chi):=\sum_{n=1}^{\infty}\frac{\chi(n)}{n^s}.
$$
For the present discussion, the important value is at $s=1$:
$$
L(1,\chi)=\sum_{n=1}^{\infty}\frac{\chi(n)}{n},
$$
which converges for every nonprincipal character. So $L(1,\chi)$ is simply a harmonic series in which each term is weighted by a periodic arithmetic pattern.

Why does this help with $F(m)$? The point is that Dirichlet characters form an orthogonal basis for functions on the reduced residue classes modulo $q$. In practice this means that the indicator of a single invertible residue class can be reconstructed from characters. Thus harmonic sums restricted to one congruence class can be rewritten as linear combinations of the numbers $L(1,\chi)$.

When $m$ is even, both residue classes $1$ and $m+1$ are units modulo $2m$, so this orthogonality applies directly and gives
$$
F(m)=\frac{1}{\varphi(2m)}\sum_{\chi\bmod 2m}\Bigl(1-\overline{\chi}(m+1)\Bigr)L(1,\chi).
$$
Here the coefficient $1-\overline{\chi}(m+1)$ measures the difference between the two residue classes appearing in $F(m)$. The principal character contributes $0$, because for that character we have $\chi(m+1)=1$, so the coefficient becomes $1-1=0$. This is exactly what one should expect: each individual harmonic progression diverges, but their difference converges, and the divergent principal part cancels out.

The simplest example is $m=2$. Then
$$
F(2)=1-\frac13+\frac15-\frac17+\cdots.
$$
Modulo $4$, the relevant nontrivial character is
$$
\chi_4(n)=
\begin{cases}
0,& n\text{ even},\\
1,& n\equiv 1\pmod 4,\\
-1,& n\equiv 3\pmod 4.
\end{cases}
$$
Therefore
$$
L(1,\chi_4)=\sum_{n=1}^{\infty}\frac{\chi_4(n)}{n}
=1-\frac13+\frac15-\frac17+\cdots
=\frac{\pi}{4}.
$$
So in this case $F(2)$ is literally a Dirichlet $L$-value.

This also explains the shape of the constants obtained for small even $m$. Values $L(1,\chi)$ are classical objects, and for characters coming from roots of unity they reduce to explicit combinations of logarithms and arctangents of algebraic numbers. That is the character-theoretic counterpart of the root-of-$-1$ decomposition above.

For odd $m$, the class $m+1$ is not invertible modulo $2m$, so a literal Dirichlet-character decomposition modulo $2m$ is less natural. In that case one usually keeps the root-of-$-1$ partial fractions above, or splits off the even progression first and then applies character methods to the remaining odd moduli. Either way, the guiding principle is the same: isolate arithmetic progressions, then express those progressions through periodic data, either by roots of unity or by characters.
