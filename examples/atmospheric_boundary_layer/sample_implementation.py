import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb
from functools import lru_cache

# Constants for profile calculation
N_APPROXIMATION_ORDER = 4  # Order of approximation for generalized Stirling formula
SCALE_FACTOR = 5.0  # Scaling factor for characteristic height

def stirling2(n, k):
    """
    Calculate Stirling numbers of the second kind S(n,k) using an iterative approach.
    
    These numbers count the ways to partition a set of n labeled objects into k non-empty subsets.
    
    Parameters:
        n (int): Number of elements
        k (int): Number of non-empty subsets
        
    Returns:
        int: The Stirling number of the second kind S(n,k)
    """
    # Handle base cases
    if k == 0:
        return 1 if n == 0 else 0
    if k > n or k == 0:
        return 0
    if k == 1 or k == n:
        return 1
    
    # Use bottom-up dynamic programming approach
    dp = np.zeros((n+1, k+1), dtype=int)
    
    # Initialize base cases
    for i in range(1, n+1):
        dp[i, 1] = 1  # One way to put n elements in one subset
    
    for i in range(1, k+1):
        dp[i, i] = 1  # One way to put n elements in n subsets
    
    # Fill the table using recurrence relation
    for i in range(2, n+1):
        for j in range(2, min(i, k)+1):
            dp[i, j] = dp[i-1, j-1] + j * dp[i-1, j]
    
    return dp[n, k]

@lru_cache(maxsize=1024)
def generalized_stirling(n, k, a, b):
    """
    Calculate generalized Stirling numbers S_{n,k}(a,b) using an iterative approach.
    
    These numbers generalize the classical Stirling numbers with parameters a and b
    that control cohesion and mixing behavior.
    
    Parameters:
        n (int): Number of elements
        k (int): Number of partitions
        a (float): Affinity/cohesion parameter
        b (float): Barrier/separation parameter
        
    Returns:
        float: The generalized Stirling number S_{n,k}(a,b)
    """
    # Handle base cases
    if k == 0:
        return 1 if n == 0 else 0
    if k > n or k == 0:
        return 0
    
    # Create a table for dynamic programming
    dp = np.zeros((n+1, k+1), dtype=float)
    
    # Initialize base cases
    dp[0, 0] = 1
    
    # Fill the table using recurrence relation
    for i in range(1, n+1):
        for j in range(1, min(i, k)+1):
            dp[i, j] = dp[i-1, j-1] + (a*(i-1) + b*j) * dp[i-1, j]
    
    return dp[n, k]

def concentration_profile(z, component, time_hours, pbl_height=1000):
    """
    Calculate the vertical concentration profile for a specific atmospheric component
    using generalized Stirling numbers to model mixing behavior.
    
    Parameters:
        z (array): Height levels (m)
        component (str): One of 'co2', 'water_vapor', 'methane', 'dust'
        time_hours (float): Time of day (0-24)
        pbl_height (float): Planetary boundary layer height (m)
    
    Returns:
        tuple: (concentrations array, units string)
    """
    # Component-specific parameters with physical meaning
    component_params = {
        'co2': {
            'a': 0,                     # Neutral cohesion
            'background': 415,          # Background concentration (ppm)
            'surface_enhancement': 30,  # Additional concentration at surface
            'units': 'ppm'              # Parts per million
        },
        'water_vapor': {
            'a': 0.5,                   # Moderate cohesion (tends to cluster)
            'background': 5000,         # Background concentration (ppm)
            'surface_enhancement': 3000, # Strong surface enhancement (evaporation)
            'units': 'ppm'
        },
        'methane': {
            'a': -0.2,                  # Slight dispersion tendency (lighter than air)
            'background': 1.9,          # Background concentration (ppm)
            'surface_enhancement': 0.5,  # Mild surface enhancement (emissions)
            'units': 'ppm'
        },
        'dust': {
            'a': 1.0,                   # Strong cohesion (particles stick together)
            'background': 20,           # Background concentration (μg/m³)
            'surface_enhancement': 40,   # Strong surface effect (dust resuspension)
            'units': 'μg/m³'
        }
    }
    
    # Time-dependent barrier parameter calculation
    # The 'b' parameter controls mixing behavior:
    # b = 1.0: Strong barrier (stable conditions, minimal mixing)
    # b = -0.5: Negative barrier (convective conditions, enhanced mixing)
    if time_hours < 8:
        # Morning transition: Stable nocturnal boundary layer gradually breaks down
        # as solar heating begins, transitioning from stable to convective
        transition_factor = time_hours / 8.0
        b = 1.0 - 1.5 * transition_factor  # Linear transition from 1.0 to -0.5
    elif time_hours < 16:
        # Daytime: Fully developed convective boundary layer with strong vertical mixing
        b = -0.5  # Enhanced mixing (negative barrier)
    else:
        # Evening transition: Convective mixing weakens as solar heating diminishes
        # and stable nocturnal boundary layer begins to form
        transition_factor = (time_hours - 16) / 8.0
        b = -0.5 + 1.5 * transition_factor  # Linear transition from -0.5 to 1.0
    
    # Get component parameters
    params = component_params[component]
    a = params['a']
    background = params['background']
    surface_enhancement = params['surface_enhancement']
    
    # Calculate characteristic scale height (distance over which concentration decreases by ~63%)
    CHARACTERISTIC_HEIGHT = pbl_height / SCALE_FACTOR
    
    # Calculate concentration profile using generalized Stirling approach
    concentrations = np.zeros_like(z) + background
    
    for k in range(1, N_APPROXIMATION_ORDER+1):
        stirling_value = generalized_stirling(N_APPROXIMATION_ORDER, k, a, b)
        # Apply exponential decrease with height, weighted by Stirling number
        concentrations += surface_enhancement * stirling_value * np.exp(-k * z / CHARACTERISTIC_HEIGHT)
    
    return concentrations, params['units']

