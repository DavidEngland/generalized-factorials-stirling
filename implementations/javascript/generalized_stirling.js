/**
 * Generalized Stirling Numbers Implementation
 * 
 * This module implements the generalized Stirling numbers L{n,k}^{α,β} based on
 * the paper "Combinatorial approach of certain generalized Stirling numbers"
 * by Belbachir, Belkhir, and Bousbaa.
 */

class GeneralizedStirling {
  /**
   * Create a generalized Stirling number calculator with parameters α and β
   * 
   * @param {number} alpha - Weight parameter for non-head elements (default: 1.0)
   * @param {number} beta - Weight parameter for head elements (default: 1.0)
   */
  constructor(alpha = 1.0, beta = 1.0) {
    this.alpha = alpha;
    this.beta = beta;
    this.cache = new Map();
  }

  /**
   * Calculate the rising factorial (x|α)^n
   * 
   * @param {number} x - Base value
   * @param {number} n - Number of terms
   * @param {number} increment - Increment between terms
   * @returns {number} The rising factorial value
   */
  risingFactorial(x, n, increment = 1.0) {
    if (n === 0) return 1.0;
    
    let result = 1.0;
    for (let i = 0; i < n; i++) {
      result *= (x + i * increment);
    }
    return result;
  }

  /**
   * Calculate binomial coefficient C(n,k)
   * 
   * @param {number} n 
   * @param {number} k 
   * @returns {number}
   */
  binomialCoefficient(n, k) {
    if (k < 0 || k > n) return 0;
    if (k === 0 || k === n) return 1;
    
    let result = 1;
    for (let i = 1; i <= k; i++) {
      result *= (n - (i - 1));
      result /= i;
    }
    return result;
  }

  /**
   * Calculate factorial of n
   * 
   * @param {number} n 
   * @returns {number}
   */
  factorial(n) {
    if (n <= 1) return 1;
    let result = 1;
    for (let i = 2; i <= n; i++) {
      result *= i;
    }
    return result;
  }

  /**
   * Compute L{n,k}^{α,β} using the triangular recurrence relation
   * 
   * @param {number} n - Number of elements
   * @param {number} k - Number of ordered lists
   * @returns {number} The generalized Stirling number
   */
  triangularRecurrence(n, k) {
    // Create a cache key
    const key = `${n}:${k}`;
    
    // Check if already computed
    if (this.cache.has(key)) {
      return this.cache.get(key);
    }
    
    // Base cases
    if (k === 0) {
      return n === 0 ? 1.0 : 0.0;
    }
    if (n === 0 || k > n) {
      return 0.0;
    }
    if (k === n) {
      return 1.0;
    }
    
    // Apply recurrence relation
    const term1 = this.triangularRecurrence(n-1, k-1);
    const term2 = (this.alpha * (n-1) + this.beta * k) * this.triangularRecurrence(n-1, k);
    
    const result = term1 + term2;
    
    // Cache the result
    this.cache.set(key, result);
    
    return result;
  }

  /**
   * Compute L{n,k}^{α,β} using the explicit formula
   * 
   * @param {number} n - Number of elements
   * @param {number} k - Number of ordered lists
   * @returns {number} The generalized Stirling number
   */
  explicitFormula(n, k) {
    // Handle base cases
    if (k === 0) {
      return n === 0 ? 1.0 : 0.0;
    }
    if (n === 0 || k > n) {
      return 0.0;
    }
    if (k === n) {
      return 1.0;
    }
    
    let result = 0.0;
    for (let j = 0; j <= k; j++) {
      // Calculate binomial coefficient C(k,j)
      const binom = this.binomialCoefficient(k, j);
      
      // Calculate rising factorial (β(k-j)|α)^n
      const base = this.beta * (k - j);
      const risingFact = this.risingFactorial(base, n, this.alpha);
      
      // Add to sum with alternating sign
      result += (Math.pow(-1, j)) * binom * risingFact;
    }
    
    // Divide by β^k * k!
    const denominator = Math.pow(this.beta, k) * this.factorial(k);
    return denominator !== 0 ? result / denominator : 0.0;
  }

  /**
   * Compute L{n,1}^{α,β} using the special case formula
   * 
   * @param {number} n - Number of elements
   * @param {number} k - Should be 1 for this special case
   * @returns {number} The generalized Stirling number
   */
  specialCase(n, k = 1) {
    if (k !== 1) {
      throw new Error("This special case only applies for k=1");
    }
    
    if (n <= 0) {
      return 0.0;
    }
    if (n === 1) {
      return 1.0;
    }
    
    let result = 1.0;
    for (let j = 1; j < n; j++) {
      result *= (j * this.alpha + this.beta);
    }
    
    return result;
  }

  /**
   * Compute L{n,k}^{α,β} using the specified method
   * 
   * @param {number} n - Number of elements
   * @param {number} k - Number of ordered lists
   * @param {string} method - Method to use ('triangular', 'explicit', 'special')
   * @returns {number} The generalized Stirling number
   */
  compute(n, k, method = 'triangular') {
    // For k=1, use the special case formula which is more efficient
    if (k === 1 && method !== 'explicit') {
      return this.specialCase(n, k);
    }
    
    if (method === 'explicit') {
      return this.explicitFormula(n, k);
    } else {
      return this.triangularRecurrence(n, k);
    }
  }

  /**
   * Generate a triangle of generalized Stirling numbers
   * 
   * @param {number} nMax - Maximum row number
   * @returns {Array<Array<number>>} Triangle of generalized Stirling numbers
   */
  generateTriangle(nMax) {
    const triangle = [];
    for (let n = 1; n <= nMax; n++) {
      const row = [];
      for (let k = 1; k <= n; k++) {
        row.push(this.compute(n, k));
      }
      triangle.push(row);
    }
    return triangle;
  }
}

/**
 * Compute the unsigned Stirling number of the first kind
 * 
 * @param {number} n - Number of elements
 * @param {number} k - Number of cycles
 * @returns {number} The Stirling number of the first kind
 */
function stirlingFirstKind(n, k) {
  const gs = new GeneralizedStirling(1.0, 0.0);
  return gs.compute(n, k);
}

/**
 * Compute the Stirling number of the second kind
 * 
 * @param {number} n - Number of elements
 * @param {number} k - Number of subsets
 * @returns {number} The Stirling number of the second kind
 */
function stirlingSecondKind(n, k) {
  const gs = new GeneralizedStirling(0.0, 1.0);
  return gs.compute(n, k);
}

/**
 * Compute the Lah number
 * 
 * @param {number} n - Number of elements
 * @param {number} k - Number of ordered lists
 * @returns {number} The Lah number
 */
function lahNumber(n, k) {
  const gs = new GeneralizedStirling(1.0, 1.0);
  return gs.compute(n, k);
}

// Export as module if in Node.js environment
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    GeneralizedStirling,
    stirlingFirstKind,
    stirlingSecondKind,
    lahNumber
  };
}
