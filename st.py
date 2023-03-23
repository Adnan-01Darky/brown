import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Brownian Motion Simulation")

# Simulation parameters
num_particles = st.sidebar.slider("Number of particles", min_value=1, max_value=100, value=10)
num_steps = st.sidebar.slider("Number of steps", min_value=100, max_value=1000, step=100, value=500)
step_size = st.sidebar.slider("Step size", min_value=0.01, max_value=1.0, step=0.01, value=0.1)

# Set up the initial positions of the particles
initial_positions = np.zeros((num_particles, 2))

# Run the simulation
all_positions = []
for i in range(num_particles):
    positions = [initial_positions[i]]
    for j in range(num_steps):
        new_position = positions[-1] + step_size * np.random.randn(2)
        positions.append(new_position)
    all_positions.append(positions)

# Plot the results
fig, ax = plt.subplots(figsize=(8, 8))
for positions in all_positions:
    x = [pos[0] for pos in positions]
    y = [pos[1] for pos in positions]
    ax.plot(x, y)
ax.set_xlabel("X position")
ax.set_ylabel("Y position")
ax.set_title("Brownian Motion Simulation")
ax.set_aspect("equal")
st.pyplot(fig)