import unittest
from src.apt_calculator import APTCalculator

class TestAPTCalculator(unittest.TestCase):
    def test_calculate_expected_return(self):
        factor_betas = [0.5, 0.3]
        factor_risks = [0.02, 0.03]
        risk_free_rate = 0.01
        calculator = APTCalculator(factor_betas, factor_risks, risk_free_rate)
        result = calculator.calculate_expected_return()
        expected = 0.01 + (0.5 * 0.02) + (0.3 * 0.03)
        self.assertAlmostEqual(result, expected)
