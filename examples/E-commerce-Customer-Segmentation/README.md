# E-commerce Customer Segmentation with Stirling Measure

This example demonstrates how to apply the Stirling Measure to e-commerce customer data to discover natural customer segments and optimize marketing strategies.

## Overview

E-commerce businesses struggle with efficiently segmenting their customer base for targeted marketing. Traditional approaches like RFM analysis or k-means clustering often require arbitrary parameter choices. The Stirling Measure provides a mathematical foundation for discovering the natural clustering tendencies in your customer base.

## What You'll Learn

1. How to preprocess e-commerce transaction data
2. How to calculate the Stirling Measure from customer clustering patterns
3. How to estimate parameters (a,b) that govern customer segmentation
4. How to apply these insights to marketing strategy
5. How to validate the approach with business metrics

## The Data

This example uses the Online Retail Dataset from the UCI Machine Learning Repository, which contains:
- 541,909 transactions
- 4,373 unique customers
- 3,684 unique products
- 1 year of transaction data (2010-2011)

## Approach

We'll track how customers naturally cluster into segments based on:
- Purchase frequency
- Average order value
- Product category preferences

For each time period, we'll calculate:
- n = number of active customers
- k = number of natural segments (determined by clustering)
- Stirling Measure = (S_{n+1,k} - S_{n,k-1})/S_{n,k}

Then we'll use regression to estimate parameters a and b, which reveal:
- Parameter a: Customer tendency to join existing segments
- Parameter b: "Cost" or barrier to form new customer segments

## Implementation Steps

1. Data loading and cleaning (see `data_prep.py`)
2. Customer feature extraction (see `feature_extraction.py`) 
3. Time-series segmentation analysis (see `segment_analysis.py`)
4. Stirling Measure calculation (see `stirling_measure.py`)
5. Parameter estimation (see `parameter_estimation.py`)
6. Marketing strategy recommendations (see `marketing_insights.py`)
7. Visualization and reporting (see `visualize.py`)

## Results Preview

When applied to e-commerce data, the Stirling Measure typically reveals:
- Parameter a values between 0.2-0.4, indicating moderate customer similarity within segments
- Parameter b values between 1.2-2.5, indicating significant barriers to new segment formation

These parameters can inform:
- Optimal number of customer segments for marketing campaigns
- Which customer segments are likely to merge over time
- When to create new targeted segments vs. expanding existing ones
- How aggressively to pursue cross-selling between segments

## Getting Started

Follow these steps to run the example:

```bash
# Install dependencies
pip install -r requirements.txt

# Download and prepare the data
python data_prep.py

# Run the complete analysis
python run_analysis.py

# Generate visualizations
python visualize.py
```

See the Jupyter notebook `E-commerce_Segmentation.ipynb` for a step-by-step walkthrough.
