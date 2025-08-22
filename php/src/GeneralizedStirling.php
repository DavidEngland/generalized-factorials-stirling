<?php

namespace GeneralizedStirling;

use GeneralizedStirling\Exception\StirlingException;

/**
 * Implementation of generalized Stirling numbers with parameters α and β.
 * 
 * These numbers have a combinatorial interpretation as the total weight
 * of distributing n elements into k ordered non-empty lists, where:
 * 1. The head of each list has weight β
 * 2. Other elements in lists have weight α
 * 3. The first element placed in each list has weight 1
 * 
 * Special cases:
 * - Stirling numbers of the first kind: L{n,k}^{1,0}
 * - Stirling numbers of the second kind: L{n,k}^{0,1}
 * - Lah numbers: L{n,k}^{1,1}
 */
class GeneralizedStirling
{
    /** @var float Weight parameter for non-head elements (α) */
    private float $alpha;
    
    /** @var float Weight parameter for head elements (β) */
    private float $beta;
    
    /** @var int Maximum size for memory cache */
    private int $cacheSize;
    
    /** @var bool Whether to use disk-based caching */
    private bool $useDiskCache;
    
    /** @var string|null Directory for disk cache */
    private ?string $cacheDir;
    
    /** @var array In-memory cache for quick lookups */
    private array $memoryCache = [];
    
    /** @var array Cache for precomputed values (special cases) */
    private array $precomputed = [];
    
    /** @var array<string, float> Time spent in each computation method */
    private array $computeTime = [];
    
    /** @var array<string, int> Number of cache hits for each method */
    private array $cacheHits = [];
    
    /** @var array<string, int> Number of cache misses for each method */
    private array $cacheMisses = [];
    
