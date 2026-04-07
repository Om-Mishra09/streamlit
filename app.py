import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Linear Regression Visualizer", layout="wide")

# Title
st.title("📈 Simple Linear Regression Visualizer")

st.markdown("Interactively explore how slope and intercept affect a regression line.")

# Sidebar controls
st.sidebar.header("⚙️ Controls")

num_points = st.sidebar.slider("Number of Data Points", 10, 200, 50)
slope = st.sidebar.slider("Slope (m)", -10.0, 10.0, 1.0)
intercept = st.sidebar.slider("Intercept (b)", -20.0, 20.0, 0.0)
noise = st.sidebar.slider("Noise Level", 0.0, 20.0, 5.0)

# Generate data
np.random.seed(42)
X = np.linspace(0, 10, num_points)
y = slope * X + intercept + np.random.randn(num_points) * noise

# Plot
fig, ax = plt.subplots()

ax.scatter(X, y, label="Data Points")
ax.plot(X, slope * X + intercept, color='red', label="Regression Line")

ax.set_xlabel("X")
ax.set_ylabel("y")
ax.set_title("Linear Regression Fit")
ax.legend()

# Layout
col1, col2 = st.columns([3, 1])

with col1:
    st.pyplot(fig)

with col2:
    st.subheader("📌 Model Info")
    st.write(f"**Equation:** y = {slope:.2f}x + {intercept:.2f}")
    st.metric("Data Points", num_points)
    st.metric("Noise Level", noise)

# Footer
st.markdown("---")
st.caption("Built with Streamlit • Linear Regression Demo")