import matplotlib.pyplot as plt
import seaborn as sns

def plot_trends(df, output_path):
    """Plot trends for pitch speed and accuracy"""
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['PitchSpeed'], marker='o', label='Pitch Speed (mph)')
    plt.plot(df['Date'], df['Accuracy'], marker='x', label='Accuracy')
    plt.xlabel('Date')
    plt.title('Athlete Performance Over Time')
    plt.legend()
    plt.savefig(output_path)
    plt.close()
