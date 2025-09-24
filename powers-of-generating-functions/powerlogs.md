# Series and Asymptotic Expansions for $(\ln x)^s$

This document provides practical expansions for $(\ln x)^s$ (real or complex $s$), with explicit formulas for coefficients, error bounds, and connections to Stirling numbers.

---

## Domains and Branches

- **Real $x$:** $x > 0$, principal real branch.
- **Complex $x$:** Use principal branch $\Log z$; branch cut $(-\infty,0]$.
- **Near $x=0$:** $\ln x \to -\infty$; expand in terms of $x=e^{-t}$ if needed.

---

## Power Series Expansion Around $x=a>0$

Let $u = \frac{x-a}{a}$, so $\ln x = \ln a + \ln(1+u)$, $|u| < 1$.

### General Expansion

\[
(\ln x)^s = \left(\ln a + \ln(1+u)\right)^s = \sum_{m=0}^\infty \binom{s}{m} (\ln a)^{s-m} \left[\ln(1+u)\right]^m
\]

Expand $\ln(1+u)$ as a power series:
\[
\ln(1+u) = \sum_{n=1}^\infty (-1)^{n+1} \frac{u^n}{n}
\]

Raise to the $m$-th power:
\[
\left[\ln(1+u)\right]^m = m! \sum_{n=m}^\infty s(n,m) \frac{u^n}{n!}
\]
where $s(n,m)$ are the (unsigned) Stirling numbers of the first kind.

### Combined Expansion

\[
(\ln x)^s = \sum_{m=0}^\infty \binom{s}{m} (\ln a)^{s-m} m! \sum_{n=m}^\infty s(n,m) \frac{u^n}{n!}
= \sum_{n=0}^\infty c_n u^n
\]

where
\[
c_n = \sum_{m=0}^n \binom{s}{m} (\ln a)^{s-m} m! \frac{s(n,m)}{n!}
\]

**Summary:**  
- Coefficients $c_n$ are explicit in terms of binomial coefficients and Stirling numbers of the first kind.
- For integer $s=m$, only $m$ terms contribute.

---

## Special Case: Expansion Around $x=1$

Set $a=1$, $u=x-1$:
\[
(\ln x)^s = \sum_{n=0}^\infty c_n (x-1)^n
\]
with
\[
c_n = \sum_{m=0}^n \binom{s}{m} m! \frac{s(n,m)}{n!}
\]

---

## Asymptotic Expansion for Large $x$

For $x \to \infty$,
\[
\ln(x+a) = \ln x + \sum_{k=1}^\infty (-1)^{k+1} \frac{a^k}{k x^k}
\]
\[
(\ln(x+a))^s = (\ln x)^s \left[ 1 + \sum_{m=1}^\infty \binom{s}{m} \frac{1}{(\ln x)^m} \left( \sum_{k=1}^\infty (-1)^{k+1} \frac{a^k}{k x^k} \right)^m \right]
\]

Expand the inner sum and collect by powers of $x^{-1}$; coefficients involve multinomial expansions and powers of $1/\ln x$.

---

## Error Estimates

- **Local series ($|u|<1$):** Truncation error after $N$ terms:
  \[
  |R_N(u)| \leq \frac{|u|^{N+1}}{(N+1)(1-|u|)}
  \]
- **Asymptotic series:** Error is comparable to the first omitted term in $x^{-K}$.

---

## Computational Notes

- **Stirling numbers $s(n,m)$:** Can be computed recursively:
  \[
  s(n,m) = s(n-1,m-1) + (n-1) s(n-1,m)
  \]
  with $s(0,0)=1$, $s(n,0)=0$ for $n>0$, $s(0,m)=0$ for $m>0$.
- **Binomial coefficients $\binom{s}{m}$:** For general $s$, use $\binom{s}{m} = \frac{s(s-1)\cdots(s-m+1)}{m!}$.
- **For integer powers:** Only $m \leq s$ contribute.

---

## Compact Algorithm

1. **Choose center $a>0$; set $u=(x-a)/a$.**
2. **Compute coefficients $c_n$ up to desired $N$ using Stirling numbers and binomials.**
3. **Evaluate series $\sum_{n=0}^N c_n u^n$ for $|u|<1$.**
4. **For large $x$, use asymptotic expansion in $x^{-1}$ and truncate at optimal $K$.**

---

## References

- Stirling numbers: see combinatorics texts or OEIS A048993.
- Bell polynomials for general composition expansions.
- Asymptotic series: Olver, "Asymptotics and Special Functions".