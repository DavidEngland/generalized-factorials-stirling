# Wedding Reception Planner

This interactive tool helps plan seating arrangements for weddings and other events using the generalized Stirling number framework.

## Features

- Calculate optimal table arrangements based on guest groups
- Visualize different seating strategies with varying degrees of group mixing
- Compare costs between different arrangement options
- Export your seating plan

## Mathematical Background

This tool uses the $(a,b)$-parameterized Stirling framework where:

- **a parameter**: Controls how strongly guests from the same group prefer to sit together
- **b parameter**: Controls the cost/effectiveness of separating different groups

Key parameter settings:
- Classical $(0,1)$: Keeps groups separate (families sit together)
- Half-barrier $(0,1/2)$: Balanced approach (some mixing between groups)
- Anti-barrier $(0,-1/2)$: Encourages mixing between groups

## Usage

Simply open `wedding_reception_planner.html` in any modern web browser - no server or installation required.
