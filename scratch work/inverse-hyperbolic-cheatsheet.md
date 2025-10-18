# Inverse Hyperbolic Functions Cheatsheet

## Definitions in Terms of Logarithms

- $\operatorname{arsinh} x = \ln \left(x + \sqrt{x^2 + 1}\right)$
- $\operatorname{arcosh} x = \ln \left(x + \sqrt{x^2 - 1}\right)$
- $\operatorname{artanh} x = \frac{1}{2}\ln\frac{1+x}{1-x}$
- $\operatorname{arcsch} x = \ln \left(\frac{1}{x} + \sqrt{\frac{1}{x^2} + 1}\right)$
- $\operatorname{arsech} x = \ln \left(\frac{1}{x} + \sqrt{\frac{1}{x^2} - 1}\right)$
- $\operatorname{arcoth} x = \frac{1}{2}\ln\frac{x+1}{x-1}$

## Addition Formulae

- $\operatorname{arsinh} u \pm \operatorname{arsinh} v = \operatorname{arsinh} \left(u \sqrt{1 + v^2} \pm v \sqrt{1 + u^2}\right)$
- $\operatorname{arcosh} u \pm \operatorname{arcosh} v = \operatorname{arcosh} \left(u v \pm \sqrt{(u^2 - 1) (v^2 - 1)}\right)$
- $\operatorname{artanh} u \pm \operatorname{artanh} v = \operatorname{artanh} \left( \frac{u \pm v}{1 \pm uv} \right)$
- $\operatorname{arcoth} u \pm \operatorname{arcoth} v = \operatorname{arcoth} \left( \frac{1 \pm uv}{u \pm v} \right)$

## Other Identities

- $2\operatorname{arcosh}x = \operatorname{arcosh}(2x^2-1)$
- $4\operatorname{arcosh}x = \operatorname{arcosh}(8x^4-8x^2+1)$
- $2\operatorname{arsinh}x = \pm\operatorname{arcosh}(2x^2+1)$
- $4\operatorname{arsinh}x = \operatorname{arcosh}(8x^4+8x^2+1)$

- $\ln(x) = \operatorname{arcosh} \left( \frac{x^2 + 1}{2x}\right) = \operatorname{arsinh} \left( \frac{x^2 - 1}{2x}\right) = \operatorname{artanh} \left( \frac{x^2 - 1}{x^2 + 1}\right)$

## Composition with Hyperbolic Functions

- $\sinh(\operatorname{arcosh}x) = \sqrt{x^{2} - 1}$
- $\sinh(\operatorname{artanh}x) = \frac{x}{\sqrt{1-x^{2}}}$
- $\cosh(\operatorname{arsinh}x) = \sqrt{1+x^{2}}$
- $\cosh(\operatorname{artanh}x) = \frac{1}{\sqrt{1-x^{2}}}$
- $\tanh(\operatorname{arsinh}x) = \frac{x}{\sqrt{1+x^{2}}}$
- $\tanh(\operatorname{arcosh}x) = \frac{\sqrt{x^{2} - 1}}{x}$

## Composition with Circular Functions

- $\operatorname{arsinh}(\tan \alpha) = \operatorname{artanh}(\sin \alpha) = \ln\left( \frac{1 + \sin \alpha}{\cos \alpha} \right) = \pm \operatorname{arcosh}\left( \frac{1}{\cos \alpha} \right)$
- $\ln|\tan \alpha| = -\operatorname{artanh}(\cos 2\alpha)$

## Conversions

- $\ln x = \operatorname{artanh} \left( \frac{x^2-1}{x^2+1}\right) = \operatorname{arsinh} \left( \frac{x^2-1}{2 x}\right) = \pm \operatorname{arcosh} \left( \frac{x^2+1}{2 x}\right)$
- $\operatorname{artanh} x = \operatorname{arsinh} \left( \frac{x}{\sqrt{1-x^2}}\right) = \pm \operatorname{arcosh} \left( \frac{1}{\sqrt{1-x^2}}\right)$
- $\operatorname{arsinh} x = \operatorname{artanh} \left( \frac{x}{\sqrt{1+x^2}}\right) = \pm \operatorname{arcosh} \left( \sqrt{1+x^2}\right)$
- $\operatorname{arcosh} x = |\operatorname{arsinh}(\sqrt{x^2-1})| = |\operatorname{artanh}(\sqrt{x^2-1}/x)|$

