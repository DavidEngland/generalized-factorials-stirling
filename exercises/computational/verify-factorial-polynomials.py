"""
Verification code for generalized factorial polynomials P(x,a,m)

This module provides tools to:
1. Compute P(x,a,m) accurately
2. Verify mathematical properties
3. Test edge cases and special cases
4. Compare different computational approaches
"""

import math
from typing import Union

def P_direct(x: Union[int, float], a: Union[int, float], m: int) -> Union[int, float]:
    """
    Direct computation of P(x,a,m) = x(x+a)(x+2a)...(x+(m-1)a)
    
    Args:
        x: Variable value
        a: Increment parameter  
        m: Degree (number of factors)
    
    Returns:
        Value of P(x,a,m)
    """
    if m == 0:
        return 1
    
    result = 1
    for k in range(m):
        result *= (x + k * a)
    
    return result

def P_gamma(x: Union[int, float], a: Union[int, float], m: int) -> float:
    """
    Gamma function computation of P(x,a,m) = a^m * Gamma(x/a + m) / Gamma(x/a)
    Only valid when a != 0
    """
    if a == 0:
        return x**m
    
    return a**m * math.gamma(x/a + m) / math.gamma(x/a)

def verify_recurrence(x: Union[int, float], a: Union[int, float], m: int, tolerance: float = 1e-10) -> bool:
    """
    Verify that P(x,a,m+1) = P(x,a,m) * (x + ma)
    """
    left_side = P_direct(x, a, m + 1)
    right_side = P_direct(x, a, m) * (x + m * a)
    
    return abs(left_side - right_side) < tolerance

def verify_gamma_consistency(x: Union[int, float], a: Union[int, float], m: int, tolerance: float = 1e-10) -> bool:
    """
    Verify that direct computation matches gamma function computation
    """
    if a == 0:
        return True  # Gamma formula doesn't apply
    
    direct = P_direct(x, a, m)
    gamma = P_gamma(x, a, m)
    
    return abs(direct - gamma) < tolerance

def test_special_cases():
    """
    Test all the special cases and verify expected behavior
    """
    print("Testing Special Cases:")
    print("=" * 40)
    
    # Test 1: Monomial case P(x,0,m) = x^m
    test_cases = [(5, 0, 3), (2, 0, 4), (10, 0, 2)]
    print("Monomial case P(x,0,m) = x^m:")
    for x, a, m in test_cases:
        result = P_direct(x, a, m)
        expected = x**m
        status = "✓" if result == expected else "✗"
        print(f"  P({x},{a},{m}) = {result}, x^m = {expected} {status}")
    
    # Test 2: Rising factorial P(x,1,m)
    print("\nRising factorial P(x,1,m):")
    test_cases = [(3, 1, 4), (5, 1, 3), (2, 1, 5)]
    for x, a, m in test_cases:
        result = P_direct(x, a, m)
        # Manual calculation for verification
        manual = 1
        for k in range(m):
            manual *= (x + k)
        status = "✓" if result == manual else "✗"
        print(f"  P({x},{a},{m}) = {result}, manual = {manual} {status}")
    
    # Test 3: Falling factorial P(x,-1,m)  
    print("\nFalling factorial P(x,-1,m):")
    test_cases = [(5, -1, 3), (6, -1, 4), (4, -1, 2)]
    for x, a, m in test_cases:
        result = P_direct(x, a, m)
        # Manual calculation
        manual = 1
        for k in range(m):
            manual *= (x - k)
        status = "✓" if result == manual else "✗"
        print(f"  P({x},{a},{m}) = {result}, manual = {manual} {status}")

def test_recurrence_relations():
    """
    Test the fundamental recurrence relation
    """
    print("\nTesting Recurrence Relations:")
    print("=" * 40)
    
    test_cases = [
        (3, 2, 3), (5, 1, 4), (2, -1, 3), (7, 3, 2)
    ]
    
    for x, a, m in test_cases:
        is_valid = verify_recurrence(x, a, m)
        status = "✓" if is_valid else "✗"
        
        # Show the actual values for verification
        left = P_direct(x, a, m + 1)
        right = P_direct(x, a, m) * (x + m * a)
        
        print(f"  P({x},{a},{m+1}) = P({x},{a},{m}) * ({x} + {m}*{a})")
        print(f"    {left} = {P_direct(x, a, m)} * {x + m * a} = {right} {status}")

def test_gamma_function_consistency():
    """
    Test consistency between direct and gamma function computations
    """
    print("\nTesting Gamma Function Consistency:")
    print("=" * 40)
    
    test_cases = [
        (3.5, 1, 3), (2.7, 2, 4), (1.5, 0.5, 3)
    ]
    
    for x, a, m in test_cases:
        is_consistent = verify_gamma_consistency(x, a, m)
        status = "✓" if is_consistent else "✗"
        
        direct = P_direct(x, a, m)
        gamma = P_gamma(x, a, m)
        
        print(f"  P({x},{a},{m}): direct = {direct:.6f}, gamma = {gamma:.6f} {status}")

def interactive_calculator():
    """
    Interactive calculator for exploring P(x,a,m)
    """
    print("\nInteractive Calculator:")
    print("=" * 40)
    print("Enter values to calculate P(x,a,m)")
    print("Type 'quit' to exit")
    
    while True:
        try:
            x_input = input("Enter x: ")
            if x_input.lower() == 'quit':
                break
            x = float(x_input)
            
            a = float(input("Enter a: "))
            m = int(input("Enter m: "))
            
            result = P_direct(x, a, m)
            print(f"P({x},{a},{m}) = {result}")
            
            # Show step-by-step if small enough
            if m <= 5:
                factors = [f"({x}+{k}*{a})" for k in range(m)]
                factor_values = [x + k*a for k in range(m)]
                print(f"  = {' × '.join(factors)}")
                print(f"  = {' × '.join(map(str, factor_values))}")
                print(f"  = {result}")
            
            print()
            
        except (ValueError, KeyboardInterrupt):
            break

if __name__ == "__main__":
    print("Generalized Factorial Polynomial Verification")
    print("=" * 50)
    
    test_special_cases()
    test_recurrence_relations() 
    test_gamma_function_consistency()
    
    print("\nAll tests completed!")
    print("\nWould you like to try the interactive calculator? (y/n)")
    if input().lower().startswith('y'):
        interactive_calculator()
