# Sequence Notation and Operations

## Basic Sequence Definitions

### Power Sequences
A power sequence of variable $x$ is denoted as:
$$\mathcal{P}_x = \{x^n\}_{n=1}^{\infty} = (x^1, x^2, x^3, \ldots)$$

For a general base $a$:
$$\mathcal{P}_a = \{a^n\}_{n=1}^{\infty} = (a^1, a^2, a^3, \ldots)$$

### Indexed Sequences
A general indexed sequence is denoted as:
$$\mathcal{A} = \{a_n\}_{n=1}^{\infty} = (a_1, a_2, a_3, \ldots)$$

Alternative notations for specific sequences:
- $\mathcal{B} = \{b_n\}_{n=1}^{\infty} = (b_1, b_2, b_3, \ldots)$
- $\mathcal{C} = \{c_n\}_{n=1}^{\infty} = (c_1, c_2, c_3, \ldots)$

## Sequence Operations

### Scalar Multiplication
For a scalar $k$ and sequence $\mathcal{A} = \{a_n\}_{n=1}^{\infty}$:
$$k \cdot \mathcal{A} = \{k \cdot a_n\}_{n=1}^{\infty} = (k \cdot a_1, k \cdot a_2, k \cdot a_3, \ldots)$$

**Example:**
If $\mathcal{A} = (2, 4, 6, \ldots)$ and $k = 3$, then:
$$3 \cdot \mathcal{A} = (6, 12, 18, \ldots)$$

### Hadamard Product (Element-wise Product)
For two sequences $\mathcal{A} = \{a_n\}_{n=1}^{\infty}$ and $\mathcal{B} = \{b_n\}_{n=1}^{\infty}$:
$$\mathcal{A} \odot \mathcal{B} = \{a_n \cdot b_n\}_{n=1}^{\infty} = (a_1 \cdot b_1, a_2 \cdot b_2, a_3 \cdot b_3, \ldots)$$

### Product of Indexed and Power Sequences
For an indexed sequence $\mathcal{A} = \{a_n\}_{n=1}^{\infty}$ and power sequence $\mathcal{P}_x = \{x^n\}_{n=1}^{\infty}$:
$$\mathcal{A} \odot \mathcal{P}_x = \{a_n \cdot x^n\}_{n=1}^{\infty} = (a_1 x^1, a_2 x^2, a_3 x^3, \ldots)$$

This can also be written as:
$$\sum_{n=1}^{\infty} a_n x^n$$

## Advanced Operations

### Sequence Addition
For sequences $\mathcal{A} = \{a_n\}_{n=1}^{\infty}$ and $\mathcal{B} = \{b_n\}_{n=1}^{\infty}$:
$$\mathcal{A} \oplus \mathcal{B} = \{a_n + b_n\}_{n=1}^{\infty} = (a_1 + b_1, a_2 + b_2, a_3 + b_3, \ldots)$$

### Convolution Product
For sequences $\mathcal{A} = \{a_n\}_{n=0}^{\infty}$ and $\mathcal{B} = \{b_n\}_{n=0}^{\infty}$:
$$(\mathcal{A} * \mathcal{B})_n = \sum_{k=0}^{n} a_k b_{n-k}$$

### Transformation Operators
Define linear operators that act on sequences:

#### Shift Operator $E$
$$E(\mathcal{A}) = E(\{a_n\}_{n=1}^{\infty}) = \{a_{n+1}\}_{n=1}^{\infty}$$

#### Difference Operator $\Delta$
$$\Delta(\mathcal{A}) = \{a_{n+1} - a_n\}_{n=1}^{\infty}$$

## Bell Polynomial Context

### Notation Clarification
We distinguish between:
- **Individual Bell polynomials** $B_{n,k}(x_1, x_2, \ldots, x_n)$ 
- **Complete Bell polynomials** $B_n(x_1, x_2, \ldots, x_n) = \sum_{k} B_{n,k}(x_1, x_2, \ldots, x_n)$

### Exponential Bell Polynomials
The complete exponential Bell polynomials $B_n(x_1, x_2, \ldots, x_n)$ can be constructed using sequence operations.

For a sequence $\mathcal{X} = \{x_n\}_{n=1}^{\infty}$, we define:
$$B_n(\mathcal{X}) = B_n(x_1, x_2, \ldots, x_n)$$

The complete Bell polynomials are defined by their exponential generating function:
$$\exp\left(\sum_{n=1}^{\infty} x_n \frac{t^n}{n!}\right) = \sum_{n=0}^{\infty} B_n(\mathcal{X}) \frac{t^n}{n!}$$

