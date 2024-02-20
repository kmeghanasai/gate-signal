import numpy as np
import matplotlib.pyplot as plt

# Given data
wave_height = 3.5  # meters
wave_period = 9.0  # seconds
g = 9.81  # acceleration due to gravity in m/s^2

# Calculate wavelength
wavelength = (g * wave_period**2) / (2 * np.pi)

# Define time array
t = np.linspace(0, 4*wave_period, 1000)

# Calculate the sinusoidal wave
wave = wave_height * np.sin(2 * np.pi / wave_period * t)

# Plot the wave
plt.plot(t, wave, color='blue')
plt.xlabel('Time (s)')
plt.ylabel('Wave Height (m)')
plt.grid(True)

# Save the figure as plot.png
plt.savefig('plot.png')

plt.show()

