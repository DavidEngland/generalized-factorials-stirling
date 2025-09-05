#!/usr/bin/env python3
"""
Interactive Route Explorer for Dual-Perspective Delivery Optimization

This script provides an interactive visualization of route optimization results
from the dual_perspective_delivery.py module. It allows users to:
- Compare constructive and deconstructive approaches
- Explore individual routes on an interactive map
- Examine detailed route metrics
- Experiment with different parameter values
"""

import argparse
import json
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap, MarkerCluster, Draw
import tempfile
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional, Any, Union
import webbrowser

# Try to import optional dependencies
try:
    import ipywidgets as widgets
    from IPython.display import display, HTML, clear_output
    IPYWIDGETS_AVAILABLE = True
except ImportError:
    IPYWIDGETS_AVAILABLE = False
    print("Warning: ipywidgets not available. Install with 'pip install ipywidgets'")
    print("Falling back to static visualization.")

try:
    # Try to import dash components for interactive web app
    import dash
    from dash import dcc, html, Input, Output, State, callback
    import dash_bootstrap_components as dbc
    import plotly.express as px
    import plotly.graph_objects as go
    DASH_AVAILABLE = True
except ImportError:
    DASH_AVAILABLE = False
    print("Warning: Dash not available. Install with 'pip install dash dash-bootstrap-components plotly'")
    print("Falling back to static visualization.")


