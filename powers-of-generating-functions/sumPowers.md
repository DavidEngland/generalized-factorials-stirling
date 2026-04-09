# Sums of Powers, EGF, and Extension to Real x

## 1) Classical finite sum and its EGF

For integer upper limit x >= 1, define

S_n(x) = sum_{k=0}^{x-1} k^n.

The exponential generating function (EGF) in n is

sum_{n>=0} S_n(x) t^n / n! = sum_{k=0}^{x-1} e^{k t} = (e^{x t} - 1)/(e^t - 1).

This is an EGF with respect to n (the power index), with x treated as a parameter.

## 2) Bernoulli connection

Use

t e^{x t}/(e^t - 1) = sum_{m>=0} B_m(x) t^m / m!,

t/(e^t - 1) = sum_{m>=0} B_m t^m / m!.

Then

(e^{x t} - 1)/(e^t - 1)
= (1/t) * (t e^{x t}/(e^t - 1) - t/(e^t - 1))
= sum_{n>=0} (B_{n+1}(x) - B_{n+1}) t^n/(n+1)!.

Hence

S_n(x) = (B_{n+1}(x) - B_{n+1})/(n+1).

So the geometric-series EGF and the Bernoulli-polynomial formula are equivalent.

## 3) Partial derivative with respect to x

Let

F(x,t) = (e^{x t} - 1)/(e^t - 1) = sum_{n>=0} S_n(x) t^n/n!.

Differentiate in x:

partial_x F(x,t) = t e^{x t}/(e^t - 1) = sum_{n>=0} B_n(x) t^n/n!.

Coefficientwise,

d/dx S_n(x) = B_n(x).

This is consistent with S_n(x) = (B_{n+1}(x)-B_{n+1})/(n+1), since B'_{n+1}(x) = (n+1)B_n(x).

## 4) Extending x from integers to real values

Yes, there is a natural extension. For each fixed n >= 0, define

S_n(x) := (B_{n+1}(x) - B_{n+1})/(n+1)

for real (or complex) x. This is a polynomial identity in x, so it extends the integer sum exactly:

for integer m >= 1,

S_n(m) = sum_{k=0}^{m-1} k^n.

Equivalent extension using the Hurwitz zeta function:

S_n(x) = zeta(-n) - zeta(-n, x),

and for integer n >= 0,

zeta(-n, x) = -B_{n+1}(x)/(n+1),

so this matches the Bernoulli formula.

Interpretation:
- Integer x: literal finite sum.
- Real x: analytic continuation/interpolation of that sum.

## 5) Small checks

n = 0:
S_0(x) = B_1(x) - B_1 = (x - 1/2) - (-1/2) = x.

At integer x = m, this gives S_0(m) = m = sum_{k=0}^{m-1} 1.

n = 1:
S_1(x) = (B_2(x) - B_2)/2 = (x^2 - x)/2.

At integer x = m, S_1(m) = m(m-1)/2 = sum_{k=0}^{m-1} k.

## 6) Practical takeaway

The master object

F(x,t) = (e^{x t} - 1)/(e^t - 1)

simultaneously gives:
- power sums via EGF coefficients in t,
- Bernoulli-polynomial structure via x-derivatives,
- and a canonical extension from integer to real/complex x.

