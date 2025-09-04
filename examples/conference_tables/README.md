# Conference Table Allocation Example

This example demonstrates how to use generalized Stirling numbers to optimize table allocation for a mathematics conference. The scenario involves allocating tables for 160 mathematicians from different fields, balancing their natural tendency to cluster by specialty against the desire for interdisciplinary discussions.

## Problem Description

A conference organizer for the Annual Advances in Mathematical Sciences Conference needs to determine how many tables to purchase for lunch sessions. The conference has 160 registered mathematicians from various fields.

**Key Considerations:**
- Mathematicians naturally cluster by specialty (algebraists sit with algebraists, etc.)
- Organizers want to promote interdisciplinary discussion
- Budget constraints require optimizing the number of tables purchased

## Files

- `conference_table_allocation.py`: Main Python script implementing the simulation
- `visualize_results.py`: Script to visualize the allocation results
- `sample_output.txt`: Sample output from running the simulation

## Usage

```bash
# Run the basic simulation
python conference_table_allocation.py

# Run with specific parameters
python conference_table_allocation.py --mathematicians 160 --fields 5 --affinity 0 --barrier 0.5

# Generate visualizations
python visualize_results.py
```

## Mathematical Background

This example uses the generalized Stirling framework with parameters $(a,b)$ where:

- $a$ (affinity parameter): Controls how strongly mathematicians prefer to sit with colleagues from the same field
- $b$ (barrier parameter): Controls the cost and effectiveness of creating diverse tables

The simulation explores three key parameter settings:
1. Classical Separation $(0,1)$: Full barriers between tables
2. Half-Barrier Approach $(0,1/2)$: Partial separation with more cost-effective table arrangement
3. Mixing Encouragement $(0,-1/2)$: Arrangement that actively promotes cross-field discussions

For the half-barrier case, we use the formula: $S_{n,k}(0,1/2) = 2^{k-n}S(n,k)$, where $S(n,k)$ is the classical Stirling number of the second kind.
