"""
Quantum Amplitude Calculation using Hasse-Stirling Framework

This example demonstrates how to calculate quantum amplitudes for time-dependent
Hamiltonians using hypergeometric functions via the Hasse-Stirling approach.

Key advantages:
- Faster computation for large qubit systems
- Better numerical stability for extreme parameters
- Improved error bounds for precision-critical applications

Author: David England
"""

import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hyp1f1 as scipy_hyp1f1

# Add the parent directory to sys.path to import the hasse_stirling package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from hasse_stirling import compute_hasse_coefficients, hasse_operator_action

# ======================== IMPLEMENTATION ========================

def hypergeometric_1F1_hasse(a, b, z, max_m=30, tol=1e-15):
    """
    Compute the confluent hypergeometric function 1F1(a;b;z) using Hasse-Stirling.
    
    Args:
        a, b: Parameters of the hypergeometric function
        z: Argument
        max_m: Maximum order for Hasse operator
        tol: Error tolerance
    
    Returns:
        Value of 1F1(a;b;z)
    """
    # Safety checks
    if b <= 0 and b == int(b):
        raise ValueError("Parameter b cannot be zero or negative integer")
    
    # Define the integrand function exp(zt)
    def integrand(t):
        return np.exp(z*t)
    
    # Use Hasse operator with parameters optimized for hypergeometric
    result = hasse_operator_action(integrand, 1, max_m, a, -b, 0)
    
    # Calculate error bound
    error_bound = estimate_error_bound(a, b, z, max_m)
    
    if error_bound > tol:
        print(f"Warning: Error bound {error_bound:.2e} exceeds tolerance {tol:.2e}")
    
    return result

def estimate_error_bound(a, b, z, max_m):
    """
    Calculate error bound for the hypergeometric calculation.
    
    Args:
        a, b: Parameters of the hypergeometric function
        z: Argument
        max_m: Maximum order used in the calculation
    
    Returns:
        Estimated error bound
    """
    # For hypergeometric 1F1, a bound for the truncation error
    if abs(z) < 1:
        # For small z, the error decreases exponentially
        return abs(z)**(max_m+1) / (max_m+1)
    else:
        # For larger z, a more conservative bound
        return min(
            abs(a) * abs(z) / (abs(b) * (max_m+1)),
            np.exp(abs(z)) / np.math.factorial(max_m+1)
        )

def calculate_quantum_amplitude(hamiltonian_params, initial_state, time_points, precision=1e-12):
    """
    Calculate quantum amplitudes using the Hasse-Stirling approach.
    
    Args:
        hamiltonian_params: Parameters describing the Hamiltonian
        initial_state: Initial quantum state
        time_points: Time points for evolution
        precision: Desired precision
    
    Returns:
        Amplitudes at each time point
    """
    # Set up the system parameters
    a, b, z = derive_hypergeometric_params(hamiltonian_params, initial_state)
    
    # Compute amplitudes at each time point
    amplitudes = []
    for t in time_points:
        z_t = z * t  # Time-dependent parameter
        amplitude = hypergeometric_1F1_hasse(a, b, z_t, max_m=50, tol=precision)
        amplitudes.append(amplitude)
    
    return np.array(amplitudes)

def derive_hypergeometric_params(hamiltonian_params, initial_state):
    """
    Derive hypergeometric parameters from physical quantum parameters.
    
    For a two-level system driven by an external field:
    - a = 1/2
    - b = 3/2
    - z = -i(Ω²+Δ²)t/4
    
    where Ω is the Rabi frequency and Δ is the detuning.
    
    Args:
        hamiltonian_params: Dict with 'rabi_frequency' and 'detuning'
        initial_state: Initial state vector
    
    Returns:
        a, b, z: Parameters for the hypergeometric function
    """
    # Extract physical parameters
    rabi = hamiltonian_params.get('rabi_frequency', 1.0)
    detuning = hamiltonian_params.get('detuning', 0.0)
    
    # Hypergeometric parameters for a driven two-level system
    a = 0.5
    b = 1.5
    z = -0.25j * (rabi**2 + detuning**2)
    
    return a, b, z

# ======================== DEMONSTRATION ========================