def plot_profiles(times=[6, 12, 18], components=['co2', 'water_vapor', 'methane', 'dust']):
    """
    Create a multi-panel figure showing concentration profiles for different 
    atmospheric components at different times of day.
    
    Parameters:
        times (list): List of hours (0-24) to plot
        components (list): List of component names to plot
        
    Returns:
        matplotlib.figure.Figure: The created figure object
    """
    z = np.linspace(0, 2000, 100)  # Heights from 0 to 2000m
    
    # Create figure and axes with appropriate dimensions
    fig, axes = plt.subplots(len(components), len(times), 
                            figsize=(5*len(times), 3*len(components)),
                            squeeze=False)  # Prevent squeezing of dimensions
    
    # Set overall figure title
    fig.suptitle('Atmospheric Component Profiles in the Planetary Boundary Layer', 
                fontsize=16, y=0.98)
    
    # Find global min/max for consistent axis limits
    min_conc = float('inf')
    max_conc = float('-inf')
    
    # First pass to find global limits
    for component in components:
        for time in times:
            conc, _ = concentration_profile(z, component, time)
            min_conc = min(min_conc, np.min(conc))
            max_conc = max(max_conc, np.max(conc))
    
    # Add 5% padding to limits
    range_conc = max_conc - min_conc
    min_conc -= 0.05 * range_conc
    max_conc += 0.05 * range_conc
    
    # Create plots
    for i, component in enumerate(components):
        for j, time in enumerate(times):
            concentrations, units = concentration_profile(z, component, time)
            
            # Determine boundary layer state based on time
            if time < 8:
                state = "Morning Transition"
            elif time < 16:
                state = "Daytime Convective"
            else:
                state = "Evening Transition"
            
            ax = axes[i, j]
            ax.plot(concentrations, z, 'b-', linewidth=2)
            ax.set_xlabel(f'Concentration ({units})')
            ax.set_ylabel('Height (m)')
            ax.set_title(f'{component.capitalize()} at {time:02d}:00\n({state})')
            ax.grid(True)
            ax.set_ylim(0, 2000)
            
            # Use component-specific x-limits for better visualization
            # while maintaining consistent limits for the same component
            if component == 'co2':
                ax.set_xlim(min(410, min_conc), max(450, max_conc))
            elif component == 'water_vapor':
                ax.set_xlim(min(4500, min_conc), max(8500, max_conc))
            elif component == 'methane':
                ax.set_xlim(min(1.8, min_conc), max(2.5, max_conc))
            elif component == 'dust':
                ax.set_xlim(min(10, min_conc), max(70, max_conc))
    
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Make room for suptitle
    return fig

if __name__ == "__main__":
    # Plot profiles for different times of day
    fig = plot_profiles()
    plt.savefig("atmospheric_profiles.png", dpi=300)
    plt.show()
    
    # Plot diurnal evolution for CO2
    hours = np.linspace(0, 24, 13)  # 0, 2, 4, ..., 24
    z = np.linspace(0, 2000, 100)
    
    plt.figure(figsize=(10, 6))
    
    # Define a colormap for time progression
    colors = plt.cm.viridis(np.linspace(0, 1, len(hours)))
    
    for i, hour in enumerate(hours):
        co2, units = concentration_profile(z, 'co2', hour)
        
        # Determine boundary layer state
        if hour < 8:
            state = "Morning"
        elif hour < 16:
            state = "Daytime"
        else:
            state = "Evening"
        
        plt.plot(co2, z, label=f'{int(hour):02d}:00 ({state})', 
                color=colors[i], linewidth=2)
    
    plt.xlabel(f'CO₂ Concentration ({units})')
    plt.ylabel('Height (m)')
    plt.title('Diurnal Evolution of CO₂ Profile in the Planetary Boundary Layer')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.ylim(0, 2000)
    plt.xlim(410, 450)  # Reasonable limits for CO2
    plt.tight_layout()
    plt.savefig("co2_diurnal_evolution.png", dpi=300)
    plt.show()
