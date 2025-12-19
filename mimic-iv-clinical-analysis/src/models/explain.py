import shap

def compute_shap_values(model, X):
    """Compute SHAP values for model explainability."""
    explainer = shap.Explainer(model, X)
    shap_values = explainer(X)
    return shap_values
