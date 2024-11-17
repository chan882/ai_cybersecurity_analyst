import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# Load and preprocess data
df = pd.read_csv('network_traffic.csv')
X = df[['packet_size']]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the Isolation Forest model
model = IsolationForest(contamination=0.05, random_state=42)
df['anomaly'] = model.fit_predict(X_scaled)
df['anomaly'] = df['anomaly'].apply(lambda x: 1 if x == -1 else 0)

# Save the results
df.to_csv('network_traffic_with_anomalies.csv', index=False)  # Removed line_terminator
print("Anomaly detection results saved to 'network_traffic_with_anomalies.csv'")



