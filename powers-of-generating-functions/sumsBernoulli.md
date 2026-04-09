This is a beautifully concise derivation. You’ve essentially mapped out the "Discrete Calculus" version of the Fundamental Theorem of Calculus. By treating S_n(x) as a polynomial in x, you bridge the gap between discrete summation and continuous analysis perfectly.
Here are a few additional insights to round out this "master object" perspective:
1. The Discrete Derivative Connection
In discrete calculus, the forward difference operator \Delta f(x) = f(x+1) - f(x) acts as the analog to the derivative. For your sum S_n(x):


This is the discrete version of \frac{d}{dx} \int_0^x f(t)dt = f(x). Your derivation in Section 3 shows that while the discrete derivative of S_n(x) is x^n, its continuous derivative is B_n(x). This positions Bernoulli polynomials as the "interpolated" rate of change for discrete power sums.
2. The Euler-Maclaurin Perspective
The relationship you noted—S_n(x) = \frac{B_{n+1}(x) - B_{n+1}}{n+1}—is actually a specific case of the Euler-Maclaurin Formula. Usually, Euler-Maclaurin is used to approximate sums with integrals, but for polynomials, the formula terminates, giving you this exact identity.
3. Visualizing the "Real x" Extension
When you extend x to real values, S_n(x) stops being a "count" of terms and becomes a smooth curve that passes through the cumulative sum at every integer point.
 * For n=1, S_1(x) = \frac{x(x-1)}{2} is just the classic parabola passing through the triangular numbers (shifted by one).
 * For higher n, the Bernoulli polynomials introduce "wiggles" between the integers to account for the increasing curvature of k^n.
4. Symmetry and the Reflection Formula
Because of the properties of Bernoulli polynomials, your extended S_n(x) satisfies a reflection functional equation:


This symmetry is often hidden when we only look at integer x \ge 1, but it becomes obvious once you view F(x, t) as the primary object.
One interesting edge case:
Your EGF \frac{e^{xt}-1}{e^t-1} is well-defined at t=0 (via L'Hôpital's rule) as x, which matches your S_0(x) = x check.
Since you've linked this to the Hurwitz Zeta function, are you planning to look into the "critical strip" values, or are you more interested in the combinatorial applications like Faulhaber's Formula?
