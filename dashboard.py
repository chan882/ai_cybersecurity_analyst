import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('network_traffic_with_anomalies.csv')

st.title("Cybersecurity Anomaly Detection Dashboard")

# Display raw data
st.subheader("Raw Network Traffic Data")
st.dataframe(df)

# Traffic over time
st.subheader("Traffic Volume Over Time")
fig1 = px.line(df, x='timestamp', y='packet_size', title='Traffic Volume Over Time')
st.plotly_chart(fig1)

# Source vs Destination IP mapping
st.subheader("Source and Destination IPs")
fig2 = px.histogram(df, x='source_ip', color='destination_ip', title='Source to Destination IP Mapping')
st.plotly_chart(fig2)

# Malicious traffic
st.subheader("Anomalous Traffic")
anomalies = df[df['malicious'] == 1]
st.write(f"Number of anomalies detected: {len(anomalies)}")
st.dataframe(anomalies)

if len(anomalies) > 0:
    st.subheader("Anomalous Traffic Visualized")
    fig3 = px.scatter(anomalies, x='timestamp', y='packet_size', color='source_ip', title='Anomalous Traffic')
    st.plotly_chart(fig3)
