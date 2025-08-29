"""
Application library for Stirling numbers and Bell polynomials.
Provides implementations for clustering, partitioning, and optimization.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from .stirling_core import StirlingComputation, BellPolynomials, ParameterEstimation

class StirlingPartitioning:
    """Class implementing the Stirling partitioning algorithm for clustering."""
    
    def __init__(self, min_k=2, max_k=None, use_bell_polynomials=True):
        """Initialize the partitioning algorithm.
        
        Args:
            min_k (int): Minimum number of clusters to consider
            max_k (int, optional): Maximum number of clusters to consider
            use_bell_polynomials (bool): Whether to use Bell polynomials for parameter estimation
        """
        self.min_k = min_k
        self.max_k = max_k
        self.use_bell_polynomials = use_bell_polynomials
        
    def fit(self, data, normalize=True):
        """Apply the Stirling partitioning algorithm to find optimal clustering.
        
        Args:
            data (numpy.ndarray): Data matrix (samples × features)
            normalize (bool): Whether to normalize the data
            
        Returns:
            dict: Results including optimal k, labels, parameters, etc.
        """
        n_samples, n_features = data.shape
        
        # Set max_k if not provided
        if self.max_k is None:
            self.max_k = min(15, int(np.sqrt(n_samples)))
        
        # Normalize data if requested
        if normalize:
            scaler = StandardScaler()
            data = scaler.fit_transform(data)
        
        results = []
        
        # Try different cluster counts
        for k in range(self.min_k, self.max_k + 1):
            # Apply k-means clustering
            kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
            labels = kmeans.fit_predict(data)
            centroids = kmeans.cluster_centers_
            
            # Calculate silhouette score
            sil_score = silhouette_score(data, labels) if k > 1 else 0.0
            
            # Standard metrics: within-cluster distances and between-cluster distances
            if not self.use_bell_polynomials:
                # Traditional approach
                affinity = np.mean([
                    np.mean(np.linalg.norm(data[labels == i] - centroids[i], axis=1))
                    for i in range(k)
                ])
                
                if k > 1:
                    centroid_distances = [
                        np.linalg.norm(centroids[i] - centroids[j])
                        for i in range(k) for j in range(i+1, k)
                    ]
                    cost = np.mean(centroid_distances)
                else:
                    cost = 0.0
            else:
                # Bell polynomial approach
                bell_values = []
                for i in range(k):
                    cluster_data = data[labels == i]
                    if len(cluster_data) > 1:
                        b_2_1 = BellPolynomials.multivariate_bell(2, 1, cluster_data)
                        b_2_2 = BellPolynomials.multivariate_bell(2, 2, cluster_data)
                        bell_values.append((b_2_1, b_2_2))
                
                if bell_values:
                    # Average across clusters
                    avg_b_2_1 = np.mean([b[0] for b in bell_values], axis=0)
                    avg_b_2_2 = np.mean([b[1] for b in bell_values], axis=0)
                    
                    # Estimate affinity and cost using Bell polynomials
                    affinity = -np.linalg.norm(avg_b_2_1)
                    cost = np.linalg.norm(avg_b_2_2)
                else:
                    # Fallback to traditional method
                    affinity = np.mean([
                        np.mean(np.linalg.norm(data[labels == i] - centroids[i], axis=1))
                        for i in range(k)
                    ])
                    if k > 1:
                        centroid_distances = [
                            np.linalg.norm(centroids[i] - centroids[j])
                            for i in range(k) for j in range(i+1, k)
                        ]
                        cost = np.mean(centroid_distances)
                    else:
                        cost = 0.0
            
            # Store results
            results.append({
                'k': k,
                'affinity': affinity,
                'cost': cost,
                'silhouette': sil_score,
                'labels': labels,
                'centroids': centroids
            })
        
        # Find best result based on silhouette score
        best_result = max(results, key=lambda r: r['silhouette'])
        optimal_k = best_result['k']
        optimal_labels = best_result['labels']
        
        # Estimate parameters (a, b) using robust regression
        ks = np.array([r['k'] for r in results])
        affinities = np.array([r['affinity'] for r in results])
        costs = np.array([r['cost'] for r in results])
        
        from sklearn.linear_model import RANSACRegressor
        a_model = RANSACRegressor(random_state=42).fit(ks.reshape(-1, 1), affinities)
        b_model = RANSACRegressor(random_state=42).fit(ks.reshape(-1, 1), costs)
        
        a_fit = [a_model.estimator_.coef_[0], a_model.estimator_.intercept_]
        b_fit = [b_model.estimator_.coef_[0], b_model.estimator_.intercept_]
        
        # Store in result dictionary
        final_result = {
            'optimal_k': optimal_k,
            'labels': optimal_labels,
            'a_param': a_fit[0],
            'b_param': b_fit[0],
            'silhouette': best_result['silhouette'],
            'centroids': best_result['centroids'],
            'all_results': results
        }
        
        return final_result
    
    def plot_silhouette_curve(self, results, save_path=None):
        """Plot silhouette scores for different k values.
        
        Args:
            results (dict): Results from fit() method
            save_path (str, optional): Path to save the plot
        """
        all_results = results['all_results']
        ks = [r['k'] for r in all_results]
        silhouettes = [r['silhouette'] for r in all_results]
        
        plt.figure(figsize=(10, 6))
        plt.plot(ks, silhouettes, 'o-', linewidth=2, markersize=8)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.xlabel('Number of Clusters (k)')
        plt.ylabel('Silhouette Score')
        plt.title('Cluster Quality vs. Number of Clusters')
        
        # Highlight optimal k
        optimal_k = results['optimal_k']
        optimal_idx = ks.index(optimal_k)
        plt.scatter([optimal_k], [silhouettes[optimal_idx]], color='red', s=150,
                   label=f'Optimal k={optimal_k}', zorder=10, edgecolor='black')
        plt.legend()
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
            
        plt.close()
    
    def plot_parameter_space(self, a_param, b_param, save_path=None):
        """Plot the estimated parameters in the (a,b) parameter space.
        
        Args:
            a_param (float): Estimated a parameter
            b_param (float): Estimated b parameter
            save_path (str, optional): Path to save the plot
        """
        plt.figure(figsize=(8, 8))
        
        # Define special points in the parameter space
        special_points = {
            'Stirling 1st kind': (1, 0),
            'Stirling 2nd kind': (0, 1),
            'Lah numbers': (1, 1),
            'Exp-Log inverse': (1, -1),
            'Geometric-Alternating': (0, -1)
        }
        
        # Plot special points
        for name, (a, b) in special_points.items():
            plt.scatter(a, b, s=100, label=name)
        
        # Plot estimated parameters
        plt.scatter(a_param, b_param, s=150, color='red', 
                   label=f'Estimated: ({a_param:.2f}, {b_param:.2f})', 
                   zorder=10, edgecolor='black')
        
        # Add grid and labels
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        plt.xlabel('a (Affinity)')
        plt.ylabel('b (Barrier)')
        plt.title('Generalized Stirling Parameter Space')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
            
        plt.close()


class InverseFunctionEstimation:
    """Class for estimating inverse function relationships using Stirling transforms."""
    
    def __init__(self):
        """Initialize the inverse function estimator."""
        pass
    
    def estimate_inverse_function(self, f_coeffs, degree, a=None, b=None):
        """Estimate the coefficients of the inverse function.
        
        Args:
            f_coeffs (list): Coefficients of the function f(x)
            degree (int): Degree of the inverse function approximation
            a (float, optional): Parameter a (if known)
            b (float, optional): Parameter b (if known)
            
        Returns:
            list: Estimated coefficients of the inverse function g(x)
        """
        # Ensure we have enough coefficients
        if len(f_coeffs) < 2:
            raise ValueError("Need at least 2 coefficients")
        
        # Normalize to ensure f_0 = 0, f_1 ≠ 0
        if f_coeffs[0] != 0:
            f_coeffs = np.array(f_coeffs) - f_coeffs[0]
        
        # If parameters not provided, guess common values
        if a is None or b is None:
            # Check common patterns
            if all(np.isclose(f_coeffs[i], 1) for i in range(1, min(len(f_coeffs), 4))):
                # Likely exp(x)-1, use (1,-1)
                a = 1.0
                b = -1.0
            elif np.isclose(f_coeffs[1], 1) and all(np.isclose(f_coeffs[i], 1) for i in range(2, min(len(f_coeffs), 4))):
                # Likely x/(1-x), use (0,-1)
                a = 0.0
                b = -1.0
            else:
                # Default values
                a = 1.0
                b = 0.0
        
        # Initialize result with g_0 = 0 and g_1 = 1/f_1
        g_coeffs = np.zeros(degree + 1)
        g_coeffs[1] = 1.0 / f_coeffs[1]
        
        # Compute generalized Stirling numbers
        stirling = StirlingComputation(a, b)
        
        # Build system of equations for g_2, g_3, ..., g_degree
        for n in range(2, degree + 1):
            # This is derived from the condition g(f(x)) = x
            # We need the coefficient of x^n in g(f(x)) to be 0 for n > 1
            
            # This is a simplified approach; a more rigorous method would use
            # the complete Bell polynomial formulation for function composition
            
            sum_term = 0
            for k in range(1, n):
                coef = 0
                for j in range(k, n+1):
                    # Use Stirling numbers to compute the coefficient
                    s = stirling.compute(j, k)
                    if s != 0:
                        prod_term = 1
                        for i in range(1, j+1):
                            if i <= len(f_coeffs) - 1:
                                prod_term *= f_coeffs[i]
                        coef += s * prod_term
                sum_term += g_coeffs[k] * coef
            
            # Set g_n to cancel out the sum
            g_coeffs[n] = -sum_term / f_coeffs[1]**n
        
        return g_coeffs


class ClusteringReport:
    """Class for generating reports on clustering results."""
    
    def __init__(self, title="Stirling Partitioning Analysis", output_dir="results"):
        """Initialize the report generator.
        
        Args:
            title (str): Report title
            output_dir (str): Directory for output files
        """
        self.title = title
        self.output_dir = output_dir
        
        # Create output directory if it doesn't exist
        import os
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def generate_html(self, results, feature_names=None, sample_data=None, save_path=None):
        """Generate an HTML report for clustering results.
        
        Args:
            results (dict): Results from StirlingPartitioning.fit()
            feature_names (list, optional): Names of the features
            sample_data (pandas.DataFrame, optional): Sample data to display
            save_path (str, optional): Path to save the HTML file
            
        Returns:
            str: HTML content
        """
        # Extract parameters from results
        optimal_k = results['optimal_k']
        a_param = results['a_param']
        b_param = results['b_param']
        silhouette = results['silhouette']
        
        # Interpret parameters
        if a_param < -0.5:
            a_interp = "Strong affinity (elements strongly attracted to groups)"
        elif a_param < 0:
            a_interp = "Moderate affinity (elements moderately attracted to groups)"
        elif a_param < 0.5:
            a_interp = "Weak affinity (elements weakly attracted to groups)"
        else:
            a_interp = "Negative affinity (elements repel from groups)"
            
        if b_param < -0.5:
            b_interp = "Negative barrier (easy to form new groups)"
        elif b_param < 0:
            b_interp = "Low barrier (moderately easy to form new groups)"
        elif b_param < 0.5:
            b_interp = "Moderate barrier (some resistance to new groups)"
        else:
            b_interp = "High barrier (difficult to form new groups)"
        
        # Sample data HTML
        sample_html = ""
        if sample_data is not None:
            if hasattr(sample_data, 'to_html'):
                sample_html = f"<h2>Sample Data</h2>{sample_data.head(10).to_html()}"
            else:
                sample_html = "<h2>Sample Data</h2><p>Data provided but not in DataFrame format</p>"
        
        # Create HTML content
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{self.title}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
                h1, h2 {{ color: #2c3e50; }}
                .summary {{ background-color: #f8f9fa; padding: 20px; border-radius: 5px; }}
                .interpretation {{ background-color: #e8f4f8; padding: 15px; border-radius: 5px; margin-top: 20px; }}
                table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: center; }}
                th {{ background-color: #f2f2f2; }}
                img {{ max-width: 100%; height: auto; margin: 20px 0; }}
            </style>
        </head>
        <body>
            <h1>{self.title}</h1>
            
            <div class="summary">
                <h2>Clustering Results</h2>
                <ul>
                    <li>Optimal number of clusters: <strong>{optimal_k}</strong></li>
                    <li>Affinity parameter (a): <strong>{a_param:.4f}</strong></li>
                    <li>Barrier parameter (b): <strong>{b_param:.4f}</strong></li>
                    <li>Silhouette score: <strong>{silhouette:.4f}</strong></li>
                </ul>
            </div>
            
            <div class="interpretation">
                <h2>Parameter Interpretation</h2>
                <p><strong>Affinity parameter (a = {a_param:.4f}):</strong> {a_interp}</p>
                <p><strong>Barrier parameter (b = {b_param:.4f}):</strong> {b_interp}</p>
                <p><strong>Overall interpretation:</strong> This dataset exhibits {a_interp.lower()} and {b_interp.lower()}.</p>
            </div>
            
            <h2>Visualizations</h2>
            <p>See the saved visualization files in the results directory.</p>
            
            {sample_html}
            
            <div class="footer">
                <p>Generated using the Generalized Stirling Partitioning Algorithm</p>
            </div>
        </body>
        </html>
        """
        
        # Save HTML if path provided
        if save_path:
            with open(save_path, 'w') as f:
                f.write(html)
        
        return html
