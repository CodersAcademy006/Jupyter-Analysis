import pandas as pd

def extract_data(file_path: str) -> pd.DataFrame:
    """Load raw CSV/SQL data."""
    return pd.read_csv(file_path)
