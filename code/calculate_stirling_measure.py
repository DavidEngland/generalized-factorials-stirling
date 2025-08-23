def calculate_stirling_measure(n, k, a_test=0.5, b_test=0.5):
    """Calculate the Stirling measure for given n, k and parameters a, b"""
    gs = GeneralizedStirling(alpha=a_test, beta=b_test)
    
    s_n_k = gs.compute(n, k)
    s_n_plus_1_k = gs.compute(n+1, k)
    s_n_k_minus_1 = gs.compute(n, k-1) if k > 1 else 0
    
    # Avoid division by zero
    if s_n_k == 0:
        return None
    
    return (s_n_plus_1_k - s_n_k_minus_1) / s_n_k

# Calculate observed measures
observed_measures = []
n_values = []
k_values = []

for n, k in n_k_pairs:
    # Ensure values are reasonable for computation
    if n > 0 and k > 0 and n < 1000 and k < 100:  # Adjust limits as needed
        n_values.append(n)
        k_values.append(k)
        # This would be the actual observed value from your data
        # For demonstration, we'll calculate it using assumed a,b values
        true_a, true_b = 0.3, 0.7  # The "true" parameters we're trying to estimate
        observed_measure = true_a * n + true_b * k + np.random.normal(0, 0.1)  # Add some noise
        observed_measures.append(observed_measure)