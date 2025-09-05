#!/bin/bash

# Navigate to the project directory
cd /Users/davidengland/Documents/GitHub/generalized-factorials-stirling/examples/atmospheric_boundary_layer

# Option 1: Create and activate a virtual environment (recommended)
# Uncomment these lines if you want to use a virtual environment
# python -m venv venv
# source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Run the planetary comparison script
python planetary_comparison.py

# Create a directory for results if it doesn't exist
mkdir -p results

# Move generated figures to results directory
mv *.png results/

# Print results location
echo "Results saved in: results/"

# Optional: Generate report with key findings
echo "Generating summary report..."
python -c "
import matplotlib.pyplot as plt
from planetary_comparison import calculate_planetary_differences
metrics = calculate_planetary_differences()

with open('results/comparison_summary.txt', 'w') as f:
    f.write('Earth vs Mars Atmospheric Comparison Summary\n')
    f.write('===========================================\n\n')
    
    f.write('Component | Background Ratio | Enhancement Ratio | Diurnal Amplitude | Vertical Gradient | Cohesion Diff\n')
    f.write('----------|------------------|------------------|-------------------|-------------------|-------------\n')
    
    for component, values in metrics.items():
        f.write(f\"{component:9} | {values['background_ratio']:16.2f} | {values['surface_enhancement_ratio']:16.2f} | \"
              f\"{values['diurnal_amplitude_ratio']:17.2f} | {values['vertical_gradient_ratio']:17.2f} | \"
              f\"{values['cohesion_difference']:13.2f}\n\")
    
    f.write('\nScientific Insights:\n')
    
    # CO2 analysis
    if metrics['co2']['background_ratio'] > 900:
        f.write('✓ CO2 concentration on Mars is realistic (~95% vs 0.04% on Earth)\n')
    else:
        f.write('✗ CO2 concentration ratio is not realistic\n')
        
    # Water vapor analysis
    if metrics['water_vapor']['background_ratio'] < 0.1:
        f.write('✓ Water vapor on Mars is realistically low compared to Earth\n')
    else:
        f.write('✗ Water vapor ratio is not realistic\n')
        
    # Dust analysis
    if metrics['dust']['background_ratio'] > 3:
        f.write('✓ Dust levels on Mars are realistically higher than Earth\n')
    else:
        f.write('✗ Dust level ratio is not realistic\n')
        
    # Diurnal analysis
    if any(values['diurnal_amplitude_ratio'] > 1.5 for values in metrics.values()):
        f.write('✓ Stronger diurnal cycles on Mars due to thin atmosphere confirmed\n')
    else:
        f.write('✗ Diurnal cycle strength not accurately represented\n')
"

echo "Analysis complete! Check results/comparison_summary.txt for detailed findings."
