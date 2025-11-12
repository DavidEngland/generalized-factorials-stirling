# Minimal peas to weigh up to N grams on a balance

Setting
- Allowed pea weights (grams): W = {1, 2, 5, 10}. You can use peas on both pans (two‑pan balance), so each pea contributes −w, 0, or +w.
- Goal: For a given integer N ≥ 0, find the least number of peas so that every integer mass 1..N is weighable.

Two‑pan coverage lemma (standard)
- Let w1 ≤ w2 ≤ … be a multiset of positive weights. Write Rk for the largest integer mass you can guarantee to weigh (i.e., every t with 0 ≤ t ≤ Rk is representable using signs in {−1,0,1}).
- If R0 = 0 and at step k you add a new weight w,
  - Necessity and sufficiency: w ≤ 2R_{k−1} + 1.
  - Then Rk = R_{k−1} + w.
- Proof sketch: with two pans you cover [−R_{k−1}, R_{k−1}]. Adding ±w enlarges coverage to [−(R_{k−1}+w), R_{k−1}+w] with no gap iff w ≤ 2R_{k−1}+1.

Greedy optimality
- To minimize the number of peas for a target N, iteratively pick the largest available weight w ∈ W that satisfies w ≤ 2R + 1 until R ≥ N. This minimizes the count because each step maximizes range growth per pea.

Closed form for W = {1,2,5,10}
- Start R = 0.
  1) Add 1 (since 1 ≤ 1): R = 1.
  2) Next admissible ≤ 2·1+1 = 3 → pick 2: R = 3.
  3) Next admissible ≤ 2·3+1 = 7 → pick 5: R = 8.
  4) Next admissible ≤ 2·8+1 = 17 → pick 10: R = 18.
  5+) Thereafter 10 ≤ 2R+1 always holds, so each extra 10 increases coverage by 10: R → R+10.

Therefore the minimal number of peas m(N) is:
- N = 0: m = 0.
- 1 ≤ N ≤ 1: m = 1.
- 2 ≤ N ≤ 3: m = 2.
- 4 ≤ N ≤ 8: m = 3.
- 9 ≤ N ≤ 18: m = 4.
- N ≥ 19: m = 4 + ceil((N − 18)/10).

Composition (one optimal multiset)
- For N ≤ 18: {1,2,5,10} truncated appropriately as above.
- For N > 18: {1,2,5} plus (k) copies of 10 where k = 1 + ceil((N − 18)/10); any further extras beyond reaching N are unnecessary.

One‑pan variant (for comparison)
- With a single pan (weights only on one side), the coverage lemma becomes w ≤ R + 1 and R → R + w; the same greedy rule (largest admissible w) is optimal.

Generating‑function remark
- Idea: build a formal catalogue of all ways to place peas. Use:
  • x = marker for total net weight on the right pan.
  • y = marker for how many peas you used (regardless of which pan).
- One pea of weight w has three choices:
  • not used: contributes 1 (weight 0, peas 0),
  • on right pan: contributes y·x^{+w},
  • on left pan: contributes y·x^{−w} (subtracts w from the right‑pan total).
  So for one weight w the contribution is: 1 + y x^{w} + y x^{−w}.
- If all weights in your set W are independent choices, multiply these factors:
  \[
  F(x,y)=\prod_{w\in W}\bigl(1 + y x^{w} + y x^{-w}\bigr).
  \]
- Group the symmetric ± terms:
  \[
  1 + y x^{w} + y x^{-w} = 1 + y(x^{w}+x^{-w}) = 1 + 2y x^{w} \text{ (after re‑indexing powers when collecting positive weights)}.
  \]
  This yields the (purely positive‑power) form often written as
  \[
  \prod_{w\in W}\bigl(1 + 2\sum_{m\ge1} y^{m} x^{m w}\bigr),
  \]
  because choosing x^{−w} can be seen as contributing a positive power after a global sign shift; the key point is “two ways” (±) for each positive multiple m·w.
- How to read coefficients:
  Expand F(x,y). A term y^{k} x^{N} means: there is a way to reach net weight N using exactly k peas
    return len(used), used

# Examples:
# N=18 -> (4, [1,2,5,10]); N=37 -> (6, [1,2,5,10,10,10])
````

## Choosing peas optimally (design weights for a given N)

Goal
- Pick a multiset of peas (weights) so that every integer mass 1..N is weighable on a two‑pan balance using signs {−1,0,+1}, with the fewest peas (and, under proportional cost by mass, minimal total mass).

Balanced‑ternary optimum (classic)
- Let R be the guaranteed coverage after some peas; to avoid gaps and maximize new coverage per pea, each new weight must satisfy w ≤ 2R+1 (two‑pan coverage lemma). Equality w = 2R+1 achieves maximal expansion.
- Starting at R=0 and enforcing equality yields the unique sequence
  w_1 = 1, w_{i+1} = 2(1+3+…+3^{i-1}) + 1 = 3^i,
  i.e., weights {1, 3, 9, …, 3^{k-1}}.
- Coverage with k peas is R_k = (3^k − 1)/2. Hence the minimal number of peas for target N is
  k = ceil(log_3(2N+1)),
  and one optimal set is {3^0, 3^1, …, 3^{k-1}}.

Example (N=40)
- 2N+1 = 81 ⇒ log_3(81)=4 ⇒ k=4; weights {1,3,9,27} cover up to (3^4−1)/2=40 exactly.
- The alternative {2,6,18,54} fails: all weights are even, so odd targets (e.g., 1, 3, 5, …) are impossible. Moreover, with two‑pan optimality the smallest weight must be 1 to cover target 1.

Why this is optimal (sketch)
- If any step uses w < 2R+1, you leave a gap you cannot fill later without adding an extra pea, increasing the count.
- If any step uses w > 2R+1, you introduce an immediate gap, making some targets unreachable.
- Thus equality at each step minimizes both the number of peas and (under cost ∝ mass) the total mass.

Balanced‑ternary representation
- Every m ∈ [−R_k, R_k] has a unique signed base‑3 expansion m = ∑_{i=0}^{k-1} d_i 3^i with digits d_i ∈ {−1,0,1}, giving the placement of each pea (left, unused, right).

Compact Python helper
```python
# filepath: /Users/davidengland/Documents/GitHub/generalized-factorials-stirling/examples/partitions/partitions.md
import math

def optimal_two_pan_weights(N):
    """Return minimal count k and the optimal weight set for two-pan coverage up to N."""
    k = math.ceil(math.log(2*N + 1, 3)) if N > 0 else 0
    weights = [3**i for i in range(k)]
    return k, weights

def balanced_ternary_representation(m, weights):
    """Digits in {-1,0,1} for m using given powers-of-3 weights."""
    digits = []
    x = m
    for w in weights:
        # choose digit to keep remainder small: d ∈ {-1,0,1}
        # greedy by rounding to nearest multiple of w
        d = round(x / w) - round((x - w) / w)
        # simpler: use mod 3 rule with carry
        r = x % 3
        if r == 2: d = -1; x = (x + 1) // 3
        elif r == 1: d = 1; x = (x - 1) // 3
        else: d = 0; x = x // 3
        digits.append(d)
    return digits  # aligns with weights[0..]

# Example: N=40
# k=4, weights=[1,3,9,27]
```