## Derivatives

- $\frac{d}{dx} \operatorname{arsinh} x = \frac{1}{\sqrt{x^2+1}}$
- $\frac{d}{dx} \operatorname{arcosh} x = \frac{1}{\sqrt{x^2-1}}$
- $\frac{d}{dx} \operatorname{artanh} x = \frac{1}{1-x^2}$
- $\frac{d}{dx} \operatorname{arcoth} x = \frac{1}{1-x^2}$
- $\frac{d}{dx} \operatorname{arsech} x = \frac{-1}{x\sqrt{1-x^2}}$
- $\frac{d}{dx} \operatorname{arcsch} x = \frac{-1}{|x|\sqrt{1+x^2}}$

## Series Expansions

- $\operatorname{arsinh} x = x - \frac{1}{2} \frac{x^3}{3} + \frac{1 \cdot 3}{2 \cdot 4} \frac{x^5}{5} - \frac{1 \cdot 3 \cdot 5}{2 \cdot 4 \cdot 6} \frac{x^7}{7} \pm \cdots$
- $\operatorname{arsinh} x = \sum_{n=0}^\infty \frac{(-1)^n (2n)!}{2^{2n} (n!)^2} \frac{x^{2n+1}}{2n+1}$

- $\operatorname{arcosh} x = \ln(2x) - \sum_{n=1}^\infty \frac{(2n)!}{2^{2n}(n!)^2} \frac{x^{-2n}}{2n}$

- $\operatorname{artanh} x = x + \frac{x^3}{3} + \frac{x^5}{5} + \frac{x^7}{7} + \cdots = \sum_{n=0}^\infty \frac{x^{2n+1}}{2n+1}$

- $\operatorname{arcsch} x = \sum_{n=0}^\infty \frac{(-1)^n (2n)!}{2^{2n} (n!)^2} \frac{x^{-(2n+1)}}{2n+1}$

- $\operatorname{arsech} x = \ln \frac{2}{x} - \sum_{n=1}^\infty \frac{(2n)!}{2^{2n}(n!)^2} \frac{x^{2n}}{2n}$

- $\operatorname{arcoth} x = \sum_{n=0}^\infty \frac{x^{-(2n+1)}}{2n+1}$

## Asymptotic Expansion

- $\operatorname{arsinh} x = \ln(2x) + \sum_{n=1}^\infty (-1)^{n-1} \frac{(2n-1)!!}{2n (2n)!!} \frac{1}{x^{2n}}$

## Principal Values (Complex Plane)

- $\operatorname{arsinh} z = \operatorname{Log}(z + \sqrt{z^2 + 1})$
- $\operatorname{arcosh} z = \operatorname{Log}(z + \sqrt{z+1} \sqrt{z-1})$
- $\operatorname{artanh} z = \frac{1}{2}\operatorname{Log}\left(\frac{1+z}{1-z}\right)$
- $\operatorname{arcoth} z = \frac{1}{2}\operatorname{Log}\left(\frac{z+1}{z-1}\right)$
- $\operatorname{arcsch} z = \operatorname{Log}\left( \frac{1}{z} + \sqrt{ \frac{1}{z^2} +1 } \right)$
- $\operatorname{arsech} z = \operatorname{Log}\left( \frac{1}{z} + \sqrt{ \frac{1}{z} + 1 } \sqrt{ \frac{1}{z} -1 } \right)$

## See Also

- Complex logarithm
- Hyperbolic secant distribution
- List of integrals of inverse hyperbolic functions

---

**References:**  
- Wikipedia: Inverse hyperbolic functions  
- Wolfram MathWorld: Inverse Hyperbolic Functions  
- NIST Digital Library of Mathematical Functions (DLMF)