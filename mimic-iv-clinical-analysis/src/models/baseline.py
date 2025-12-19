import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, average_precision_score

def train_logistic_regression(X: pd.DataFrame, y: pd.Series):
    """Train static Logistic Regression baseline."""
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    y_pred = model.predict_proba(X)[:, 1]
    auroc = roc_auc_score(y, y_pred)
    auprc = average_precision_score(y, y_pred)
    return model, auroc, auprc
