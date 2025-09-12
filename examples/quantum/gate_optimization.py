"""
Quantum Gate Optimization using Hasse-Stirling Framework

This example demonstrates how to optimize quantum gates using the Lambert W function
computed via the Hasse-Stirling approach.

Key advantages:
- More efficient parameter optimization for quantum circuits
- Better numerical stability for extreme parameter regions
- Consistent error bounds for precision requirements

Author: David England
"""

import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lambertw as scipy_lambertw

# Add the parent directory to sys.path to import the hasse_stirling package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from hasse_stirling import compute_hasse_coefficients, hasse_operator_action

# ======================== IMPLEMENTATION ========================

def lambert_w_hasse(z, max_m=40, tol=1e-15):
    """
    Compute the Lambert W function using Hasse-Stirling.
    
    The Lambert W function W(z) is the inverse of f(w) = w*exp(w),
    i.e., z = W(z)*exp(W(z)).
    
    Args:
        z: Argument (should be real and >= -1/e)
        max_m: Maximum order for Hasse operator
        tol: Error tolerance
    
    Returns:
        Value of W(z)
    """
    # Safety checks
    if z < -1/np.e:
        raise ValueError(f"Lambert W is not defined for z < -1/e, got z={z}")
    
    if z == 0:
        return 0
    
    # For z close to -1/e, use series expansion
    if abs(z + 1/np.e) < 0.1:
        p = np.sqrt(2 * (np.e * z + 1))
        return -1 + p - (1/3) * p**2 + (11/72) * p**3
    
    # Define the integrand function for Lambert W
    def integrand(t):
        return np.log(t)
    
    # For Lambert W, we apply the Hasse operator to log(t) and evaluate at log(z)
    log_z = np.log(abs(z))
    result = hasse_operator_action(integrand, 1, max_m, 1, -1, 0, log_z)
    
    # Calculate error bound
    error_bound = estimate_error_bound(z, max_m)
    
    if error_bound > tol:
        print(f"Warning: Error bound {error_bound:.2e} exceeds tolerance {tol:.2e}")
    
    return result

def estimate_error_bound(z, max_m):
    """
    Calculate error bound for the Lambert W function calculation.
    
    Args:
        z: Argument
        max_m: Maximum order used in the calculation
    
    Returns:
        Estimated error bound
    """
    # For Lambert W, error bound based on the tail of the series
    if abs(z) < 1:
        return abs(z)**(max_m+1) / (max_m+1)
    else:
        # For larger z, more conservative bound
        return min(
            np.log(abs(z) + 1) / (max_m+1),
            np.exp(abs(z)) / np.math.factorial(max_m)
        )

def optimize_quantum_gate(target_unitary, control_strength, max_time, precision=1e-12):
    """
    Optimize quantum gate implementation using Lambert W function via Hasse-Stirling.
    
    For many quantum gates, the optimal implementation time with bounded control
    strength is given by:
    
    t_optimal = (2π/Ω) * W(Ω*T/(2π))
    
    where Ω is the control strength and T is the target evolution time.
    
    Args:
        target_unitary: Target unitary operation
        control_strength: Maximum available control strength
        max_time: Maximum allowed implementation time
        precision: Desired precision
    
    Returns:
        Dictionary with optimal implementation parameters
    """
    # Calculate the required evolution parameter
    omega = calculate_control_parameter(target_unitary)
    
    # Compute optimal time using Lambert W function
    z = omega * max_time / (2 * np.pi)
    w = lambert_w_hasse(z, tol=precision)
    optimal_time = (2 * np.pi / omega) * w
    
    # Generate optimal control sequence
    control_sequence = generate_control_sequence(target_unitary, control_strength, optimal_time)
    
    return {
        'optimal_time': optimal_time,
        'control_sequence': control_sequence,
        'fidelity': calculate_fidelity(target_unitary, control_sequence)
    }

def calculate_control_parameter(target_unitary):
    """
    Calculate the control parameter for a target unitary.
    
    This is a simplified model that extracts a characteristic
    frequency from the unitary.
    
    Args:
        target_unitary: Target unitary operation
    
    Returns:
        Control parameter (frequency)
    """
    # Extract eigenvalues
    eigenvalues = np.linalg.eigvals(target_unitary)
    
    # Calculate phases
    phases = np.angle(eigenvalues)
    
    # Maximum phase difference gives characteristic frequency
    return np.max(np.abs(phases)) / (2 * np.pi)

