import pandas as pd
from sklearn.impute import SimpleImputer

def forward_fill(df: pd.DataFrame) -> pd.DataFrame:
    """Forward fill missing values."""
    return df.ffill()

def gaussian_impute(df: pd.DataFrame) -> pd.DataFrame:
    """Impute missing values using Gaussian process (placeholder: mean imputation)."""
    numeric_cols = df.select_dtypes(include=['number']).columns
    imputer = SimpleImputer(strategy='mean')
    df[numeric_cols] = imputer.fit_transform(df[numeric_cols])
    return df