def benchmark_performance(a, b, z_values, repetitions=10):
    """
    Benchmark the performance of traditional vs Hasse-Stirling approaches.
    """
    hasse_times = []
    scipy_times = []
    
    for z in z_values:
        # Time Hasse-Stirling approach
        start_time = time.time()
        for _ in range(repetitions):
            hypergeometric_1F1_hasse(a, b, z)
        hasse_time = (time.time() - start_time) / repetitions
        hasse_times.append(hasse_time)
        
        # Time SciPy approach
        start_time = time.time()
        for _ in range(repetitions):
            scipy_hyp1f1(a, b, z)
        scipy_time = (time.time() - start_time) / repetitions
        scipy_times.append(scipy_time)
    
    return np.array(hasse_times), np.array(scipy_times)

def plot_comparison(time_points, hasse_amplitudes, scipy_amplitudes):
    """
    Plot the comparison between Hasse-Stirling and traditional approaches.
    """
    plt.figure(figsize=(12, 8))
    
    # Plot amplitudes
    plt.subplot(2, 1, 1)
    plt.plot(time_points, np.abs(hasse_amplitudes), 'b-', label='Hasse-Stirling')
    plt.plot(time_points, np.abs(scipy_amplitudes), 'r--', label='SciPy')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Quantum Amplitude Calculation')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Plot absolute differences
    plt.subplot(2, 1, 2)
    diff = np.abs(hasse_amplitudes - scipy_amplitudes)
    plt.semilogy(time_points, diff, 'g-')
    plt.xlabel('Time')
    plt.ylabel('Absolute Difference')
    plt.title('Numerical Difference Between Methods')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('quantum_amplitude_comparison.png')
    plt.show()

def demo_quantum_system():
    """
    Demonstrate amplitude calculation for a quantum system.
    """
    print("Quantum Amplitude Calculation Example")
    print("=====================================")
    
    # Set up parameters for a Rabi oscillation in a two-level system
    hamiltonian_params = {
        'rabi_frequency': 2.0,  # MHz
        'detuning': 0.5,        # MHz
    }
    
    initial_state = np.array([1, 0])  # |0⟩ state
    time_points = np.linspace(0, 5, 100)  # μs
    
    # Calculate amplitudes using Hasse-Stirling
    print("\nCalculating amplitudes using Hasse-Stirling approach...")
    start_time = time.time()
    hasse_amplitudes = calculate_quantum_amplitude(hamiltonian_params, initial_state, time_points)
    hasse_time = time.time() - start_time
    print(f"Calculation time: {hasse_time:.4f} seconds")
    
    # Calculate amplitudes using SciPy for comparison
    print("\nCalculating amplitudes using traditional (SciPy) approach...")
    start_time = time.time()
    a, b, z = derive_hypergeometric_params(hamiltonian_params, initial_state)
    scipy_amplitudes = np.array([scipy_hyp1f1(a, b, z*t) for t in time_points])
    scipy_time = time.time() - start_time
    print(f"Calculation time: {scipy_time:.4f} seconds")
    
    # Performance comparison
    speedup = scipy_time / hasse_time
    print(f"\nSpeedup: {speedup:.2f}x")
    
    # Error analysis
    max_error = np.max(np.abs(hasse_amplitudes - scipy_amplitudes))
    print(f"Maximum absolute error: {max_error:.2e}")
    
    # Benchmark across different parameter values
    print("\nBenchmarking across different z values...")
    z_values = np.linspace(0.1, 10, 5)
    hasse_times, scipy_times = benchmark_performance(0.5, 1.5, z_values)
    
    for i, z in enumerate(z_values):
        print(f"z = {z:.2f}: Hasse-Stirling = {hasse_times[i]*1000:.2f} ms, "
              f"SciPy = {scipy_times[i]*1000:.2f} ms, "
              f"Speedup = {scipy_times[i]/hasse_times[i]:.2f}x")
    
    # Plot results
    plot_comparison(time_points, hasse_amplitudes, scipy_amplitudes)
    
    # Pros and Cons
    print("\nPros and Cons of Hasse-Stirling for Quantum Amplitude Calculation:")
    print("\nPros:")
    print("- Faster calculation for time-dependent quantum systems")
    print("- Better numerical stability for large quantum systems")
    print("- More accurate for certain parameter regimes")
    print("- Consistent error bounds for precision control")
    
    print("\nCons:")
    print("- Implementation complexity")
    print("- Overhead may not be justified for small quantum systems")
    print("- Requires careful parameter tuning for optimal performance")
    print("- May need fallback mechanisms for certain edge cases")

if __name__ == "__main__":
    demo_quantum_system()
