# **Analysis of Spectral Clustering Against Kleinberg's Consistency Axiom**

## **1\. Introduction and Background**

This document examines the axiomatic properties of Spectral Clustering, specifically addressing whether a natural implementation of the algorithm adheres to the criterion known as Kleinberg's Consistency Axiom.

### **1.1 Similarity vs. Metric in Clustering**

Clustering algorithms typically rely on measuring the distance or relationship between data points.

* **Metric:** A formal distance function \\rho(x, y) that satisfies non-negativity, identity of indiscernibles, symmetry, and the triangle inequality.
* **Similarity Function:** A function W(x, y) which measures how alike two points are. Spectral clustering algorithms primarily rely on a similarity function (often represented as a weighted adjacency matrix W in a graph).
* **Conversion:** A metric \\rho can be converted to a similarity function, such as using a Gaussian kernel: W(x,y) \= e^{-\\rho(x,y)^2 / (2\\sigma^2)}.

### **1.2 The Clustering Framework**

A clustering algorithm A takes a finite point set S and an associated metric \\rho as input, and outputs a non-trivial partition of S, called a clustering \\mathcal{C}.

## **2\. Kleinberg's Consistency Axiom**

Kleinberg's Consistency Axiom (often referred to as Kleinberg-consistency) demands stability of a clustering algorithm's output under specific transformations of the input metric.
**Axiom Definition:** Let A run on (S, \\rho) yield the clustering \\mathcal{C}. Consider a new metric \\rho' that satisfies two conditions relative to the clustering \\mathcal{C}:

1. **Within-Cluster Contraction:** For any two points x, y \\in S that fell into the *same* cluster C \\in \\mathcal{C}, the new distance is smaller or equal to the original distance:
2. **Between-Cluster Expansion:** For any two points x, y \\in S that fell into *distinct* clusters, the new distance is larger or equal to the original distance:

**Consistency Requirement:** If A is run on the new input (S, \\rho'), the resulting clustering must be the same: A(S, \\rho') \= \\mathcal{C}.
Essentially, the axiom requires that if we selectively make the members of the current clusters closer and the members of different clusters farther apart, the algorithm should confirm its original decision.

## **3\. Analysis: Spectral Clustering and Consistency**

**Question:** Is there any specific natural spectral clustering algorithm that is known (not) to be Kleinberg-consistent?
**Conclusion:** The standard **Normalized Spectral Clustering (NSC)** algorithm is **NOT** Kleinberg-consistent.

### **3.1 The Normalized Spectral Clustering (NSC) Algorithm**

The standard implementation of Spectral Clustering typically follows these steps:

1. **Graph Construction:** Create a similarity matrix W from the metric \\rho, commonly using a Gaussian kernel W\_{ij} \= e^{-\\rho(x\_i, x\_j)^2 / (2\\sigma^2)}.
2. **Laplacian Derivation:** Compute the Normalized Graph Laplacian L\_{\\text{norm}} \= I \- D^{-1/2} W D^{-1/2}.
3. **Spectral Embedding:** Compute the k eigenvectors corresponding to the smallest non-zero eigenvalues of L\_{\\text{norm}} to form an embedding matrix V.
4. **Final Partition:** Apply k-means clustering to the rows of V to obtain the final clustering \\mathcal{C}.

### **3.2 Reasons for Failure of Consistency**

The NSC algorithm fails the consistency axiom due to the cumulative effect of its non-linear steps, specifically:

#### **A. Non-Axiomatic Transformation of the Metric**

The step that converts the metric \\rho to the similarity matrix W via a kernel function (like the Gaussian kernel) is non-linear and parameterized by \\sigma.

* When the metric is changed from \\rho to \\rho' (satisfying the axiom), the non-linear kernel transformation results in complex changes in the similarity matrix W'.
* The relationship between the distances is altered non-monotonically in terms of similarity, making the effect on the Laplacian unpredictable and preventing the axiom from holding universally.

#### **B. Sensitivity of the Eigen-Decomposition**

The core of NSC relies on the stability of the eigenvectors of the normalized Laplacian L\_{\\text{norm}}.

* The small changes introduced in W by the distance transformation \\rho \\rightarrow \\rho' can significantly perturb the matrix L\_{\\text{norm}}.
* Eigenvectors, particularly those associated with closely spaced eigenvalues (a small spectral gap), are highly sensitive to matrix perturbations. A small perturbation in the graph weights can lead to a rotation or substantial change in the resulting k-dimensional spectral embedding space.

