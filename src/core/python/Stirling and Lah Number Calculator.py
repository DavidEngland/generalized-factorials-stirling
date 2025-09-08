# The Stirling and Lah Number Calculator
# This program demonstrates a bottom-up approach to calculating
# Stirling numbers of the first and second kind, and Lah numbers,
# using dynamic programming to "cache" results.

# ---
# Stirling Numbers of the Second Kind S(n, k)
# Combinatorial Meaning: The number of ways to partition a set of n
# elements into k non-empty, unlabeled subsets.
# Example: S(3, 2) = 3 because the set {1, 2, 3} can be partitioned
# into 2 subsets in 3 ways: {{1,2}, {3}}, {{1,3}, {2}}, {{2,3}, {1}}.
# ---

def stirling_second_kind(n, k):
    """
    Calculates S(n, k) using a bottom-up, dynamic programming approach.
    Recurrence: S(n, k) = S(n-1, k-1) + k * S(n-1, k)
    """
    if k == 0 or n < k:
        return 0

    # Create a 2D list (cache/table) to store results
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Base case: S(n, n) = 1 and S(n, 0) = 0 for n > 0
    # Also S(0, 0) = 1
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0:
                dp[i][j] = 0
            elif i == j:
                dp[i][j] = 1
            else:
                # Apply the recurrence relation
                dp[i][j] = dp[i-1][j-1] + j * dp[i-1][j]

    return dp[n][k]

# ---
# Unsigned Stirling Numbers of the First Kind |s(n, k)|
# Combinatorial Meaning: The number of ways to permute n elements
# into k disjoint cycles.
# Example: |s(3, 2)| = 3 because the set {1, 2, 3} can be permuted
# into 2 cycles in 3 ways: {(1)(2,3)}, {(2)(1,3)}, {(3)(1,2)}.
# ---

def stirling_first_kind(n, k):
    """
    Calculates |s(n, k)| using a bottom-up, dynamic programming approach.
    Recurrence: |s(n, k)| = |s(n-1, k-1)| + (n-1) * |s(n-1, k)|
    """
    if k == 0 or n < k:
        return 0

    # Create a 2D list (cache/table) to store results
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Base cases: |s(n, n)| = 1 and |s(n, 0)| = 0 for n > 0
    # Also |s(0, 0)| = 1
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if i == j:
                dp[i][j] = 1
            else:
                # Apply the recurrence relation
                dp[i][j] = dp[i-1][j-1] + (i - 1) * dp[i-1][j]

    return dp[n][k]

# ---
# Lah Numbers L(n, k)
# Combinatorial Meaning: The number of ways to partition a set of n
# elements into k non-empty, ordered subsets.
# Example: L(3, 2) = 6 because {{1,2}, {3}} is different from {{3}, {1,2}}.
# The partitions {{1,2},{3}}, {{1,3},{2}}, {{2,3},{1}} each can be ordered
# in 2 ways, giving 3 * 2 = 6 total ways.
# ---

def lah_number(n, k):
    """
    Calculates L(n, k) using a bottom-up, dynamic programming approach.
    Recurrence: L(n, k) = L(n-1, k-1) + (n+k-1) * L(n-1, k)
    """
    if k == 0 or n < k:
        return 0

    # Create a 2D list (cache/table) to store results
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Base cases: L(n, n) = n! and L(n, 0) = 0 for n > 0
    # L(0, 0) = 1
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if i == j:
                dp[i][j] = 1 # The base case is actually 1 for L(n,n)
            elif j == 1:
                dp[i][j] = i * dp[i-1][j] # Recurrence simplifies to i! in this column.
            else:
                # Apply the recurrence relation
                dp[i][j] = dp[i-1][j-1] + (i + j - 1) * dp[i-1][j]

    return dp[n][k]

if __name__ == "__main__":
    # Test cases
    n_val = 5
    k_val = 3

    print("--- Bottom-Up Calculation ---")

    # Stirling numbers of the second kind
    print(f"S({n_val}, {k_val}) = {stirling_second_kind(n_val, k_val)}")
    print("This means there are 25 ways to partition 5 elements into 3 non-empty subsets.")

    # Unsigned Stirling numbers of the first kind
    print(f"\n|s({n_val}, {k_val})| = {stirling_first_kind(n_val, k_val)}")
    print("This means there are 35 ways to permute 5 elements into 3 disjoint cycles.")

    # Lah numbers
    print(f"\nL({n_val}, {k_val}) = {lah_number(n_val, k_val)}")
    print("This means there are 120 ways to partition 5 elements into 3 ordered subsets.")
