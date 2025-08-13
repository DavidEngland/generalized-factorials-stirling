# Project: Create the Stirling Windmill Visualization

## Project Overview

Your mission: Create a visual representation of the "Stirling Windmill" - a graphic that shows how the four fundamental triangular matrices of Stirling numbers relate to each other in quadrant form.

## Learning Objectives

By completing this project, you will:
- Deeply understand the relationships between different Stirling number types
- Practice matrix computations and visualizations
- See the "big picture" of how generalized coefficients unify classical results
- Create something visually compelling and mathematically meaningful

## Project Phases

### Phase 1: Mathematical Foundation (2-3 hours)

**Task 1.1:** Review the theory
- Read `/docs/Stirling-Windmill-Graphic.md`
- Understand the four quadrants and their parameter pairs
- Identify which classical Stirling numbers go in each quadrant

**Task 1.2:** Compute the matrices
Create 5×5 matrices for each quadrant:
- **Quadrant I**: $S_{m,n}(1,0)$ - Stirling numbers of the second kind
- **Quadrant II**: $S_{m,n}(0,1)$ - Signed Stirling numbers of the first kind  
- **Quadrant III**: $S_{m,n}(-1,0)$ - Signed Stirling numbers of the second kind
- **Quadrant IV**: $S_{m,n}(0,-1)$ - Unsigned Stirling numbers of the first kind

**Deliverable:** Four 5×5 matrices with all entries computed and verified.

### Phase 2: Static Visualization (3-4 hours)

**Task 2.1:** Choose your tools
Options include:
- Python (matplotlib, seaborn)
- JavaScript (D3.js, Chart.js)
- LaTeX/TikZ
- Web-based (HTML/CSS/SVG)
- Even Excel or Google Sheets!

**Task 2.2:** Create the basic layout
- Four quadrants arranged around a central axis
- Clear labels for each quadrant with parameter pairs
- Numbers displayed in a readable triangular matrix format

**Task 2.3:** Add visual elements
- Color coding for each quadrant (see suggestions in the docs)
- Central hub showing the identity transformation
- Grid lines like "graph paper" to show the lattice structure

**Deliverable:** A static image showing all four matrices in windmill arrangement.

### Phase 3: Interactive Features (4-6 hours)

**Task 3.1:** Add interactivity (choose 2-3 features):
- **Hover effects**: Show combinatorial interpretation when hovering over entries
- **Click to highlight**: Show orthogonality relationships (e.g., click an entry in Quadrant I to highlight corresponding entries in Quadrant II)
- **Animation**: "Rotate" the windmill to show parameter transformations
- **Zoom**: Allow detailed examination of matrix entries
- **Calculation display**: Show the actual computation for each entry

**Task 3.2:** Educational annotations
- Brief text explaining what each quadrant represents
- Examples showing how to read the matrices
- Connection arrows showing inverse relationships

**Deliverable:** Interactive visualization with at least 2 working features.

### Phase 4: Mathematical Extensions (3-5 hours)

**Task 4.1:** Add more spokes
Include additional parameter pairs:
- $(2,0)$ and $(0,2)$ - Scaled Stirling transformations
- $(1,-1)$ and $(-1,1)$ - Lah number transformations
- Create "minor spokes" showing these relationships

**Task 4.2:** Verification tools
- Input fields to compute $S_{m,n}(a,b)$ for arbitrary parameters
- Show the calculation steps
- Verify matrix inverse relationships interactively

**Task 4.3:** Higher dimensions
- Show how the windmill concept extends to 3D (multiple parameters)
- Create a conceptual diagram of the "infinite windmill"

**Deliverable:** Extended visualization with additional mathematical content.

## Technical Specifications

### Minimum Requirements
- Display all four 5×5 classical Stirling number matrices
- Clear quadrant layout with parameter labels
- Readable numbers in triangular arrangement
- Basic color coding or visual distinction

