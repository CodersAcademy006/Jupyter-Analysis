import shap
import matplotlib.pyplot as plt

def plot_shap_beeswarm(shap_values, feature_names):
    """Plot SHAP beeswarm plot."""
    shap.summary_plot(shap_values, feature_names=feature_names, plot_type='dot')
