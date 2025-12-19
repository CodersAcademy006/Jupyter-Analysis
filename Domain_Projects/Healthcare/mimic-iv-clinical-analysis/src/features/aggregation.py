import pandas as pd
import numpy as np

def aggregate_features(window_df: pd.DataFrame, value_col: str, time_col: str = 'hours_in') -> pd.DataFrame:
    """Compute mean, max, slope for each window."""
    # Aggregate hospital_expire_flag if present
    if 'hospital_expire_flag' in window_df.columns:
        window_df['hospital_expire_flag'] = window_df['hospital_expire_flag'].max()
    # Only aggregate if value_col exists
    if value_col in window_df.columns:
        window_df[f'{value_col}_mean'] = window_df[value_col].mean(skipna=True)
        window_df[f'{value_col}_max'] = window_df[value_col].max(skipna=True)
        if time_col in window_df.columns:
            window_df[f'{value_col}_slope'] = window_df[value_col].diff().fillna(0) / window_df[time_col].diff().fillna(1)
        else:
            window_df[f'{value_col}_slope'] = np.nan
    else:
        window_df[f'{value_col}_mean'] = np.nan
        window_df[f'{value_col}_max'] = np.nan
        window_df[f'{value_col}_slope'] = np.nan
    return window_df
