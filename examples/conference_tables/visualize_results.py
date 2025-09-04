"""
Visualization script for the conference table allocation results.

This script creates visualizations to help understand the impact of
different (a,b) parameter settings on table allocations.
"""

import matplotlib.pyplot as plt
import numpy as np
from conference_table_allocation import ConferenceTableAllocator
import seaborn as sns

def visualize_parameter_space():
    """Create a visualization of the parameter space with key points highlighted"""
    # Create figure
    plt.figure(figsize=(10, 8))
    
    # Define axes
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    # Plot key parameter points
    points = [
        (0, 1, "Classical (0,1)"),
        (0, 0.5, "Half-barrier (0,0.5)"),
        (0, -0.5, "Anti-barrier (0,-0.5)"),
        (1, 0, "First Kind (1,0)"),
        (1, 1, "Lah (1,1)")
    ]
    
    a_vals, b_vals, labels = zip(*points)
    plt.scatter(a_vals, b_vals, s=100, c='blue', zorder=5)
    
    # Add labels
    for a, b, label in points:
        plt.annotate(label, (a, b), xytext=(10, 10), textcoords="offset points")
    
    # Add hyperbolic strip
    plt.plot([-1, 1], [0.5, 0.5], 'r--', alpha=0.7, label="Hyperbolic Strip")
    plt.plot([-1, 1], [-0.5, -0.5], 'r--', alpha=0.7)
    
    # Add labels and title
    plt.xlabel('Affinity Parameter (a)')
    plt.ylabel('Barrier Parameter (b)')
    plt.title('Parameter Space for Conference Table Allocation')
    plt.grid(True, alpha=0.3)
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    
    # Add annotations for regions
    plt.annotate("High Barriers", (0.5, 1.2), ha='center')
    plt.annotate("Low Barriers", (0.5, -1.2), ha='center')
    plt.annotate("High Affinity", (1.2, 0), va='center')
    plt.annotate("Low Affinity", (-1.2, 0), va='center')
    
    plt.tight_layout()
    plt.savefig('parameter_space.png')
    plt.close()

def visualize_cost_comparison():
    """Visualize cost comparison across different parameter settings"""
    # Initialize allocator
    allocator = ConferenceTableAllocator()
    
    # Calculate results for different parameter settings
    param_settings = [
        (0, 1, "Classical"),
        (0, 0.5, "Half-barrier"),
        (0, -0.5, "Anti-barrier")
    ]
    
    costs = []
    diversity_scores = []
    labels = []
    
    for a, b, label in param_settings:
        result = allocator.calculate_table_needs(a, b)
        costs.append(result['total_cost'])
        diversity_scores.append(result['avg_diversity'])
        labels.append(label)
    
    # Create figure
    plt.figure(figsize=(12, 6))
    
    # Create a bar chart
    x = np.arange(len(labels))
    width = 0.35
    
    ax1 = plt.subplot(1, 2, 1)
    ax1.bar(x, costs, width, label='Total Cost ($)')
    ax1.set_ylabel('Cost ($)')
    ax1.set_title('Total Cost by Parameter Setting')
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels)
    
    ax2 = plt.subplot(1, 2, 2)
    ax2.bar(x, diversity_scores, width, color='green', label='Diversity Score')
    ax2.set_ylabel('Diversity Score (higher is better)')
    ax2.set_title('Diversity by Parameter Setting')
    ax2.set_xticks(x)
    ax2.set_xticklabels(labels)
    
    plt.tight_layout()
    plt.savefig('cost_comparison.png')
    plt.close()

def visualize_table_distributions():
    """Visualize how mathematicians are distributed across tables"""
    # Initialize allocator
    allocator = ConferenceTableAllocator()
    
    # Calculate results for different parameter settings
    param_settings = [
        (0, 1, "Classical"),
        (0, 0.5, "Half-barrier"),
        (0, -0.5, "Anti-barrier")
    ]
    
    # Create figure
    plt.figure(figsize=(15, 10))
    
    for i, (a, b, label) in enumerate(param_settings):
        result = allocator.calculate_table_needs(a, b)
        tables = result['tables']
        
        # Convert tables to a matrix for visualization
        # Each row is a table, each value is a field ID
        matrix = np.zeros((len(tables), max(len(table) for table in tables)))
        matrix.fill(-1)  # Fill with -1 to represent empty seats
        
        for t, table in enumerate(tables):
            for s, field_id in enumerate(table):
                if s < matrix.shape[1]:
                    matrix[t, s] = field_id
        
        ax = plt.subplot(1, 3, i+1)
        sns.heatmap(matrix, cmap='tab10', ax=ax, cbar=False, 
                   mask=matrix < 0, linewidth=0.5)
        ax.set_title(f"{label} (a={a}, b={b})")
        ax.set_xlabel("Seat Position")
        ax.set_ylabel("Table Number")
    
    plt.tight_layout()
    plt.savefig('table_distributions.png')
    plt.close()

def main():
    """Generate all visualizations"""
    print("Generating parameter space visualization...")
    visualize_parameter_space()
    
    print("Generating cost comparison visualization...")
    visualize_cost_comparison()
    
    print("Generating table distribution visualization...")
    visualize_table_distributions()
    
    print("All visualizations completed. See the PNG files in the current directory.")

if __name__ == "__main__":
    main()
