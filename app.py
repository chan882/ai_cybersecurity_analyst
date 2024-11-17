from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def dashboard():
    try:
        # Load data
        df = pd.read_csv('network_traffic_with_anomalies.csv')
        anomalies = df[df['anomaly'] == 1]

        # Pass anomaly data to the dashboard
        return render_template('dashboard.html', data=anomalies.to_dict(orient='records'))
    except FileNotFoundError:
        return "Error: 'network_traffic_with_anomalies.csv' not found. Please generate it first."
    except pd.errors.ParserError as e:
        return f"Error parsing CSV file: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)


