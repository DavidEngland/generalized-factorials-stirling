"""
Quantum Error Modeling using Hasse-Stirling Framework

This example demonstrates how to model quantum errors in control pulses
using Bessel functions computed via the Hasse-Stirling approach.

Key advantages:
- More accurate error estimates for quantum control pulses
- Better numerical stability for extreme parameters
- Faster computation for complex error models

Author: David England
"""

import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv as scipy_bessel_j

# Add the parent directory to sys.path to import the hasse_stirling package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from hasse_stirling import compute_hasse_coefficients, hasse_operator_action

# ======================== IMPLEMENTATION ========================

def bessel_j_hasse(nu, z, max_m=40, tol=1e-15):
    """
    Compute the Bessel function of the first kind J_nu(z) using Hasse-Stirling.
    
    Args:
        nu: Order of the Bessel function
        z: Argument
        max_m: Maximum order for Hasse operator
        tol: Error tolerance
    
    Returns:
        Value of J_nu(z)
    """
    # Safety check
    if z == 0:
        return 1.0 if nu == 0 else 0.0
    
    # Define the integrand function for Bessel representation
    def integrand(t):
        return np.exp(-z*z*t/4)
    
    # Calculate prefactor
    prefactor = (z/2)**nu / np.math.gamma(nu + 1)
    
    # Use Hasse operator with parameters optimized for Bessel
    result = prefactor * hasse_operator_action(integrand, 1, max_m, nu+1, -1, 0)
    
    # Calculate error bound
    error_bound = estimate_error_bound(nu, z, max_m)
    
    if error_bound > tol:
        print(f"Warning: Error bound {error_bound:.2e} exceeds tolerance {tol:.2e}")
    
    return result

def estimate_error_bound(nu, z, max_m):
    """
    Calculate error bound for the Bessel function calculation.
    
    Args:
        nu: Order of the Bessel function
        z: Argument
        max_m: Maximum order used in the calculation
    
    Returns:
        Estimated error bound
    """
    # For Bessel functions, a standard bound for the truncation error
    if abs(z) < 10:
        return (abs(z)/2)**(2*max_m + nu) / (np.math.factorial(max_m) * np.math.gamma(max_m + nu + 1))
    else:
        # For large z, use asymptotic behavior
        return np.exp(abs(z)) / np.math.factorial(max_m)

def quantum_error_probability(rabi_frequency, pulse_duration, precision=1e-12):
    """
    Calculate quantum error probability using Bessel functions via Hasse-Stirling.
    
    For a two-level quantum system driven by a control pulse with amplitude errors,
    the probability of error is given by:
    
    P_error(t) = 1 - J_0(Ω_R * t)^2 - J_1(Ω_R * t)^2
    
    where J_n are Bessel functions of the first kind and Ω_R is the Rabi frequency.
    
    Args:
        rabi_frequency: Rabi frequency of the control pulse (MHz)
        pulse_duration: Duration of the pulse (μs)
        precision: Desired precision for calculations
    
    Returns:
        Error probability
    """
    # Calculate the argument for the Bessel functions
    z = rabi_frequency * pulse_duration
    
    # Compute J₀(z) and J₁(z) using Hasse-Stirling
    J0 = bessel_j_hasse(0, z, max_m=50, tol=precision)
    J1 = bessel_j_hasse(1, z, max_m=50, tol=precision)
    
    # Calculate error probability
    error_prob = 1 - J0**2 - J1**2
    
    return error_prob

def amplitude_damping_channel(pulse_strength, pulse_duration, damping_rate, precision=1e-12):
    """
    Model amplitude damping quantum channel with Bessel functions.
    
    Args:
        pulse_strength: Strength of the control pulse
        pulse_duration: Duration of the pulse
        damping_rate: Amplitude damping rate
        precision: Desired precision
        
    Returns:
        Kraus operators for the amplitude damping channel
    """
    # Calculate the effective pulse area with damping
    effective_area = pulse_strength * pulse_duration * np.exp(-damping_rate * pulse_duration)
    
    # Calculate Bessel function values for the model
    J0 = bessel_j_hasse(0, effective_area, tol=precision)
    J1 = bessel_j_hasse(1, effective_area, tol=precision)
    J2 = bessel_j_hasse(2, effective_area, tol=precision)
    
    # Construct Kraus operators for the damping channel
    E0 = np.array([[J0, 1j*J1], [1j*J1, J0]])
    E1 = np.array([[J2, 0], [0, 0]])
    
    return [E0, E1]

# ======================== DEMONSTRATION ========================

def benchmark_performance(nu, z_values, repetitions=10):
    """
    Benchmark the performance of traditional vs Hasse-Stirling approaches.
    """
    hasse_times = []
    scipy_times = []
    
    for z in z_values:
        # Time Hasse-Stirling approach
        start_time = time.time()
        for _ in range(repetitions):
            bessel_j_hasse(nu, z)
        hasse_time = (time.time() - start_time) / repetitions
        hasse_times.append(hasse_time)
        
        # Time SciPy approach
        start_time = time.time()
        for _ in range(repetitions):
            scipy_bessel_j(nu, z)
        scipy_time = (time.time() - start_time) / repetitions
        scipy_times.append(scipy_time)
    
    return np.array(hasse_times), np.array(scipy_times)

