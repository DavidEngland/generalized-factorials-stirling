"""
Comparison of Different Generalized Stirling Number Notations

This example demonstrates the relationship between different notations:
- L_{n,k}^{α,β} from Belbachir et al.
- S(n,k;α,β,r) from Hsu and Shiue
"""

import sys
import os
from pathlib import Path

# Add the src directory to the path
sys.path.append(str(Path(__file__).parent.parent / "src"))
from generalized_stirling import GeneralizedStirling
from hsu_shiue_stirling import (
    HsuShiueStirling, 
    convert_L_to_hsu_shiue, 
    compute_from_L_notation,
    r_stirling_first_kind,
    r_stirling_second_kind,
    whitney_first_kind,
    whitney_second_kind
)

def print_separator():
    print("\n" + "-" * 60 + "\n")

def compare_notations():
    """Compare values computed using different notations"""
    print("Comparing L_{n,k}^{α,β} and S(n,k;α,β,r) notations")
    print_separator()
    
    # Parameters for comparison
    test_cases = [
        (5, 3, 1.0, 1.0),  # Lah numbers
        (5, 3, 0.0, 1.0),  # Stirling numbers of the second kind
        (5, 3, 1.0, 0.0),  # Stirling numbers of the first kind
        (5, 3, 2.0, 3.0),  # Custom parameters
    ]
    
    for n, k, alpha, beta in test_cases:
        # Compute using L notation
        gs_L = GeneralizedStirling(alpha=alpha, beta=beta)
        L_value = gs_L.compute(n, k)
        
        # Convert to Hsu-Shiue parameters
        hs_n, hs_k, hs_alpha, hs_beta, hs_r = convert_L_to_hsu_shiue(n, k, alpha, beta)
        
        # Compute using Hsu-Shiue notation
        gs_HS = HsuShiueStirling(alpha=hs_alpha, beta=hs_beta, r=hs_r)
        HS_value = gs_HS.compute(hs_n, hs_k)
        
        # Compare values
        print(f"L_{{{n},{k}}}^{{{alpha},{beta}}} = {L_value}")
        print(f"S({hs_n},{hs_k};{hs_alpha},{hs_beta},{hs_r}) = {HS_value}")
        print(f"Equal: {abs(L_value - HS_value) < 1e-10}")
        print()

def demonstrate_special_cases():
    """Demonstrate special cases of generalized Stirling numbers"""
    print("Special Cases of Generalized Stirling Numbers")
    print_separator()
    
    # Classic Stirling numbers
    n, k = 5, 3
    
    # First kind (unsigned)
    s1 = compute_from_L_notation(n, k, 1.0, 0.0)
    gs_L = GeneralizedStirling(alpha=1.0, beta=0.0)
    L_s1 = gs_L.compute(n, k)
    print(f"Stirling number of the first kind s({n},{k}) = {s1}")
    print(f"Using L notation: L_{{{n},{k}}}^{{1,0}} = {L_s1}")
    print(f"Equal: {abs(s1 - L_s1) < 1e-10}")
    print()
    
    # Second kind
    s2 = compute_from_L_notation(n, k, 0.0, 1.0)
    gs_L = GeneralizedStirling(alpha=0.0, beta=1.0)
    L_s2 = gs_L.compute(n, k)
    print(f"Stirling number of the second kind S({n},{k}) = {s2}")
    print(f"Using L notation: L_{{{n},{k}}}^{{0,1}} = {L_s2}")
    print(f"Equal: {abs(s2 - L_s2) < 1e-10}")
    print()
    
    # Lah numbers
    lah = compute_from_L_notation(n, k, 1.0, 1.0)
    gs_L = GeneralizedStirling(alpha=1.0, beta=1.0)
    L_lah = gs_L.compute(n, k)
    print(f"Lah number L({n},{k}) = {lah}")
    print(f"Using L notation: L_{{{n},{k}}}^{{1,1}} = {L_lah}")
    print(f"Equal: {abs(lah - L_lah) < 1e-10}")
    print()

def demonstrate_r_stirling():
    """Demonstrate r-Stirling numbers"""
    print("r-Stirling Numbers")
    print_separator()
    
    n, k, r = 5, 3, 2
    
    # r-Stirling numbers of the first kind
    rs1 = r_stirling_first_kind(n, k, r)
    print(f"r-Stirling number of the first kind s_r({n},{k},{r}) = {rs1}")
    
    # r-Stirling numbers of the second kind
    rs2 = r_stirling_second_kind(n, k, r)
    print(f"r-Stirling number of the second kind S_r({n},{k},{r}) = {rs2}")
    
    # Show that r=0 gives the classical Stirling numbers
    rs1_0 = r_stirling_first_kind(n, k, 0)
    rs2_0 = r_stirling_second_kind(n, k, 0)
    
    gs_L1 = GeneralizedStirling(alpha=1.0, beta=0.0)
    gs_L2 = GeneralizedStirling(alpha=0.0, beta=1.0)
    
    L_s1 = gs_L1.compute(n, k)
    L_s2 = gs_L2.compute(n, k)
    
    print(f"\nr=0 should give classical Stirling numbers:")
    print(f"s_0({n},{k}) = {rs1_0}, s({n},{k}) = {L_s1}, Equal: {abs(rs1_0 - L_s1) < 1e-10}")
    print(f"S_0({n},{k}) = {rs2_0}, S({n},{k}) = {L_s2}, Equal: {abs(rs2_0 - L_s2) < 1e-10}")

def demonstrate_whitney():
    """Demonstrate Whitney numbers"""
    print("Whitney Numbers of Dowling Lattices")
    print_separator()
    
    n, k, m = 5, 3, 2
    
    # Whitney numbers of the first kind
    w1 = whitney_first_kind(n, k, m)
    print(f"Whitney number of the first kind w_m({n},{k},{m}) = {w1}")
    
    # Whitney numbers of the second kind
    w2 = whitney_second_kind(n, k, m)
    print(f"Whitney number of the second kind W_m({n},{k},{m}) = {w2}")
    
    # Show that m=1 gives values related to the classical Stirling numbers
    w1_1 = whitney_first_kind(n, k, 1)
    w2_1 = whitney_second_kind(n, k, 1)
    
    gs_L1 = GeneralizedStirling(alpha=1.0, beta=0.0)
    gs_L2 = GeneralizedStirling(alpha=0.0, beta=1.0)
    
    L_s1 = gs_L1.compute(n, k)
    L_s2 = gs_L2.compute(n, k)
    
    print(f"\nm=1 gives values related to classical Stirling numbers:")
    print(f"w_1({n},{k}) = {w1_1}, Relationship to s({n},{k}): w_1(n,k) = (-1)^(n-k)s(n,k)")
    print(f"W_1({n},{k}) = {w2_1}, S({n},{k}) = {L_s2}, Equal: {abs(w2_1 - L_s2) < 1e-10}")

def main():
    """Run all demonstrations"""
    compare_notations()
    demonstrate_special_cases()
    demonstrate_r_stirling()
    demonstrate_whitney()

if __name__ == "__main__":
    main()
