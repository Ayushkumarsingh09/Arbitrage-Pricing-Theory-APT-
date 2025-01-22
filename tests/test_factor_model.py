import unittest
import numpy as np
import pandas as pd
from src.factor_model import FactorModel

class TestFactorModel(unittest.TestCase):
    def test_estimate_factor_betas(self):
        stock_returns = np.array([0.1, 0.2, 0.15])
        factor_returns = np.array([[0.05, 0.02], [0.03, 0.04], [0.06, 0.01]])
        model = FactorModel(None)
        betas = model.estimate_factor_betas(stock_returns, factor_returns)
        self.assertEqual(len(betas), 2)

    def test_calculate_factor_risks(self):
        factor_returns = pd.DataFrame([[0.05, 0.02], [0.03, 0.04], [0.06, 0.01]])
        model = FactorModel(None)
        risks = model.calculate_factor_risks(factor_returns)
        self.assertEqual(len(risks), 2)
