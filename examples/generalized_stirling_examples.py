"""
Examples demonstrating the use of generalized Stirling numbers.

This file contains examples based on the paper
"Combinatorial approach of certain generalized Stirling numbers"
by Belbachir, Belkhir, and Bousbaa.
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Add the src directory to the path
sys.path.append(str(Path(__file__).parent.parent / "src"))
from generalized_stirling import GeneralizedStirling, stirling_first_kind, stirling_second_kind, lah_number


def print_triangle(triangle, title):
    """Print a triangle of numbers with a title."""
    print(f"\n{title}")
    print("-" * len(title))
    
    for i, row in enumerate(triangle, 1):
        print(f"{i}: {' '.join(row)}")


def example_basic_properties():
    """Demonstrate basic properties of generalized Stirling numbers."""
    print("EXAMPLE: Basic Properties of Generalized Stirling Numbers")
    
    # Create instances with different parameters
    gs_default = GeneralizedStirling(alpha=1.0, beta=1.0)  # Lah numbers
    gs_first = GeneralizedStirling(alpha=1.0, beta=0.0)    # First kind
    gs_second = GeneralizedStirling(alpha=0.0, beta=1.0)   # Second kind
    
    # Print triangles
    n_max = 6
    
    print_triangle(gs_first.generate_triangle(n_max), 
                   "Stirling Numbers of the First Kind (α=1, β=0)")
    
    print_triangle(gs_second.generate_triangle(n_max), 
                   "Stirling Numbers of the Second Kind (α=0, β=1)")
    
    print_triangle(gs_default.generate_triangle(n_max), 
                   "Lah Numbers (α=1, β=1)")
    
    # Custom parameters
    gs_custom = GeneralizedStirling(alpha=2.0, beta=3.0)
    print_triangle(gs_custom.generate_triangle(n_max), 
                   "Generalized Stirling Numbers (α=2, β=3)")


def example_recurrence_relations():
    """Demonstrate recurrence relations for generalized Stirling numbers."""
    print("\nEXAMPLE: Recurrence Relations")
    
    gs = GeneralizedStirling(alpha=1.5, beta=2.5)
    n, k = 5, 3
    
    # Triangular recurrence: L{n,k} = L{n-1,k-1} + (α(n-1) + βk) * L{n-1,k}
    direct = gs.compute(n, k)
    term1 = gs.compute(n-1, k-1)
    coeff = gs.alpha * (n-1) + gs.beta * k
    term2 = coeff * gs.compute(n-1, k)
    recurrence = term1 + term2
    
    print(f"Triangular Recurrence for L{{{n},{k}}}^{{{gs.alpha},{gs.beta}}}:")
    print(f"Direct computation: {direct}")
    print(f"Using recurrence: {term1} + ({coeff}) * {gs.compute(n-1, k)} = {recurrence}")
    print(f"Match: {abs(direct - recurrence) < 1e-10}")
    
    # Horizontal recurrence
    horizontal = gs.compute(n, k, method='horizontal')
    print(f"\nHorizontal Recurrence for L{{{n},{k}}}^{{{gs.alpha},{gs.beta}}}:")
    print(f"Direct computation: {direct}")
    print(f"Using horizontal recurrence: {horizontal}")
    print(f"Match: {abs(direct - horizontal) < 1e-10}")
    
    # Vertical recurrence (only for L{n+1,k+1})
    vertical = gs.compute(n+1, k+1, method='vertical')
    direct_next = gs.compute(n+1, k+1)
    print(f"\nVertical Recurrence for L{{{n+1},{k+1}}}^{{{gs.alpha},{gs.beta}}}:")
    print(f"Direct computation: {direct_next}")
    print(f"Using vertical recurrence: {vertical}")
    print(f"Match: {abs(direct_next - vertical) < 1e-10}")


def example_special_case():
    """Demonstrate special case for k=1."""
    print("\nEXAMPLE: Special Case L{n,1}")
    
    gs = GeneralizedStirling(alpha=2.0, beta=3.0)
    
    for n in range(1, 6):
        direct = gs.compute(n, 1)
        special = gs.special_case(n, 1)
        product = " * ".join([f"({j}*{gs.alpha} + {gs.beta})" for j in range(1, n)])
        
        print(f"L{{{n},1}}^{{{gs.alpha},{gs.beta}}} = {direct}")
        print(f"Using special formula: {product} = {special}")
        print(f"Match: {abs(direct - special) < 1e-10}")
        print()


def example_combinatorial_interpretation():
    """Demonstrate the combinatorial interpretation with a simple example."""
    print("\nEXAMPLE: Combinatorial Interpretation")
    
    print("Consider distributing elements {1,2,3} into 1 ordered list:")
    print("Each distribution has a weight based on position:")
    
    distributions = [
        ("(1,2,3)", "α²", "First element has weight 1, others have weight α"),
        ("(1,3,2)", "α²", "First element has weight 1, others have weight α"),
        ("(3,1,2)", "αβ", "First element has weight 1, head has weight β, other has weight α"),
        ("(2,1,3)", "αβ", "First element has weight 1, head has weight β, other has weight α"),
        ("(2,3,1)", "αβ", "First element has weight 1, head has weight β, other has weight α"),
        ("(3,2,1)", "β²", "First element has weight 1, both others are heads with weight β")
    ]
    
    for dist, weight, explanation in distributions:
        print(f"{dist}: weight = {weight} - {explanation}")
    
    print("\nTotal weight = 2α² + 3αβ + β² = (α+β)(2α+β)")
    
    # Verify with computation
    gs = GeneralizedStirling(alpha=1.0, beta=1.0)  # Using α=β=1 for simplicity
    value = gs.compute(3, 1)
    expected = 6  # When α=β=1, we get (1+1)(2*1+1) = 2*3 = 6
    
    print(f"With α=β=1: L{{3,1}}^{{1,1}} = {value}")
    print(f"Expected: 6")
    print(f"Match: {value == expected}")


def example_symmetric_function():
    """Demonstrate the symmetric function formula."""
    print("\nEXAMPLE: Symmetric Function Formula")
    
    gs = GeneralizedStirling(alpha=1.0, beta=1.0)
    n, k = 3, 2
    
    direct = gs.compute(n+k, n)
    symmetric = gs.symmetric_function(n, k)
    
    print(f"L{{{n+k},{n}}}^{{{gs.alpha},{gs.beta}}} = {direct}")
    print(f"Using symmetric function formula: {symmetric}")
    print(f"Match: {abs(direct - symmetric) < 1e-10}")
    
    print("\nThis equals the sum over all 1 ≤ i₁ ≤ i₂ ≤ 3 of:")
    print("((α+β)i₁) * ((α+β)i₂ + α)")
    
    # Explicitly calculate for small example
    result = 0
    for i1 in range(1, n+1):
        for i2 in range(i1, n+1):
            term = ((gs.alpha + gs.beta) * i1) * ((gs.alpha + gs.beta) * i2 + gs.alpha)
            print(f"  i₁={i1}, i₂={i2}: ((1+1)*{i1}) * ((1+1)*{i2} + 1) = {term}")
            result += term
    
    print(f"Sum = {result}")


def visualize_stirling_numbers():
    """Create visualizations of different generalized Stirling number triangles."""
    print("\nCreating visualizations of Stirling number triangles...")
    
    # Parameters to visualize
    params = [
        (1.0, 0.0, "Stirling First Kind (α=1, β=0)"),
        (0.0, 1.0, "Stirling Second Kind (α=0, β=1)"),
        (1.0, 1.0, "Lah Numbers (α=1, β=1)"),
        (2.0, 1.0, "Generalized (α=2, β=1)"),
        (1.0, 2.0, "Generalized (α=1, β=2)"),
    ]
    
    n_max = 8
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()
    
    for i, (alpha, beta, title) in enumerate(params):
        gs = GeneralizedStirling(alpha=alpha, beta=beta)
        
        # Calculate values
        values = np.zeros((n_max, n_max))
        for n in range(1, n_max+1):
            for k in range(1, n+1):
                values[n-1, k-1] = gs.compute(n, k)
        
        # Create heatmap
        im = axes[i].imshow(np.log1p(values[:n_max, :n_max]), cmap='viridis')
        axes[i].set_title(title)
        axes[i].set_xlabel('k')
        axes[i].set_ylabel('n')
        axes[i].set_xticks(range(n_max))
        axes[i].set_yticks(range(n_max))
        axes[i].set_xticklabels(range(1, n_max+1))
        axes[i].set_yticklabels(range(1, n_max+1))
        
        # Add colorbar
        plt.colorbar(im, ax=axes[i])
    
    # Remove unused subplot
    axes[-1].axis('off')
    
    plt.tight_layout()
    plt.savefig('generalized_stirling_visualization.png')
    print("Visualization saved as 'generalized_stirling_visualization.png'")


if __name__ == "__main__":
    example_basic_properties()
    example_recurrence_relations()
    example_special_case()
    example_combinatorial_interpretation()
    example_symmetric_function()
    
    try:
        visualize_stirling_numbers()
    except ImportError:
        print("Matplotlib not available. Skipping visualizations.")
