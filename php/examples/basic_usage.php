<?php

require_once __DIR__ . '/../vendor/autoload.php';

use GeneralizedStirling\GeneralizedStirling;
use GeneralizedStirling\Util\StirlingNumbers;
use GeneralizedStirling\Exception\StirlingException;

// Create a new GeneralizedStirling instance for Lah numbers
$gs = new GeneralizedStirling(1.0, 1.0);

// Compute some values
echo "Lah numbers (α=1.0, β=1.0):\n";
for ($n = 1; $n <= 5; $n++) {
    $row = [];
    for ($k = 1; $k <= $n; $k++) {
        $row[] = $gs->compute($n, $k);
    }
    echo "n={$n}: " . implode(", ", $row) . "\n";
}

echo "\n";

// Compute using different methods
echo "Computing L{5,3}^{1,1} using different methods:\n";
echo "Triangular recurrence: " . $gs->compute(5, 3, 'triangular') . "\n";
echo "Bottom-up computation: " . $gs->compute(5, 3, 'bottom_up') . "\n";
echo "Explicit formula: " . $gs->compute(5, 3, 'explicit') . "\n";

echo "\n";

// Use convenience functions for special cases
echo "Special cases:\n";
echo "Stirling number of the first kind s(5,3): " . StirlingNumbers::stirlingFirstKind(5, 3) . "\n";
echo "Stirling number of the second kind S(5,3): " . StirlingNumbers::stirlingSecondKind(5, 3) . "\n";
echo "Lah number L(5,3): " . StirlingNumbers::lahNumber(5, 3) . "\n";

echo "\n";

// Generate a triangle
echo "Triangle of Stirling numbers of the second kind up to n=5:\n";
$gs2 = new GeneralizedStirling(0.0, 1.0);
$triangle = $gs2->generateTriangle(5);

foreach ($triangle as $n => $row) {
    echo "n=" . ($n + 1) . ": " . implode(", ", $row) . "\n";
}

echo "\n";

// Show performance statistics
echo "Performance statistics:\n";
$gs->summary();
