# Generalized Factorial Polynomials & Stirling Coefficients - Quick Reference

## Basic Definitions

$$P(x,a,m) = x(x+a)(x+2a)\cdots(x+(m-1)a)$$

$$P(x,a,m) = \sum_{n=0}^{m} S_{m,n}(a,b) \cdot P(x,b,n)$$

**Special Cases:**
- $P(x,0,m) = x^m$  
- $P(x,1,m) = x(x+1)\cdots(x+m-1)$
- $P(x,-1,m) = x(x-1)\cdots(x-m+1)$

## Classical Stirling Numbers

| Type | Symbol | Parameters |
|------|--------|------------|
| **2nd Kind** | $\left\{\begin{array}{c}m\\n\end{array}\right\}$ | $S_{m,n}(1,0)$ |
| **1st Kind (Unsigned)** | $\left[\begin{array}{c}m\\n\end{array}\right]$ | $S_{m,n}(0,-1)$ |
| **1st Kind (Signed)** | $s(m,n)$ | $S_{m,n}(0,1)$ |

## Stirling Number Tables

**Second Kind** $\left\{\begin{array}{c}m\\n\end{array}\right\}$

| $m \setminus n$ | **1** | **2** | **3** | **4** | **5** |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | 1 | 0 | 0 | 0 | 0 |
| **2** | 1 | 1 | 0 | 0 | 0 |
| **3** | 1 | 3 | 1 | 0 | 0 |
| **4** | 1 | 7 | 6 | 1 | 0 |
| **5** | 1 | 15 | 25 | 10 | 1 |

**Unsigned First Kind** $\left[\begin{array}{c}m\\n\end{array}\right]$

| $m \setminus n$ | **1** | **2** | **3** | **4** | **5** |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | 1 | 0 | 0 | 0 | 0 |
| **2** | 1 | 1 | 0 | 0 | 0 |
| **3** | 2 | 3 | 1 | 0 | 0 |
| **4** | 6 | 11 | 6 | 1 | 0 |
| **5** | 24 | 50 | 35 | 10 | 1 |

## Key Properties

$$S_{m,n}(a,a) = [m=n]$$
$$S_{m,n}(a,b) = 0 \text{ for } n > m$$
$$\mathbf{S}(a,b) \cdot \mathbf{S}(b,a) = \mathbf{I}$$

## Recurrence Relations

$$\left\{\begin{array}{c}m+1\\n\end{array}\right\} = n \left\{\begin{array}{c}m\\n\end{array}\right\} + \left\{\begin{array}{c}m\\n-1\end{array}\right\}$$

$$\left[\begin{array}{c}m+1\\n\end{array}\right] = m \left[\begin{array}{c}m\\n\end{array}\right] + \left[\begin{array}{c}m\\n-1\end{array}\right]$$

$$P(x,a,m+1) = P(x,a,m) \cdot (x + ma)$$

## Scaling Relationships

$$S_{m,n}(a,0) = a^{m-n} \left\{\begin{array}{c}m\\n\end{array}\right\}$$

$$S_{m,n}(0,b) = b^{-n} s(m,n)$$

$$S_{m,n}(0,-b) = (-1)^n b^{-n} \left[\begin{array}{c}m\\n\end{array}\right]$$

## Gamma Function Representation

$$P(x,a,m) = a^m \frac{\Gamma(x/a + m)}{\Gamma(x/a)} \quad (a \neq 0)$$

## Derivatives

$$\frac{d}{dx} P(x,a,m) = P(x,a,m) \sum_{k=0}^{m-1} \frac{1}{x + ak} \quad (a \neq 0)$$

$$\frac{d}{dx} P(x,0,m) = m x^{m-1}$$

## Matrix Inverse Pairs

$$\sum_{k=0}^{m} s(m,k) \left\{\begin{array}{c}k\\n\end{array}\right\} = [m=n]$$

$$\sum_{k=0}^{m} \left[\begin{array}{c}m\\k\end{array}\right\] \cdot S_{k,n}(-1,0) = [m=n]$$

## Lah Numbers

$$L(m,n) = \binom{m-1}{n-1} \frac{m!}{n!}$$

$$S_{m,n}(1,-1) = (-1)^{m-n} L(m,n)$$
