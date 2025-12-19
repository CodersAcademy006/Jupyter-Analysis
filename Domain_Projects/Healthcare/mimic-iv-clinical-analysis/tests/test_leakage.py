import unittest
import pandas as pd
from src.features.windowing import create_sliding_windows

class TestLeakage(unittest.TestCase):
    def test_no_future_leakage(self):
        df = pd.DataFrame({
            'subject_id': [1, 1, 1],
            'time': [0, 1, 2],
            'value': [10, 12, 14]
        })
        windowed = create_sliding_windows(df, window_size=2, time_col='time')
        # For each subject, ensure window's max time does not exceed original max time
        for subject in df['subject_id'].unique():
            max_time = df[df['subject_id'] == subject]['time'].max()
            self.assertTrue((windowed[windowed['subject_id'] == subject]['time'] <= max_time).all())
if __name__ == '__main__':
    unittest.main()
