import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestNeighbors

def propensity_score_matching(df, treatment_col, covariate_cols):
    """Match treated vs untreated using propensity scores."""
    X = df[covariate_cols]
    y = df[treatment_col]
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    scores = model.predict_proba(X)[:, 1]
    df['propensity_score'] = scores
    treated = df[df[treatment_col] == 1]
    untreated = df[df[treatment_col] == 0]
    nn = NearestNeighbors(n_neighbors=1)
    nn.fit(untreated[['propensity_score']])
    matched_indices = nn.kneighbors(treated[['propensity_score']], return_distance=False)
    matched_untreated = untreated.iloc[matched_indices.flatten()]
    return treated, matched_untreated

def estimate_ate(treated, matched_untreated, outcome_col):
    """Estimate average treatment effect (ATE)."""
    ate = treated[outcome_col].mean() - matched_untreated[outcome_col].mean()
    return ate
