import pandas as pd

def load_session_data(file_path):
    """Load training session data from CSV"""
    return pd.read_csv(file_path, parse_dates=['Date'])