### Recursive Construction
The Bell polynomials satisfy the recursion:
$$B_{n+1}(\mathcal{X}) = \sum_{k=0}^{n} \binom{n}{k} B_k(\mathcal{X}) \cdot x_{n-k+1}$$

where $B_0(\mathcal{X}) = 1$.

**Note:** The individual Bell polynomials $B_{n,k}$ satisfy a different recursion where the sum ranges over different indices as specified by the user's construction.

### Lemma Template Structure
For lemmas involving Bell polynomials acting on sequences, use this template:

**Lemma [Number]:** *Statement about Bell polynomial operation on sequence*

**Proof:** 
1. *Step involving sequence notation*
2. *Application of Bell polynomial recursion*
3. *Conclusion using sequence operations*

### Fundamental Lemmas

**Lemma 1 (Scalar Factorization):** For any scalar $k$ and sequence $\mathcal{A} = \{a_n\}_{n=1}^{\infty}$:
$$B_n(k \cdot \mathcal{A}) = k^n B_n(\mathcal{A})$$

**Proof:** We proceed by induction on $n$.

*Base case:* For $n = 0$, we have $B_0(k \cdot \mathcal{A}) = 1 = k^0 \cdot 1 = k^0 B_0(\mathcal{A})$.

For $n = 1$, we have $B_1(k \cdot \mathcal{A}) = (k \cdot \mathcal{A})_1 = k \cdot a_1 = k^1 \cdot a_1 = k^1 B_1(\mathcal{A})$.

*Inductive step:* Assume the lemma holds for all $j \leq n$, i.e., $B_j(k \cdot \mathcal{A}) = k^j B_j(\mathcal{A})$ for all $j \leq n$.

We need to show that $B_{n+1}(k \cdot \mathcal{A}) = k^{n+1} B_{n+1}(\mathcal{A})$.

Using the Bell polynomial recursion formula:
$$B_{n+1}(k \cdot \mathcal{A}) = \sum_{j=0}^{n} \binom{n}{j} B_j(k \cdot \mathcal{A}) \cdot (k \cdot \mathcal{A})_{n-j+1}$$

Since $(k \cdot \mathcal{A})_{n-j+1} = k \cdot a_{n-j+1}$, and by the inductive hypothesis $B_j(k \cdot \mathcal{A}) = k^j B_j(\mathcal{A})$:
$$B_{n+1}(k \cdot \mathcal{A}) = \sum_{j=0}^{n} \binom{n}{j} k^j B_j(\mathcal{A}) \cdot k \cdot a_{n-j+1}$$

$$= k \sum_{j=0}^{n} \binom{n}{j} k^j B_j(\mathcal{A}) \cdot a_{n-j+1}$$

$$= k \cdot k^n \sum_{j=0}^{n} \binom{n}{j} k^{j-n} B_j(\mathcal{A}) \cdot a_{n-j+1}$$

Since we can factor out the highest power:
$$= k^{n+1} \sum_{j=0}^{n} \binom{n}{j} B_j(\mathcal{A}) \cdot a_{n-j+1}$$

$$= k^{n+1} B_{n+1}(\mathcal{A})$$

Therefore, by mathematical induction, $B_n(k \cdot \mathcal{A}) = k^n B_n(\mathcal{A})$ for all $n \geq 0$. □

## Special Sequence Types

### Factorial Sequences
$$\mathcal{F} = \{n!\}_{n=1}^{\infty} = (1!, 2!, 3!, \ldots)$$

### Stirling Number Sequences
Second kind: $\mathcal{S}_2^{(n)} = \{S(n,k)\}_{k=1}^{n}$
First kind: $\mathcal{S}_1^{(n)} = \{s(n,k)\}_{k=1}^{n}$

### Moments Sequences
For a probability distribution: $\mathcal{M} = \{\mu_n\}_{n=1}^{\infty}$

## Notation Summary

| Symbol | Meaning |
|--------|---------|
| $\mathcal{P}_x$ | Power sequence in $x$ |
| $\mathcal{A}$ | General indexed sequence |
| $k \cdot \mathcal{A}$ | Scalar multiplication |
| $\mathcal{A} \odot \mathcal{B}$ | Hadamard product |
| $\mathcal{A} \oplus \mathcal{B}$ | Element-wise addition |
| $\mathcal{A} * \mathcal{B}$ | Convolution |
| $E(\mathcal{A})$ | Shift operator |
| $\Delta(\mathcal{A})$ | Difference operator |
| $B_n(\mathcal{X})$ | Bell polynomial on sequence |
