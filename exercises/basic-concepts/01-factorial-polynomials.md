# Exercise 1: Understanding Generalized Factorial Polynomials

## Quick Theory Review

A **generalized factorial polynomial** is defined as:
$$P(x,a,m) = x(x+a)(x+2a)\cdots(x+(m-1)a)$$

**Special cases:**
- $P(x,0,m) = x^m$ (monomials)
- $P(x,1,m) = x(x+1)(x+2)\cdots(x+m-1)$ (rising factorials)
- $P(x,-1,m) = x(x-1)(x-2)\cdots(x-m+1)$ (falling factorials)

## Warm-up Calculations

**Problem 1.1:** Calculate by hand
1. $P(3,2,3)$
2. $P(5,1,4)$ 
3. $P(4,0,3)$
4. $P(6,-1,3)$

**Problem 1.2:** Verify the recurrence relation
Starting with $P(x,a,m+1) = P(x,a,m) \cdot (x + ma)$:
1. Use $P(2,3,2) = 2 \cdot 5 = 10$ to find $P(2,3,3)$
2. Check your answer by direct calculation

**Problem 1.3:** Pattern recognition
Calculate $P(1,1,n)$ for $n = 1,2,3,4,5$. What do you notice?

## Hands-on Verification

**Problem 1.4:** Implement and test
```python
def P(x, a, m):
    """Calculate P(x,a,m) = x(x+a)(x+2a)...(x+(m-1)a)"""
    # YOUR CODE HERE
    pass

# Test cases - verify these give the expected results
assert P(3, 2, 3) == 3*5*7  # Should be 105
assert P(5, 1, 4) == 5*6*7*8  # Should be 1680
assert P(4, 0, 3) == 4**3  # Should be 64
```

**Problem 1.5:** Edge cases
What should happen when:
1. $m = 0$? 
2. $x = 0$ and $a \neq 0$?
3. $a = 0$ and $m > 0$?

Test your implementation with these cases.

## Your Turn

**Problem 1.6:** Derive the gamma function representation
Starting with the product definition, show that:
$$P(x,a,m) = a^m \frac{\Gamma(x/a + m)}{\Gamma(x/a)}$$
when $a \neq 0$.

**Hint:** Use the property $\Gamma(z+1) = z\Gamma(z)$.

**Problem 1.7:** Connection puzzle
If $P(x,2,3) = 315$ when $x = 5$, can you find $P(10,1,3)$ without direct calculation?

**Hint:** Think about the scaling relationship.

## Check Your Understanding

Before moving on, make sure you can:
- [ ] Calculate $P(x,a,m)$ by hand for small values
- [ ] Implement the function correctly in code
- [ ] Explain why $P(x,0,m) = x^m$
- [ ] Use the recurrence relation
- [ ] Connect to gamma functions (at least conceptually)

## Next Steps

Once comfortable with these basics, move on to:
- `02-classical-stirling-numbers.md` - Review the classical cases
- `../computational/verify-factorial-polynomials.py` - More extensive testing
