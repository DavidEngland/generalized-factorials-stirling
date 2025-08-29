"""
Generalized Stirling Numbers package.

This package provides implementations of generalized Stirling numbers and related
combinatorial sequences across different programming languages.
"""

from src.generalized_stirling import (
    GeneralizedStirling,
    stirling_first_kind,
    stirling_second_kind,
    lah_number
)
from .stirling_core import StirlingComputation, BellPolynomials, ParameterEstimation, StirlingTransform
from .stirling_applications import StirlingPartitioning, InverseFunctionEstimation, ClusteringReport

__version__ = "0.1.0"

__all__ = [
    'StirlingComputation',
    'BellPolynomials',
    'ParameterEstimation',
    'StirlingTransform',
    'StirlingPartitioning',
    'InverseFunctionEstimation',
    'ClusteringReport'
]