#### **C. Inconsistency of the k-means Post-Processing**

The final clustering step, k-means, is applied to the low-dimensional spectral embedding V. The k-means algorithm itself is known to be **NOT Kleinberg-consistent**.

* Since the consistency axiom must hold for all steps of the algorithm, the failure of k-means on the output of the spectral step is sufficient to render the entire NSC algorithm inconsistent. The change in the embedded feature space V \\rightarrow V' may shift the optimal k-means centers, leading to a different partition \\mathcal{C}' \\ne \\mathcal{C}.

In summary, the use of a non-linear kernel, the dependence on the highly sensitive eigen-decomposition, and the application of the inconsistent k-means post-processing step ensures that the standard Normalized Spectral Clustering algorithm violates Kleinberg's Consistency Axiom.

---

## Reference Answer (RA)

Let $A$ be the usual spectral algorithm (compute the Laplacian from the similarity matrix, take the second eigenvector and run $k$-means). Run it on
$$
W=
\begin{pmatrix}
0 & 10 & 1 & 1\\
10 & 0 & 1 & 1\\
1 & 1 & 0 & 10\\
1 & 1 & 10 & 0
\end{pmatrix}
\quad (k=2).
$$
The second eigenvector of the Laplacian separates $\{a,b\}$ from $\{c,d\}$.

Now modify the distances consistently with this clustering, e.g.
$$
W'=
\begin{pmatrix}
0 & 20 & 0.1 & 0.1\\
20 & 0 & 0.1 & 0.1\\
0.1 & 0.1 & 0 & 5\\
0.1 & 0.1 & 5 & 0
\end{pmatrix},
$$
which increases all within–cluster similarities and decreases all between–cluster ones.

For $W'$ the second eigenvector has signs $+,-,+,-$, so spectral clustering outputs $\{a,c\},\{b,d\}$. Thus changing the metric in the manner required by Kleinberg’s consistency can change the spectral clustering. Standard (normalized or unnormalized) spectral clustering algorithms are not Kleinberg‑consistent (no natural spectral method is known to satisfy the axiom).

---

## GIVEN ANSWER (GA)

Consider the similarity matrices
$$W=
\begin{pmatrix}
0 & 1 & 1 & 1\\
1 & 0 & 1 & 1\\
1 & 1 & 0 & 1\\
1 & 1 & 1 & 0
\end{pmatrix}
\quad \text{and} \quad
W'=
\begin{pmatrix}
0 & 2 & 0.5 & 0.5\\
2 & 0 & 0.5 & 0.5\\
0.5 & 0.5 & 0 & 1\\
0.5 & 0.5 & 1 & 0
\end{pmatrix}.
$$
Both have the same non-zero eigenvalues and eigenvectors for the normalized Laplacian, so spectral clustering yields the same result. Yet $W'$ has larger between-cluster distances and smaller within-cluster distances for any reasonable notion of distance.

### Caveats on GA’s Example and Generalization

* Metric validity: Kleinberg’s axiom is stated for metrics $(S,\rho)$ and transformed metrics $\rho'$ satisfying within-cluster contraction and between-cluster expansion. GA constructs similarity matrices $W,W'$ directly and does not show that there exist valid metrics $\rho,\rho'$ (satisfying non-negativity, symmetry, identity, triangle inequality) that map to $W,W'$ via a fixed similarity-construction rule (e.g., a Gaussian kernel with fixed $\sigma$). Without such a mapping, the example may not meet the axiom’s conditions.

* Fixed construction rule: To assess consistency, the algorithm must be run under the same metric-to-similarity mapping before and after the transformation. GA does not fix a mapping $W=f(\rho)$ and verify $W'=f(\rho')$ for a valid $\rho'$ obeying the axiom’s inequalities.

* Scope of claim: The statement “standard spectral algorithms are not Kleinberg-consistent” is broadly plausible, but GA’s single constructed case does not constitute a rigorous proof. A formal demonstration requires either:
  * a general argument that, for any valid $(S,\rho)$ producing clustering $\mathcal{C}$, there exists a metric $\rho'$ satisfying the axiom’s inequalities such that spectral clustering changes the output, under a fixed $f(\cdot)$; or
  * an explicit family of metric transformations and corresponding spectra showing instability across the allowed transformations.

