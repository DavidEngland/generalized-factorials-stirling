"""
Stirling Measure calculation for E-commerce Customer Segmentation.

This module implements the core functionality for calculating the Stirling Measure
from customer segmentation data and estimating the underlying parameters.
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from typing import Tuple, List, Dict, Optional
import sys
import os

# Add the project root to the Python path to import the generalized Stirling implementation
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
try:
    from src.core.python.stirling import GeneralizedStirling
except ImportError:
    # Simplified implementation if the main library isn't available
    class GeneralizedStirling:
        def __init__(self, a=1.0, b=1.0):
            self.a = a
            self.b = b
            self._cache = {}
        
        def compute(self, n, k):
            """Simple implementation of generalized Stirling numbers."""
            if k == 0:
                return 1.0 if n == 0 else 0.0
            if n == 0 or k > n:
                return 0.0
            if k == n:
                return 1.0
            if (n, k) in self._cache:
                return self._cache[(n, k)]
            
            # Use triangular recurrence relation
            result = self.compute(n-1, k-1) + (self.a * (n-1) + self.b * k) * self.compute(n-1, k)
            self._cache[(n, k)] = result
            return result


def calculate_stirling_measure(n: int, k: int, a_test: float = 1.0, b_test: float = 1.0) -> Optional[float]:
    """
    Calculate the Stirling measure for given n, k and test parameters a, b.
    
    Args:
        n: Number of customers
        k: Number of segments
        a_test: Test parameter for customer affinity
        b_test: Test parameter for segment barrier
        
    Returns:
        The calculated Stirling measure or None if calculation fails
    """
    gs = GeneralizedStirling(a=a_test, b=b_test)
    
    s_n_k = gs.compute(n, k)
    s_n_plus_1_k = gs.compute(n+1, k)
    s_n_k_minus_1 = gs.compute(n, k-1) if k > 1 else 0
    
    # Avoid division by zero
    if s_n_k == 0:
        return None
    
    return (s_n_plus_1_k - s_n_k_minus_1) / s_n_k


def estimate_parameters(n_k_pairs: List[Tuple[int, int, float]]) -> Tuple[float, float, float]:
    """
    Estimate parameters a and b from observed data using the Stirling measure.
    
    Args:
        n_k_pairs: List of (n, k, measure) tuples
        
    Returns:
        Tuple of (a, b, r_squared) with estimated parameters and goodness of fit
    """
    X = np.array([[n, k] for n, k, _ in n_k_pairs])
    y = np.array([measure for _, _, measure in n_k_pairs])
    
    # Perform linear regression
    model = LinearRegression()
    model.fit(X, y)
    
    # Extract parameters
    a, b = model.coef_
    
    # Calculate R² to evaluate goodness of fit
    y_pred = model.predict(X)
    r_squared = r2_score(y, y_pred)
    
    return a, b, r_squared


def analyze_customer_segments(
    customer_counts: List[int],
    segment_counts: List[int],
    time_periods: List[str],
    plot: bool = True
) -> Dict:
    """
    Analyze customer segment data and estimate Stirling parameters.
    
    Args:
        customer_counts: List of customer counts (n) for each time period
        segment_counts: List of segment counts (k) for each time period
        time_periods: List of time period labels (e.g., months)
        plot: Whether to generate plots
        
    Returns:
        Dictionary with analysis results
    """
    # Calculate Stirling measures for each time period
    measures = []
    valid_periods = []
    valid_n_values = []
    valid_k_values = []
    
    for i, (n, k, period) in enumerate(zip(customer_counts, segment_counts, time_periods)):
        # Need valid n and k values
        if n <= 0 or k <= 0 or k > n:
            continue
            
        # Calculate measure
        measure = calculate_stirling_measure(n, k)
        if measure is not None:
            measures.append(measure)
            valid_periods.append(period)
            valid_n_values.append(n)
            valid_k_values.append(k)
    
    # Estimate parameters
    n_k_measure_tuples = list(zip(valid_n_values, valid_k_values, measures))
    a, b, r_squared = estimate_parameters(n_k_measure_tuples)
    
    # Create plots if requested
    if plot:
        # Plot the regression
        plt.figure(figsize=(10, 6))
        
        # Create scatter plot of actual measures
        plt.scatter(valid_n_values, measures, c=valid_k_values, cmap='viridis', 
                   alpha=0.8, edgecolors='w', s=100, label='Observed Measures')
        
        # Create predicted values
        n_range = np.linspace(min(valid_n_values), max(valid_n_values), 100)
        k_mean = np.mean(valid_k_values)
        y_pred = a * n_range + b * k_mean
        
        plt.plot(n_range, y_pred, 'r-', label=f'Fitted Line (a={a:.2f}, b={b:.2f})')
        
        plt.xlabel('Number of Customers (n)')
        plt.ylabel('Stirling Measure')
        plt.title('Customer Segmentation Stirling Measure Analysis')
        plt.colorbar(label='Number of Segments (k)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig('customer_segmentation_analysis.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # Plot time series
        plt.figure(figsize=(12, 8))
        fig, ax1 = plt.subplots(figsize=(12, 6))
        
        color = 'tab:blue'
        ax1.set_xlabel('Time Period')
        ax1.set_ylabel('Number of Customers (n)', color=color)
        ax1.plot(valid_periods, valid_n_values, 'o-', color=color)
        ax1.tick_params(axis='y', labelcolor=color)
        
        ax2 = ax1.twinx()
        color = 'tab:red'
        ax2.set_ylabel('Number of Segments (k)', color=color)
        ax2.plot(valid_periods, valid_k_values, 's-', color=color)
        ax2.tick_params(axis='y', labelcolor=color)
        
        plt.title('Customer and Segment Counts Over Time')
        fig.tight_layout()
        plt.savefig('customer_segments_time_series.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    # Return the results
    return {
        'estimated_a': a,
        'estimated_b': b,
        'r_squared': r_squared,
        'time_periods': valid_periods,
        'customer_counts': valid_n_values,
        'segment_counts': valid_k_values,
        'measures': measures
    }


def interpret_parameters(a: float, b: float) -> Dict[str, str]:
    """
    Provide business interpretation of the estimated parameters.
    
    Args:
        a: Estimated parameter a (customer affinity)
        b: Estimated parameter b (segment barrier)
        
    Returns:
        Dictionary with interpretations
    """
    interpretations = {}
    
    # Interpret parameter a (customer affinity)
    if a < 0.2:
        interpretations['a_interpretation'] = ("Low customer affinity. Customers have minimal tendency to "
                                             "join the same segments. They display highly heterogeneous "
                                             "behaviors, suggesting very personalized marketing approaches.")
    elif a < 0.5:
        interpretations['a_interpretation'] = ("Moderate customer affinity. Customers show some tendency to "
                                             "cluster in similar segments. A balanced approach of segment-specific "
                                             "and personalized marketing is recommended.")
    else:
        interpretations['a_interpretation'] = ("High customer affinity. Customers strongly tend to join the "
                                             "same segments. Broad segment-based marketing campaigns will "
                                             "be effective.")
    
    # Interpret parameter b (segment barrier)
    if b < 1.0:
        interpretations['b_interpretation'] = ("Low segment barrier. New customer segments form easily. "
                                             "The market is highly dynamic with constantly evolving customer "
                                             "groups. Frequent reassessment of segmentation is recommended.")
    elif b < 2.0:
        interpretations['b_interpretation'] = ("Moderate segment barrier. There is some resistance to forming "
                                             "new segments. Existing segments are relatively stable but can "
                                             "evolve over time.")
    else:
        interpretations['b_interpretation'] = ("High segment barrier. New segments rarely form. The market has "
                                             "very stable, distinct customer groups. Long-term investment in "
                                             "serving these distinct segments is recommended.")
    
    # Marketing strategy recommendations
    if a < 0.3 and b < 1.0:
        interpretations['strategy'] = ("Highly personalized marketing: Low affinity and low barriers suggest "
                                      "a market with many small, dynamic segments. Focus on individual-level "
                                      "personalization and frequent reassessment.")
    elif a > 0.5 and b > 2.0:
        interpretations['strategy'] = ("Mass segment marketing: High affinity and high barriers indicate "
                                      "a market with few, stable segments. Focus on developing deep segment-specific "
                                      "offerings and mass marketing within each segment.")
    elif a < 0.3 and b > 2.0:
        interpretations['strategy'] = ("Micro-segment targeting: Low affinity but high barriers suggest "
                                      "stable micro-segments. Develop specialized offerings for each distinct "
                                      "customer group.")
    elif a > 0.5 and b < 1.0:
        interpretations['strategy'] = ("Adaptive mass marketing: High affinity but low barriers indicate "
                                      "customers cluster together but in evolving ways. Focus on broad campaigns "
                                      "with regular adaptation to shifting segments.")
    else:
        interpretations['strategy'] = ("Balanced segmentation: Moderate affinity and barriers suggest "
                                      "a traditional segmentation approach with periodic reassessment. "
                                      "Develop segment-specific campaigns with some personalization.")
    
    return interpretations


if __name__ == "__main__":
    # Example usage with synthetic data
    np.random.seed(42)
    
    # Generate synthetic data
    periods = [f"2023-{month:02d}" for month in range(1, 13)]
    customer_growth = np.linspace(100, 500, len(periods)) + np.random.normal(0, 20, len(periods))
    customers = [int(max(50, c)) for c in customer_growth]  # Ensure at least 50 customers
    
    # True parameters
    true_a = 0.3
    true_b = 1.8
    
    # Generate segments based on true parameters
    segments = []
    for n in customers:
        # Simplistic model: k ~ n/(a*n + b)
        expected_k = int(n / (true_a * n + true_b) + np.random.normal(0, 1))
        segments.append(max(1, min(n, expected_k)))  # Ensure 1 ≤ k ≤ n
    
    # Run analysis
    results = analyze_customer_segments(customers, segments, periods, plot=True)
    
    # Print results
    print(f"Estimated parameters: a = {results['estimated_a']:.4f}, b = {results['estimated_b']:.4f}")
    print(f"R-squared: {results['r_squared']:.4f}")
    print(f"True parameters: a = {true_a}, b = {true_b}")
    
    # Get interpretation
    interpretation = interpret_parameters(results['estimated_a'], results['estimated_b'])
    print("\nInterpretation:")
    for key, value in interpretation.items():
        print(f"{key}: {value}")
