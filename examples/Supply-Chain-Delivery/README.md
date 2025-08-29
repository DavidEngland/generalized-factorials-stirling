# Supply Chain Delivery Demo: Bell-Enhanced Stirling Partitioning

This example demonstrates how the Bell-Enhanced Stirling Partitioning Algorithm can be applied to delivery and logistics data to optimize route grouping and fleet management.

## Advanced Bell Polynomial Methodology

This demo uses Bell polynomials to derive higher-order corrections to clustering parameters:

- **Quadratic Parameter Fitting**: Captures non-linear scaling effects as route counts increase
- **Higher-Order Moments**: Analyzes skewness and other higher-order patterns in delivery data 
- **Multivariate Bell Polynomials**: Handles complex multidimensional feature spaces efficiently

## Scenario

In supply chain management, each order has features such as delivery location, size, and urgency. The goal is to group orders into delivery routes (clusters) so that similar orders are delivered together, and to decide when to add a new truck (route) versus using existing ones.

- **Affinity (Parameter a):** Measures how strongly orders tend to be grouped into the same route (e.g., nearby locations, similar delivery windows).
- **Barrier (Parameter b):** Represents the cost of starting a new route (e.g., dispatching a new truck, driver cost, fuel).

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
- How to use Bell polynomial-enhanced clustering to optimize delivery routes
- How higher-order corrections improve route assignments
- How to visualize and interpret the enhanced parameters

## Files

- `supply_chain_delivery_demo.py`: Main script with Bell polynomial enhancements
- `visualizations/`: Output charts and HTML report including:
  - `bell_enhanced_analysis.png`: Advanced analysis of routing parameters
  - `higher_order_metrics.png`: Visualization of Bell polynomial metrics

## Example Output

- Optimal number of delivery routes (trucks)
- Affinity and cost parameters for route grouping
- Route distribution plot
- HTML report summarizing the delivery optimization

---

This demo is ideal for logistics managers, fleet operators, or anyone seeking to optimize delivery efficiency and resource allocation.
