import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from sample_implementation import concentration_profile, get_params

"""
Comparative analysis between Earth and Mars atmospheric boundary layers.
This script tests whether our generalized Stirling number approach 
produces physically realistic differences between planetary atmospheres.
"""

def compare_vertical_profiles(components=['co2', 'dust', 'water_vapor'], time_hours=12):
    """
    Compare vertical profiles of specified components between Earth and Mars
    at the same local time.
    """
    # Heights to calculate concentrations at (m)
    z = np.linspace(0, 2000, 100)
    
    # Adjust heights for Mars (boundary layer can be much higher)
    z_mars = np.linspace(0, 5000, 100)
    
    # Create comparison figure
    fig = plt.figure(figsize=(15, 10))
    
    # Use GridSpec for more control over layout
    gs = GridSpec(len(components), 3, figure=fig, width_ratios=[1, 1, 0.1])
    
    # For each component, create Earth vs Mars comparison
    for i, component in enumerate(components):
        # Get Earth profile
        earth_conc, earth_units = concentration_profile(z, component, time_hours, 
                                                        environment='earth_atmosphere')
        
        # Get Mars profile
        mars_conc, mars_units = concentration_profile(z_mars, component, time_hours, 
                                                     environment='mars_atmosphere', 
                                                     pbl_height=2500)  # Higher BL on Mars
        
        # First plot: Direct comparison with different y-axes
        ax1 = fig.add_subplot(gs[i, 0])
        
        # Plot Earth profile
        earth_line, = ax1.plot(earth_conc, z, 'b-', linewidth=2, label=f'Earth')
        ax1.set_xlabel(f'{component.capitalize()} ({earth_units})')
        ax1.set_ylabel('Height (m)')
        ax1.set_title(f'{component.capitalize()} at {time_hours:02d}:00')
        ax1.grid(True)
        ax1.set_ylim(0, 2000)
        
        # Create twin axis for Mars
        ax1_twin = ax1.twiny()
        mars_line, = ax1_twin.plot(mars_conc, z_mars, 'r-', linewidth=2, label=f'Mars')
        ax1_twin.set_xlabel(f'Mars {component.capitalize()} ({mars_units})')
        
        # Add legends
        ax1.legend(handles=[earth_line, mars_line], loc='upper right')
        
        # Second plot: Normalized comparison
        ax2 = fig.add_subplot(gs[i, 1])
        
        # Normalize both profiles to range [0, 1] for shape comparison
        earth_norm = (earth_conc - np.min(earth_conc)) / (np.max(earth_conc) - np.min(earth_conc))
        mars_norm = (mars_conc - np.min(mars_conc)) / (np.max(mars_conc) - np.min(mars_conc))
        
        # Plot normalized profiles
        ax2.plot(earth_norm, z, 'b-', linewidth=2, label=f'Earth')
        # Fix: Use same z range for Mars profile (trim z_mars to match length of z)
        ax2.plot(mars_norm[:len(z)], z, 'r-', linewidth=2, label=f'Mars')
        ax2.set_xlabel(f'Normalized Concentration')
        ax2.set_title(f'Normalized Profile Comparison')
        ax2.grid(True)
        ax2.set_ylim(0, 2000)
        ax2.legend(loc='upper right')
        
        # Add text box with key differences
        earth_params = get_params(component, 'earth_atmosphere')
        mars_params = get_params(component, 'mars_atmosphere')
        
        # Calculate gradient (rate of decrease with height)
        earth_gradient = (earth_conc[0] - earth_conc[-1]) / z[-1]
        mars_gradient = (mars_conc[0] - mars_conc[-1]) / z_mars[-1]
        
        textbox = f"""Key Differences:
Earth: a={earth_params.get('a', 'N/A')}, bg={earth_params.get('background', 'N/A')}
Mars: a={mars_params.get('a', 'N/A')}, bg={mars_params.get('background', 'N/A')}
Vertical gradient ratio (Mars/Earth): {mars_gradient/earth_gradient:.2f}
"""
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        ax2.text(1.05, 0.5, textbox, transform=ax2.transAxes, fontsize=9,
                verticalalignment='center', bbox=props)
    
    # Add overall title
    plt.suptitle("Earth vs Mars Atmospheric Profiles - Generalized Stirling Model", fontsize=16, y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    return fig

def compare_diurnal_cycles(component='co2', max_height=1000):
    """
    Compare diurnal cycles of concentration at different heights between Earth and Mars.
    """
    # Times to sample throughout the day
    hours = np.linspace(0, 24, 25)  # Include full 24-hour cycle
    
    # Heights to compare (m)
    heights = [10, 100, 500, max_height]
    
    # Create arrays to store concentrations
    earth_concs = np.zeros((len(hours), len(heights)))
    mars_concs = np.zeros((len(hours), len(heights)))
    
    # Calculate concentrations at each time and height
    for i, hour in enumerate(hours):
        # Get full profile for Earth
        earth_profile, earth_units = concentration_profile(
            np.array(heights), component, hour, environment='earth_atmosphere')
        
        # Get full profile for Mars
        mars_profile, mars_units = concentration_profile(
            np.array(heights), component, hour, environment='mars_atmosphere', 
            pbl_height=2500)
        
        # Store values
        earth_concs[i, :] = earth_profile
        mars_concs[i, :] = mars_profile
    
    # Create figure
    fig, axs = plt.subplots(2, 2, figsize=(15, 10), sharex=True)
    axs = axs.flatten()
    
    # Plot diurnal cycles at each height
    for i, height in enumerate(heights):
        ax = axs[i]
        
        # Normalize concentrations to the daily mean for better comparison
        earth_norm = earth_concs[:, i] / np.mean(earth_concs[:, i])
        mars_norm = mars_concs[:, i] / np.mean(mars_concs[:, i])
        
        # Plot both planets
        ax.plot(hours, earth_norm, 'b-', linewidth=2, label=f'Earth')
        ax.plot(hours, mars_norm, 'r-', linewidth=2, label=f'Mars')
        
        # Calculate and display diurnal amplitude
        earth_amplitude = np.max(earth_norm) - np.min(earth_norm)
        mars_amplitude = np.max(mars_norm) - np.min(mars_norm)
        
        ax.set_title(f'Height: {height}m - Diurnal Amplitude Ratio (Mars/Earth): {mars_amplitude/earth_amplitude:.2f}')
        ax.set_ylabel('Normalized Concentration')
        ax.grid(True)
        ax.legend()
        
        # Add markers for key times of day
        ax.axvline(x=6, color='gray', linestyle='--', alpha=0.5)
        ax.axvline(x=12, color='gray', linestyle='--', alpha=0.5)
        ax.axvline(x=18, color='gray', linestyle='--', alpha=0.5)
        
        # Add time of day labels
        ax.text(0, 1.05, 'Midnight', transform=ax.get_xaxis_transform(), ha='center')
        ax.text(6, 1.05, 'Sunrise', transform=ax.get_xaxis_transform(), ha='center')
        ax.text(12, 1.05, 'Noon', transform=ax.get_xaxis_transform(), ha='center')
        ax.text(18, 1.05, 'Sunset', transform=ax.get_xaxis_transform(), ha='center')
    
    # Add x-label to bottom plots
    axs[2].set_xlabel('Hour of Day')
    axs[3].set_xlabel('Hour of Day')
    
    # Set overall title
    plt.suptitle(f"Earth vs Mars Diurnal Cycles of {component.upper()} - Generalized Stirling Model", 
                fontsize=16, y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    return fig

def calculate_planetary_differences():
    """
    Calculate key quantitative differences between Earth and Mars atmospheres
    according to our model.
    """
    components = ['co2', 'dust', 'water_vapor']
    z = np.linspace(0, 1000, 50)  # Heights for comparison
    
    # Times representing different parts of the day
    times = [3, 9, 15, 21]  # Night, morning, afternoon, evening
    
    # Store metrics in a dictionary
    metrics = {}
    
    for component in components:
        metrics[component] = {
            'background_ratio': None,
            'surface_enhancement_ratio': None,
            'diurnal_amplitude_ratio': None,
            'vertical_gradient_ratio': None,
            'cohesion_difference': None
        }
        
        # Get parameters
        earth_params = get_params(component, 'earth_atmosphere')
        mars_params = get_params(component, 'mars_atmosphere')
        
        # Background concentration ratio
        metrics[component]['background_ratio'] = (
            mars_params.get('background', 1) / earth_params.get('background', 1)
        )
        
        # Surface enhancement ratio
        metrics[component]['surface_enhancement_ratio'] = (
            mars_params.get('surface_enhancement', 0) / earth_params.get('surface_enhancement', 1)
        )
        
        # Cohesion parameter difference
        metrics[component]['cohesion_difference'] = (
            mars_params.get('a', 0) - earth_params.get('a', 0)
        )
        
        # Calculate profiles at different times
        earth_profiles = []
        mars_profiles = []
        
        for time in times:
            earth_profile, _ = concentration_profile(z, component, time, environment='earth_atmosphere')
            mars_profile, _ = concentration_profile(z, component, time, environment='mars_atmosphere', 
                                                  pbl_height=2500)
            
            earth_profiles.append(earth_profile)
            mars_profiles.append(mars_profile)
        
        # Convert to arrays
        earth_profiles = np.array(earth_profiles)
        mars_profiles = np.array(mars_profiles)
        
        # Calculate diurnal amplitude (max - min) at surface
        earth_diurnal_range = np.max(earth_profiles[:, 0]) - np.min(earth_profiles[:, 0])
        mars_diurnal_range = np.max(mars_profiles[:, 0]) - np.min(mars_profiles[:, 0])
        
        # Normalize by mean concentration for fair comparison
        earth_diurnal_amplitude = earth_diurnal_range / np.mean(earth_profiles[:, 0])
        mars_diurnal_amplitude = mars_diurnal_range / np.mean(mars_profiles[:, 0])
        
        metrics[component]['diurnal_amplitude_ratio'] = mars_diurnal_amplitude / earth_diurnal_amplitude
        
        # Calculate vertical gradient (afternoon profile)
        earth_afternoon = earth_profiles[2]
        mars_afternoon = mars_profiles[2]
        
        earth_gradient = (earth_afternoon[0] - earth_afternoon[-1]) / z[-1]
        mars_gradient = (mars_afternoon[0] - mars_afternoon[-1]) / z[-1]
        
        # Normalize by surface concentration
        earth_norm_gradient = earth_gradient / earth_afternoon[0]
        mars_norm_gradient = mars_gradient / mars_afternoon[0]
        
        metrics[component]['vertical_gradient_ratio'] = mars_norm_gradient / earth_norm_gradient
    
    return metrics

if __name__ == "__main__":
    # Compare vertical profiles
    profile_fig = compare_vertical_profiles()
    plt.savefig("earth_mars_profile_comparison.png", dpi=300)
    
    # Compare diurnal cycles for CO2
    diurnal_fig = compare_diurnal_cycles('co2')
    plt.savefig("earth_mars_diurnal_comparison.png", dpi=300)
    
    # Calculate and display metrics
    metrics = calculate_planetary_differences()
    
    print("\nEarth vs Mars Atmospheric Differences (from Generalized Stirling Model):\n")
    print("Component | Background Ratio | Enhancement Ratio | Diurnal Amplitude | Vertical Gradient | Cohesion Diff")
    print("----------|------------------|------------------|-------------------|-------------------|-------------")
    
    for component, values in metrics.items():
        print(f"{component:9} | {values['background_ratio']:16.2f} | {values['surface_enhancement_ratio']:16.2f} | "
              f"{values['diurnal_amplitude_ratio']:17.2f} | {values['vertical_gradient_ratio']:17.2f} | "
              f"{values['cohesion_difference']:13.2f}")
    
    print("\nBackground Ratio: Mars concentration / Earth concentration")
    print("Enhancement Ratio: Mars surface enhancement / Earth surface enhancement")
    print("Diurnal Amplitude: Ratio of normalized daily concentration ranges")
    print("Vertical Gradient: Ratio of normalized concentration decrease with height")
    print("Cohesion Diff: Mars affinity parameter - Earth affinity parameter\n")
    
    print("Expected realistic features:")
    print("1. CO2 much higher on Mars (~95% vs 0.04% on Earth)")
    print("2. Water vapor much lower on Mars")
    print("3. Dust levels much higher on Mars, especially during dust events")
    print("4. Stronger diurnal cycles on Mars due to thin atmosphere")
    print("5. Different mixing dynamics due to lack of water-driven processes on Mars")
    
    plt.show()
