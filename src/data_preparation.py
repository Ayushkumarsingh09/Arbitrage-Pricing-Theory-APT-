import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(data):
    data = data.dropna()
    return data

def split_data(data, features, target):
    X = data[features]
    y = data[target]
    return X, y
