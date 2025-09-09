# The Weierstrass Formulation for the Reciprocal Factorial Function

## Introduction

The factorial function, \( s! \), is defined for non-negative integers. Its analytic continuation to the complex plane is given by the gamma function, \( \Gamma(s+1) \). Thus, the reciprocal factorial function, \( 1/s! \), is represented as the entire function \( 1/\Gamma(s+1) \), which is holomorphic everywhere in the complex plane.

The Weierstrass factorization theorem states that any entire function can be expressed as a product involving its zeros.

## Derivation

**Zeros:**  
The zeros of \( 1/\Gamma(s+1) \) are the poles of \( \Gamma(s+1) \), which occur at \( s = -n \) for \( n = 1, 2, 3, \ldots \).  
There is no zero at \( s = 0 \) since \( 1/0! = 1 \).

**Weierstrass Factorization:**  
The general form for an entire function \( f(s) \) with zeros at \( s_n \) is:
\[
f(s) = e^{g(s)} \prod_{n=1}^{\infty} E_p\left(\frac{s}{s_n}\right)
\]
where \( E_1(z) = (1-z)e^z \) is the first-order primary factor, and \( g(s) \) is an entire function.

For \( 1/\Gamma(s+1) \), the zeros are at \( s_n = -n \), so the product becomes:
\[
\prod_{n=1}^{\infty} \left(1 + \frac{s}{n}\right) e^{-s/n}
\]

The exponential factor for \( 1/\Gamma(s+1) \) is known to be \( e^{\gamma s} \), where \( \gamma \) is the Euler-Mascheroni constant.

**Constant Determination:**  
Evaluating at \( s = 0 \):
\[
1 = e^C \implies C = 0
\]

## Final Formula

The Weierstrass product for the reciprocal factorial function is:
\[
\frac{1}{s!} = \frac{1}{\Gamma(s+1)} = e^{\gamma s} \prod_{n=1}^{\infty} \left(1 + \frac{s}{n}\right) e^{-s/n}
\]

where \( \gamma \) is the Euler-Mascheroni constant.

---

This formula shows that the analytic continuation of the factorial is determined by its zeros at the negative integers and a growth factor related to \( \gamma \).