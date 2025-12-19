import unittest
import pandas as pd
from src.features.windowing import create_sliding_windows
from src.features.aggregation import aggregate_features

class TestFeatureEngineering(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'subject_id': [1, 1, 1, 2, 2],
            'time': [0, 1, 2, 0, 1],
            'value': [10, 12, 14, 20, 22]
        })
    def test_windowing(self):
        windowed = create_sliding_windows(self.df, window_size=2, time_col='time')
        self.assertTrue('subject_id' in windowed.columns)
    def test_aggregation(self):
        agg = aggregate_features(self.df, value_col='value')
        self.assertTrue('mean' in agg.columns)
        self.assertTrue('max' in agg.columns)
        self.assertTrue('slope' in agg.columns)
if __name__ == '__main__':
    unittest.main()