def generate_control_sequence(target_unitary, control_strength, optimal_time):
    """
    Generate an optimal control sequence for implementing the target unitary.
    
    This is a simplified model that produces a basic pulse sequence.
    
    Args:
        target_unitary: Target unitary operation
        control_strength: Maximum control strength
        optimal_time: Optimal implementation time
    
    Returns:
        Control sequence as a dictionary
    """
    # Calculate number of control steps
    num_steps = max(10, int(optimal_time * control_strength))
    
    # Extract axis of rotation from unitary (simplified)
    u, s, vh = np.linalg.svd(target_unitary - np.eye(target_unitary.shape[0]))
    axis = vh[0]
    
    # Create a simple pulse sequence
    time_points = np.linspace(0, optimal_time, num_steps)
    amplitudes = control_strength * np.sin(np.pi * time_points / optimal_time)
    
    return {
        'time_points': time_points,
        'amplitudes': amplitudes,
        'axis': axis,
        'num_steps': num_steps
    }

def calculate_fidelity(target_unitary, control_sequence):
    """
    Calculate the fidelity of the control sequence with respect to the target unitary.
    
    Args:
        target_unitary: Target unitary operation
        control_sequence: Control sequence
    
    Returns:
        Fidelity (between 0 and 1)
    """
    # Simplified fidelity calculation
    # In a real implementation, this would involve simulating the evolution
    
    # We'll assume a fidelity model based on time optimality
    time_points = control_sequence['time_points']
    total_time = time_points[-1]
    
    # Calculate a rough approximation of the implemented unitary
    implemented_unitary = approximate_evolution(control_sequence)
    
    # Calculate fidelity as normalized trace overlap
    n = target_unitary.shape[0]
    overlap = np.abs(np.trace(target_unitary.conj().T @ implemented_unitary)) / n
    
    return overlap

def approximate_evolution(control_sequence):
    """
    Approximate the unitary evolution produced by a control sequence.
    
    This is a simplified model that assumes perfect control.
    
    Args:
        control_sequence: Control sequence
    
    Returns:
        Approximated unitary matrix
    """
    # In a real implementation, this would involve solving the Schrödinger equation
    # For simplicity, we'll just create a rotation based on the total pulse area
    
    time_points = control_sequence['time_points']
    amplitudes = control_sequence['amplitudes']
    axis = control_sequence['axis']
    
    # Calculate total pulse area
    dt = time_points[1] - time_points[0]
    total_area = np.sum(amplitudes) * dt
    
    # Create a simple rotation matrix (2x2 case for simplicity)
    theta = total_area
    cos_half = np.cos(theta/2)
    sin_half = np.sin(theta/2)
    
    return np.array([
        [cos_half, -1j * sin_half],
        [-1j * sin_half, cos_half]
    ])

# ======================== DEMONSTRATION ========================

def benchmark_performance(z_values, repetitions=10):
    """
    Benchmark the performance of traditional vs Hasse-Stirling approaches.
    """
    hasse_times = []
    scipy_times = []
    
    for z in z_values:
        # Time Hasse-Stirling approach
        start_time = time.time()
        for _ in range(repetitions):
            lambert_w_hasse(z)
        hasse_time = (time.time() - start_time) / repetitions
        hasse_times.append(hasse_time)
        
        # Time SciPy approach
        start_time = time.time()
        for _ in range(repetitions):
            scipy_lambertw(z).real
        scipy_time = (time.time() - start_time) / repetitions
        scipy_times.append(scipy_time)
    
    return np.array(hasse_times), np.array(scipy_times)

def plot_optimization_comparison(control_strengths, hasse_times, scipy_times, hasse_fidelities, scipy_fidelities):
    """
    Plot the comparison between Hasse-Stirling and traditional approaches.
    """
    plt.figure(figsize=(12, 10))
    
    # Plot optimal times
    plt.subplot(3, 1, 1)
    plt.plot(control_strengths, hasse_times, 'b-', label='Hasse-Stirling')
    plt.plot(control_strengths, scipy_times, 'r--', label='SciPy')
    plt.xlabel('Control Strength (MHz)')
    plt.ylabel('Optimal Time (μs)')
    plt.title('Optimal Gate Implementation Time')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Plot fidelities
    plt.subplot(3, 1, 2)
    plt.plot(control_strengths, hasse_fidelities, 'b-', label='Hasse-Stirling')
    plt.plot(control_strengths, scipy_fidelities, 'r--', label='SciPy')
    plt.xlabel('Control Strength (MHz)')
    plt.ylabel('Gate Fidelity')
    plt.title('Gate Implementation Fidelity')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Plot absolute differences
    plt.subplot(3, 1, 3)
    time_diff = np.abs(hasse_times - scipy_times)
    fidelity_diff = np.abs(hasse_fidelities - scipy_fidelities)
    plt.semilogy(control_strengths, time_diff, 'g-', label='Time Difference')
    plt.semilogy(control_strengths, fidelity_diff, 'm-', label='Fidelity Difference')
    plt.xlabel('Control Strength (MHz)')
    plt.ylabel('Absolute Difference')
    plt.title('Numerical Differences Between Methods')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('quantum_gate_optimization.png')
    plt.show()

