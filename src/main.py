from data_loader import load_session_data
from performance_analyzer import plot_trends
from model_trainer import predict_future
from report_generator import generate_text_report
import os

if __name__ == "__main__":
    file_path = os.path.join('data', 'sessions.csv')
    df = load_session_data(file_path)
    
    # Plot trends
    chart_path = os.path.join('reports', 'performance_trends.png')
    plot_trends(df, chart_path)
    
    # Predict future performance
    prediction = predict_future(df, 'PitchSpeed', days_ahead=30)
    
    # Generate report
    report_path = os.path.join('reports', 'performance_report.txt')
    generate_text_report(prediction, report_path)
    
    print("✅ Analysis complete. Charts and report saved in /reports")
