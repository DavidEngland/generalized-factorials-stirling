# Getting Started with OpenRouteOpt

This guide will help you set up and run the OpenRouteOpt proof of concept on your local machine.

## Prerequisites

Before beginning, ensure you have the following installed:

- **Python 3.9+**
- **Julia 1.8+** (optional, for performance-critical components)
- **Node.js 16+** (for the UI components)
- **Git**

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/open-route-opt.git
cd open-route-opt
```

### 2. Set Up Python Environment

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Set Up Julia (Optional)

If you want to use the high-performance Julia implementation:

```bash
# Install Julia dependencies
julia -e 'using Pkg; Pkg.activate("."); Pkg.instantiate()'

# Install PyJulia for Python-Julia interoperability
pip install julia
python -c "import julia; julia.install()"
```

### 4. Set Up UI Components

```bash
# Navigate to UI directory
cd src/ui

# Install dependencies
npm install

# Return to project root
cd ../..
```

## Running the Proof of Concept

### 1. Start the API Server

```bash
# Ensure virtual environment is activated
cd src/api
uvicorn main:app --reload
```

The API server will be available at http://localhost:8000.

### 2. Start the UI Development Server

In a new terminal:

```bash
cd src/ui
npm start
```

The UI will be available at http://localhost:3000.

## Using the API

The API provides several endpoints for route optimization:

### Optimize Routes

```bash
curl -X POST http://localhost:8000/optimize \
  -H "Content-Type: application/json" \
  -d '{
    "delivery_points": [
      {
        "id": "p1",
        "lat": 40.7128,
        "lng": -74.0060,
        "time_window_start": "09:00",
        "time_window_end": "12:00"
      },
      {
        "id": "p2",
        "lat": 40.7282,
        "lng": -73.7949,
        "time_window_start": "10:00",
        "time_window_end": "15:00"
      }
    ],
    "vehicles": [
      {
        "id": "v1",
        "start_lat": 40.7300,
        "start_lng": -73.9950
      }
    ],
    "parameters": {
      "a": 1.5,
      "b": 2.0
    }
  }'
```

### Estimate Parameters

```bash
curl -X POST http://localhost:8000/parameters/estimate \
  -H "Content-Type: application/json" \
  -d '{
    "historical_data": [
      {"n": 10, "k": 3, "measure": 7.5},
      {"n": 15, "k": 4, "measure": 10.2},
      {"n": 20, "k": 5, "measure": 13.8}
    ]
  }'
```

## Working with Sample Data

The project includes sample datasets in the `data/` directory:

```bash
# Process NYC Taxi dataset
python scripts/process_nyc_taxi.py

# Run optimization on processed data
python scripts/optimize_sample.py
```

## Troubleshooting

### API Server Issues

- **"ModuleNotFoundError"**: Ensure you're running from the project root and the virtual environment is activated
- **Port conflicts**: If port 8000 is in use, specify a different port with `--port 8001`

### Julia Integration Issues

- **"Julia not found"**: Ensure Julia is in your PATH or set `JULIA_BINDIR` environment variable
- **"Package not found"**: Run `julia -e 'using Pkg; Pkg.activate("."); Pkg.instantiate()'` again

### Performance Optimization

If you encounter performance issues with large datasets:

1. Enable the Julia backend:
   ```python
   import os
   os.environ["USE_JULIA_BACKEND"] = "1"
   ```

2. Reduce the dataset size for testing:
   ```python
   from src.core.python.data_utils import sample_dataset
   
   # Sample 20% of the data
   small_dataset = sample_dataset(full_dataset, 0.2)
   ```

## Next Steps

Once you have the proof of concept running:

1. Try modifying the parameters `a` and `b` to see how they affect route assignments
2. Experiment with different dataset sizes to test scalability
3. Compare with the OR-Tools baseline implementation
4. Explore the visualization options in the UI

For more detailed information, refer to the [API documentation](api.md) and [architecture overview](architecture.md).
