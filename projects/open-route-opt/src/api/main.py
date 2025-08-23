"""
FastAPI server for OpenRouteOpt proof of concept.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
import sys
import os
from datetime import datetime

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.core.python.stirling import DeliveryPoint, Vehicle, RouteOptimizer

app = FastAPI(
    title="OpenRouteOpt API",
    description="API for route optimization using generalized Stirling numbers",
    version="0.1.0"
)

# Enable CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only - restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DeliveryPointModel(BaseModel):
    """API model for delivery points."""
    id: str
    lat: float
    lng: float
    time_window_start: Optional[str] = None  # Format: "HH:MM"
    time_window_end: Optional[str] = None    # Format: "HH:MM"
    service_duration: float = 300.0          # In seconds
    demand: float = 1.0

class VehicleModel(BaseModel):
    """API model for vehicles."""
    id: str
    start_lat: float
    start_lng: float
    capacity: float = 100.0
    max_distance: Optional[float] = None
    max_duration: Optional[float] = None  # In seconds

class OptimizationRequest(BaseModel):
    """API request model for route optimization."""
    delivery_points: List[DeliveryPointModel]
    vehicles: List[VehicleModel]
    parameters: Dict[str, float] = {"a": 1.0, "b": 1.0}

class OptimizationResponse(BaseModel):
    """API response model for route optimization."""
    routes: Dict[str, List[str]]
    metrics: Dict[str, float]
    visualization_data: Dict

class ParameterEstimationRequest(BaseModel):
    """API request model for parameter estimation."""
    historical_data: List[Dict]

class ParameterEstimationResponse(BaseModel):
    """API response model for parameter estimation."""
    parameters: Dict[str, float]
    confidence_intervals: Dict[str, List[float]]

def _convert_time_to_seconds(time_str: Optional[str]) -> Optional[float]:
    """Convert HH:MM time string to seconds from midnight."""
    if not time_str:
        return None
    
    hours, minutes = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60

def _prepare_visualization_data(
    delivery_points: List[DeliveryPoint],
    vehicles: List[Vehicle],
    routes: Dict[str, List[str]]
) -> Dict:
    """Prepare data for frontend visualization."""
    points_dict = {p.id: p for p in delivery_points}
    vehicles_dict = {v.id: v for v in vehicles}
    
    route_coordinates = {}
    for vehicle_id, route in routes.items():
        vehicle = vehicles_dict[vehicle_id]
        coords = []
        
        # Start at depot
        coords.append([vehicle.start_lng, vehicle.start_lat])
        
        # Add each stop
        for point_id in route:
            point = points_dict[point_id]
            coords.append([point.lng, point.lat])
        
        # Return to depot
        coords.append([vehicle.start_lng, vehicle.start_lat])
        
        route_coordinates[vehicle_id] = coords
    
    return {
        "routes": route_coordinates,
        "points": [
            {
                "id": p.id,
                "coordinates": [p.lng, p.lat]
            } for p in delivery_points
        ],
        "depots": [
            {
                "id": v.id,
                "coordinates": [v.start_lng, v.start_lat]
            } for v in vehicles
        ]
    }

@app.post("/optimize", response_model=OptimizationResponse)
async def optimize_routes(request: OptimizationRequest):
    """
    Optimize routes for the given delivery points and vehicles.
    """
    try:
        # Convert API models to domain models
        delivery_points = []
        for p in request.delivery_points:
            delivery_points.append(DeliveryPoint(
                id=p.id,
                lat=p.lat,
                lng=p.lng,
                time_window_start=_convert_time_to_seconds(p.time_window_start),
                time_window_end=_convert_time_to_seconds(p.time_window_end),
                service_duration=p.service_duration,
                demand=p.demand
            ))
        
        vehicles = []
        for v in request.vehicles:
            vehicles.append(Vehicle(
                id=v.id,
                start_lat=v.start_lat,
                start_lng=v.start_lng,
                capacity=v.capacity,
                max_distance=v.max_distance,
                max_duration=v.max_duration
            ))
        
        # Run optimization
        optimizer = RouteOptimizer(
            a=request.parameters.get("a", 1.0),
            b=request.parameters.get("b", 1.0)
        )
        routes = optimizer.optimize(delivery_points, vehicles)
        
        # Calculate metrics
        points_dict = {p.id: p for p in delivery_points}
        total_distance = 0.0
        route_distances = {}
        
        for vehicle_id, route in routes.items():
            vehicle = next(v for v in vehicles if v.id == vehicle_id)
            distance = optimizer.calculate_route_cost(route, points_dict, vehicle)
            route_distances[vehicle_id] = distance
            total_distance += distance
        
        # Prepare visualization data
        viz_data = _prepare_visualization_data(delivery_points, vehicles, routes)
        
        return OptimizationResponse(
            routes=routes,
            metrics={
                "total_distance": total_distance,
                "route_distances": route_distances,
                "vehicles_used": len([v for v in routes.values() if len(v) > 0])
            },
            visualization_data=viz_data
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/parameters/estimate", response_model=ParameterEstimationResponse)
async def estimate_parameters(request: ParameterEstimationRequest):
    """
    Estimate parameters a and b from historical data.
    """
    try:
        # Extract n, k pairs and measures from historical data
        n_k_pairs = []
        for data_point in request.historical_data:
            n = data_point.get("n")
            k = data_point.get("k")
            measure = data_point.get("measure")
            
            if n is not None and k is not None and measure is not None:
                n_k_pairs.append((n, k, measure))
        
        if not n_k_pairs:
            raise HTTPException(
                status_code=400, 
                detail="No valid data points found in historical data"
            )
        
        # Estimate parameters
        optimizer = RouteOptimizer()
        a, b = optimizer.stirling.estimate_parameters(n_k_pairs)
        
        # In a real implementation, we would calculate confidence intervals
        # Here we'll just provide dummy values
        confidence_intervals = {
            "a": [a - 0.1, a + 0.1],
            "b": [b - 0.1, b + 0.1]
        }
        
        return ParameterEstimationResponse(
            parameters={"a": a, "b": b},
            confidence_intervals=confidence_intervals
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """
    Simple health check endpoint.
    """
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
