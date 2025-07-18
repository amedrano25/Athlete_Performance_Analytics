def generate_text_report(prediction, output_path):
    """Generate a simple text report"""
    with open(output_path, 'w') as f:
        f.write(f"Predicted pitch speed in 30 days: {prediction:.2f} mph\n")
