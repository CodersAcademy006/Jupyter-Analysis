import pandas as pd

def create_sliding_windows(df: pd.DataFrame, window_size: int, time_col: str) -> pd.DataFrame:
    """Generate time windows for each patient."""
    # Explicit rolling window to prevent future leakage
    results = []
    numeric_cols = [col for col in df.select_dtypes(include=['number']).columns if col not in ['subject_id', time_col]]
    for subject_id, group in df.groupby('subject_id'):
        group = group.sort_values(time_col)
        for i in range(window_size - 1, len(group)):
            window = group.iloc[i - window_size + 1:i + 1]
            row = {
                'subject_id': subject_id,
                time_col: window[time_col].max()
            }
            for col in numeric_cols:
                row[f'{col}_mean'] = window[col].mean()
                row[f'{col}_max'] = window[col].max()
            results.append(row)
    return pd.DataFrame(results)