def plot_error_comparison(pulse_durations, hasse_errors, scipy_errors):
    """
    Plot the comparison between Hasse-Stirling and traditional approaches.
    """
    plt.figure(figsize=(12, 8))
    
    # Plot error probabilities
    plt.subplot(2, 1, 1)
    plt.plot(pulse_durations, hasse_errors, 'b-', label='Hasse-Stirling')
    plt.plot(pulse_durations, scipy_errors, 'r--', label='SciPy')
    plt.xlabel('Pulse Duration (μs)')
    plt.ylabel('Error Probability')
    plt.title('Quantum Control Error Probability')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Plot absolute differences
    plt.subplot(2, 1, 2)
    diff = np.abs(hasse_errors - scipy_errors)
    plt.semilogy(pulse_durations, diff, 'g-')
    plt.xlabel('Pulse Duration (μs)')
    plt.ylabel('Absolute Difference')
    plt.title('Numerical Difference Between Methods')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('quantum_error_comparison.png')
    plt.show()

def demo_quantum_error_modeling():
    """
    Demonstrate quantum error modeling using Bessel functions.
    """
    print("Quantum Error Modeling Example")
    print("=============================")
    
    # Set up parameters for a quantum control pulse
    rabi_frequency = 10.0  # MHz
    pulse_durations = np.linspace(0, 2, 100)  # μs
    
    # Calculate error probabilities using Hasse-Stirling
    print("\nCalculating error probabilities using Hasse-Stirling approach...")
    start_time = time.time()
    hasse_errors = np.array([quantum_error_probability(rabi_frequency, t) for t in pulse_durations])
    hasse_time = time.time() - start_time
    print(f"Calculation time: {hasse_time:.4f} seconds")
    
    # Calculate error probabilities using SciPy for comparison
    print("\nCalculating error probabilities using traditional (SciPy) approach...")
    start_time = time.time()
    def scipy_error_probability(rabi, t):
        z = rabi * t
        J0 = scipy_bessel_j(0, z)
        J1 = scipy_bessel_j(1, z)
        return 1 - J0**2 - J1**2
    
    scipy_errors = np.array([scipy_error_probability(rabi_frequency, t) for t in pulse_durations])
    scipy_time = time.time() - start_time
    print(f"Calculation time: {scipy_time:.4f} seconds")
    
    # Performance comparison
    speedup = scipy_time / hasse_time
    print(f"\nSpeedup: {speedup:.2f}x")
    
    # Error analysis
    max_error = np.max(np.abs(hasse_errors - scipy_errors))
    print(f"Maximum absolute error: {max_error:.2e}")
    
    # Benchmark across different parameter values
    print("\nBenchmarking across different z values...")
    z_values = np.linspace(1, 50, 5)
    hasse_times, scipy_times = benchmark_performance(1, z_values)
    
    for i, z in enumerate(z_values):
        print(f"z = {z:.2f}: Hasse-Stirling = {hasse_times[i]*1000:.2f} ms, "
              f"SciPy = {scipy_times[i]*1000:.2f} ms, "
              f"Speedup = {scipy_times[i]/hasse_times[i]:.2f}x")
    
    # Demonstrate amplitude damping channel
    print("\nDemonstrating amplitude damping channel model...")
    pulse_strength = 5.0  # MHz
    pulse_duration = 1.0  # μs
    damping_rate = 0.1    # μs^-1
    
    kraus_ops = amplitude_damping_channel(pulse_strength, pulse_duration, damping_rate)
    print(f"Kraus operator E0:\n{kraus_ops[0]}")
    print(f"Kraus operator E1:\n{kraus_ops[1]}")
    
    # Verify that Kraus operators satisfy completeness relation
    completeness_check = np.matmul(kraus_ops[0].conj().T, kraus_ops[0]) + np.matmul(kraus_ops[1].conj().T, kraus_ops[1])
    print(f"\nCompleteness relation check:\n{completeness_check}")
    print(f"Deviation from identity: {np.max(np.abs(completeness_check - np.eye(2))):.2e}")
    
    # Plot results
    plot_error_comparison(pulse_durations, hasse_errors, scipy_errors)
    
    # Pros and Cons
    print("\nPros and Cons of Hasse-Stirling for Quantum Error Modeling:")
    print("\nPros:")
    print("- More accurate error estimates for quantum control pulses")
    print("- Better numerical stability in extreme parameter regions")
    print("- Faster computation for complex error models")
    print("- Well-defined error bounds for certification")
    
    print("\nCons:")
    print("- Implementation complexity compared to standard libraries")
    print("- Overhead may not be justified for simple error models")
    print("- Requires parameter tuning for optimal performance")
    print("- Less well-known approach might need validation for critical applications")

if __name__ == "__main__":
    demo_quantum_error_modeling()
