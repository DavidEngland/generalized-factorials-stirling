# Supply Chain Delivery Demo: Stirling Partitioning for Logistics Optimization

This example demonstrates how the Stirling Partitioning Algorithm can be applied to delivery and logistics data to optimize route grouping and fleet management.

## Scenario

In supply chain management, each order has features such as delivery location, size, and urgency. The goal is to group orders into delivery routes (clusters) so that similar orders are delivered together, and to decide when to add a new truck (route) versus using existing ones.

- **Affinity (Parameter a):** Measures how strongly orders tend to be grouped into the same route (e.g., nearby locations, similar delivery windows).
- **Barrier (Parameter b):** Represents the cost of starting a new route (e.g., dispatching a new truck, driver cost, fuel).

## How to Run

1. Install dependencies:
   ```
   pip install numpy pandas matplotlib scikit-learn
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
- How to use clustering to optimize delivery routes
- How affinity and barrier parameters guide fleet size and route assignment
- How to visualize and report the results

## Files

- `supply_chain_delivery_demo.py`: Main script
- `visualizations/`: Output charts and HTML report

## Example Output

- Optimal number of delivery routes (trucks)
- Affinity and cost parameters for route grouping
- Route distribution plot
- HTML report summarizing the delivery optimization

---

This demo is ideal for logistics managers, fleet operators, or anyone seeking to optimize delivery efficiency and resource allocation.
