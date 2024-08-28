#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Explanation and Introduction
st.title(r"Euler's Formula and Planetary Motion")
st.markdown(r"""
Euler's formula, stated as $e^{ix} = \cos(x) + i\sin(x)$, is a fundamental relationship in mathematics that shows a deep connection between exponential functions, trigonometry, and complex numbers.
This relationship can be visualized as a circular motion in the complex plane. When we introduce time, this circular motion becomes a helical path.

In this app, we'll visualize the concept of planetary motion as observed from a time spiral, connecting the dots between how planets move and how time flows.
""")

# User Inputs
st.sidebar.header("User Inputs")
turns = st.sidebar.slider("Number of Turns (Years)", min_value=1, max_value=10, value=6, step=1)
points_per_turn = st.sidebar.slider("Points Per Year", min_value=20, max_value=100, value=70, step=10)
planet_offset_factor = st.sidebar.slider("Distance from Time Spiral", min_value=0.5, max_value=2.0, value=1.0, step=0.1)
animation_speed = st.sidebar.slider("Animation Speed (ms per frame)", min_value=10, max_value=100, value=30, step=5)

# Calculate the data for the spiral and planets
theta = np.linspace(0, 2 * np.pi * turns, points_per_turn * turns)
z = np.linspace(0, turns, points_per_turn * turns)

# Central Time Spiral (Sun's position in this analogy)
x_spiral = np.zeros_like(theta)
y_spiral = np.zeros_like(theta)

# Create the figure for the animation
fig = go.Figure()

# Precompute frames for better performance
frames = []

