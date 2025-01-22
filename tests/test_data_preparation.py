import unittest
import pandas as pd
from src.data_preparation import preprocess_data

class TestDataPreparation(unittest.TestCase):
    def test_preprocess_data(self):
        data = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
        clean_data = preprocess_data(data)
        self.assertEqual(clean_data.isnull().sum().sum(), 0)
