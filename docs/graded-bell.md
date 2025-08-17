# Graded Bell Polynomials: Beta Definition and Recurrence

Let $\alpha = (\alpha_1,\alpha_2,\ldots)$ be a sequence. Define the family $\{\beta_{m,n}(\alpha)\}_{m,n \ge 0}$ by the bases
\[
\beta_{0,0}(\alpha)=1,\qquad
\beta_{m,0}(\alpha)=0\ \ (m>0),\qquad
\beta_{m,n}(\alpha)=0\ \ \text{if } n>m \text{ or } n<0,
\]
and for $m,n \ge 1$ the recurrence
\[
\beta_{m,n}(\alpha)
= \frac{1}{n}\sum_{j=n-1}^{m-1} \alpha_{\,m-j}\, \beta_{j,\,n-1}(\alpha).
\]
Equivalently, with the index shift $k = m-j$,
\[
\beta_{m,n}(\alpha)
= \frac{1}{n}\sum_{k=1}^{m-n+1} \alpha_k\, \beta_{\,m-k,\,n-1}(\alpha).
\]

## Combinatorial Interpretation (Partitions)

Interpret $\beta$ as encoding partitions of an $m$-set into $n$ nonempty unlabeled parts by monomials:
- A partition type is specified by counts $(m_1, m_2, \ldots)$ with $\sum_j m_j = n$ and $\sum_j j m_j = m$.
- The monomial attached to a partition type is $\prod_{j \ge 1} \alpha_j^{m_j}$, where $\alpha_j$ weights a part of size $j$.
- The graded (ordinary) perspective omits multinomial coefficients (unlike the exponential case).

Two closely related recurrences appear in the literature:

1) Normalized graded form (this document’s $\beta$, with $1/n$)
- Bases:
  $\beta_{0,0}(\alpha)=1$; $\beta_{m,0}(\alpha)=0$ $(m>0)$; $\beta_{m,n}(\alpha)=0$ if $n>m$ or $n<0$.
- Recurrence:
  $\beta_{m,n}(\alpha) = (1/n) \sum_{j=1}^{m-n+1} \alpha_j \cdot \beta_{m-j,n-1}(\alpha)$.

2) Unnormalized graded form (no $1/n$; convenient for direct partition-building)
- Bases:
  $\overline{B}_{0,0}(\alpha)=1$; $\overline{B}_{m,0}(\alpha)=0$ $(m>0)$; $\overline{B}_{m,n}(\alpha)=0$ if $n>m$ or $n<0$.
- Recurrence:
  $\overline{B}_{m,n}(\alpha) = \sum_{j=1}^{m-n+1} \alpha_j \cdot \overline{B}_{m-j,n-1}(\alpha)$.

Relationship
- The $1/n$ factor symmetrizes the creation of the $n$ parts. A convenient link is
  $n! \cdot \beta_{m,n}(\alpha) = \sum$ over ordered builds of $n$ parts $\prod \alpha_{\text{size(part)}}$.
  In particular, for single partition types, $\beta_{m,n}$ differs from $\overline{B}_{m,n}$ by a simple normalization.

Example ($m=4$, $n=3$)
- The only partition type is $2+1+1$, so the graded (unnormalized) polynomial is
  $\overline{B}_{4,3}(\alpha) = \alpha_1^2 \alpha_2$.
- Using the normalized recurrence (with $1/n$) yields
  $\beta_{4,3}(\alpha) = (1/2) \alpha_1^2 \alpha_2$.

## Triangular Matrix (first 6 rows) for \(\beta_{m,n}(\alpha)\)

Let \(\alpha=(\alpha_1,\alpha_2,\ldots)\). The lower-triangular array \(\big(\beta_{m,n}(\alpha)\big)_{0\le m,n\le 5}\) is:

\[
\begin{array}{c|cccccc}
 & n=0 & 1 & 2 & 3 & 4 & 5 \\
\hline
m=0 & 1 & 0 & 0 & 0 & 0 & 0 \\
1 & 0 & \alpha_1 & 0 & 0 & 0 & 0 \\
2 & 0 & \alpha_2 & \dfrac{\alpha_1^2}{2!} & 0 & 0 & 0 \\
3 & 0 & \alpha_3 & \alpha_1\alpha_2 & \dfrac{\alpha_1^3}{3!} & 0 & 0 \\
4 & 0 & \alpha_4 & \alpha_1\alpha_3 + \dfrac{\alpha_2^2}{2} & \dfrac{\alpha_1^2\alpha_2}{2} & \dfrac{\alpha_1^4}{4!} & 0 \\
5 & 0 & \alpha_5 & \alpha_1\alpha_4 + \alpha_2\alpha_3 & \dfrac{\alpha_1^2\alpha_3 + \alpha_1\alpha_2^2}{2} & \dfrac{\alpha_1^3\alpha_2}{3!} & \dfrac{\alpha_1^5}{5!}
\end{array}
\]

