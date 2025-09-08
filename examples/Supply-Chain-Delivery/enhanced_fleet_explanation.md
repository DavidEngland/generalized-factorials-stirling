# Enhanced Fleet Optimizer: Dynamic Stirling Parameters

This enhanced version of the fleet optimizer uses **dynamic affinity and barrier parameters** that adapt based on vehicle capabilities and payload characteristics, providing more realistic and flexible fleet optimization.

## Key Improvements

### 1. Dynamic Affinity Parameter (a)
The affinity parameter now adapts based on:
- **Vehicle-Payload Matching**: How well vehicle capabilities match payload requirements
- **Capacity Utilization**: Efficient use of vehicle capacity
- **Driver Skill Level**: Higher skilled drivers for complex deliveries
- **Specialized Equipment**: Equipment bonuses for specific payload types

### 2. Dynamic Barrier Parameter (b)
The barrier parameter now incorporates:
- **Fuel Efficiency**: Higher barriers for less efficient vehicles
- **Maintenance Costs**: Age and condition-based operational costs
- **Time Constraints**: Penalties for tight delivery windows
- **Handling Complexity**: Different handling rates for different vehicle types

### 3. Enhanced Fleet Data Structure
The fleet CSV now supports additional attributes:
```csv
id,type,capacity,age,maintenance_cost,fuel_efficiency,handling_rate,specialized_equipment,driver_skill_level,base_cost_per_km
1,van,800,2,0.05,18,1.2,0,4,0.45
2,truck,1500,5,0.12,12,0.8,1,3,0.65
3,refrigerated_van,600,1,0.08,15,1.0,1,5,0.75
```

### 4. Payload Complexity Analysis
Automatically computes complexity metrics:
- **Size Complexity**: Relative package size difficulty
- **Priority Factor**: Delivery urgency weighting
- **Time Flexibility**: Time window constraints

## Mathematical Framework

For each vehicle-route combination, the optimizer computes:

**Dynamic Affinity:**
