"""
Visualization module for E-commerce Customer Segmentation analysis.

This script creates comprehensive visualizations of the Stirling Measure analysis
and customer segmentation results.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.offline as pyo
from stirling_measure import analyze_customer_segments, interpret_parameters
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def create_comprehensive_visualizations():
    """Create a comprehensive set of visualizations for the analysis."""
    
    # Load data
    try:
        summary = pd.read_csv('segment_summary.csv')
    except FileNotFoundError:
        print("Error: segment_summary.csv not found. Run data_prep.py first.")
        return
    
    print("Creating comprehensive visualizations...")
    
    # Extract data
    time_periods = summary['month'].tolist()
    customer_counts = summary['n_customers'].tolist()
    segment_counts = summary['n_segments'].tolist()
    
    # Run Stirling analysis
    results = analyze_customer_segments(
        customer_counts=customer_counts,
        segment_counts=segment_counts,
        time_periods=time_periods,
        plot=False  # We'll create our own plots
    )
    
    # Create visualizations
    create_parameter_evolution_plot(results)
    create_3d_stirling_surface(results)
    create_business_insights_dashboard(results)
    create_interactive_plotly_dashboard(results, summary)
    
    print("All visualizations created successfully!")

def create_parameter_evolution_plot(results):
    """Create a plot showing parameter evolution and model fit."""
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # 1. Stirling Measure vs Customer Count
    ax1 = axes[0, 0]
    scatter = ax1.scatter(results['customer_counts'], results['measures'], 
                         c=results['segment_counts'], cmap='viridis', 
                         s=100, alpha=0.7, edgecolors='white', linewidth=2)
    
    # Add trend line
    if len(results['customer_counts']) > 1:
        z = np.polyfit(results['customer_counts'], results['measures'], 1)
        p = np.poly1d(z)
        ax1.plot(results['customer_counts'], p(results['customer_counts']), 
                "r--", alpha=0.8, linewidth=2)
    
    ax1.set_xlabel('Number of Customers (n)', fontsize=12)
    ax1.set_ylabel('Stirling Measure', fontsize=12)
    ax1.set_title('Stirling Measure vs Customer Count', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Add colorbar
    cbar = plt.colorbar(scatter, ax=ax1)
    cbar.set_label('Number of Segments (k)', fontsize=10)
    
    # 2. Time series of customers and segments
    ax2 = axes[0, 1]
    ax2_twin = ax2.twinx()
    
    line1 = ax2.plot(results['time_periods'], results['customer_counts'], 
                     'o-', color='#2E86AB', linewidth=3, markersize=8, label='Customers')
    line2 = ax2_twin.plot(results['time_periods'], results['segment_counts'], 
                         's-', color='#F24236', linewidth=3, markersize=8, label='Segments')
    
    ax2.set_xlabel('Time Period', fontsize=12)
    ax2.set_ylabel('Number of Customers', color='#2E86AB', fontsize=12)
    ax2_twin.set_ylabel('Number of Segments', color='#F24236', fontsize=12)
    ax2.set_title('Customer and Segment Evolution', fontsize=14, fontweight='bold')
    
    # Rotate x-axis labels
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(True, alpha=0.3)
    
    # 3. Parameter interpretation visualization
    ax3 = axes[1, 0]
    a = results['estimated_a']
    b = results['estimated_b']
    
    # Create parameter space visualization
    a_range = np.linspace(0, 1, 50)
    b_range = np.linspace(0, 3, 50)
    A, B = np.meshgrid(a_range, b_range)
    
    # Color regions based on interpretation
    regions = np.zeros_like(A)
    regions[(A < 0.3) & (B < 1.0)] = 1  # Highly personalized
    regions[(A > 0.5) & (B > 2.0)] = 2  # Mass segment
    regions[(A < 0.3) & (B > 2.0)] = 3  # Micro-segment
    regions[(A > 0.5) & (B < 1.0)] = 4  # Adaptive mass
    
    im = ax3.imshow(regions, extent=[0, 1, 0, 3], origin='lower', 
                    cmap='Set3', alpha=0.6, aspect='auto')
    
    # Plot actual parameters
    ax3.scatter(a, b, color='red', s=200, marker='*', 
               edgecolors='black', linewidth=2, zorder=5)
    
    # Add region labels
    ax3.text(0.15, 0.5, 'Highly\nPersonalized', ha='center', va='center', fontsize=9)
    ax3.text(0.75, 2.5, 'Mass\nSegment', ha='center', va='center', fontsize=9)
    ax3.text(0.15, 2.5, 'Micro-\nSegment', ha='center', va='center', fontsize=9)
    ax3.text(0.75, 0.5, 'Adaptive\nMass', ha='center', va='center', fontsize=9)
    
    ax3.set_xlabel('Parameter a (Customer Affinity)', fontsize=12)
    ax3.set_ylabel('Parameter b (Segment Barrier)', fontsize=12)
    ax3.set_title(f'Marketing Strategy Map\n(a={a:.3f}, b={b:.3f})', 
                 fontsize=14, fontweight='bold')
    
    # 4. Model fit diagnostics
    ax4 = axes[1, 1]
    
    # Predicted vs actual values
    n_vals = np.array(results['customer_counts'])
    k_vals = np.array(results['segment_counts'])
    predicted = a * n_vals + b * k_vals
    actual = np.array(results['measures'])
    
    ax4.scatter(actual, predicted, alpha=0.7, s=100, edgecolors='white', linewidth=2)
    
    # Perfect fit line
    min_val = min(min(actual), min(predicted))
    max_val = max(max(actual), max(predicted))
    ax4.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, alpha=0.8)
    
    ax4.set_xlabel('Actual Stirling Measure', fontsize=12)
    ax4.set_ylabel('Predicted Stirling Measure', fontsize=12)
    ax4.set_title(f'Model Fit (R² = {results["r_squared"]:.3f})', 
                 fontsize=14, fontweight='bold')
    ax4.grid(True, alpha=0.3)
    
    # Add R² text
    ax4.text(0.05, 0.95, f'R² = {results["r_squared"]:.3f}', 
            transform=ax4.transAxes, fontsize=12, 
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('comprehensive_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_3d_stirling_surface(results):
    """Create a 3D surface plot of the Stirling Measure."""
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create meshgrid for surface
    n_range = np.linspace(min(results['customer_counts']), 
                         max(results['customer_counts']), 20)
    k_range = np.linspace(min(results['segment_counts']), 
                         max(results['segment_counts']), 20)
    N, K = np.meshgrid(n_range, k_range)
    
    # Calculate theoretical surface using estimated parameters
    a = results['estimated_a']
    b = results['estimated_b']
    Z = a * N + b * K
    
    # Plot surface
    surf = ax.plot_surface(N, K, Z, alpha=0.6, cmap='viridis')
    
    # Plot actual data points
    ax.scatter(results['customer_counts'], results['segment_counts'], 
              results['measures'], color='red', s=100, alpha=0.8)
    
    ax.set_xlabel('Number of Customers (n)')
    ax.set_ylabel('Number of Segments (k)')
    ax.set_zlabel('Stirling Measure')
    ax.set_title('3D Stirling Measure Surface')
    
    # Add colorbar
    fig.colorbar(surf, shrink=0.5, aspect=5)
    
    plt.savefig('stirling_measure_3d.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_business_insights_dashboard(results):
    """Create a business-focused dashboard."""
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    a = results['estimated_a']
    b = results['estimated_b']
    interpretations = interpret_parameters(a, b)
    
    # 1. Parameter gauges
    ax1 = axes[0, 0]
    create_gauge(ax1, a, 0, 1, 'Customer Affinity (a)', 
                 ['Low', 'Moderate', 'High'], ['#ff4444', '#ffaa44', '#44ff44'])
    
    ax2 = axes[0, 1]
    create_gauge(ax2, b, 0, 3, 'Segment Barrier (b)', 
                 ['Low', 'Moderate', 'High'], ['#44ff44', '#ffaa44', '#ff4444'])
    
    # 2. Customer growth trend
    ax3 = axes[0, 2]
    periods = results['time_periods']
    customers = results['customer_counts']
    
    # Calculate growth rate
    if len(customers) > 1:
        growth_rates = [(customers[i] - customers[i-1]) / customers[i-1] * 100 
                       for i in range(1, len(customers))]
        avg_growth = np.mean(growth_rates)
    else:
        avg_growth = 0
    
    ax3.bar(range(len(customers)), customers, color='steelblue', alpha=0.7)
    ax3.set_xlabel('Time Period')
    ax3.set_ylabel('Number of Customers')
    ax3.set_title(f'Customer Growth\n(Avg: {avg_growth:.1f}% per period)')
    ax3.set_xticks(range(len(periods)))
    ax3.set_xticklabels(periods, rotation=45)
    
    # 3. Segment stability
    ax4 = axes[1, 0]
    segments = results['segment_counts']
    segment_stability = np.std(segments) / np.mean(segments) if segments else 0
    
    ax4.plot(range(len(segments)), segments, 'o-', linewidth=3, markersize=8)
    ax4.fill_between(range(len(segments)), segments, alpha=0.3)
    ax4.set_xlabel('Time Period')
    ax4.set_ylabel('Number of Segments')
    ax4.set_title(f'Segment Stability\n(CV: {segment_stability:.2f})')
    ax4.grid(True, alpha=0.3)
    
    # 4. Strategy recommendation
    ax5 = axes[1, 1]
    ax5.axis('off')
    
    strategy_text = interpretations.get('strategy', 'Balanced segmentation approach')
    ax5.text(0.5, 0.5, f"Recommended Strategy:\n\n{strategy_text}", 
            ha='center', va='center', fontsize=11, 
            bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.8),
            wrap=True)
    ax5.set_title('Marketing Strategy Recommendation', fontsize=14, fontweight='bold')
    
    # 5. Model quality metrics
    ax6 = axes[1, 2]
    metrics = ['R²', 'Data Points', 'Time Range']
    values = [results['r_squared'], len(results['measures']), len(results['time_periods'])]
    
    bars = ax6.bar(metrics, values, color=['#ff9999', '#66b3ff', '#99ff99'])
    ax6.set_title('Model Quality Metrics')
    ax6.set_ylabel('Value')
    
    # Add value labels on bars
    for bar, value in zip(bars, values):
        height = bar.get_height()
        ax6.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{value:.3f}' if isinstance(value, float) else f'{value}',
                ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('business_insights_dashboard.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_gauge(ax, value, min_val, max_val, title, labels, colors):
    """Create a gauge chart for parameter visualization."""
    
    # Normalize value
    norm_val = (value - min_val) / (max_val - min_val)
    
    # Create gauge background
    theta = np.linspace(0, np.pi, 100)
    x = np.cos(theta)
    y = np.sin(theta)
    
    # Color zones
    n_zones = len(labels)
    for i in range(n_zones):
        start_angle = i * np.pi / n_zones
        end_angle = (i + 1) * np.pi / n_zones
        theta_zone = np.linspace(start_angle, end_angle, 50)
        x_zone = np.cos(theta_zone)
        y_zone = np.sin(theta_zone)
        
        # Create wedge
        ax.fill_between(x_zone, 0, y_zone, color=colors[i], alpha=0.7)
    
    # Add gauge needle
    needle_angle = norm_val * np.pi
    needle_x = [0, np.cos(needle_angle)]
    needle_y = [0, np.sin(needle_angle)]
    ax.plot(needle_x, needle_y, 'black', linewidth=4)
    ax.scatter([0], [0], color='black', s=100, zorder=5)
    
    # Add labels
    for i, label in enumerate(labels):
        angle = (i + 0.5) * np.pi / n_zones
        label_x = 0.8 * np.cos(angle)
        label_y = 0.8 * np.sin(angle)
        ax.text(label_x, label_y, label, ha='center', va='center', fontsize=9)
    
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-0.2, 1.2)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(f'{title}\n{value:.3f}', fontsize=12, fontweight='bold')

def create_interactive_plotly_dashboard(results, summary):
    """Create an interactive Plotly dashboard."""
    
    # Create subplots
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Stirling Measure Analysis', 'Time Series Evolution',
                       'Parameter Space', 'Model Diagnostics'),
        specs=[[{"secondary_y": False}, {"secondary_y": True}],
               [{"secondary_y": False}, {"secondary_y": False}]]
    )
    
    # 1. Stirling Measure scatter plot
    fig.add_trace(
        go.Scatter(
            x=results['customer_counts'],
            y=results['measures'],
            mode='markers',
            marker=dict(
                size=12,
                color=results['segment_counts'],
                colorscale='viridis',
                showscale=True,
                colorbar=dict(title="Segments")
            ),
            text=[f"Period: {p}<br>Customers: {n}<br>Segments: {k}<br>Measure: {m:.3f}"
                  for p, n, k, m in zip(results['time_periods'], 
                                       results['customer_counts'],
                                       results['segment_counts'],
                                       results['measures'])],
            hovertemplate='%{text}<extra></extra>',
            name='Data Points'
        ),
        row=1, col=1
    )
    
    # Add trend line
    if len(results['customer_counts']) > 1:
        z = np.polyfit(results['customer_counts'], results['measures'], 1)
        p = np.poly1d(z)
        trend_x = np.linspace(min(results['customer_counts']), 
                             max(results['customer_counts']), 100)
        fig.add_trace(
            go.Scatter(
                x=trend_x,
                y=p(trend_x),
                mode='lines',
                line=dict(dash='dash', color='red'),
                name='Trend Line'
            ),
            row=1, col=1
        )
    
    # 2. Time series
    fig.add_trace(
        go.Scatter(
            x=results['time_periods'],
            y=results['customer_counts'],
            mode='lines+markers',
            name='Customers',
            line=dict(color='blue')
        ),
        row=1, col=2
    )
    
    fig.add_trace(
        go.Scatter(
            x=results['time_periods'],
            y=results['segment_counts'],
            mode='lines+markers',
            name='Segments',
            line=dict(color='red'),
            yaxis='y2'
        ),
        row=1, col=2, secondary_y=True
    )
    
    # 3. Parameter space heatmap
    a_range = np.linspace(0, 1, 20)
    b_range = np.linspace(0, 3, 20)
    A, B = np.meshgrid(a_range, b_range)

    # Create strategy regions
    regions = np.zeros_like(A)
    regions[(A < 0.3) & (B < 1.0)] = 1  # Highly personalized
    regions[(A > 0.5) & (B > 2.0)] = 2  # Mass segment
    regions[(A < 0.3) & (B > 2.0)] = 3  # Micro-segment
    regions[(A > 0.5) & (B < 1.0)] = 4  # Adaptive mass

    # Use a valid Plotly colorscale instead of 'Set3'
    fig.add_trace(
        go.Heatmap(
            x=a_range,
            y=b_range,
            z=regions,
            colorscale='Viridis',  # Changed from 'Set3' to 'Viridis'
            showscale=False,
            hovertemplate='a: %{x:.2f}<br>b: %{y:.2f}<extra></extra>'
        ),
        row=2, col=1
    )
    
    # Add actual parameters point
    fig.add_trace(
        go.Scatter(
            x=[results['estimated_a']],
            y=[results['estimated_b']],
            mode='markers',
            marker=dict(
                size=15,
                color='yellow',
                symbol='star',
                line=dict(color='black', width=2)
            ),
            name='Estimated Parameters',
            hovertemplate=f'a: {results["estimated_a"]:.3f}<br>b: {results["estimated_b"]:.3f}<extra></extra>'
        ),
        row=2, col=1
    )
    
    # 4. Model diagnostics
    n_vals = np.array(results['customer_counts'])
    k_vals = np.array(results['segment_counts'])
    predicted = results['estimated_a'] * n_vals + results['estimated_b'] * k_vals
    actual = np.array(results['measures'])
    
    fig.add_trace(
        go.Scatter(
            x=actual,
            y=predicted,
            mode='markers',
            marker=dict(size=10),
            name='Predicted vs Actual',
            hovertemplate='Actual: %{x:.3f}<br>Predicted: %{y:.3f}<extra></extra>'
        ),
        row=2, col=2
    )
    
    # Perfect fit line
    min_val = min(min(actual), min(predicted))
    max_val = max(max(actual), max(predicted))
    fig.add_trace(
        go.Scatter(
            x=[min_val, max_val],
            y=[min_val, max_val],
            mode='lines',
            line=dict(dash='dash', color='red'),
            name='Perfect Fit'
        ),
        row=2, col=2
    )
    
    # Update layout
    fig.update_layout(
        title_text="E-commerce Customer Segmentation: Stirling Measure Analysis",
        showlegend=True,
        height=800
    )
    
    # Update axis labels
    fig.update_xaxes(title_text="Customers (n)", row=1, col=1)
    fig.update_yaxes(title_text="Stirling Measure", row=1, col=1)
    
    fig.update_xaxes(title_text="Time Period", row=1, col=2)
    fig.update_yaxes(title_text="Customers", row=1, col=2)
    fig.update_yaxes(title_text="Segments", row=1, col=2, secondary_y=True)
    
    fig.update_xaxes(title_text="Parameter a (Affinity)", row=2, col=1)
    fig.update_yaxes(title_text="Parameter b (Barrier)", row=2, col=1)
    
    fig.update_xaxes(title_text="Actual Measure", row=2, col=2)
    fig.update_yaxes(title_text="Predicted Measure", row=2, col=2)
    
    # Save as HTML
    pyo.plot(fig, filename='interactive_dashboard.html', auto_open=False)
    print("Interactive dashboard saved as 'interactive_dashboard.html'")

if __name__ == "__main__":
    create_comprehensive_visualizations()
