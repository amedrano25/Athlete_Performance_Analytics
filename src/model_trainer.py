from sklearn.linear_model import LinearRegression
import numpy as np

def predict_future(df, feature, days_ahead):
    """Predict future performance using linear regression"""
    df = df.copy()
    df['Day'] = (df['Date'] - df['Date'].min()).dt.days
    X = df[['Day']]
    y = df[feature]
    model = LinearRegression()
    model.fit(X, y)
    future_day = np.array([[df['Day'].max() + days_ahead]])
    predicted_value = model.predict(future_day)
    return predicted_value[0]
