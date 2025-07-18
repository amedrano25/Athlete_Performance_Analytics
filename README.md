# ⚾ Athlete Performance Analytics

A Python and Streamlit app to analyze training data, visualize athlete performance trends, and predict future improvements using machine learning.

## 📦 Features
- Analyze session data (pitch speed, accuracy, fatigue)
- Visualize trends (line charts)
- Predict future performance with linear regression
- CLI tool and interactive Streamlit web app

## 🚀 Live Demo (when deployed)
👉 [Try the App](https://amedrano25-athlete-performance-analytics-app-f85ajs.streamlit.app/)

## 📂 Project Structure
```
athlete-performance-analytics/
│
├── app.py                     <-- Streamlit web app
├── data/
│   ├── sessions.csv           <-- Training session data
│
├── reports/
│   ├── performance_report.pdf
│
├── src/
│   ├── data_loader.py
│   ├── performance_analyzer.py
│   ├── model_trainer.py
│   ├── report_generator.py
│
├── requirements.txt
└── README.md
```

## 🛠 Tech Stack
- Python: pandas, numpy, matplotlib, scikit-learn
- Streamlit: Interactive dashboard

## 🚀 Getting Started
### Install dependencies
```bash
pip install -r requirements.txt
```

### Run CLI Tool
```bash
python src/main.py
```

### Run Web App
```bash
streamlit run app.py
```

---
