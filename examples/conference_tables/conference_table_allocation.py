"""
Conference Table Allocation Example using Generalized Stirling Numbers

This script demonstrates how to apply the generalized Stirling framework
to a practical problem: allocating tables for a mathematics conference.
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import argparse

# Calculate Stirling numbers of the second kind
def stirling_second_kind(n, k):
    """Calculate S(n,k), Stirling numbers of the second kind"""
    if k == 0:
        return 1 if n == 0 else 0
    if k > n or k == 0:
        return 0
    
    # Use recurrence relation: S(n,k) = S(n-1,k-1) + k*S(n-1,k)
    result = stirling_second_kind(n-1, k-1) + k * stirling_second_kind(n-1, k)
    return result

# Calculate generalized Stirling numbers
def generalized_stirling(n, k, a, b):
    """Calculate S_{n,k}(a,b), the generalized Stirling numbers"""
    # Special case for the hyperbolic strip
    if a == 0 and b == 0.5:
        return 2**(k-n) * stirling_second_kind(n, k)
    if a == 0 and b == -0.5:
        return (-1)**(n-k) * 2**(k-n) * stirling_second_kind(n, k)
    
    # General case using recurrence relation
    if k == 0:
        return 1 if n == 0 else 0
    if k > n or k == 0:
        return 0
    
    return generalized_stirling(n-1, k-1, a, b) + (a*(n-1) + b*k) * generalized_stirling(n-1, k, a, b)

class ConferenceTableAllocator:
    def __init__(self, num_mathematicians=160, num_fields=5, field_sizes=None):
        self.num_mathematicians = num_mathematicians
        self.num_fields = num_fields
        
        # Define field sizes if not provided
        if field_sizes is None:
            self.field_sizes = [42, 38, 35, 25, 20]  # Default: 5 fields with given sizes
        else:
            self.field_sizes = field_sizes
            
        # Table options with their costs and capacities
        self.table_options = {
            'small': {'capacity': 8, 'cost': 120},
            'medium': {'capacity': 10, 'cost': 150},
            'large': {'capacity': 16, 'cost': 200}
        }
    
    def calculate_table_needs(self, a, b, target_tables=None):
        """
        Calculate the optimal table allocation based on the (a,b) parameters.
        
        Args:
            a: Affinity parameter (how strongly mathematicians cluster by field)
            b: Barrier parameter (cost/effectiveness of creating diverse tables)
            target_tables: Optional target number of tables to use
            
        Returns:
            Dictionary with allocation details and costs
        """
        results = {}
        
        # If target_tables is not specified, calculate optimal number
        if target_tables is None:
            # Heuristic: try different numbers of tables and pick the best based on cost and diversity
            possible_tables = range(10, 25)
            costs = []
            diversity_scores = []
            
            for k in possible_tables:
                # Calculate the generalized Stirling number for this configuration
                gen_stirling = generalized_stirling(self.num_mathematicians, k, a, b)
                
                # Calculate cost (simplified model)
                avg_table_size = self.num_mathematicians / k
                if avg_table_size <= 8:
                    table_cost = k * self.table_options['small']['cost']
                elif avg_table_size <= 10:
                    table_cost = k * self.table_options['medium']['cost']
                else:
                    table_cost = k * self.table_options['large']['cost']
                
                # Calculate diversity score (higher is better)
                # This is a simplified model - in reality would depend on field distributions
                diversity_score = gen_stirling / (k * self.num_mathematicians)
                
                costs.append(table_cost)
                diversity_scores.append(diversity_score)
            
            # Normalize scores
            normalized_costs = [c/max(costs) for c in costs]
            normalized_diversity = [d/max(diversity_scores) for d in diversity_scores]
            
            # Combined score (lower is better): cost - diversity
            combined_scores = [cost - diversity for cost, diversity in zip(normalized_costs, normalized_diversity)]
            optimal_index = combined_scores.index(min(combined_scores))
            target_tables = possible_tables[optimal_index]
        
        # Calculate allocation with the target number of tables
        gen_stirling_value = generalized_stirling(self.num_mathematicians, target_tables, a, b)
        
        # Determine table types based on average capacity needed
        avg_table_size = self.num_mathematicians / target_tables
        
        # Allocate table types
        if avg_table_size <= 8:
            table_allocation = {'small': target_tables, 'medium': 0, 'large': 0}
        elif avg_table_size <= 10:
            table_allocation = {'small': 0, 'medium': target_tables, 'large': 0}
        else:
            # Mixed allocation
            large_tables = int(target_tables / 3)
            medium_tables = target_tables - large_tables
            table_allocation = {'small': 0, 'medium': medium_tables, 'large': large_tables}
        
        # Calculate total cost
        total_cost = sum(count * self.table_options[size]['cost'] 
                         for size, count in table_allocation.items())
        
        # Calculate total capacity
        total_capacity = sum(count * self.table_options[size]['capacity'] 
                             for size, count in table_allocation.items())
        
        # Simulate field distribution across tables
        tables = [[] for _ in range(target_tables)]
        
        # Function to assign mathematicians to tables based on parameters
        def assign_to_tables():
            # Create mathematicians with field labels
            mathematicians = []
            for field_id, field_size in enumerate(self.field_sizes):
                mathematicians.extend([field_id] * field_size)
            
            # Shuffle mathematicians (with seed for reproducibility)
            np.random.seed(42)
            np.random.shuffle(mathematicians)
            
            # Assign to tables
            for i, field_id in enumerate(mathematicians):
                if a == 0 and b == 1:
                    # Classical case - try to keep fields separate
                    table_id = i % target_tables
                elif a == 0 and b == 0.5:
                    # Half-barrier - some mixing but still field-biased
                    if np.random.random() < 0.7:  # 70% chance of field-based assignment
                        table_id = field_id % target_tables
                    else:
                        table_id = i % target_tables
                elif a == 0 and b == -0.5:
                    # Anti-barrier - actively mix fields
                    field_counts = [sum(1 for m in table if m == field_id) for table in tables]
                    table_id = field_counts.index(min(field_counts))
                else:
                    # General case
                    table_id = i % target_tables
                
                tables[table_id].append(field_id)
        
        assign_to_tables()
        
        # Calculate diversity metrics
        diversity_per_table = []
        for table in tables:
            field_counts = defaultdict(int)
            for field_id in table:
                field_counts[field_id] += 1
            
            # Calculate diversity as ratio of unique fields to table size
            unique_fields = len(field_counts)
            table_size = len(table)
            diversity = unique_fields / min(table_size, self.num_fields)
            diversity_per_table.append(diversity)
        
        avg_diversity = sum(diversity_per_table) / len(diversity_per_table)
        
        # Prepare results
        results = {
            'parameters': {'a': a, 'b': b},
            'num_tables': target_tables,
            'table_allocation': table_allocation,
            'total_cost': total_cost,
            'total_capacity': total_capacity,
            'avg_table_size': avg_table_size,
            'generalized_stirling_value': gen_stirling_value,
            'avg_diversity': avg_diversity,
            'tables': tables
        }
        
        return results

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Conference Table Allocation Simulator')
    parser.add_argument('--mathematicians', type=int, default=160, help='Number of mathematicians')
    parser.add_argument('--fields', type=int, default=5, help='Number of fields')
    parser.add_argument('--affinity', type=float, default=0, help='Affinity parameter (a)')
    parser.add_argument('--barrier', type=float, default=1, help='Barrier parameter (b)')
    args = parser.parse_args()
    
    # Create the allocator
    allocator = ConferenceTableAllocator(
        num_mathematicians=args.mathematicians,
        num_fields=args.fields
    )
    
    # Compare different parameter settings
    param_settings = [
        (0, 1),     # Classical approach
        (0, 0.5),   # Half-barrier approach
        (0, -0.5)   # Mixing approach
    ]
    
    print("Conference Table Allocation Comparison\n")
    print(f"Conference details: {args.mathematicians} mathematicians from {args.fields} fields\n")
    
    results = []
    for a, b in param_settings:
        result = allocator.calculate_table_needs(a, b)
        results.append(result)
        
        print(f"Parameter setting (a={a}, b={b}):")
        print(f"  Tables needed: {result['num_tables']}")
        print(f"  Table allocation: {result['table_allocation']}")
        print(f"  Total cost: ${result['total_cost']}")
        print(f"  Average table size: {result['avg_table_size']:.1f}")
        print(f"  Average diversity score: {result['avg_diversity']:.2f}")
        print()
    
    # Also calculate for the specific requested parameters
    if (args.affinity, args.barrier) not in param_settings:
        result = allocator.calculate_table_needs(args.affinity, args.barrier)
        print(f"Custom parameter setting (a={args.affinity}, b={args.barrier}):")
        print(f"  Tables needed: {result['num_tables']}")
        print(f"  Table allocation: {result['table_allocation']}")
        print(f"  Total cost: ${result['total_cost']}")
        print(f"  Average table size: {result['avg_table_size']:.1f}")
        print(f"  Average diversity score: {result['avg_diversity']:.2f}")
    
    # Save results to a file
    with open('allocation_results.txt', 'w') as f:
        f.write("Conference Table Allocation Results\n\n")
        for i, (a, b) in enumerate(param_settings):
            result = results[i]
            f.write(f"Parameter setting (a={a}, b={b}):\n")
            f.write(f"  Tables needed: {result['num_tables']}\n")
            f.write(f"  Table allocation: {result['table_allocation']}\n")
            f.write(f"  Total cost: ${result['total_cost']}\n")
            f.write(f"  Average diversity score: {result['avg_diversity']:.2f}\n\n")
    
    print("\nResults saved to allocation_results.txt")

if __name__ == "__main__":
    main()
