# Fleet Optimizer: Lah Numbers and Heterogeneous Vehicle Assignment

This script (`fleet_optimizer.py`) uses generalized Stirling numbers—specifically the Lah numbers case (a=1, b=1)—to optimize delivery route assignments for a heterogeneous fleet.

## What Does the Code Do?

- **Loads Delivery Data:** Reads a CSV file of delivery points, including location and package size.
- **Loads Fleet Data:** Reads a CSV file of available vehicles, including type, capacity, age, maintenance cost, and fuel efficiency.
- **Determines Optimal Number of Routes:** Uses the Lah numbers (generalized Stirling numbers with a=1, b=1) to find the best number of routes for the given deliveries and fleet.
- **Clusters Deliveries:** Groups delivery points into routes using K-means clustering.
- **Calculates Route Properties:** For each route, computes total distance and total load.
- **Assigns Routes to Vehicles:** Matches routes to vehicles using a greedy algorithm, prioritizing capacity and minimizing estimated cost (fuel + maintenance).
- **Reports Results:** Prints assignments, total cost, and highlights any routes that could not be assigned due to capacity limits.

## Why Lah Numbers?

Lah numbers naturally model the scenario where both affinity (vehicle capability) and barrier (management/assignment cost) are equally weighted. This is ideal for fleets with diverse vehicles and operational constraints.

## How to Use

1. Prepare your delivery data CSV (e.g., `sample_deliveries.csv`).
2. Prepare your fleet composition CSV (e.g., `fleet_composition.csv`).
3. Run:
   ```
   python fleet_optimizer.py --data sample_deliveries.csv --fleet fleet_composition.csv --params 1,1
   ```
4. Review the printed assignments and summary.

## Customization

- Change the `--params` argument to use different Stirling parameters for other optimization strategies.
- Extend the assignment logic for more complex cost models or constraints.
- Integrate with visualization tools for route mapping.

## References

- Hsu, L. C. and Shiue, P. J.-S. "A unified approach to generalized Stirling numbers." *Adv. in Appl. Math.*, 20(3):366-384, 1998.
- See README.md for more context on dual-perspective optimization and fleet management.
