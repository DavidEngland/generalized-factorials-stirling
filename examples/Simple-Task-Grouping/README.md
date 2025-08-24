-->
# Simple Task Grouping Demo: Stirling Partitioning in Action

This example demonstrates how to use the Stirling Partitioning Algorithm to optimally group tasks based on their similarity, using only basic Python and scikit-learn.

## Scenario

Suppose you have a list of tasks, each described by a few features (e.g., estimated time, required skill level, priority). You want to group these tasks into clusters so that similar tasks are grouped together, and the number of clusters is chosen automatically using the Stirling Partitioning Algorithm.

## How to Run

1. Install dependencies:
   ```
   pip install numpy pandas matplotlib scikit-learn
   ```
2. Run the demo:
   ```
   python simple_task_grouping.py
   ```
3. View results:
   - Visualizations are saved in the `visualizations/` folder.
   - Open `task_grouping_report.html` in your browser for a summary.

## What You'll Learn

- How to represent tasks as feature vectors
- How to use k-means clustering and silhouette score to find the optimal number of groups
- How to interpret affinity and cost parameters for your clusters
- How to visualize and report the results

## Files

- `simple_task_grouping.py`: Main script
- `visualizations/`: Output charts and HTML report

## Example Output

- Optimal number of task groups (k)
- Affinity and cost parameters for clustering
- Cluster distribution plot
- HTML report summarizing the grouping and recommendations

---

This demo is ideal for project managers, team leads, or anyone needing a quick, interpretable way to group tasks for scheduling or assignment.
