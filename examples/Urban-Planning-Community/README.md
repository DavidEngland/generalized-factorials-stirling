# Urban Planning & Community Design Demo: Stirling Partitioning for Neighborhood Grouping

This example shows how the Stirling Partitioning Algorithm can be used to group households or buildings into neighborhoods or community zones, optimizing for social affinity and infrastructure costs.

## Scenario

In urban planning, each household/building has features such as location, household size, income, and lifestyle preferences. The goal is to group these into neighborhoods so that similar households are together, and to decide when to create a new community zone versus expanding existing ones.

- **Affinity (Parameter a):** Measures how strongly households prefer to be grouped together (e.g., similar demographics, shared interests).
- **Barrier (Parameter b):** Represents the cost of establishing a new neighborhood (e.g., infrastructure, zoning, administrative overhead).

## How to Run

1. Install dependencies:
   ```
   pip install numpy pandas matplotlib scikit-learn
   ```
2. Run the demo:
   ```
   python urban_planning_demo.py
   ```
3. View results:
   - Visualizations are saved in the `visualizations/` folder.
   - Open `urban_planning_report.html` in your browser for a summary.

## What You'll Learn

- How to represent households/buildings as feature vectors
- How to use clustering to design neighborhoods
- How affinity and barrier parameters guide zoning and infrastructure decisions
- How to visualize and report the results

## Files

- `urban_planning_demo.py`: Main script
- `visualizations/`: Output charts and HTML report

## Example Output

- Optimal number of neighborhoods (zones)
- Affinity and cost parameters for grouping
- Neighborhood distribution plot
- HTML report summarizing the community design

---

This demo is ideal for urban planners, architects, and policymakers seeking data-driven approaches to community design and resource allocation.