for i in range(0, len(theta), max(1, len(theta)//100)):
    frame_data = []
    
    # Time Spiral (Sun's position)
    frame_data.append(go.Scatter3d(x=x_spiral[:i+1], y=y_spiral[:i+1], z=z[:i+1], 
                                   mode='lines', line=dict(color='blue', width=4), name='Time Spiral'))

    # Planetary Orbits with markers
    colors = ['red', 'green', 'orange']
    for j in range(1, 4):  # Simulating 3 planets with distinct orbits
        radius = planet_offset_factor * j
        speed = 1 / j  # Simulate different orbital speeds for each planet
        
        x_planet = radius * np.cos(speed * theta[:i+1])
        y_planet = radius * np.sin(speed * theta[:i+1])
        z_planet = z[:i+1]

        frame_data.append(go.Scatter3d(x=x_planet, y=y_planet, z=z_planet, mode='lines+markers',
                                       line=dict(width=2, color=colors[j-1]), 
                                       marker=dict(size=4, color=colors[j-1]), 
                                       name=f'Planet {j}'))

    frames.append(go.Frame(data=frame_data, name=str(i)))

# Add the initial data (first frame)
fig.add_trace(go.Scatter3d(x=x_spiral[:1], y=y_spiral[:1], z=z[:1], 
                           mode='lines', line=dict(color='blue', width=4), name='Time Spiral'))

colors = ['red', 'green', 'orange']
for j in range(1, 4):
    radius = planet_offset_factor * j
    speed = 1 / j
    
    x_planet = radius * np.cos(speed * theta[:1])
    y_planet = radius * np.sin(speed * theta[:1])
    z_planet = z[:1]

    fig.add_trace(go.Scatter3d(x=x_planet, y=y_planet, z=z_planet, mode='lines+markers', 
                               line=dict(width=2, color=colors[j-1]), 
                               marker=dict(size=4, color=colors[j-1]), 
                               name=f'Planet {j}'))

# Configure layout and sliders for the animation
fig.update_layout(
    title="Time Spiral and Planetary Motion Visualization",
    scene=dict(
        xaxis_title='Real Part',
        yaxis_title='Imaginary Part',
        zaxis_title='Time (Years)',
        xaxis=dict(range=[-3, 3]),
        yaxis=dict(range=[-3, 3]),
        zaxis=dict(range=[0, turns]),
    ),
    updatemenus=[dict(type="buttons",
                      buttons=[dict(label="Play",
                                    method="animate",
                                    args=[None, {"frame": {"duration": animation_speed, "redraw": True},
                                                 "fromcurrent": True, "mode": "immediate"}]),
                               dict(label="Pause",
                                    method="animate",
                                    args=[[None], {"frame": {"duration": 0, "redraw": True},
                                                   "mode": "immediate"}])])],
    sliders=[dict(steps=[dict(method="animate",
                              args=[[f.name], {"frame": {"duration": animation_speed, "redraw": True},
                                               "mode": "immediate"}],
                              label=f.name) for f in frames],
                 active=0)]
)

# Add frames to the figure
fig.frames = frames

# Display the plot in Streamlit
st.plotly_chart(fig)

# Enhanced Mathematical Explanation Section
st.header("Mathematical Foundations of Euler's Formula and Planetary Motion")
st.markdown(r"""
### Introduction to $\pi$ and Its Significance

$\pi$ (Pi) is one of the most fundamental constants in mathematics, defined as the ratio of a circle's circumference to its diameter. It is an irrational number, approximately $3.14159$, and plays a crucial role in many areas of mathematics, especially those involving circles and periodic functions.

### Euler's Formula and $\pi$

Euler's formula, $e^{ix} = \cos(x) + i\sin(x)$, is a powerful equation that unifies exponential functions, trigonometry, and complex numbers. When $x = \pi$, the formula yields the famous and elegant **Euler's Identity**:

$$
e^{i\pi} + 1 = 0
$$

This identity is often celebrated as one of the most beautiful equations in mathematics because it connects five fundamental constants: $e$ (the base of natural logarithms), $i$ (the imaginary unit, $\sqrt{-1}$), $\pi$ (the fundamental constant related to circles), $1$ (the multiplicative identity), and $0$ (the additive identity).

### Intuition Behind Euler's Identity

Euler’s Identity, $e^{i\pi} + 1 = 0$, can be seen as both expansive and contractive at the same time, which mirrors the fundamental principles of how the universe operates.

#### Expansive Nature:
- **Exponential Growth and Motion:** The term $e^{ix}$ describes an exponential function that, in the complex plane, manifests as a rotation around the origin. This rotation is not static; it represents continuous motion, spiraling outward along the unit circle as $x$ increases. This motion can be thought of as an expansion—much like how the universe itself is expanding. The universe's expansion is characterized by galaxies moving away from each other, which can be seen as a manifestation of the exponential nature of growth.

#### Contractive Nature:
- **Convergence to a Point:** Despite the expansive nature of $e^{ix}$, when $x = \pi$, the complex exponential lands precisely at $-1$ on the real axis. Adding $1$ to this value contracts it back to zero. This contraction to a singular point represents a form of convergence, where seemingly boundless expansion eventually collapses into a single, unified outcome. This is analogous to theoretical models of the universe that predict a possible future contraction, such as the "Big Crunch," where the universe might ultimately reverse its expansion and collapse back into a singularity.

#### Why This Matters:
- **Balance of Forces:** Euler’s Identity embodies the balance of expansion and contraction—forces that are fundamental to the universe. In the context of cosmology, these forces could be likened to the interplay between dark energy (which drives expansion) and gravity (which can cause contraction). This delicate balance is captured in a simple mathematical expression, demonstrating that the universe’s complexity can be described through elegant, underlying principles.

- **The Circle of Life and Death:** The circular motion in Euler’s formula, combined with the contraction to zero, can be seen as a metaphor for the cycles of life and death, growth and decay, expansion and contraction. These are universal principles that govern not
 just physical processes but also many natural and social phenomena.

- **Unified View of the Universe:** The constants in Euler’s Identity—$e$, $i$, $\pi$, 1, and 0—each play a role in various branches of mathematics and physics. By bringing them together in one equation, Euler’s Identity provides a unified view of these seemingly disparate concepts, suggesting that the underlying structure of the universe is fundamentally connected.

### Connection to Planetary Motion

In our model, the **Time Spiral** serves as the backbone, representing the inexorable flow of time, much like how time in the universe continues forward, never ceasing. The **Planetary Orbits** follow this spiral, reflecting periodic motion. Just as planets move in their orbits due to gravitational forces, our helical paths around the Time Spiral demonstrate how periodic motion can be linked to time itself.

Euler’s formula, by defining circular motion in the complex plane, underpins the way these orbits are modeled. As time progresses, these circular paths translate into helical spirals in three-dimensional space, emphasizing the connection between time, motion, and mathematics.

In essence, Euler’s Identity not only unifies fundamental constants but also offers a deep insight into the nature of the universe—how forces of expansion and contraction, motion and stillness, are all intertwined in a delicate balance. This balance is reflected in the elegant simplicity of the equation, making it one of the most profound and powerful equations in all of mathematics.

### Why This Visualization is Powerful

- **Unified Concepts:** Euler's formula and identity connect fundamental mathematical constants with geometric and physical concepts, illustrating how abstract ideas like complex numbers and exponential growth relate to tangible phenomena like planetary motion.

- **Intuitive Understanding:** The Time Spiral provides a way to visualize the passage of time as a central, guiding force, while the helical planetary orbits show how motion is inherently linked to time.

- **Modeling Real-world Systems:** This mathematical foundation helps us model real-world systems where periodic motion (like orbits) is synchronized with time. It demonstrates that such systems can be understood through the lens of complex numbers and exponential functions.

This refined approach not only aligns with how such motions are modeled in physics but also provides an intuitive understanding of the relationship between time, motion, and the underlying mathematics.
""")

