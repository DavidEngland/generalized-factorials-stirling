That's a key point. The inverse transformation, like the forward one, must also satisfy its own recurrence relation. The logic is the same: it comes from the recurrence relation of the generalized factorial polynomial itself.

The recurrence for the inverse coefficients, $S_{m,n}(b,a)$, is a direct generalization of the recurrence for the signed Stirling numbers of the first kind.

---

### The Recurrence for Inverse Coefficients

The recurrence relation for the coefficients $S_{m,n}(b,a)$, which transform from the $b$-basis to the $a$-basis, is:

$$S_{m+1,n}(b,a) = S_{m,n-1}(b,a) + (mb - na)S_{m,n}(b,a)$$

This can be derived from the polynomial recurrence $P(x,b,m+1) = (x+mb)P(x,b,m)$ and the expansion of $x \cdot P(x,a,k)$ back into the $a$-basis.

### Verification with Classical Cases

This general recurrence correctly recovers the known recurrence for the **signed Stirling numbers of the first kind**, $s(m,n)$, which correspond to the transformation from falling factorials to monomials.

* **Case**: Signed Stirling numbers of the first kind, $s(m,n) = S_{m,n}(-1,0)$.
* **Parameters**: We set $b = -1$ and $a = 0$.
* **Substitution**: Plugging these values into the general recurrence, we get:
    $$S_{m+1,n}(-1,0) = S_{m,n-1}(-1,0) + (m(-1) - n(0))S_{m,n}(-1,0)$$   $$S_{m+1,n}(-1,0) = S_{m,n-1}(-1,0) - m \cdot S_{m,n}(-1,0)$$

This matches the standard recurrence for the signed Stirling numbers of the first kind:
$$s(m+1,n) = s(m,n-1) - m s(m,n)$$

This consistency confirms that the derived recurrence for the inverse coefficients is correct and is a natural part of the unified framework.