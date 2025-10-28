I'm having a difficult time finding the degree and basis of $\mathbb{Q}(\sqrt{5}, \sqrt{7})$ over $\mathbb{Q}$.

I know that $\sqrt{7}$ satisfies $f(x) = x^2 - 7$ and is irreducible over $\mathbb{Q}$. So $[\mathbb{Q}(\sqrt{7}) : \mathbb{Q}] = 2$. I also know that $\sqrt{5}$ satisfies $f(x) = x^2 - 5$ which is also irreducible in $\mathbb{Q}$. So $[\mathbb{Q(\sqrt{5})}: \mathbb{Q}] = 2$.

Then by some corollary which I forget the name of $[\mathbb{Q}(\sqrt{5}, \sqrt{7}) : \mathbb{Q}] \leq 4$.

I am unsure of what to do from here.

Textbook solution (degree and basis of Q(√5,√7))

1) Basic facts.
- Both x^2−5 and x^2−7 are irreducible over Q, so [Q(√5):Q]=2 and [Q(√7):Q]=2.
- Hence [Q(√5,√7):Q] is 1, 2, or 4. It equals 1 only if √5∈Q (false), equals 2 only if √5∈Q(√7) (check next), otherwise 4.

2) Show √5 ∉ Q(√7).
Assume for contradiction √5 = a + b√7 with a,b ∈ Q. Square both sides:
5 = a^2 + 7b^2 + 2ab√7.
Equating rational and √7 parts yields 2ab = 0 and a^2 + 7b^2 = 5.
If b = 0 then a^2 = 5, impossible in Q. If a = 0 then 7b^2 = 5 ⇒ b^2 = 5/7, impossible in Q. Thus no rational a,b exist, so √5 ∉ Q(√7).

3) Conclusion: degree and basis.
Therefore [Q(√5,√7):Q] = 2·2 = 4 and a convenient Q‑basis is
{1, √5, √7, √35}.
Equivalently every element can be written uniquely as r0 + r1√5 + r2√7 + r3√35 with r_i ∈ Q.

4) Additional standard remarks (textbook).
- The extension is Galois with Galois group isomorphic to the Klein four V4: the four automorphisms independently send √5 ↦ ±√5 and √7 ↦ ±√7.
- Norms and traces from Q(√5,√7) to Q factor multiplicatively through the quadratic subextensions; these are standard exercises.

Connection to log(p) and von Mangoldt

1) Q‑linear independence of prime logs.
- If rational numbers q_i satisfy ∑ q_i log p_i = 0, multiply through by a common denominator to obtain an integer relation ∑ n_i log p_i = 0, i.e. log(∏ p_i^{n_i}) = 0, so ∏ p_i^{n_i} = 1. Since primes >1, all n_i = 0. Thus the real numbers {log p : p prime} are linearly independent over Q.
- In particular log 5 and log 7 are Q‑linearly independent.

2) How this ties to Λ(n).
- By definition Λ(n) is 0 except on prime powers where Λ(p^r)=log p. Thus for each n the value Λ(n) is exactly one of the prime logs (or zero). Partial sums Ψ(x)=∑_{n≤x}Λ(n) and their differentiated analogues Ψ_k involve linear combinations (with integer coefficients coming from counts of prime powers) of the independent set {log p}.
- One may therefore view the von Mangoldt data as living in the Q‑vector space spanned by {log p : p prime}. This is an infinite-dimensional Q‑vector space; for computational work with finitely many primes (say up to X) the relevant subspace is finite-dimensional and has the obvious basis of those log p.

3) Interpretation and caveats.
- The algebraic number field Q(√5,√7) and the transcendental Q‑vector space spanned by prime logs are different types of objects: the former is a finite algebraic extension of Q, the latter an infinite-dimensional real vector space. The superficial similarity is the use of a Q‑basis in both contexts, but their arithmetic natures differ (algebraic vs transcendental).
- The cumulant/hierarchy viewpoint in your notes uses log n (and so log p) as natural weights; the Q‑independence of log p justifies treating the prime contributions as independent coordinates when reconstructing sums from zero contributions numerically.

Practical notes for experiments / student
- Use the basis {1,√5,√7,√35} for symbolic algebra in this field.
- When working numerically with von Mangoldt sums up to X, treat the finite set {log p : p ≤ X} as a Q‑basis for the computation of linear relations (integer coefficients arise naturally).
- Remember the key distinction: algebraic independence vs Q‑linear independence. Logs of primes are believed transcendental but we only needed the elementary Q‑linear independence above.

Generalization: distinct primes p and q

Claim. Let p and q be distinct primes. Then
[Q(√p, √q) : Q] = 4 and a Q‑basis is {1, √p, √q, √(pq)}.

Proof (short). The minimal polynomials x^2−p and x^2−q are irreducible over Q, so [Q(√p):Q] = [Q(√q):Q] = 2 and the compositum degree divides 4. If √p ∈ Q(√q) then there exist a,b∈Q with √p = a + b√q. Squaring gives
p = a^2 + q b^2 + 2ab√q,
so 2ab = 0 and a^2 + q b^2 = p. If b = 0 then a^2 = p (impossible in Q). If a = 0 then q b^2 = p, impossible in Q. Hence √p ∉ Q(√q), so the degree is 4 and {1, √p, √q, √(pq)} is a basis.

Remarks and small variants
- If p = q then Q(√p,√q) = Q(√p) and the degree is 2.
- The same argument works for distinct squarefree integers m,n: if neither √m nor √n lies in Q the degree is 4 unless one is a rational multiple of the other’s square (rare in squarefree setting).
- The extension is Galois with group ≅ C2×C2; automorphisms flip independent signs of the two square roots.

Q‑linear independence of prime logs and tie to von Mangoldt
- For distinct primes p≠q the real numbers log p and log q are Q‑linearly independent: a rational relation r log p + s log q = 0 with r,s∈Q implies an integer relation (clearing denominators) n log p + m log q = 0 ⇒ log(p^n q^m)=0 ⇒ p^n q^m = 1 ⇒ n=m=0.
- Consequently log 5 and log 7 are Q‑linearly independent; more generally the set {log p : p prime} is Q‑linearly independent.
- Relation to Λ(n): Λ(n) equals log p when n = p^r (prime power) and 0 otherwise. Thus the von Mangoldt values lie in the Q‑vector space spanned by the prime logs. For numerical reconstructions using finitely many primes (e.g., primes ≤X) treat {log p : p ≤ X} as a finite Q‑basis for the relevant computations.
- Caveat: the field Q(√p,√q) is an algebraic finite extension, whereas the Q‑span of prime logs is an (infinite) real vector space of transcendental nature—superficially similar (use of a Q‑basis) but fundamentally different objects.

Practical note
- Use the same algebraic-basis logic for any pair of distinct primes p,q (5 and 7 are the concrete example). For experiments with von Mangoldt sums, the independence of log p justifies treating prime contributions as independent coordinates when reconstructing linear relations numerically.