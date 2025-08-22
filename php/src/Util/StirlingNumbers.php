<?php

namespace GeneralizedStirling\Util;

use GeneralizedStirling\GeneralizedStirling;
use GeneralizedStirling\Exception\StirlingException;

/**
 * Utility functions for computing special cases of generalized Stirling numbers.
 */
class StirlingNumbers
{
    /**
     * Compute the unsigned Stirling number of the first kind.
     * 
     * This is equivalent to L{n,k}^{1,0}.
     * 
     * Stirling numbers of the first kind count the number of permutations
     * of n elements with exactly k cycles.
     * 
     * @param int $n Number of elements
     * @param int $k Number of cycles
     * 
     * @return float Value of the Stirling number of the first kind
     * 
     * @throws StirlingException If n or k are negative
     */
    public static function stirlingFirstKind(int $n, int $k): float
    {
        if ($n < 0 || $k < 0) {
            throw new StirlingException("n and k must be non-negative, got n={$n}, k={$k}");
        }
        
        $gs = new GeneralizedStirling(1.0, 0.0);
        return $gs->compute($n, $k);
    }
    
    /**
     * Compute the Stirling number of the second kind.
     * 
     * This is equivalent to L{n,k}^{0,1}.
     * 
     * Stirling numbers of the second kind count the number of ways to partition
     * a set of n elements into exactly k non-empty subsets.
     * 
     * @param int $n Number of elements
     * @param int $k Number of subsets
     * 
     * @return float Value of the Stirling number of the second kind
     * 
     * @throws StirlingException If n or k are negative
     */
    public static function stirlingSecondKind(int $n, int $k): float
    {
        if ($n < 0 || $k < 0) {
            throw new StirlingException("n and k must be non-negative, got n={$n}, k={$k}");
        }
        
        $gs = new GeneralizedStirling(0.0, 1.0);
        return $gs->compute($n, $k);
    }
    
    /**
     * Compute the Lah number.
     * 
     * This is equivalent to L{n,k}^{1,1}.
     * 
     * Lah numbers count the number of ways to partition a set of n elements
     * into exactly k non-empty ordered lists (or linearly ordered subsets).
     * 
     * @param int $n Number of elements
     * @param int $k Number of ordered lists
     * 
     * @return float Value of the Lah number
     * 
     * @throws StirlingException If n or k are negative
     */
    public static function lahNumber(int $n, int $k): float
    {
        if ($n < 0 || $k < 0) {
            throw new StirlingException("n and k must be non-negative, got n={$n}, k={$k}");
        }
        
        $gs = new GeneralizedStirling(1.0, 1.0);
        return $gs->compute($n, $k);
    }
}