### Recommended Features
- Interactive hover/click functionality
- Visual demonstration of at least one orthogonality relationship
- Export capability (save image, share link, etc.)
- Educational annotations or tooltips

### Advanced Features
- Real-time calculation of arbitrary parameters
- Animation showing parameter space "rotation"
- 3D perspective view
- Integration with computational verification code

## Getting Started Code

### Python/Matplotlib Starter
```python
import matplotlib.pyplot as plt
import numpy as np

def create_stirling_windmill():
    fig, ((ax2, ax1), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 12))
    
    # Quadrant I: S(m,n)(1,0) - Stirling second kind
    stirling_2nd = [[1, 0, 0, 0, 0],
                    [1, 1, 0, 0, 0], 
                    [1, 3, 1, 0, 0],
                    [1, 7, 6, 1, 0],
                    [1, 15, 25, 10, 1]]
    
    # TODO: Add the other three matrices
    # TODO: Create the visualizations
    # TODO: Add labels and formatting
    
    plt.title("The Stirling Windmill")
    plt.show()

if __name__ == "__main__":
    create_stirling_windmill()
```

### Web-based Starter (HTML/CSS/JavaScript)
```html
<!DOCTYPE html>
<html>
<head>
    <title>Stirling Windmill</title>
    <style>
        .windmill { display: grid; grid-template-columns: 1fr 1fr; }
        .quadrant { border: 2px solid #000; padding: 20px; }
        .matrix { font-family: monospace; }
    </style>
</head>
<body>
    <div class="windmill">
        <div class="quadrant" id="q2">
            <h3>Quadrant II: (0,1)</h3>
            <div class="matrix" id="matrix-q2"></div>
        </div>
        <div class="quadrant" id="q1">
            <h3>Quadrant I: (1,0)</h3>
            <div class="matrix" id="matrix-q1"></div>
        </div>
        <!-- TODO: Add quadrants III and IV -->
    </div>
    
    <script>
        // TODO: Add matrix data and rendering code
    </script>
</body>
</html>
```

## Evaluation Criteria

### Mathematical Accuracy (30 points)
- All matrix entries are correct
- Parameter labels are accurate
- Relationships between quadrants are properly shown

### Visual Design (25 points)
- Clear, readable layout
- Effective use of color and space
- Professional appearance

### Functionality (25 points)
- Interactive features work as intended
- User interface is intuitive
- Code is well-organized and documented

### Educational Value (20 points)
- Helps viewers understand the mathematical concepts
- Provides insights beyond just displaying numbers
- Could be used to teach others

## Submission Requirements

1. **Code/Files**: All source code and assets
2. **Documentation**: README explaining how to run/view your visualization
3. **Reflection**: 1-2 page write-up addressing:
   - What you learned about Stirling numbers through this project
   - Challenges you encountered and how you solved them
   - Ideas for extending or improving the visualization
   - How this project changed your understanding of the mathematical concepts

4. **Demo**: Brief presentation (5-10 minutes) showing your visualization and explaining one key insight you gained

## Extensions and Variations

- **Historical timeline**: Show how different mathematicians discovered these relationships
- **Applications showcase**: Demonstrate where these transformations are used in practice
- **Comparison tool**: Side-by-side comparison with other mathematical visualizations
- **Educational game**: Turn the windmill into an interactive learning game
- **Research connection**: Link to current research in generalized Stirling theory

## Resources

- Main documentation in `/docs/Stirling-Windmill-Graphic.md`
- Verification code in `/exercises/computational/`
- Matrix computation help in `/exercises/basic-concepts/`
- Similar visualizations online for inspiration (cite your sources!)

**Remember**: The goal is not just to create something that looks nice, but to build something that deepens mathematical understanding. The best visualizations reveal new insights about the underlying mathematics.

**Timeline**: Plan for 8-15 hours total, spread over 1-2 weeks. Start early and iterate!