* What would suffice: A rigorous counterexample would (i) specify $f(\rho)$ (e.g., $W_{ij}=\exp(-\rho(x_i,x_j)^2/2\sigma^2)$ with fixed $\sigma$), (ii) construct $\rho,\rho'$ that satisfy the axiom’s inequalities and are valid metrics, (iii) show $W=f(\rho)$ and $W'=f(\rho')$, and (iv) demonstrate the spectral pipeline produces different clusterings.

## Comparison: RA vs. GA

* RA (objective-focused):
  * Claims unnormalized MinCut and RatioCut satisfy Kleinberg-consistency because intra-cluster similarities do not affect the objective, while Ncut fails (volume normalization can absorb clusters).
  * Emphasizes cut objectives directly on the graph without spectral relaxation or downstream k-means.

* GA (pipeline-focused counterexample):
  * Shows standard spectral pipeline (similarity $\to$ Laplacian $\to$ eigenvectors $\to$ k-means) violates consistency via a constructive matrix example; highlights sensitivity of eigenvectors and k-means.
  * Notes both normalized and unnormalized spectral variants are not Kleinberg-consistent in practice.

* Reconciliation:
  * RA’s claim pertains to the pure combinatorial cut objective under a fixed $k$ and direct partition search (no spectral relaxation, no k-means).
  * GA addresses “natural spectral clustering” implementations that relax cut optimization and use embeddings; these commonly fail the axiom due to spectral/k-means instability.
  * Thus, “spectral clustering” as commonly implemented is not Kleinberg-consistent, while certain cut objectives (RatioCut/MinCut) can satisfy the axiom in their idealized, non-relaxed form.

## Another Perspective: Cost-Function vs. Algorithmic Pipeline

* Cost-function view:
  * If the clustering is defined as the exact minimizer of a cut objective (MinCut/RatioCut) with fixed $k$, and the metric change only decreases intra-cluster edges and increases inter-cluster edges, the original partition’s cost cannot worsen relative to alternatives, supporting consistency in the RA sense.
* Pipeline view:
  * Spectral relaxation + k-means introduces non-monotone transformations (kernel mapping, eigenvector rotations, center reassignment), breaking the axiom even under “helpful” metric changes.

### Practical note

- Consistency must be checked in the metric domain with a fixed metric-to-similarity construction. Similarity-level modifications alone do not guarantee the axiom’s premises are satisfied. A general proof of non-consistency for spectral methods should either provide metric-based counterexamples under a fixed mapping or a theoretical instability result for the spectral relaxation + k-means pipeline across all allowed metric transformations.

### Correction and Clarification to RA

* Formal requirement: Kleinberg-consistency requires that for the clustering $\mathcal{C}$ produced on $(S,\rho)$, every metric $\rho'$ satisfying
  * within-cluster contraction: $\rho'(x,y)\le \rho(x,y)$ for $x,y$ in the same $C\in\mathcal{C}$,
  * between-cluster expansion: $\rho'(x,y)\ge \rho(x,y)$ for $x,y$ in different clusters,
  must yield the same clustering $\mathcal{C}$ when the algorithm is rerun on $(S,\rho')$.

* Objective-independence is not sufficient: Even if a cut objective (e.g., MinCut/RatioCut) does not explicitly include intra-cluster edges, changing inter-cluster distances (or similarities) can still re-rank candidate cuts and alter the optimal partition. Kleinberg-consistency quantifies a universal invariance across all allowed $\rho'\,$—not just some modifications.

* Metric validity: The axiom operates on metrics. Claims of consistency must ensure that the transformed pairwise values arise from valid metrics (non-negativity, identity, symmetry, triangle inequality). Similarity-weight changes do not automatically correspond to metric transformations.

* Counterexample sketch (RatioCut/MinCut): Consider three compact groups $A,B,C$ with cut weights $w(A,B)\approx w(A,C)\ll w(B,C)$. The optimal two-way cut may separate $A$ from $B\cup C$. After a consistent modification that expands between-cluster distances in a way that disproportionately increases $w(A,B)$ relative to $w(A,C)$, the optimal cut can flip to separating $B$ from $A\cup C$, violating consistency. This occurs despite intra-cluster edges being irrelevant to the cost.

* Conclusion: The RA assertion that unnormalized MinCut and RatioCut are Kleinberg-consistent “because intra-cluster similarities do not influence the objective” is incomplete and generally incorrect. Without a formal proof over all valid metric transformations, the claim is unsupported.
