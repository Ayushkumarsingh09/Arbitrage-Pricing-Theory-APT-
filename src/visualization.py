import matplotlib.pyplot as plt

def plot_expected_returns(expected_returns):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(expected_returns)), expected_returns, color='blue')
    plt.xlabel('Assets')
    plt.ylabel('Expected Returns')
    plt.title('Expected Returns by Asset')
    plt.show()

def plot_factor_risks(factor_risks):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(factor_risks)), factor_risks, color='green')
    plt.xlabel('Factors')
    plt.ylabel('Risk Contribution')
    plt.title('Risk Contribution by Factor')
    plt.show()

