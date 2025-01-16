import unittest
from src.visualization import plot_expected_returns, plot_factor_risks

class TestVisualization(unittest.TestCase):
    def test_plot_expected_returns(self):
        # Dummy test to ensure no exceptions
        expected_returns = [0.1, 0.2, 0.15]
        try:
            plot_expected_returns(expected_returns)
        except Exception as e:
            self.fail(f"plot_expected_returns failed with exception: {e}")

    def test_plot_factor_risks(self):
        # Dummy test to ensure no exceptions
        factor_risks = [0.05, 0.03]
        try:
            plot_factor_risks(factor_risks)
        except Exception as e:
            self.fail(f"plot_factor_risks failed with exception: {e}")
