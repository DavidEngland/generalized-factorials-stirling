Creating accurate prompts for generating Bell polynomials requires clearly defining the desired type of polynomial, the input variables, and the desired output format. Below are prompts for both exponential (partial) and graded Bell polynomials, with explanations of the key components for each.

***

### Exponential Bell Polynomials ($B_{n,k}$)

These are the standard, most common type of Bell polynomials. They are used in contexts involving exponential generating functions and represent the ways to partition a set of $n$ elements into $k$ non-empty subsets. They include multinomial coefficients in their expansion.

#### Prompt Elements
A good prompt should specify:
* **The type:** "Exponential Bell polynomial," "partial Bell polynomial," or "Bell polynomial of the second kind."
* **The parameters:** The number of elements to partition ($n$) and the number of subsets ($k$).
* **The variables:** The sequence of variables $\{x_i\}$, often written as $\{x_1, x_2, \ldots, x_{n-k+1}\}$.
* **The output format:** The explicit polynomial expansion, the generating function, or the combinatorial formula.

#### Example Prompts
1.  **For an explicit polynomial:** "Generate the exponential Bell polynomial $B_{5,3}$ in terms of the variables $x_1, x_2, \ldots, x_3$."
2.  **For the generating function:** "Provide the bivariate exponential generating function for the partial Bell polynomials $B_{n,k}(x_1, x_2, \ldots)$."
3.  **For the combinatorial formula:** "Express the exponential Bell polynomial $B_{n,k}(x_1, x_2, \ldots)$ using its combinatorial sum over integer partitions."

---

### Graded Bell Polynomials ($\mathcal{B}^{(g)}_{n,k}$)

These are a less common variant, sometimes called "partition polynomials," that are used in the theory of ordinary generating functions. They omit the multinomial coefficients found in exponential Bell polynomials and focus purely on the structure of the partitions themselves. 

#### Definition and bases
- Combinatorial sum (no multinomial weights):
  \[
  \mathcal{B}^{(g)}_{n,k}(x_1,x_2,\ldots)=
  \sum_{\substack{m_1,m_2,\ldots\ge 0\\ \sum_j m_j = k\\ \sum_j j\,m_j = n}}
  \prod_{j\ge 1} x_j^{\,m_j}.
  \]
- Bases:
  \[
  \mathcal{B}^{(g)}_{0,0}=1,\quad
  \mathcal{B}^{(g)}_{n,0}=0\ (n>0),\quad
  \mathcal{B}^{(g)}_{n,k}=0\ \text{if }n<k\text{ or }n<0\text{ or }k<0.
  \]
- Recurrence (bounds j=1..n−k+1):
  \[
  \mathcal{B}^{(g)}_{n,k}=\sum_{j=1}^{n-k+1} x_j\,\mathcal{B}^{(g)}_{n-j,k-1}.
  \]

#### Relation to exponential Bell polynomials
- Exponential (partial) Bell polynomials include multinomial/binomial normalizations; graded omit them. A common conversion is
  \[
  B_{n,k}(x_1,x_2,\ldots)=
  \sum_{\substack{\sum m_j=k\\ \sum j m_j=n}}
  \frac{n!}{\prod_j (j!)^{m_j}\,m_j!}\ \prod_j x_j^{\,m_j},
  \]
  while \(\mathcal{B}^{(g)}_{n,k}\) uses just \(\prod_j x_j^{m_j}\).

#### Prompt Elements
A good prompt should specify:
- The type: “graded Bell polynomial” (partition polynomial, unweighted).
- The parameters: integers \(n\) (total size) and \(k\) (number of parts).
- The variables: \(\{x_i\}\) where \(x_i\) weights a part of size \(i\).
- Normalization: state explicitly “no multinomial coefficients” and whether any \(j!\) scaling is desired (usually none for graded).
- Base cases and domain: \(\mathcal{B}^{(g)}_{0,0}=1\), zeros for invalid \(n,k\).
- Output format: explicit polynomial, combinatorial sum, or recurrence; optional small numeric example.
- Bounds in sums: use \(j=1..(n-k+1)\) in the recurrence.

#### Example Prompts
1. Explicit polynomial
   - “Generate the graded Bell polynomial \(\mathcal{B}^{(g)}_{6,2}(x_1,\ldots,x_5)\) as an explicit sum of monomials (no multinomial coefficients).”
2. Combinatorial sum
   - “Provide the combinatorial sum for \(\mathcal{B}^{(g)}_{n,k}(x_1,x_2,\ldots)\) over \((m_j)\) with \(\sum m_j=k\), \(\sum j m_j=n\), and no multinomial factors.”
3. Recurrence
   - “State and use the recurrence \(\mathcal{B}^{(g)}_{n,k}=\sum_{j=1}^{n-k+1} x_j\,\mathcal{B}^{(g)}_{n-j,k-1}\) with bases \(\mathcal{B}^{(g)}_{0,0}=1\), \(\mathcal{B}^{(g)}_{n,0}=0\ (n>0)\).”
4. Evaluation example
   - “Evaluate \(\mathcal{B}^{(g)}_{4,3}\) symbolically and then at \(x_1=a_1,x_2=a_2,x_3=a_3,x_4=a_4\).”
5. Specializations
   - “Compute \(\mathcal{B}^{(g)}_{n,k}(1,1,\ldots)\) and interpret combinatorially.”
   - “Compute \(\mathcal{B}^{(g)}_{n,k}(0!,1!,2!,\ldots)\) and compare with cycle-count specializations.”
6. Relation to exponential Bell
   - “Given \(\mathcal{B}^{(g)}_{n,k}\), write \(B_{n,k}\) and explain the multinomial/j! normalization differences.”
7. Bounds and zero-cases
   - “Show \(\mathcal{B}^{(g)}_{n,k}=0\) for \(n<k\) and provide a short proof via the recurrence.”