In particular, the main diagonal is
\[
\beta_{m,m}(\alpha)=\frac{\alpha_1^m}{m!}\quad(m\ge 0),
\]
since the only partition of \(m\) into \(m\) parts is \(1+\cdots+1\).

### Compact submatrix (m,n ≥ 1)

Excluding the first row and column (m=0, n=0), the 5×5 lower-triangular submatrix \((\beta_{m,n}(\alpha))_{1\le m,n\le 5}\) is:
\[
\begin{pmatrix}
\alpha_1 & 0 & 0 & 0 & 0 \\
\alpha_2 & \dfrac{\alpha_1^2}{2!} & 0 & 0 & 0 \\
\alpha_3 & \alpha_1\alpha_2 & \dfrac{\alpha_1^3}{3!} & 0 & 0 \\
\alpha_4 & \alpha_1\alpha_3 + \dfrac{\alpha_2^2}{2} & \dfrac{\alpha_1^2\alpha_2}{2} & \dfrac{\alpha_1^4}{4!} & 0 \\
\alpha_5 & \alpha_1\alpha_4 + \alpha_2\alpha_3 & \dfrac{\alpha_1^2\alpha_3 + \alpha_1\alpha_2^2}{2} & \dfrac{\alpha_1^3\alpha_2}{3!} & \dfrac{\alpha_1^5}{5!}
\end{pmatrix}
\]

### How entries relate to partitions

For fixed \(m,n\), write a partition of \(m\) into \(n\) parts as counts \((m_1,m_2,\ldots)\) with \(\sum_j m_j=n\) and \(\sum_j j\,m_j=m\). Then
\[
\beta_{m,n}(\alpha)=\sum_{\substack{\sum m_j=n\\ \sum j\,m_j=m}}
\frac{1}{\prod_j m_j!}\;\prod_{j\ge 1} \alpha_j^{\,m_j}.
\]
- Each monomial \(\prod \alpha_j^{m_j}\) corresponds to a partition type with \(m_j\) parts of size \(j\).
- The factor \(1/\prod_j m_j!\) reflects the unlabeled (graded) nature: it divides by permutations of equal-sized parts.
- Examples above:
  - \(\beta_{4,2}=\alpha_1\alpha_3+\tfrac{1}{2}\alpha_2^2\) comes from types \(3+1\) and \(2+2\) with weights \(1\) and \(1/2!\).
  - \(\beta_{5,3}=\tfrac{1}{2}(\alpha_1^2\alpha_3+\alpha_1\alpha_2^2)\) from types \(3+1+1\) and \(2+2+1\), each with weight \(1/(2!)\).

### Subdiagonal pattern \(\beta_{m,m-1}(\alpha)\)

For all \(m\ge 2\),
\[
\boxed{\;\beta_{m,m-1}(\alpha)=\alpha_2\,\frac{\alpha_1^{\,m-2}}{(m-2)!}\;}
\]

Reason 1 (combinatorial). The only partition of \(m\) into \(m-1\) parts is \(2+1+\cdots+1\) (one 2 and \(m-2\) ones). The graded weight is
\[
\frac{1}{(m_2)!\,(m_1)!}\,\alpha_2^{\,m_2}\alpha_1^{\,m_1}
=\frac{1}{1!\,(m-2)!}\,\alpha_2\,\alpha_1^{\,m-2}
=\alpha_2\,\frac{\alpha_1^{\,m-2}}{(m-2)!}.
\]

Reason 2 (recurrence). Using
\[
\beta_{m,m-1}=\frac{1}{m-1}\Big(\alpha_1\,\beta_{m-1,m-2}+\alpha_2\,\beta_{m-2,m-2}\Big),
\]
the induction hypotheses \(\beta_{m-1,m-2}=\alpha_2\,\alpha_1^{\,m-3}/(m-3)!\) and
\(\beta_{m-2,m-2}=\alpha_1^{\,m-2}/(m-2)!\) give
\[
\beta_{m,m-1}
=\frac{\alpha_2\,\alpha_1^{\,m-2}}{m-1}\!\left(\frac{1}{(m-3)!}+\frac{1}{(m-2)!}\right)
=\alpha_2\,\frac{\alpha_1^{\,m-2}}{(m-2)!}.
\]

This matches the subdiagonal entries in the matrix:
\(\beta_{3,2}=\alpha_1\alpha_2\), \(\beta_{4,3}=\tfrac{1}{2}\alpha_1^2\alpha_2\), \(\beta_{5,4}=\tfrac{1}{3!}\alpha_1^3\alpha_2\).
