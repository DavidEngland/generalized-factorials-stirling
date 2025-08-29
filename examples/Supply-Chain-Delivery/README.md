# Delivery Route Optimization: Moment-Enhanced Partition Analysis

This example demonstrates how polynomial moment analysis can be applied to delivery and logistics data to optimize route grouping and fleet management.

## Advanced Methodology

This demo employs Bell polynomial moment analysis to derive precise parameter estimates:

- **Multi-Order Coefficient Estimation**: Captures both linear and non-linear aspects of routing patterns
- **Structural Refinement**: Analyzes higher-order moments to identify subtle spatial relationships
- **Multivariate Pattern Recognition**: Handles complex interactions between distance, time, and priority features

## Scenario

In supply chain management, each order has features such as delivery location, size, and urgency. The goal is to group orders into delivery routes so that similar orders are delivered together, and to determine when to create a new route versus extending existing ones.

- **Cohesion Coefficient (a):** Measures how strongly orders tend to group together (e.g., nearby locations, similar delivery windows).
- **Separation Coefficient (b):** Represents the threshold for creating a new route (e.g., dispatch costs, driver allocation).

## How to Run

1. Install dependencies:
   ```
   pip install numpy pandas matplotlib scikit-learn sympy
   ```
2. Run the demo:
   ```
   python supply_chain_delivery_demo.py
   ```
3. View results:
   - Visualizations are saved in the `visualizations/` folder.
   - Open `delivery_report.html` in your browser for a summary.

## What You'll Learn

- How to represent delivery orders as feature vectors
- How to apply moment-enhanced partition analysis to optimize routing
- How non-linear scaling refinements improve route assignments
- How to visualize and interpret structural coefficients

## Files

- `supply_chain_delivery_demo.py`: Main script with polynomial moment enhancements
- `visualizations/`: Output charts and HTML report including:
  - `polynomial_moment_analysis.png`: Advanced visualization of routing parameters
  - `structural_refinements.png`: Visualization of higher-order corrections

## Example Output

- Optimal number of delivery routes (trucks)
- Affinity and cost parameters for route grouping
- Route distribution plot
- HTML report summarizing the delivery optimization

---

This demo is ideal for logistics managers, fleet operators, or anyone seeking to optimize delivery efficiency and resource allocation.