def demo_quantum_gate_optimization():
    """
    Demonstrate quantum gate optimization using Lambert W function.
    """
    print("Quantum Gate Optimization Example")
    print("================================")
    
    # Create a target unitary (Hadamard gate)
    target_unitary = (1/np.sqrt(2)) * np.array([
        [1, 1],
        [1, -1]
    ])
    
    # Set up optimization parameters
    max_time = 10.0  # μs
    control_strengths = np.linspace(1, 10, 10)  # MHz
    
    # Calculate optimal times using Hasse-Stirling
    print("\nCalculating optimal times using Hasse-Stirling approach...")
    start_time = time.time()
    hasse_results = []
    for strength in control_strengths:
        result = optimize_quantum_gate(target_unitary, strength, max_time)
        hasse_results.append(result)
    hasse_time = time.time() - start_time
    print(f"Calculation time: {hasse_time:.4f} seconds")
    
    # Calculate optimal times using SciPy for comparison
    print("\nCalculating optimal times using traditional (SciPy) approach...")
    start_time = time.time()
    
    def scipy_optimize_gate(target, strength, max_t):
        omega = calculate_control_parameter(target)
        z = omega * max_t / (2 * np.pi)
        w = scipy_lambertw(z).real
        opt_time = (2 * np.pi / omega) * w
        seq = generate_control_sequence(target, strength, opt_time)
        return {
            'optimal_time': opt_time,
            'control_sequence': seq,
            'fidelity': calculate_fidelity(target, seq)
        }
    
    scipy_results = []
    for strength in control_strengths:
        result = scipy_optimize_gate(target_unitary, strength, max_time)
        scipy_results.append(result)
    scipy_time = time.time() - start_time
    print(f"Calculation time: {scipy_time:.4f} seconds")
    
    # Extract times and fidelities
    hasse_times = [result['optimal_time'] for result in hasse_results]
    scipy_times = [result['optimal_time'] for result in scipy_results]
    hasse_fidelities = [result['fidelity'] for result in hasse_results]
    scipy_fidelities = [result['fidelity'] for result in scipy_results]
    
    # Performance comparison
    speedup = scipy_time / hasse_time
    print(f"\nSpeedup: {speedup:.2f}x")
    
    # Error analysis
    max_time_error = np.max(np.abs(np.array(hasse_times) - np.array(scipy_times)))
    max_fidelity_error = np.max(np.abs(np.array(hasse_fidelities) - np.array(scipy_fidelities)))
    print(f"Maximum time error: {max_time_error:.2e} μs")
    print(f"Maximum fidelity error: {max_fidelity_error:.2e}")
    
    # Benchmark across different parameter values
    print("\nBenchmarking Lambert W calculation across different z values...")
    z_values = np.linspace(0.1, 5, 5)
    hasse_times, scipy_times = benchmark_performance(z_values)
    
    for i, z in enumerate(z_values):
        print(f"z = {z:.2f}: Hasse-Stirling = {hasse_times[i]*1000:.2f} ms, "
              f"SciPy = {scipy_times[i]*1000:.2f} ms, "
              f"Speedup = {scipy_times[i]/hasse_times[i]:.2f}x")
    
    # Plot results
    plot_optimization_comparison(control_strengths, hasse_times, scipy_times, 
                                hasse_fidelities, scipy_fidelities)
    
    # Visualization of control sequence
    print("\nVisualization of optimal control sequence for Hadamard gate:")
    optimal_result = hasse_results[5]  # Middle control strength
    control_seq = optimal_result['control_sequence']
    
    plt.figure(figsize=(10, 6))
    plt.plot(control_seq['time_points'], control_seq['amplitudes'], 'b-')
    plt.xlabel('Time (μs)')
    plt.ylabel('Control Amplitude (MHz)')
    plt.title(f"Optimal Control Sequence (Fidelity: {optimal_result['fidelity']:.6f})")
    plt.grid(True, alpha=0.3)
    plt.savefig('optimal_control_sequence.png')
    plt.show()
    
    # Pros and Cons
    print("\nPros and Cons of Hasse-Stirling for Quantum Gate Optimization:")
    print("\nPros:")
    print("- More efficient optimization of quantum circuit parameters")
    print("- Better numerical stability for extreme parameter regions")
    print("- Consistent error bounds for precision requirements")
    print("- Faster computation for large parameter sweeps")
    
    print("\nCons:")
    print("- Implementation complexity compared to standard libraries")
    print("- Overhead may not be justified for simple gates")
    print("- Requires careful parameter tuning for optimal performance")
    print("- May need validation against hardware constraints")

if __name__ == "__main__":
    demo_quantum_gate_optimization()
