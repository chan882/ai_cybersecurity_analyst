import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Parameters
num_records = 10000
start_time = datetime.now()

# Generate synthetic data
data = {
    'timestamp': [start_time + timedelta(seconds=i) for i in range(num_records)],
    'source_ip': np.random.choice(['192.168.1.1', '192.168.1.2', '10.0.0.1', '172.16.0.1'], num_records),
    'destination_ip': np.random.choice(['192.168.1.100', '192.168.1.101', '10.0.0.2', '172.16.0.2'], num_records),
    'packet_size': np.random.randint(20, 1500, num_records),
    'malicious': np.random.choice([0, 1], num_records, p=[0.95, 0.05])  # 5% anomaly rate
}

df = pd.DataFrame(data)
df.to_csv('network_traffic.csv', index=False)  # Removed line_terminator
print("Synthetic network traffic data saved to 'network_traffic.csv'")




