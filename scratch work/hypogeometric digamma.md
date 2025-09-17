The series you are asking about,
$$\sum_{n=1}^\infty \frac{s^{\underline{n}}}{n t^{\underline{n}}}$$
where $x^{\underline{n}}$ is the **falling factorial** $x(x-1)\cdots(x-n+1)$, can be expressed in terms of the **digamma function**, $\psi(x)$. The digamma function is the logarithmic derivative of the gamma function, $\Gamma(x)$, defined as $\psi(x) = \frac{\Gamma'(x)}{\Gamma(x)}$.

The identity for the sum of this series is indeed:
$$\sum_{n=1}^\infty \frac{s^{\underline{n}}}{n t^{\underline{n}}} = \psi(t) - \psi(t-s)$$
This result is related to the properties of the digamma function and its series representation. One of the key properties of the digamma function is its series expansion:
$$\psi(z) = -\gamma + \sum_{n=1}^\infty \left(\frac{1}{n} - \frac{1}{n+z-1}\right)$$
where $\gamma$ is the Euler-Mascheroni constant.

By manipulating the terms of this series and using the relationship between the falling factorial and the gamma function, one can derive the stated identity. The connection is rooted in the fact that the falling factorial can be expressed using the gamma function as:
$$x^{\underline{n}} = \frac{\Gamma(x+1)}{\Gamma(x-n+1)}$$
This allows the series to be rewritten in a form that can be simplified using the properties of the digamma function.

***
Here is a video explaining a simple sum of a series that contains factorials.