class RouteExplorer:
    """Interactive explorer for route optimization results."""
    
    def __init__(self, solution_file: str, data_file: Optional[str] = None):
        """
        Initialize the route explorer.
        
        Args:
            solution_file: Path to the JSON solution file
            data_file: Path to the original data CSV (optional)
        """
        self.solution_file = solution_file
        self.data_file = data_file
        self.solution_data = self._load_solution()
        self.delivery_data = self._load_delivery_data()
        self.temp_dir = tempfile.mkdtemp()
        
    def _load_solution(self) -> Dict:
        """Load solution data from JSON file."""
        try:
            with open(self.solution_file, 'r') as f:
                data = json.load(f)
                
                # Validate the structure of the loaded data
                self._validate_solution_data(data)
                
                return data
        except Exception as e:
            print(f"Error loading solution file: {e}")
            sys.exit(1)
    
    def _validate_solution_data(self, data: Dict) -> None:
        """
        Validate the solution data structure and fill in missing fields with defaults.
        
        Args:
            data: The loaded solution data
        """
        # Check for required top-level keys
        for approach in ['constructive', 'deconstructive']:
            if approach not in data:
                data[approach] = {}
                
            # Ensure all required fields exist
            if 'parameters' not in data[approach]:
                data[approach]['parameters'] = {'a': 0.0, 'b': 0.0}
            elif 'a' not in data[approach]['parameters'] or 'b' not in data[approach]['parameters']:
                data[approach]['parameters']['a'] = data[approach]['parameters'].get('a', 0.0)
                data[approach]['parameters']['b'] = data[approach]['parameters'].get('b', 0.0)
                
            if 'optimal_k' not in data[approach]:
                data[approach]['optimal_k'] = 0
                
            if 'optimal_cost' not in data[approach]:
                data[approach]['optimal_cost'] = 0.0
                
            if 'all_costs' not in data[approach]:
                data[approach]['all_costs'] = []
                
            if 'routes' not in data[approach]:
                data[approach]['routes'] = {}
                
            if 'total_distance' not in data[approach]:
                # Calculate total distance from routes if available
                if data[approach]['routes']:
                    data[approach]['total_distance'] = sum(
                        route.get('total_distance', 0) 
                        for route in data[approach]['routes'].values()
                    )
                else:
                    data[approach]['total_distance'] = 0.0
    
    def _load_delivery_data(self) -> pd.DataFrame:
        """Load delivery data from CSV file."""
        if not self.data_file:
            # Try to find the data file in standard locations
            possible_paths = [
                "data/sample_deliveries.csv",
                "../data/sample_deliveries.csv",
                "sample_deliveries.csv"
            ]
            
            for path in possible_paths:
                if os.path.exists(path):
                    self.data_file = path
                    break
            
            if not self.data_file:
                print("Warning: No delivery data file found. Limited visualization available.")
                # Create minimal dummy data from solution information
                if 'constructive' in self.solution_data and 'routes' in self.solution_data['constructive']:
                    points = []
                    for route_id, route_info in self.solution_data['constructive']['routes'].items():
                        for point_id in route_info['points']:
                            points.append(point_id)
                    
                    # Create a dataframe with just IDs
                    return pd.DataFrame({
                        'id': points,
                        'latitude': np.random.rand(len(points)) * 10,
                        'longitude': np.random.rand(len(points)) * 10
                    })
                return None
        
        try:
            df = pd.read_csv(self.data_file)
            # Convert time windows to datetime if present
            if "time_window_start" in df.columns and "time_window_end" in df.columns:
                df["time_window_start"] = pd.to_datetime(df["time_window_start"])
                df["time_window_end"] = pd.to_datetime(df["time_window_end"])
            return df
        except Exception as e:
            print(f"Error loading delivery data: {e}")
            return None
    
    def create_static_visualization(self):
        """Create static visualizations and open them in a browser."""
        # Create map visualization
        map_path = os.path.join(self.temp_dir, "interactive_map.html")
        self._create_interactive_map(map_path)
        
        # Create comparison charts
        charts_path = os.path.join(self.temp_dir, "route_charts.html")
        self._create_comparison_charts(charts_path)
        
        # Open files in browser
        webbrowser.open(f"file://{map_path}")
        webbrowser.open(f"file://{charts_path}")
        
        print(f"Visualizations created at:")
        print(f"  - Map: {map_path}")
        print(f"  - Charts: {charts_path}")
    
    def _create_interactive_map(self, output_path: str):
        """
        Create an interactive map visualization of routes.
        
        Args:
            output_path: Path to save the HTML file
        """
        if self.delivery_data is None:
            print("No delivery data available for map visualization")
            # Create a fallback map with error message
            m = folium.Map(location=[0, 0], zoom_start=2)
            folium.Marker(
                location=[0, 0],
                popup="No delivery data available. Run with --data parameter.",
                icon=folium.Icon(color="red", icon="info-sign")
            ).add_to(m)
            m.save(output_path)
            return
            
        # Calculate map center
        center = [self.delivery_data['latitude'].mean(), self.delivery_data['longitude'].mean()]
        m = folium.Map(location=center, zoom_start=12)
        
        # Add draw tools for measuring distances
        try:
            from folium.plugins import Draw
            draw = Draw(
                export=True,
                position='topleft',
                draw_options={
                    'polyline': True,
                    'rectangle': True,
                    'circle': True,
                    'marker': True,
                    'circlemarker': False,
                    'polygon': True
                }
            )
            draw.add_to(m)
        except ImportError:
            print("Draw plugin not available. Install with 'pip install folium'")
        
        # Add routes from both approaches
        colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 
                 'lightred', 'darkblue', 'cadetblue', 'darkgreen', 'pink']
        
        # Constructive routes
        if 'constructive' in self.solution_data and 'routes' in self.solution_data['constructive']:
            routes_data = self.solution_data['constructive']['routes']
            
            for route_id, route_info in routes_data.items():
                # Convert to int since JSON keys are strings
                route_id = int(route_id)
                color = colors[route_id % len(colors)]
                
                # Get point data
                point_ids = route_info['points']
                route_points = self.delivery_data[self.delivery_data['id'].isin(point_ids)]
                
                # Create a route group
                route_group = folium.FeatureGroup(name=f"Constructive Route {route_id+1}")
                
                # Add polyline for the route
                if 'ordered_indices' in route_info and len(route_info['ordered_indices']) > 1:
                    # Use the optimized order if available
                    ordered_indices = route_info['ordered_indices']
                    ordered_points = self.delivery_data.iloc[ordered_indices]
                else:
                    # Otherwise sort by ID
                    ordered_points = route_points.sort_values('id')
                
                if len(ordered_points) > 1:
                    route_coords = [(row['latitude'], row['longitude']) 
                                   for _, row in ordered_points.iterrows()]
                    
                    # Draw the route path
                    folium.PolyLine(
                        locations=route_coords,
                        color=color,
                        weight=4,
                        opacity=0.8,
                        tooltip=f"Route {route_id+1}: {route_info['point_count']} points, {route_info['total_distance']:.2f} distance"
                    ).add_to(route_group)
                
                # Add markers for each point with popup information
                for _, point in route_points.iterrows():
                    popup_content = f"""
                    <b>ID:</b> {point['id']}<br>
                    <b>Route:</b> {route_id+1} (Constructive)<br>
                    """
                    
                    # Add optional attributes if available
                    if 'package_size' in point:
                        popup_content += f"<b>Size:</b> {point['package_size']}<br>"
                    if 'delivery_priority' in point:
                        popup_content += f"<b>Priority:</b> {point['delivery_priority']}<br>"
                    if 'time_window_start' in point and 'time_window_end' in point:
                        popup_content += f"<b>Window:</b> {point['time_window_start'].strftime('%H:%M')} - {point['time_window_end'].strftime('%H:%M')}<br>"
                    
                    folium.CircleMarker(
                        location=[point['latitude'], point['longitude']],
                        radius=6,
                        color=color,
                        fill=True,
                        fill_color=color,
                        fill_opacity=0.7,
                        popup=folium.Popup(popup_content, max_width=200)
                    ).add_to(route_group)
                
                route_group.add_to(m)
        
        # Deconstructive routes (similar structure with different styling)
        if 'deconstructive' in self.solution_data and 'routes' in self.solution_data['deconstructive']:
            routes_data = self.solution_data['deconstructive']['routes']
            
            for route_id, route_info in routes_data.items():
                # Convert to int since JSON keys are strings
                route_id = int(route_id)
                color = colors[route_id % len(colors)]
                
                # Get point data
                point_ids = route_info['points']
                route_points = self.delivery_data[self.delivery_data['id'].isin(point_ids)]
                
                # Create a route group
                route_group = folium.FeatureGroup(name=f"Deconstructive Route {route_id+1}")
                
                # Add polyline for the route
                if 'ordered_indices' in route_info and len(route_info['ordered_indices']) > 1:
                    ordered_indices = route_info['ordered_indices']
                    ordered_points = self.delivery_data.iloc[ordered_indices]
                else:
                    ordered_points = route_points.sort_values('id')
                
                if len(ordered_points) > 1:
                    route_coords = [(row['latitude'], row['longitude']) 
                                   for _, row in ordered_points.iterrows()]
                    
                    # Draw the route path with dashed line to distinguish from constructive
                    folium.PolyLine(
                        locations=route_coords,
                        color=color,
                        weight=4,
                        opacity=0.8,
                        dash_array='5,10',
                        tooltip=f"Route {route_id+1}: {route_info['point_count']} points, {route_info['total_distance']:.2f} distance"
                    ).add_to(route_group)
                
                # Add markers for each point with popup information
                for _, point in route_points.iterrows():
                    popup_content = f"""
                    <b>ID:</b> {point['id']}<br>
                    <b>Route:</b> {route_id+1} (Deconstructive)<br>
                    """
                    
                    # Add optional attributes if available
                    if 'package_size' in point:
                        popup_content += f"<b>Size:</b> {point['package_size']}<br>"
                    if 'delivery_priority' in point:
                        popup_content += f"<b>Priority:</b> {point['delivery_priority']}<br>"
                    if 'time_window_start' in point and 'time_window_end' in point:
                        popup_content += f"<b>Window:</b> {point['time_window_start'].strftime('%H:%M')} - {point['time_window_end'].strftime('%H:%M')}<br>"
                    
                    folium.CircleMarker(
                        location=[point['latitude'], point['longitude']],
                        radius=6,
                        color=color,
                        fill=True,
                        fill_color=color,
                        fill_opacity=0.5,
                        popup=folium.Popup(popup_content, max_width=200),
                        dash_array='3'
                    ).add_to(route_group)
                
                route_group.add_to(m)
        
        # Add layer control and fullscreen option
        folium.LayerControl(collapsed=False).add_to(m)
        
        # Add legend
        legend_html = """
        <div style="position: fixed; 
            bottom: 50px; left: 50px; width: 180px; height: 120px; 
            border:2px solid grey; z-index:9999; background-color:white;
            padding: 10px; font-size: 14px;">
            <b>Route Types:</b><br>
            <i class="fa fa-minus" style="color:blue;"></i> Constructive<br>
            <i class="fa fa-minus" style="color:red; text-decoration: dashed;"></i> Deconstructive (dashed)<br>
            <hr>
            Use the layers control to toggle routes<br>
            Click on points for details
        </div>
        """
        m.get_root().html.add_child(folium.Element(legend_html))
        
        # Add comparison information as a pop-up
        if 'constructive' in self.solution_data and 'deconstructive' in self.solution_data:
            c = self.solution_data['constructive']
            d = self.solution_data['deconstructive']
            
            info_html = f"""
            <div style="position: fixed; 
                top: 50px; right: 50px; width: 300px; 
                border:2px solid grey; z-index:9999; background-color:white;
                padding: 10px; font-size: 14px; opacity: 0.9;">
                <h3 style="margin-top:0;">Approach Comparison</h3>
                <table style="width:100%; border-collapse: collapse;">
                    <tr style="border-bottom: 1px solid #ddd;">
                        <th style="text-align:left;">Metric</th>
                        <th style="text-align:right;">Constructive</th>
                        <th style="text-align:right;">Deconstructive</th>
                    </tr>
                    <tr style="border-bottom: 1px solid #ddd;">
                        <td>Routes</td>
                        <td style="text-align:right;">{c["optimal_k"]}</td>
                        <td style="text-align:right;">{d["optimal_k"]}</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #ddd;">
                        <td>Total Distance</td>
                        <td style="text-align:right;">{c["total_distance"]:.2f}</td>
                        <td style="text-align:right;">{d["total_distance"]:.2f}</td>
                    </tr>
                    <tr>
                        <td>Parameters (a,b)</td>
                        <td style="text-align:right;">({c["parameters"]["a"]:.2f}, {c["parameters"]["b"]:.2f})</td>
                        <td style="text-align:right;">({d["parameters"]["a"]:.2f}, {d["parameters"]["b"]:.2f})</td>
                    </tr>
                </table>
                <div style="margin-top:10px; font-style:italic;">
                    Better approach: <b>{
                    "Deconstructive" if d["total_distance"] < c["total_distance"] else 
                    "Constructive" if c["total_distance"] < d["total_distance"] else "Tie"
                    }</b>
                </div>
            </div>
            """
            m.get_root().html.add_child(folium.Element(info_html))
        
        # Save map to HTML file
        m.save(output_path)
    
    def _create_comparison_charts(self, output_path: str):
        """
        Create comparison charts and save as HTML.
        
        Args:
            output_path: Path to save the HTML file
        """
        if 'constructive' not in self.solution_data or 'deconstructive' not in self.solution_data:
            print("Missing data for comparison charts")
            return
        
        try:
            c = self.solution_data['constructive']
            d = self.solution_data['deconstructive']
            
            # Create HTML with embedded chart images
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Route Optimization Charts</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 20px; }}
                    h1, h2 {{ color: #333366; }}
                    .chart-container {{ margin: 20px 0; }}
                    .chart-row {{ display: flex; flex-wrap: wrap; gap: 20px; }}
                    .chart-card {{ flex: 1; min-width: 400px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); 
                                padding: 20px; border-radius: 5px; background: white; }}
                    .parameter-table {{ border-collapse: collapse; width: 100%; }}
                    .parameter-table th, .parameter-table td {{ padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }}
                    .parameter-row {{ display: flex; gap: 10px; }}
                    .parameter-input {{ width: 80px; padding: 5px; }}
                    .parameter-label {{ flex: 1; }}
                    .run-button {{ background: #4CAF50; color: white; border: none; padding: 10px 15px; 
                                border-radius: 4px; cursor: pointer; }}
                    .run-button:hover {{ background: #45a049; }}
                    .missing-data {{ padding: 20px; background-color: #fff3cd; color: #856404; border-radius: 5px; margin: 20px 0; }}
                </style>
                <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            </head>
            <body>
                <h1>Route Optimization Comparison</h1>
            """
            
            # Check if we have the necessary data to display the charts
            has_cost_data = ('all_costs' in c and c['all_costs'] and 'all_costs' in d and d['all_costs'])
            has_route_data = ('routes' in c and c['routes'] and 'routes' in d and d['routes'])
            
            if not has_cost_data and not has_route_data:
                html_content += """
                <div class="missing-data">
                    <h3>Limited Data Available</h3>
                    <p>The optimization results file does not contain sufficient data to generate detailed charts.</p>
                    <p>Make sure you run the optimization with the full dual-perspective approach.</p>
                </div>
                """
            else:
                html_content += """
                <div class="chart-row">
                """
                
                if has_cost_data:
                    html_content += """
                    <div class="chart-card">
                        <h2>Cost vs. Number of Routes</h2>
                        <canvas id="costChart" width="400" height="300"></canvas>
                    </div>
                    """
                
                if has_route_data:
                    html_content += """
                    <div class="chart-card">
                        <h2>Route Balance Comparison</h2>
                        <canvas id="balanceChart" width="400" height="300"></canvas>
                    </div>
                    """
                
                html_content += """
                </div>
                
                <div class="chart-row">
                """
                
                if has_route_data:
                    html_content += """
                    <div class="chart-card">
                        <h2>Route Distance Distribution</h2>
                        <canvas id="distanceChart" width="400" height="300"></canvas>
                    </div>
                    """
                
                html_content += f"""
                    <div class="chart-card">
                        <h2>Optimization Parameters</h2>
                        <table class="parameter-table">
                            <tr>
                                <th>Parameter</th>
                                <th>Constructive</th>
                                <th>Deconstructive</th>
                                <th>Interpretation</th>
                            </tr>
                            <tr>
                                <td>Affinity (a)</td>
                                <td>{c["parameters"].get("a", "N/A")}</td>
                                <td>{d["parameters"].get("a", "N/A")}</td>
                                <td>Cost of connecting/separating points</td>
                            </tr>
                            <tr>
                                <td>Barrier (b)</td>
                                <td>{c["parameters"].get("b", "N/A")}</td>
                                <td>{d["parameters"].get("b", "N/A")}</td>
                                <td>Cost of establishing route/boundary</td>
                            </tr>
                            <tr>
                                <td>Optimal k</td>
                                <td>{c.get("optimal_k", "N/A")}</td>
                                <td>{d.get("optimal_k", "N/A")}</td>
                                <td>Number of routes</td>
                            </tr>
                            <tr>
                                <td>Total Cost</td>
                                <td>{c.get("optimal_cost", "N/A")}</td>
                                <td>{d.get("optimal_cost", "N/A")}</td>
                                <td>S_{{n,k}}(a,b) value</td>
                            </tr>
                        </table>
                    </div>
                </div>
                """
            
            # JavaScript for charts - only add if we have data
            if has_cost_data or has_route_data:
                html_content += """
                <script>
                """
                
                if has_cost_data:
                    c_costs_json = json.dumps([{"x": cost[0], "y": cost[1]} for cost in c["all_costs"]] if "all_costs" in c and c["all_costs"] else [])
                    d_costs_json = json.dumps([{"x": cost[0], "y": cost[1]} for cost in d["all_costs"]] if "all_costs" in d and d["all_costs"] else [])
                    
                    html_content += f"""
                    // Cost vs k chart
                    const costCtx = document.getElementById('costChart').getContext('2d');
                    new Chart(costCtx, {{
                        type: 'line',
                        data: {{
                            datasets: [
                                {{
                                    label: 'Constructive',
                                    data: {c_costs_json},
                                    borderColor: 'blue',
                                    backgroundColor: 'rgba(0, 0, 255, 0.1)',
                                    tension: 0.1
                                }},
                                {{
                                    label: 'Deconstructive',
                                    data: {d_costs_json},
                                    borderColor: 'red',
                                    backgroundColor: 'rgba(255, 0, 0, 0.1)',
                                    tension: 0.1
                                }}
                            ]
                        }},
                        options: {{
                            scales: {{
                                x: {{
                                    type: 'linear',
                                    title: {{
                                        display: true,
                                        text: 'Number of Routes (k)'
                                    }}
                                }},
                                y: {{
                                    title: {{
                                        display: true,
                                        text: 'Total Cost'
                                    }}
                                }}
                            }}
                        }}
                    }});
                    """
                
                if has_route_data:
                    # Extract points per route and route distances safely
                    c_routes = c.get("routes", {})
                    d_routes = d.get("routes", {})
                    
                    c_points_per_route = json.dumps([r.get("point_count", 0) for r in c_routes.values()] if c_routes else [])
                    d_points_per_route = json.dumps([r.get("point_count", 0) for r in d_routes.values()] if d_routes else [])
                    
                    c_distances = json.dumps([r.get("total_distance", 0) for r in c_routes.values()] if c_routes else [])
                    d_distances = json.dumps([r.get("total_distance", 0) for r in d_routes.values()] if d_routes else [])
                    
                    html_content += f"""
                    // Route balance chart
                    const balanceCtx = document.getElementById('balanceChart').getContext('2d');
                    
                    new Chart(balanceCtx, {{
                        type: 'bar',
                        data: {{
                            labels: Array.from({{ length: Math.max({c_points_per_route}.length, {d_points_per_route}.length) }}, (_, i) => `Route ${{i+1}}`),
                            datasets: [
                                {{
                                    label: 'Constructive',
                                    data: {c_points_per_route},
                                    backgroundColor: 'rgba(0, 0, 255, 0.7)',
                                }},
                                {{
                                    label: 'Deconstructive',
                                    data: {d_points_per_route},
                                    backgroundColor: 'rgba(255, 0, 0, 0.7)',
                                }}
                            ]
                        }},
                        options: {{
                            scales: {{
                                y: {{
                                    title: {{
                                        display: true,
                                        text: 'Number of Points'
                                    }}
                                }}
                            }}
                        }}
                    }});
                    
                    // Route distance chart
                    const distanceCtx = document.getElementById('distanceChart').getContext('2d');
                    
                    new Chart(distanceCtx, {{
                        type: 'bar',
                        data: {{
                            labels: Array.from({{ length: Math.max({c_distances}.length, {d_distances}.length) }}, (_, i) => `Route ${{i+1}}`),
                            datasets: [
                                {{
                                    label: 'Constructive',
                                    data: {c_distances},
                                    backgroundColor: 'rgba(0, 0, 255, 0.7)',
                                }},
                                {{
                                    label: 'Deconstructive',
                                    data: {d_distances},
                                    backgroundColor: 'rgba(255, 0, 0, 0.7)',
                                }}
                            ]
                        }},
                        options: {{
                            scales: {{
                                y: {{
                                    title: {{
                                        display: true,
                                        text: 'Total Distance'
                                    }}
                                }}
                            }}
                        }}
                    }});
                    """
                
                html_content += """
                </script>
                """
            
            html_content += """
            </body>
            </html>
            """
            
            # Save HTML file
            with open(output_path, 'w') as f:
                f.write(html_content)
            
        except Exception as e:
            print(f"Error creating comparison charts: {e}")
            # Create a simplified error page
            with open(output_path, 'w') as f:
                f.write(f"""
                <!DOCTYPE html>
                <html>
                <head><title>Error in Chart Generation</title></head>
                <body>
                    <h1>Error Creating Charts</h1>
                    <p>An error occurred while trying to create the comparison charts:</p>
                    <pre>{e}</pre>
                    <p>Please check that your solution file has the correct structure.</p>
                </body>
                </html>
                """)
    
    def run_web_app(self, port=8050):
        """
        Run an interactive web application for exploring routes.
        
        Args:
            port: Port to run the web server on
        """
        if not DASH_AVAILABLE:
            print("Dash is not available. Please install dash and dash-bootstrap-components.")
            print("pip install dash dash-bootstrap-components")
            print("Falling back to static visualization.")
            self.create_static_visualization()
            return
            
        app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
        
        # Define app layout using dash components
        app.layout = dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H1("Dual-Perspective Route Explorer", className="text-primary my-4"),
                    html.P("Interactive exploration of route optimization results using generalized Stirling numbers"),
                ], width=12)
            ]),
            
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Optimization Parameters"),
                        dbc.CardBody([
                            dbc.Row([
                                dbc.Col([
                                    html.H5("Constructive Approach"),
                                    html.P(f"Affinity (a): {self.solution_data['constructive']['parameters']['a']:.2f}"),
                                    html.P(f"Barrier (b): {self.solution_data['constructive']['parameters']['b']:.2f}"),
                                    html.P(f"Optimal Routes: {self.solution_data['constructive']['optimal_k']}"),
                                ], width=6),
                                dbc.Col([
                                    html.H5("Deconstructive Approach"),
                                    html.P(f"Affinity (a): {self.solution_data['deconstructive']['parameters']['a']:.2f}"),
                                    html.P(f"Barrier (b): {self.solution_data['deconstructive']['parameters']['b']:.2f}"),
                                    html.P(f"Optimal Routes: {self.solution_data['deconstructive']['optimal_k']}"),
                                ], width=6),
                            ]),
                        ])
                    ], className="mb-4")
                ], width=4),
                
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Route Comparison"),
                        dbc.CardBody([
                            dcc.Graph(
                                id='cost-comparison',
                                figure=self._create_cost_comparison_figure()
                            )
                        ])
                    ])
                ], width=8)
            ]),
            
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Route Details"),
                        dbc.CardBody([
                            dbc.Tabs([
                                dbc.Tab([
                                    dcc.Graph(
                                        id='constructive-routes',
                                        figure=self._create_route_details_figure('constructive')
                                    )
                                ], label="Constructive"),
                                dbc.Tab([
                                    dcc.Graph(
                                        id='deconstructive-routes',
                                        figure=self._create_route_details_figure('deconstructive')
                                    )
                                ], label="Deconstructive"),
                            ])
                        ])
                    ])
                ], width=12)
            ]),
            
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H3("Route Map", className="mt-4"),
                        html.P("Use the button below to open an interactive map in a new browser tab:"),
                        dbc.Button("Open Interactive Map", id="open-map-btn", color="primary", className="mt-2")
                    ])
                ], width=12)
            ]),
            
            dcc.Store(id='map-created', data=False),
            
            # Hidden div for map callback
            html.Div(id='map-output', style={'display': 'none'})
            
        ], fluid=True)
        
        # Callback for map button
        @app.callback(
            Output('map-output', 'children'),
            Output('map-created', 'data'),
            Input('open-map-btn', 'n_clicks'),
            State('map-created', 'data'),
            prevent_initial_call=True
        )
        def open_map(n_clicks, map_created):
            if not n_clicks:
                return dash.no_update, dash.no_update
            
            # Create the map if not already created
            map_path = os.path.join(self.temp_dir, "interactive_map.html")
            if not map_created or not os.path.exists(map_path):
                self._create_interactive_map(map_path)
            
            # Open in browser
            webbrowser.open(f"file://{map_path}")
            
            return "Map opened", True
        
        # Run the app
        app.run_server(debug=True, port=port)
    
    def _create_cost_comparison_figure(self):
        """Create a plotly figure for cost comparison."""
        c_costs = self.solution_data['constructive']['all_costs']
        d_costs = self.solution_data['deconstructive']['all_costs']
        
        fig = go.Figure()
        
        # Add constructive approach line
        fig.add_trace(go.Scatter(
            x=[cost[0] for cost in c_costs],
            y=[cost[1] for cost in c_costs],
            mode='lines+markers',
            name='Constructive',
            line=dict(color='blue', width=2),
            marker=dict(size=8)
        ))
        
        # Add deconstructive approach line
        fig.add_trace(go.Scatter(
            x=[cost[0] for cost in d_costs],
            y=[cost[1] for cost in d_costs],
            mode='lines+markers',
            name='Deconstructive',
            line=dict(color='red', width=2),
            marker=dict(size=8)
        ))
        
        # Add vertical lines for optimal k
        fig.add_shape(
            type="line",
            x0=self.solution_data['constructive']['optimal_k'],
            y0=0,
            x1=self.solution_data['constructive']['optimal_k'],
            y1=max([cost[1] for cost in c_costs + d_costs]),
            line=dict(color="blue", width=1, dash="dash"),
        )
        
        fig.add_shape(
            type="line",
            x0=self.solution_data['deconstructive']['optimal_k'],
            y0=0,
            x1=self.solution_data['deconstructive']['optimal_k'],
            y1=max([cost[1] for cost in c_costs + d_costs]),
            line=dict(color="red", width=1, dash="dash"),
        )
        
        # Update layout
        fig.update_layout(
            title="Cost vs. Number of Routes",
            xaxis_title="Number of Routes (k)",
            yaxis_title="Total Cost",
            legend_title="Approach",
            xaxis=dict(tickmode='linear'),
            template="plotly_white"
        )
        
        return fig
    
    def _create_route_details_figure(self, approach):
        """Create a plotly figure for route details."""
        if approach not in self.solution_data or 'routes' not in self.solution_data[approach]:
            return go.Figure()
        
        routes_data = self.solution_data[approach]['routes']
        
        # Extract route information
        route_ids = [int(rid) + 1 for rid in routes_data.keys()]  # 1-based IDs for display
        point_counts = [route_info['point_count'] for route_info in routes_data.values()]
        distances = [route_info['total_distance'] for route_info in routes_data.values()]
        
        # Calculate efficiency (points per distance)
        efficiencies = [pc / (dist if dist > 0 else 1) for pc, dist in zip(point_counts, distances)]
        
        # Create figure with subplots
        fig = go.Figure()
        
        # Add points per route bar
        fig.add_trace(go.Bar(
            x=route_ids,
            y=point_counts,
            name='Points',
            marker_color='lightblue',
            opacity=0.7
        ))
        
        # Add distance line
        fig.add_trace(go.Scatter(
            x=route_ids,
            y=distances,
            mode='lines+markers',
            name='Distance',
            marker=dict(size=8),
            line=dict(color='orange', width=2),
            yaxis='y2'
        ))
        
        # Add efficiency line
        fig.add_trace(go.Scatter(
            x=route_ids,
            y=efficiencies,
            mode='lines+markers',
            name='Efficiency',
            marker=dict(size=8),
            line=dict(color='green', width=2),
            yaxis='y3'
        ))
        
        # Update layout with multiple y-axes
        fig.update_layout(
            title=f"{approach.capitalize()} Approach: Route Details",
            xaxis=dict(
                title="Route ID",
                tickmode='linear'
            ),
            yaxis=dict(
                title="Points",
                titlefont=dict(color='blue'),
                tickfont=dict(color='blue')
            ),
            yaxis2=dict(
                title="Distance",
                titlefont=dict(color='orange'),
                tickfont=dict(color='orange'),
                anchor="x",
                overlaying="y",
                side="right"
            ),
            yaxis3=dict(
                title="Efficiency",
                titlefont=dict(color='green'),
                tickfont=dict(color='green'),
                anchor="free",
                overlaying="y",
                side="right",
                position=0.95
            ),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            template="plotly_white",
            margin=dict(r=80)  # Extra margin for third y-axis
        )
        
        return fig


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description='Interactive Route Explorer for Dual-Perspective Delivery Optimization')
    parser.add_argument('--solution', type=str, required=True, help='Path to solution JSON file')
    parser.add_argument('--data', type=str, help='Path to original delivery data CSV (optional)')
    parser.add_argument('--web', action='store_true', help='Run as a web application (requires Dash)')
    parser.add_argument('--port', type=int, default=8050, help='Port for web application (default: 8050)')
    
    args = parser.parse_args()
    
    # Check if file exists
    if not os.path.exists(args.solution):
        print(f"Error: Solution file '{args.solution}' not found.")
        print("Make sure to run dual_perspective_delivery.py first to generate the solution.")
        print("Example: python dual_perspective_delivery.py --generate 50")
        sys.exit(1)
    
    explorer = RouteExplorer(args.solution, args.data)
    
    if args.web and DASH_AVAILABLE:
        explorer.run_web_app(port=args.port)
    else:
        if args.web and not DASH_AVAILABLE:
            print("Web mode requested but Dash is not installed.")
            print("Install with: pip install dash dash-bootstrap-components plotly")
        explorer.create_static_visualization()


if __name__ == "__main__":
    main()
