# Mathematical Notation for Generalized Stirling Numbers

This document provides definitions for the mathematical notation used in the documentation for generalized Stirling numbers.

## KaTeX Macros

If you're using KaTeX to render the mathematics in Markdown documentation, you can include these macro definitions to ensure proper rendering:

```html
<script>
  document.addEventListener("DOMContentLoaded", function() {
    renderMathInElement(document.body, {
      delimiters: [
        {left: "$$", right: "$$", display: true},
        {left: "$", right: "$", display: false}
      ],
      macros: {
        // Stirling numbers of the first kind (unsigned)
        "\\stirlingOne": "\\genfrac{[}{]}{0pt}{}{#1}{#2}",
        
        // Stirling numbers of the second kind
        "\\stirlingTwo": "\\genfrac{\\{}{\\}}{0pt}{}{#1}{#2}",
        
        // Lah numbers
        "\\lah": "\\genfrac{\\lfloor}{\\rfloor}{0pt}{}{#1}{#2}",
        
        // Generalized Stirling numbers
        "\\genStirling": "L_{#1,#2}^{#3,#4}",
        
        // Rising factorial
        "\\risingFactorial": "(#1|#2)^{\\overline{#3}}",
        
        // Falling factorial
        "\\fallingFactorial": "(#1|#2)^{\\underline{#3}}"
      }
    });
  });
</script>
```

## LaTeX Commands

For LaTeX documents, you can use these command definitions:

```latex
% Stirling numbers of the first kind
\newcommand{\stirlingf}[2]{\genfrac[]{0pt}{}{#1}{#2}}

% Stirling numbers of the second kind
\newcommand{\stirlings}[2]{\genfrac\{\}{0pt}{}{#1}{#2}}

% Lah numbers
\newcommand{\lah}[2]{\genfrac\lfloor\rfloor{0pt}{}{#1}{#2}}

% Generalized Stirling numbers
\newcommand{\genStirling}[4]{L_{#1,#2}^{#3,#4}}

% Rising factorial
\newcommand{\risingFactorial}[3]{(#1|#2)^{\overline{#3}}}

% Falling factorial
\newcommand{\fallingFactorial}[3]{(#1|#2)^{\underline{#3}}}
```

## Usage Examples

### Markdown with KaTeX

```markdown
The generalized Stirling numbers $L_{n,k}^{\alpha,\beta}$ include:

- Stirling numbers of the first kind: $L_{n,k}^{1,0}$ or $s(n,k)$
- Stirling numbers of the second kind: $L_{n,k}^{0,1}$ or $S(n,k)$
- Lah numbers: $L_{n,k}^{1,1}$ or $L(n,k)$
```

### LaTeX

```latex
The generalized Stirling numbers $\genStirling{n}{k}{\alpha}{\beta}$ include:

- Stirling numbers of the first kind: $\genStirling{n}{k}{1}{0}$ or $\stirlingf{n}{k}$
- Stirling numbers of the second kind: $\genStirling{n}{k}{0}{1}$ or $\stirlings{n}{k}$
- Lah numbers: $\genStirling{n}{k}{1}{1}$ or $\lah{n}{k}$
```

## Notes on Rendering

1. In GitHub Markdown and many other platforms, KaTeX or MathJax might be needed to render these expressions properly.

2. For complex notation like generalized Stirling numbers, it's often clearer to use the simple notation $L_{n,k}^{\alpha,\beta}$ instead of custom commands in web contexts.

3. The vertical bar notation in rising factorials $(x|α)^{\overline{n}}$ might cause rendering issues in some KaTeX implementations. In such cases, consider using $(x;α)^{\overline{n}}$ or another separator.
