import unittest
import pandas as pd
from src.etl.extract import extract_data
from src.etl.clean import clean_data
from src.etl.impute import forward_fill, gaussian_impute

class TestETL(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'age': [25, -1, 30],
            'gender': ['M', None, 'F']
        })
    def test_clean(self):
        cleaned = clean_data(self.df)
        self.assertTrue((cleaned['age'] >= 0).all())
    def test_forward_fill(self):
        filled = forward_fill(self.df)
        self.assertFalse(filled.isnull().any().any())
    def test_gaussian_impute(self):
        imputed = gaussian_impute(self.df)
        numeric_cols = self.df.select_dtypes(include=['number']).columns
        self.assertFalse(imputed[numeric_cols].isnull().any().any())
if __name__ == '__main__':
    unittest.main()
