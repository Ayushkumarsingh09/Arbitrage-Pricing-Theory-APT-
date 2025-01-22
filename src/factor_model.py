import pandas as pd
import numpy as np

class FactorModel:
    def __init__(self, data):
        self.data = data

    def estimate_factor_betas(self, stock_returns, factor_returns):
        factor_betas = np.linalg.lstsq(factor_returns, stock_returns, rcond=None)[0]
        return factor_betas

    def calculate_factor_risks(self, factor_returns):
        factor_risks = factor_returns.var(axis=0)
        return factor_risks
