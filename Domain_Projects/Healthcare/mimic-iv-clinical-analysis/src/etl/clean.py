import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize columns, handle outliers."""
    # Example: Remove negative ages, fill missing categorical values
    df = df[df['age'] >= 0]
    df = df.fillna({'gender': 'Unknown'})
    return df
