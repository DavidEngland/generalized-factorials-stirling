# Data Packet Network Demo: Stirling Partitioning for Decentralized Routing

This example demonstrates how the Stirling Partitioning Algorithm can be applied to model the routing of data packets in a decentralized computer network, balancing clustering efficiency and the cost of creating new servers.

## Detailed Explanation

### Conceptual Model

In decentralized networks, each incoming data packet must be routed to an appropriate server. The network faces a fundamental tradeoff:

1. **Route to existing servers (clustering)**: This leverages existing resources but may lead to overloading or suboptimal routing if packets are dissimilar.
2. **Create new servers (partitioning)**: This provides better service for dissimilar packets but increases infrastructure costs.

This perfectly mirrors the Stirling Partitioning framework, where:

- **Parameter a (Affinity)**: Represents the tendency to group similar packets together on the same server. Higher values indicate stronger preference for packing similar workloads together (efficient resource utilization).
- **Parameter b (Barrier)**: Represents the cost of creating a new server. Higher values indicate greater resistance to spinning up new infrastructure (financial or resource constraints).

### How the Algorithm Works

1. **Packet Representation**: Each data packet is represented by features including arrival time, size, priority, and source ID.
2. **Clustering Analysis**: The algorithm tests different numbers of servers (k values) using k-means clustering.
3. **Parameter Estimation**: For each k, the algorithm calculates:
   - Affinity: How similar packets are within each server cluster
   - Cost: How different servers are from each other
4. **Optimization**: The algorithm finds the optimal number of servers by maximizing clustering quality (silhouette score).
5. **Parameter Interpretation**: The slopes of affinity and cost vs. k reveal the underlying Stirling parameters.

### Practical Network Implications

- **Low a, Low b**: Many small, specialized servers (microservice architecture)
- **High a, Low b**: Few specialized servers (service-oriented architecture)
- **Low a, High b**: Many general-purpose servers (distributed computing)
- **High a, High b**: Few general-purpose servers (centralized computing)

By estimating these parameters from actual network traffic, operators can:
1. Determine the optimal number of servers
2. Decide when to route to existing servers vs. when to spin up new ones
3. Design scaling policies that align with the natural clustering tendencies of their traffic

## Scenario

In a distributed network, each incoming data packet must be assigned to a server for processing. The network can either route the packet to an existing server (clustering for efficiency) or create a new server (incurring a setup cost).

- **Affinity (Parameter a):** Measures the network's tendency to route packets to existing servers, optimizing for efficiency and resource utilization.
- **Barrier (Parameter b):** Represents the cost of establishing a new server, including hardware, energy, and setup time.

## How to Run

1. Install dependencies:
   ```
   pip install numpy pandas matplotlib scikit-learn
   ```
2. Run the demo:
   ```
   python data_packet_network_demo.py
   ```
3. View results:
   - Visualizations are saved in the `visualizations/` folder.
   - Open `network_report.html` in your browser for a summary.

## What You'll Learn

- How to represent data packets and servers as feature vectors
- How to use clustering to optimize packet routing and server allocation
- How affinity and barrier parameters guide network design and scaling
- How to visualize and report the results

## Files

- `data_packet_network_demo.py`: Main script
- `visualizations/`: Output charts and HTML report

## Example Output

- Optimal number of servers (clusters)
- Affinity and cost parameters for routing
- Server assignment plot
- HTML report summarizing the network optimization

---

This demo is ideal for network engineers, system architects, and researchers interested in decentralized systems and resource allocation.
