# Running the Examples

## Environment Setup

If you're seeing "command not found: python", you need to set up your Python environment first:

### 1. Create and Activate a Virtual Environment

```bash
# Navigate to the repository root
cd /Users/davidengland/Documents/GitHub/generalized-factorials-stirling

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

After activation, your command prompt should show `(venv)` at the beginning, indicating the virtual environment is active.

### 2. Install Dependencies

```bash
# Make sure you're in the activated virtual environment
pip install numpy pandas matplotlib scikit-learn sympy
```

## Running the Examples

With your environment set up, you can now run the examples:

```bash
# Make sure you're in the repository root with the venv activated
cd /Users/davidengland/Documents/GitHub/generalized-factorials-stirling
source venv/bin/activate  # If not already activated

# Run examples
```

### Product Affinity Analysis (Retail Demo)

```bash
# Navigate to the example directory
cd examples/Simple-Retail-Demo

# Run the example
python simple_retail_demo.py
# If that doesn't work, try:
python3 simple_retail_demo.py

# View the results
open visualizations/report.html  # On macOS
# Or manually open visualizations/report.html in your browser
```

### Delivery Route Optimization (Supply Chain)

```bash
# Navigate to the example directory
cd examples/Supply-Chain-Delivery

# Run the example
python supply_chain_delivery_demo.py
# If that doesn't work, try:
python3 supply_chain_delivery_demo.py

# View the results
open visualizations/delivery_report.html  # On macOS
# Or manually open visualizations/delivery_report.html in your browser
```

### Network Resource Allocation (Data Packet Network)

```bash
# Navigate to the example directory
cd examples/Data-Packet-Network

# Run the example
python data_packet_network_demo.py

# View the results
open visualizations/network_report.html  # On macOS
# Or manually open visualizations/network_report.html in your browser
```

### 4. Basic Usage Example

```bash
# Run the basic usage example from the repository root
python examples/basic_usage.py
```

## Troubleshooting

### Command Not Found: python

If you see "command not found: python", try these solutions:

1. **Use `python3` instead of `python`**: 
   ```bash
   python3 examples/basic_usage.py
   ```

2. **Check your Python installation**:
   ```bash
   which python3
   ```

3. **Ensure the virtual environment is activated**:
   The command prompt should show `(venv)` at the beginning.

4. **Install Python if needed**:
   - macOS: `brew install python3`
   - Windows: Download from [python.org](https://www.python.org/downloads/)

### Import Errors

If you encounter import errors even with the virtual environment:

```bash
# From the repository root with venv activated
PYTHONPATH=$PYTHONPATH:$(pwd) python examples/Simple-Retail-Demo/simple_retail_demo.py
```

### Creating a Requirements File

To make dependency installation easier, you can create a requirements.txt file:

```bash
# In the repository root
echo "numpy\npandas\nmatplotlib\nscikit-learn\nsympy" > requirements.txt

# Then install dependencies with:
pip install -r requirements.txt
```
