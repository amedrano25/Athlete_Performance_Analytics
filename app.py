import streamlit as st
import pandas as pd
from src.performance_analyzer import plot_trends
from src.model_trainer import predict_future
import os

st.set_page_config(page_title="Athlete Performance Analytics", layout="wide")
st.title("⚾ Athlete Performance Analytics")

uploaded_file = st.file_uploader("Upload Session Data (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=['Date'])
    st.write("### 📊 Raw Data", df)
    
    # Plot trends
    chart_path = os.path.join("reports", "streamlit_trends.png")
    plot_trends(df, chart_path)
    st.image(chart_path, caption="Performance Trends")
    
    # Predict future performance
    future_speed = predict_future(df, 'PitchSpeed', 30)
    st.success(f"📈 Predicted Pitch Speed in 30 days: {future_speed:.2f} mph")
