<?php

namespace GeneralizedStirling\Util;

use GeneralizedStirling\GeneralizedStirling;
use GeneralizedStirling\Exception\StirlingException;

/**
 * Utility class for parallel computation of generalized Stirling numbers.
 */
class Parallel
{
    /**
     * Generate a triangle of generalized Stirling numbers using parallel processing.
     * 
     * Note: This implementation uses multiple PHP processes for parallelization.
     * It requires the PHP pcntl and posix extensions to be available.
     * 
     * @param int $nMax Maximum row number
     * @param float $alpha Weight parameter for non-head elements
     * @param float $beta Weight parameter for head elements
     * @param string $method Method to use for computation
     * @param int|null $processes Number of processes to use (null = use all available cores)
     * 
     * @return array Triangle of generalized Stirling numbers
     * 
     * @throws StirlingException If parallel processing is not available or if nMax is negative
     */
    public static function parallelGenerateTriangle(
        int $nMax,
        float $alpha = 1.0,
        float $beta = 1.0,
        string $method = 'auto',
        ?int $processes = null
    ): array {
        if ($nMax < 0) {
            throw new StirlingException("nMax must be non-negative, got {$nMax}");
        }
        
        // Check if parallel processing is available
        if (!function_exists('pcntl_fork') || !function_exists('posix_getpid')) {
            // Fall back to non-parallel implementation
            $gs = new GeneralizedStirling($alpha, $beta);
            return $gs->generateTriangle($nMax, "%.6f", $method, false);
        }
        
        // Determine number of processes to use
        if ($processes === null) {
            $processes = self::getNumCores();
        }
        $processes = max(1, min($processes, 32));  // Limit between 1 and 32
        
        // Generate all (n,k) pairs to compute
        $pairs = [];
        for ($n = 1; $n <= $nMax; $n++) {
            for ($k = 1; $k <= $n; $k++) {
                $pairs[] = [$n, $k];
            }
        }
        
        $numPairs = count($pairs);
        $pairsPerProcess = ceil($numPairs / $processes);
        
        // Prepare temporary files for results
        $tempFiles = [];
        $pids = [];
        
        // Create temporary directory if it doesn't exist
        $tempDir = sys_get_temp_dir() . '/gsn_parallel_' . uniqid();
        if (!is_dir($tempDir) && !mkdir($tempDir, 0777, true)) {
            throw new StirlingException("Failed to create temporary directory: {$tempDir}");
        }
        
        // Fork processes
        for ($i = 0; $i < $processes; $i++) {
            $start = $i * $pairsPerProcess;
            $end = min($start + $pairsPerProcess, $numPairs);
            
            if ($start >= $numPairs) {
                break;
            }
            
            $tempFile = $tempDir . "/process_{$i}.json";
            $tempFiles[] = $tempFile;
            
            $pid = pcntl_fork();
            
            if ($pid === -1) {
                // Fork failed
                throw new StirlingException("Failed to fork process {$i}");
            } elseif ($pid === 0) {
                // Child process
                $gs = new GeneralizedStirling($alpha, $beta);
                $results = [];
                
                for ($j = $start; $j < $end; $j++) {
                    [$n, $k] = $pairs[$j];
                    $results[] = [
                        'n' => $n,
                        'k' => $k,
                        'value' => $gs->compute($n, $k, $method)
                    ];
                }
                
                file_put_contents($tempFile, json_encode($results));
                exit(0);
            } else {
                // Parent process
                $pids[] = $pid;
            }
        }
        
        // Wait for all child processes to finish
        foreach ($pids as $pid) {
            pcntl_waitpid($pid, $status);
        }
        
        // Combine results
        $triangle = array_fill(0, $nMax, []);
        
        foreach ($tempFiles as $tempFile) {
            if (file_exists($tempFile)) {
                $results = json_decode(file_get_contents($tempFile), true);
                
                foreach ($results as $result) {
                    $n = $result['n'];
                    $k = $result['k'];
                    $value = $result['value'];
                    
                    $triangle[$n-1][$k-1] = $value;
                }
                
                // Clean up temporary file
                unlink($tempFile);
            }
        }
        
        // Clean up temporary directory
        rmdir($tempDir);
        
        return $triangle;
    }
    
    /**
     * Get the number of CPU cores available.
     * 
     * @return int Number of CPU cores
     */
    private static function getNumCores(): int
    {
        // Try different methods to detect the number of cores
        if (function_exists('sys_getloadavg') && function_exists('shell_exec')) {
            $cores = (int) shell_exec('nproc 2>/dev/null || sysctl -n hw.ncpu 2>/dev/null || echo 1');
            return $cores > 0 ? $cores : 1;
        }
        
        return 1;  // Default to 1 core if detection fails
    }
}
