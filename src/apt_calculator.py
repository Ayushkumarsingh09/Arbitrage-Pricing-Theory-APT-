import numpy as np

class APTCalculator:
    def __init__(self, factor_betas, factor_risks, risk_free_rate):
        self.factor_betas = factor_betas
        self.factor_risks = factor_risks
        self.risk_free_rate = risk_free_rate

    def calculate_expected_return(self):
        risk_premium = np.dot(self.factor_betas, self.factor_risks)
        expected_return = self.risk_free_rate + risk_premium
        return expected_return
