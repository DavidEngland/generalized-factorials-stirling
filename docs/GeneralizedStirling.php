<?php
// filepath: /Users/davidengland/Documents/GitHub/generalized-factorials-stirling/implementations/php/GeneralizedStirling.php
/**
 * Generalized Stirling Numbers Implementation
 *
 * This class implements the generalized Stirling numbers L{n,k}^{α,β} based on
 * the paper "Combinatorial approach of certain generalized Stirling numbers"
 * by Belbachir, Belkhir, and Bousbaa.
 */
class GeneralizedStirling {
    /**
     * Weight parameter for non-head elements
     * @var float
     */
    private $alpha;

    /**
     * Weight parameter for head elements
     * @var float
     */
    private $beta;

    /**
     * Cache for computed values
     * @var array
     */
    private $cache = [];

    /**
     * Create a generalized Stirling number calculator with parameters α and β
     *
     * @param float $alpha Weight parameter for non-head elements (default: 1.0)
     * @param float $beta Weight parameter for head elements (default: 1.0)
     */
    public function __construct($alpha = 1.0, $beta = 1.0) {
        $this->alpha = $alpha;
        $this->beta = $beta;
    }

    /**
     * Calculate the rising factorial (x|α)^n
     *
     * @param float $x Base value
     * @param int $n Number of terms
     * @param float $increment Increment between terms
     * @return float The rising factorial value
     */
    public function risingFactorial($x, $n, $increment = 1.0) {
        if ($n === 0) {
            return 1.0;
        }

        $result = 1.0;
        for ($i = 0; $i < $n; $i++) {
            $result *= ($x + $i * $increment);
        }

        return $result;
    }

    /**
     * Calculate binomial coefficient C(n,k)
     *
     * @param int $n
     * @param int $k
     * @return float
     */
    public function binomialCoefficient($n, $k) {
        if ($k < 0 || $k > $n) {
            return 0;
        }
        if ($k === 0 || $k === $n) {
            return 1;
        }

        $result = 1;
        for ($i = 1; $i <= $k; $i++) {
            $result *= ($n - ($i - 1));
            $result /= $i;
        }

        return $result;
    }

    /**
     * Compute L{n,k}^{α,β} using the triangular recurrence relation
     *
     * @param int $n Number of elements
     * @param int $k Number of ordered lists
     * @return float The generalized Stirling number
     */
    public function triangularRecurrence($n, $k) {
        // Create a cache key
        $key = "{$n}:{$k}";

        // Check if already computed
        if (isset($this->cache[$key])) {
            return $this->cache[$key];
        }

        // Base cases
        if ($k === 0) {
            return $n === 0 ? 1.0 : 0.0;
        }
        if ($n === 0 || $k > $n) {
            return 0.0;
        }
        if ($k === $n) {
            return 1.0;
        }

        // Apply recurrence relation
        $term1 = $this->triangularRecurrence($n-1, $k-1);
        $term2 = ($this->alpha * ($n-1) + $this->beta * $k) * $this->triangularRecurrence($n-1, $k);

        $result = $term1 + $term2;

        // Cache the result
        $this->cache[$key] = $result;

        return $result;
    }

    /**
     * Compute L{n,k}^{α,β} using the explicit formula
     *
     * @param int $n Number of elements
     * @param int $k Number of ordered lists
     * @return float The generalized Stirling number
     */
    public function explicitFormula($n, $k) {
        // Handle base cases
        if ($k === 0) {
            return $n === 0 ? 1.0 : 0.0;
        }
        if ($n === 0 || $k > $n) {
            return 0.0;
        }
        if ($k === $n) {
            return 1.0;
        }

        $result = 0.0;
        for ($j = 0; $j <= $k; $j++) {
            // Calculate binomial coefficient C(k,j)
            $binom = $this->binomialCoefficient($k, $j);

            // Calculate rising factorial (β(k-j)|α)^n
            $base = $this->beta * ($k - $j);
            $risingFact = $this->risingFactorial($base, $n, $this->alpha);

            // Add to sum with alternating sign
            $result += (pow(-1, $j)) * $binom * $risingFact;
        }

        // Divide by β^k * k!
        $denominator = pow($this->beta, $k) * factorial($k);
        return $denominator !== 0 ? $result / $denominator : 0.0;
    }

    /**
     * Compute L{n,1}^{α,β} using the special case formula
     *
     * @param int $n Number of elements
     * @param int $k Should be 1 for this special case
     * @return float The generalized Stirling number
     * @throws Exception If k is not 1
     */
    public function specialCase($n, $k = 1) {
        if ($k !== 1) {
            throw new Exception("This special case only applies for k=1");
        }

        if ($n <= 0) {
            return 0.0;
        }
        if ($n === 1) {
            return 1.0;
        }

        $result = 1.0;
        for ($j = 1; $j < $n; $j++) {
            $result *= ($j * $this->alpha + $this->beta);
        }

        return $result;
    }

    /**
     * Compute L{n,k}^{α,β} using the specified method
     *
     * @param int $n Number of elements
     * @param int $k Number of ordered lists
     * @param string $method Method to use ('triangular', 'explicit', 'special')
     * @return float The generalized Stirling number
     */
    public function compute($n, $k, $method = 'triangular') {
        // For k=1, use the special case formula which is more efficient
        if ($k === 1 && $method !== 'explicit') {
            return $this->specialCase($n, $k);
        }

        if ($method === 'explicit') {
            return $this->explicitFormula($n, $k);
        } else {
            return $this->triangularRecurrence($n, $k);
        }
    }

    /**
     * Generate a triangle of generalized Stirling numbers
     *
     * @param int $nMax Maximum row number
     * @return array Triangle of generalized Stirling numbers
     */
    public function generateTriangle($nMax) {
        $triangle = [];
        for ($n = 1; $n <= $nMax; $n++) {
            $row = [];
            for ($k = 1; $k <= $n; $k++) {
                $row[] = $this->compute($n, $k);
            }
            $triangle[] = $row;
        }
        return $triangle;
    }
}

/**
 * Calculate factorial of n
 *
 * @param int $n
 * @return float
 */
function factorial($n) {
    if ($n <= 1) {
        return 1;
    }
    $result = 1;
    for ($i = 2; $i <= $n; $i++) {
        $result *= $i;
    }
    return $result;
}

/**
 * Compute the unsigned Stirling number of the first kind
 *
 * @param int $n Number of elements
 * @param int $k Number of cycles
 * @return float The Stirling number of the first kind
 */
function stirling_first_kind($n, $k) {
    $gs = new GeneralizedStirling(1.0, 0.0);
    return $gs->compute($n, $k);
}

/**
 * Compute the Stirling number of the second kind
 *
 * @param int $n Number of elements
 * @param int $k Number of subsets
 * @return float The Stirling number of the second kind
 */
function stirling_second_kind($n, $k) {
    $gs = new GeneralizedStirling(0.0, 1.0);
    return $gs->compute($n, $k);
}

/**
 * Compute the Lah number
 *
 * @param int $n Number of elements
 * @param int $k Number of ordered lists
 * @return float The Lah number
 */
function lah_number($n, $k) {
    $gs = new GeneralizedStirling(1.0, 1.0);
    return $gs->compute($n, $k);
}
?>