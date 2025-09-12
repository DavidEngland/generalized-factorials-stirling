"""
Spin Chain Model using the Hasse-Stirling Framework

This example demonstrates how the Hasse-Stirling parameters (α, β, r) can be
used to model a one-dimensional spin chain with various interaction types.

In this physical interpretation:
- -α represents the affinity/cohesion (nearest-neighbor coupling)
- β represents barriers to spin flips (magnetic anisotropy)
- r represents external bias (magnetic field)

Author: David England
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import seaborn as sns
from collections import defaultdict
import time

class HasseStirlingSpin:
    """
    Implementation of a spin chain model using Hasse-Stirling framework.
    """
    
    def __init__(self, chain_length=10, max_order=5):
        """
        Initialize the spin chain model.
        
        Args:
            chain_length: Number of spins in the chain
            max_order: Maximum order for Hasse-Stirling expansions
        """
        self.L = chain_length
        self.max_order = max_order
        self.states = self._generate_states()
        self.stirling_cache = {}
        self.hasse_cache = {}
    
    def _generate_states(self):
        """Generate all possible spin configurations."""
        return [self._int_to_spins(i) for i in range(2**self.L)]
    
    def _int_to_spins(self, i):
        """Convert integer to spin configuration."""
        return np.array([(i >> j) & 1 for j in range(self.L)], dtype=int)
    
    def _spins_to_int(self, spins):
        """Convert spin configuration to integer."""
        return sum(spins[j] << j for j in range(self.L))
    
    def generalized_stirling(self, n, k, alpha, beta, r):
        """
        Compute generalized Stirling numbers using recurrence relation.
        
        Args:
            n, k: Indices for Stirling number S(n,k)
            alpha, beta, r: Hasse-Stirling parameters
            
        Returns:
            Generalized Stirling number S(n,k;α,β,r)
        """
        # Base cases
        if n < 0 or k < 0 or k > n:
            return 0
        if n == 0 and k == 0:
            return 1
        
        # Check cache
        key = (n, k, alpha, beta, r)
        if key in self.stirling_cache:
            return self.stirling_cache[key]
        
        # Recurrence relation
        result = self.generalized_stirling(n-1, k-1, alpha, beta, r) + \
                 (beta * k - alpha * n + r) * self.generalized_stirling(n-1, k, alpha, beta, r)
        
        # Cache result
        self.stirling_cache[key] = result
        return result
    
    def hasse_coefficient(self, m, n, alpha, beta, r):
        """
        Compute Hasse coefficient H_{m,n}^{α,β,r}.
        
        Args:
            m, n: Indices for Hasse coefficient
            alpha, beta, r: Hasse-Stirling parameters
            
        Returns:
            Hasse coefficient H_{m,n}^{α,β,r}
        """
        # Check cache
        key = (m, n, alpha, beta, r)
        if key in self.hasse_cache:
            return self.hasse_cache[key]
        
        # Base case
        if m < 0 or n < 0 or n > m:
            return 0
        if m == 0 and n == 0:
            return 1
        
        # Direct calculation from Stirling numbers
        result = 0
        for j in range(n+1):
            result += ((-1)**(n-j)) * self._binomial(n, j) * \
                     self.generalized_stirling(m, j, alpha, beta, r) / (m+1)
        
        # Cache result
        self.hasse_cache[key] = result
        return result
    
    def _binomial(self, n, k):
        """Compute binomial coefficient (n choose k)."""
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1
        return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n-k))
    
    def energy_contribution(self, spins, alpha, beta, r):
        """
        Calculate energy contribution for a spin configuration.
        
        In this model:
        - -α: Nearest-neighbor coupling (negative = ferromagnetic, positive = antiferromagnetic)
        - β: Energy barrier for spin flips (anisotropy)
        - r: External field strength
        
        Args:
            spins: Spin configuration array
            alpha, beta, r: Physical parameters
            
        Returns:
            Energy contribution from Hasse-Stirling framework
        """
        # Convert spins (0,1) to physical spins (-1,1)
        phys_spins = 2*spins - 1
        
        # Nearest-neighbor interaction term (-α)
        nn_term = 0
        for i in range(self.L-1):
            nn_term += phys_spins[i] * phys_spins[i+1]
        nn_energy = -alpha * nn_term
        
        # Barrier term (β)
        # Count domain walls as barriers
        barriers = sum(1 for i in range(self.L-1) if phys_spins[i] != phys_spins[i+1])
        barrier_energy = beta * barriers
        
        # External field term (r)
        field_energy = -r * sum(phys_spins)
        
        return nn_energy + barrier_energy + field_energy
    
    def hasse_energy_correction(self, spins, alpha, beta, r):
        """
        Calculate energy correction using Hasse-Stirling framework.
        
        This represents higher-order corrections beyond mean-field theory.
        
        Args:
            spins: Spin configuration array
            alpha, beta, r: Physical parameters
            
        Returns:
            Energy correction from Hasse-Stirling approach
        """
        # Convert spins (0,1) to physical spins (-1,1)
        phys_spins = 2*spins - 1
        
        # Hasse energy correction uses the Hasse coefficients
        correction = 0
        for m in range(1, self.max_order+1):
            for n in range(m+1):
                # Apply Hasse coefficient to shifted spin products
                if n < self.L:
                    # Shifted spin product
                    shifted_product = 1.0
                    for i in range(n):
                        if i < self.L:
                            shifted_product *= phys_spins[i]
                    
                    hasse_coef = self.hasse_coefficient(m, n, alpha, beta, r)
                    correction += hasse_coef * shifted_product
        
        return correction
    
    def total_energy(self, spins, alpha, beta, r, include_hasse=True):
        """
        Calculate total energy for a spin configuration.
        
        Args:
            spins: Spin configuration array
            alpha, beta, r: Physical parameters
            include_hasse: Whether to include Hasse-Stirling corrections
            
        Returns:
            Total energy
        """
        base_energy = self.energy_contribution(spins, alpha, beta, r)
        
        if include_hasse:
            correction = self.hasse_energy_correction(spins, alpha, beta, r)
            return base_energy + correction
        return base_energy
    
    def compute_partition_function(self, alpha, beta, r, temperature=1.0, include_hasse=True):
        """
        Compute the partition function Z = Σ exp(-E/kT).
        
        Args:
            alpha, beta, r: Physical parameters
            temperature: System temperature
            include_hasse: Whether to include Hasse-Stirling corrections
            
        Returns:
            Partition function value
        """
        Z = 0
        for state in self.states:
            energy = self.total_energy(state, alpha, beta, r, include_hasse)
            Z += np.exp(-energy / temperature)
        return Z
    
    def compute_magnetization(self, alpha, beta, r, temperature=1.0, include_hasse=True):
        """
        Compute average magnetization <M> = <Σ s_i>.
        
        Args:
            alpha, beta, r: Physical parameters
            temperature: System temperature
            include_hasse: Whether to include Hasse-Stirling corrections
            
        Returns:
            Average magnetization per site
        """
        Z = self.compute_partition_function(alpha, beta, r, temperature, include_hasse)
        
        mag_sum = 0
        for state in self.states:
            phys_spins = 2*state - 1
            magnetization = np.sum(phys_spins)
            energy = self.total_energy(state, alpha, beta, r, include_hasse)
            mag_sum += magnetization * np.exp(-energy / temperature)
        
        return mag_sum / (Z * self.L)  # Normalize by system size
    
    def compute_correlation(self, alpha, beta, r, temperature=1.0, include_hasse=True):
        """
        Compute nearest-neighbor correlation <s_i s_{i+1}>.
        
        Args:
            alpha, beta, r: Physical parameters
            temperature: System temperature
            include_hasse: Whether to include Hasse-Stirling corrections
            
        Returns:
            Average correlation
        """
        Z = self.compute_partition_function(alpha, beta, r, temperature, include_hasse)
        
        corr_sum = 0
        for state in self.states:
            phys_spins = 2*state - 1
            correlation = sum(phys_spins[i] * phys_spins[i+1] for i in range(self.L-1)) / (self.L-1)
            energy = self.total_energy(state, alpha, beta, r, include_hasse)
            corr_sum += correlation * np.exp(-energy / temperature)
        
        return corr_sum / Z
    
    def phase_diagram(self, alpha_range, beta_range, r, temperature=1.0, include_hasse=True):
        """
        Compute phase diagram across α-β parameter space.
        
        Args:
            alpha_range: Range of α values
            beta_range: Range of β values
            r: Fixed external field
            temperature: System temperature
            include_hasse: Whether to include Hasse-Stirling corrections
            
        Returns:
            2D arrays for magnetization and correlation
        """
        magnetization = np.zeros((len(alpha_range), len(beta_range)))
        correlation = np.zeros((len(alpha_range), len(beta_range)))
        
        for i, alpha in enumerate(alpha_range):
            for j, beta in enumerate(beta_range):
                magnetization[i, j] = self.compute_magnetization(alpha, beta, r, temperature, include_hasse)
                correlation[i, j] = self.compute_correlation(alpha, beta, r, temperature, include_hasse)
        
        return magnetization, correlation


def plot_phase_diagram(alpha_range, beta_range, magnetization, correlation):
    """
    Plot phase diagram results.
    
    Args:
        alpha_range: Range of α values
        beta_range: Range of β values
        magnetization: 2D array of magnetization values
        correlation: 2D array of correlation values
    """
    # Set up figure
    fig = plt.figure(figsize=(15, 6))
    
    # Plot magnetization
    ax1 = fig.add_subplot(121)
    im1 = ax1.contourf(alpha_range, beta_range, magnetization.T, cmap='viridis', levels=20)
    ax1.set_xlabel(r'Affinity Parameter ($-\alpha$)')
    ax1.set_ylabel(r'Barrier Parameter ($\beta$)')
    ax1.set_title('Average Magnetization')
    plt.colorbar(im1, ax=ax1, label=r'$\langle M \rangle$')
    
    # Plot correlation
    ax2 = fig.add_subplot(122)
    im2 = ax2.contourf(alpha_range, beta_range, correlation.T, cmap='plasma', levels=20)
    ax2.set_xlabel(r'Affinity Parameter ($-\alpha$)')
    ax2.set_ylabel(r'Barrier Parameter ($\beta$)')
    ax2.set_title('Nearest-Neighbor Correlation')
    plt.colorbar(im2, ax=ax2, label=r'$\langle s_i s_{i+1} \rangle$')
    
    # Add a line where α + β = 0 (the "half-barrier")
    for ax in [ax1, ax2]:
        ax.plot(alpha_range, -alpha_range, 'k--', label=r'$\alpha + \beta = 0$')
        ax.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig('spin_chain_phase_diagram.png', dpi=300)
    plt.show()


def compare_with_without_hasse(model, alpha_values, beta=0.0, r=0.0, temperature=1.0):
    """
    Compare results with and without Hasse-Stirling corrections.
    
    Args:
        model: HasseStirlingSpin model instance
        alpha_values: Range of α values to test
        beta: Fixed β value
        r: Fixed external field
        temperature: System temperature
    """
    # Compute magnetization with and without corrections
    mag_with_hasse = []
    mag_without_hasse = []
    
    for alpha in alpha_values:
        mag_with_hasse.append(model.compute_magnetization(alpha, beta, r, temperature, include_hasse=True))
        mag_without_hasse.append(model.compute_magnetization(alpha, beta, r, temperature, include_hasse=False))
    
    # Plot comparison
    plt.figure(figsize=(10, 6))
    plt.plot(alpha_values, mag_with_hasse, 'b-', label='With Hasse-Stirling Corrections')
    plt.plot(alpha_values, mag_without_hasse, 'r--', label='Without Corrections (Mean Field)')
    
    plt.xlabel(r'Affinity Parameter ($-\alpha$)')
    plt.ylabel('Magnetization per Site')
    plt.title(f'Effect of Hasse-Stirling Corrections (β={beta}, r={r}, T={temperature})')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Mark critical point (α = 0)
    plt.axvline(x=0, color='k', linestyle=':', label='Mean Field Critical Point')
    
    plt.savefig('hasse_stirling_comparison.png', dpi=300)
    plt.show()


def main():
    """Main function to run the example."""
    print("Spin Chain Model using Hasse-Stirling Framework")
    print("==============================================")
    
    # Create a small chain for demonstration (full enumeration gets expensive quickly)
    L = 6  # chain length
    print(f"Initializing spin chain with {L} sites")
    
    # Create model
    start_time = time.time()
    model = HasseStirlingSpin(chain_length=L, max_order=3)
    print(f"Model initialized in {time.time() - start_time:.2f} seconds")
    
    # Parameter interpretation for physics
    print("\nParameter interpretation:")
    print("- (-α): Affinity/cohesion - Nearest-neighbor coupling")
    print("- β: Barrier/resistance - Energy cost for domain walls")
    print("- r: Offset/bias - External magnetic field")
    
    # Phase diagram
    print("\nGenerating phase diagram...")
    start_time = time.time()
    
    # Define parameter ranges
    alpha_range = np.linspace(-1.0, 1.0, 20)  # From antiferromagnetic to ferromagnetic
    beta_range = np.linspace(-0.5, 0.5, 20)   # From domain wall attraction to repulsion
    r = 0.0  # No external field
    
    # Compute phase diagram
    magnetization, correlation = model.phase_diagram(alpha_range, beta_range, r, temperature=0.5)
    print(f"Phase diagram computed in {time.time() - start_time:.2f} seconds")
    
    # Plot phase diagram
    plot_phase_diagram(alpha_range, beta_range, magnetization, correlation)
    
    # Compare with and without Hasse corrections
    print("\nComparing with and without Hasse-Stirling corrections...")
    alpha_values = np.linspace(-1.0, 1.0, 40)
    compare_with_without_hasse(model, alpha_values, beta=0.0, r=0.0, temperature=0.5)
    
    # Test different parameter combinations
    print("\nClassical physical parameter combinations:")
    
    # 1. Ferromagnetic case (Ising model)
    alpha, beta, r = 0.5, 0.0, 0.0
    mag = model.compute_magnetization(alpha, beta, r, temperature=0.5)
    corr = model.compute_correlation(alpha, beta, r, temperature=0.5)
    print(f"Ferromagnetic (α={alpha}, β={beta}, r={r}):")
    print(f"  Magnetization: {mag:.4f}")
    print(f"  Correlation: {corr:.4f}")
    
    # 2. Antiferromagnetic case
    alpha, beta, r = -0.5, 0.0, 0.0
    mag = model.compute_magnetization(alpha, beta, r, temperature=0.5)
    corr = model.compute_correlation(alpha, beta, r, temperature=0.5)
    print(f"Antiferromagnetic (α={alpha}, β={beta}, r={r}):")
    print(f"  Magnetization: {mag:.4f}")
    print(f"  Correlation: {corr:.4f}")
    
    # 3. With external field
    alpha, beta, r = 0.0, 0.0, 0.5
    mag = model.compute_magnetization(alpha, beta, r, temperature=0.5)
    corr = model.compute_correlation(alpha, beta, r, temperature=0.5)
    print(f"External field (α={alpha}, β={beta}, r={r}):")
    print(f"  Magnetization: {mag:.4f}")
    print(f"  Correlation: {corr:.4f}")
    
    # 4. Critical point
    alpha, beta, r = 0.0, 0.0, 0.0
    mag = model.compute_magnetization(alpha, beta, r, temperature=0.5)
    corr = model.compute_correlation(alpha, beta, r, temperature=0.5)
    print(f"Critical point (α={alpha}, β={beta}, r={r}):")
    print(f"  Magnetization: {mag:.4f}")
    print(f"  Correlation: {corr:.4f}")
    
    print("\nNote: In this model, negative α represents ferromagnetic coupling")
    print("      and positive α represents antiferromagnetic coupling.")


if __name__ == "__main__":
    main()