    /**
     * Constructor for GeneralizedStirling.
     * 
     * @param float $alpha Weight parameter for non-head elements
     * @param float $beta Weight parameter for head elements
     * @param int $cacheSize Maximum size for memory cache
     * @param bool $useDiskCache Whether to use disk-based caching
     * @param string|null $cacheDir Directory for disk cache
     * 
     * @throws StirlingException If alpha or beta are invalid
     */
    public function __construct(
        float $alpha = 1.0,
        float $beta = 1.0,
        int $cacheSize = 10000,
        bool $useDiskCache = false,
        ?string $cacheDir = null
    ) {
        // Validate input parameters
        if (!is_finite($alpha)) {
            throw new StirlingException("Alpha must be a finite number, got {$alpha}");
        }
        if (!is_finite($beta)) {
            throw new StirlingException("Beta must be a finite number, got {$beta}");
        }
        if ($cacheSize < 0) {
            throw new StirlingException("Cache size must be non-negative, got {$cacheSize}");
        }
        
        $this->alpha = $alpha;
        $this->beta = $beta;
        $this->cacheSize = $cacheSize;
        $this->useDiskCache = $useDiskCache;
        
        // Set up disk cache directory if enabled
        if ($useDiskCache) {
            if ($cacheDir === null) {
                $this->cacheDir = sys_get_temp_dir() . '/gsn_cache_' . md5($alpha . '_' . $beta);
            } else {
                $this->cacheDir = $cacheDir;
            }
            // Create cache directory if it doesn't exist
            if (!is_dir($this->cacheDir) && !mkdir($this->cacheDir, 0777, true) && !is_dir($this->cacheDir)) {
                throw new StirlingException("Failed to create cache directory: {$this->cacheDir}");
            }
        } else {
            $this->cacheDir = $cacheDir;
        }
        
        // Precompute tables for common special cases
        if (in_array([$this->alpha, $this->beta], [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]], true)) {
            $this->precomputeCommonValues();
        }
    }
    
    /**
     * Compute L{n,k}^{α,β} using the specified method.
     * Automatically selects the most appropriate algorithm if method='auto'.
     * 
     * @param int $n Number of elements
     * @param int $k Number of ordered lists
     * @param string $method Method to use for computation
     * 
     * @return float Value of the generalized Stirling number
     * 
     * @throws StirlingException If n or k are negative, or if method is not recognized
     */
    public function compute(int $n, int $k, string $method = 'auto'): float
    {
        // Validate inputs
        if ($n < 0 || $k < 0) {
            throw new StirlingException("n and k must be non-negative, got n={$n}, k={$k}");
        }
        
        $validMethods = [
            'auto', 'triangular', 'explicit', 'horizontal', 'vertical', 
            'bottom_up', 'symmetric', 'single_list'
        ];
        if (!in_array($method, $validMethods, true)) {
            throw new StirlingException("Unknown method: {$method}. Valid methods are: " . implode(', ', $validMethods));
        }
        
        // Handle base cases for efficiency
        if ($k === 0) {
            return $n === 0 ? 1.0 : 0.0;
        }
        if ($n === 0) {
            return 0.0;  // L_{0,k} = 0 for k > 0
        }
        if ($k > $n) {
            return 0.0;  // L_{n,k} = 0 for k > n
        }
        if ($k === $n) {
            return 1.0;  // L_{n,n} = 1
        }
        
        // For k=1, use the singleListCase formula which is more efficient
        if ($k === 1) {
            return $this->singleListCase($n, $k);
        }
        
        // Auto-select the best method based on input size and parameters
        if ($method === 'auto') {
            $method = $this->selectBestMethod($n, $k);
        }
        
        // Use the selected method
        switch ($method) {
            case 'explicit':
                return $this->explicitFormula($n, $k);
            case 'triangular':
                return $this->triangularRecurrence($n, $k);
            case 'bottom_up':
                return $this->bottomUpComputation($n, $k);
            case 'horizontal':
                return $this->horizontalRecurrence($n, $k);
            case 'vertical':
                return $n > 0 && $k > 0 
                    ? $this->verticalRecurrence($n - 1, $k - 1) 
                    : $this->triangularRecurrence($n, $k);
            case 'symmetric':
                return $n >= $k 
                    ? $this->symmetricFunction($k, $n - $k) 
                    : $this->triangularRecurrence($n, $k);
            case 'single_list':
                if ($k === 1) {
                    return $this->singleListCase($n, $k);
                }
                throw new StirlingException("single_list method only valid for k=1, got k={$k}");
            default:
                return $this->triangularRecurrence($n, $k);
        }
    }
    
    /**
     * Generate a triangle of generalized Stirling numbers.
     * 
     * @param int $nMax Maximum row number
     * @param string $formatStr Format string for displaying numbers
     * @param string $method Method to use for computation
     * @param bool $sparse If true, return a sparse representation as associative array
     * 
     * @return array Triangle of generalized Stirling numbers
     * 
     * @throws StirlingException If nMax is negative
     */
    public function generateTriangle(int $nMax, string $formatStr = "%.0f", string $method = 'auto', bool $sparse = false): array
    {
        if ($nMax < 0) {
            throw new StirlingException("nMax must be non-negative, got {$nMax}");
        }
        
        if ($sparse) {
            // Return a sparse representation as an associative array
            $triangle = [];
            for ($n = 1; $n <= $nMax; $n++) {
                for ($k = 1; $k <= $n; $k++) {
                    $value = $this->compute($n, $k, $method);
                    if ($value != 0) {
                        $triangle["{$n},{$k}"] = sprintf($formatStr, $value);
                    }
                }
            }
            return $triangle;
        } else {
            // Return a dense representation as a nested array
            $triangle = [];
            for ($n = 1; $n <= $nMax; $n++) {
                $row = [];
                for ($k = 1; $k <= $n; $k++) {
                    $row[] = sprintf($formatStr, $this->compute($n, $k, $method));
                }
                $triangle[] = $row;
            }
            return $triangle;
        }
    }
    
    /**
     * Print a summary of performance statistics.
     * 
     * @return void
     */
    public function summary(): void
    {
        $stats = $this->getPerformanceStats();
        
        echo "\nPerformance Summary\n";
        echo str_repeat('-', 50) . "\n";
        echo "Parameters: α={$this->alpha}, β={$this->beta}\n";
        
        // Cache statistics
        $totalHits = array_sum($stats['cache_hits']);
        $totalMisses = array_sum($stats['cache_misses']);
        $totalOperations = $totalHits + $totalMisses;
        $hitRatio = $totalOperations > 0 ? $totalHits / $totalOperations : 0;
        
        echo "\nCache Statistics:\n";
        echo "  Total operations: {$totalOperations}\n";
        echo "  Cache hits: {$totalHits}\n";
        echo "  Cache misses: {$totalMisses}\n";
        echo "  Overall hit ratio: " . sprintf("%.1f%%", $hitRatio * 100) . "\n";
        
        // Per-method statistics
        echo "\nPer-Method Statistics:\n";
        $methods = array_unique(array_merge(array_keys($stats['cache_hits']), array_keys($stats['cache_misses'])));
        sort($methods);
        
        foreach ($methods as $method) {
            $hits = $stats['cache_hits'][$method] ?? 0;
            $misses = $stats['cache_misses'][$method] ?? 0;
            $methodTotal = $hits + $misses;
            $ratio = $methodTotal > 0 ? $hits / $methodTotal : 0;
            $time = $stats['compute_time'][$method] ?? 0;
            
            echo "  {$method}:\n";
            echo "    Operations: {$methodTotal}\n";
            echo "    Hit ratio: " . sprintf("%.1f%%", $ratio * 100) . "\n";
            echo "    Compute time: " . sprintf("%.6f", $time) . " seconds\n";
        }
        
        // Disk cache info
        if ($stats['disk_cache_enabled']) {
            echo "\nDisk Cache:\n";
            echo "  Directory: {$stats['disk_cache_dir']}\n";
            echo "  Size: " . sprintf("%.1f", $stats['disk_cache_size'] / 1024) . " KB\n";
        }
        
        echo str_repeat('-', 50) . "\n";
    }
    
    /**
     * Get performance statistics for the different computation methods.
     * 
     * @return array<string, mixed> Performance statistics
     */
    public function getPerformanceStats(): array
    {
        $stats = [
            'compute_time' => $this->computeTime,
            'cache_hits' => $this->cacheHits,
            'cache_misses' => $this->cacheMisses,
            'hit_ratio' => [],
            'disk_cache_enabled' => $this->useDiskCache,
            'disk_cache_dir' => $this->useDiskCache ? $this->cacheDir : null,
            'disk_cache_size' => 0
        ];
        
        // Calculate hit ratios
        foreach ($this->cacheHits as $method => $hits) {
            $total = $hits + ($this->cacheMisses[$method] ?? 0);
            $stats['hit_ratio'][$method] = $total > 0 ? $hits / $total : 0;
        }
        
        // Calculate disk cache size if enabled
        if ($this->useDiskCache && is_dir($this->cacheDir)) {
            try {
                $totalSize = 0;
                foreach (glob($this->cacheDir . '/*.cache') as $file) {
                    $totalSize += filesize($file);
                }
                $stats['disk_cache_size'] = $totalSize;
            } catch (\Exception $e) {
                // Ignore errors in file size calculation
            }
        }
        
        return $stats;
    }
    
    /**
     * Clear all caches to free memory and disk space.
     * 
     * @return void
     */
    public function clearCache(): void
    {
        $this->memoryCache = [];
        
        // Clear disk cache if enabled
        if ($this->useDiskCache && is_dir($this->cacheDir)) {
            try {
                foreach (glob($this->cacheDir . '/*.cache') as $file) {
                    unlink($file);
                }
            } catch (\Exception $e) {
                // Ignore errors in file deletion
            }
        }
        
        // Reset performance counters
        $this->computeTime = [];
        $this->cacheHits = [];
        $this->cacheMisses = [];
    }
    
    // -------------------------------------------------------------------------
    // Computational methods (stubs with docblocks for documentation)
    // -------------------------------------------------------------------------
    
    /**
     * Compute using the explicit formula (if available).
     * @param int $n
     * @param int $k
     * @return float
     */
    private function explicitFormula(int $n, int $k): float
    {
        // ...implementation...
        throw new StirlingException("explicitFormula not implemented yet.");
    }
    
    /**
     * Compute using the triangular recurrence relation.
     * @param int $n
     * @param int $k
     * @return float
     */
    private function triangularRecurrence(int $n, int $k): float
    {
        // ...implementation...
        throw new StirlingException("triangularRecurrence not implemented yet.");
    }
    
    /**
     * Compute using a bottom-up dynamic programming approach.
     * @param int $n
     * @param int $k
     * @return float
     */
    private function bottomUpComputation(int $n, int $k): float
    {
        // ...implementation...
        throw new StirlingException("bottomUpComputation not implemented yet.");
    }
    
    /**
     * Compute using horizontal recurrence.
     * @param int $n
     * @param int $k
     * @return float
     */
    private function horizontalRecurrence(int $n, int $k): float
    {
        // ...implementation...
        throw new StirlingException("horizontalRecurrence not implemented yet.");
    }
    
    /**
     * Compute using vertical recurrence.
     * @param int $n
     * @param int $k
     * @return float
     */
    private function verticalRecurrence(int $n, int $k): float
    {
        // ...implementation...
        throw new StirlingException("verticalRecurrence not implemented yet.");
    }
    
    /**
     * Compute using the symmetric function approach.
     * @param int $n
     * @param int $k
     * @return float
     */
    private function symmetricFunction(int $n, int $k): float
    {
        // ...implementation...
        throw new StirlingException("symmetricFunction not implemented yet.");
    }
    
    /**
     * Efficient computation for the single list case (k=1).
     * @param int $n
     * @param int $k
     * @return float
     */
    private function singleListCase(int $n, int $k): float
    {
        // ...implementation...
        throw new StirlingException("singleListCase not implemented yet.");
    }
    
    /**
     * Select the best computation method based on input size and parameters.
     * @param int $n
     * @param int $k
     * @return string
     */
    private function selectBestMethod(int $n, int $k): string
    {
        // ...implementation...
        return 'triangular'; // Default for now
    }
    
    /**
     * Precompute values for common special cases (Stirling/Lah).
     * @return void
     */
    private function precomputeCommonValues(): void
    {
        // ...implementation...
    }
    
    // -------------------------------------------------------------------------
    // Helper methods for caching (stubs for documentation)
    // -------------------------------------------------------------------------
    
    /**
     * Get a disk cache key for a given n, k, method.
     * @param int $n
     * @param int $k
     * @param string $method
     * @return string
     */
    private function _getDiskCacheKey(int $n, int $k, string $method): string
    {
        // ...implementation...
        return "{$n}_{$k}_{$method}";
    }
    
    /**
     * Save a computed value to cache.
     * @param int $n
     * @param int $k
     * @param string $method
     * @param float $value
     * @return void
     */
    private function _saveToCache(int $n, int $k, string $method, float $value): void
    {
        // ...implementation...
    }
    
    // ...existing code...
}
