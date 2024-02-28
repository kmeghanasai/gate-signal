import numpy as np
import matplotlib.pyplot as plt

# Define the function
def y(t, omega):
    return (15/4) * omega * np.cos(10.5 * omega * t)

# Generate time values
t = np.linspace(0, 2*np.pi, 1000)

# Specify the values of omega
omega_values = [1.0, 2.0]  # You can adjust this list

# Plot the graph for each omega value
for omega_value in omega_values:
    y_values = y(t, omega_value)
    plt.plot(t, y_values, label=f'$y(t), \\omega = {omega_value:.2f}$')

plt.xlabel('t')
plt.ylabel('$y(t)$')
plt.grid(False)
plt.legend()

# Set custom x-axis ticks
custom_ticks = np.arange(0, 2*np.pi+1, 2)
plt.xticks(custom_ticks)

plt.savefig('plot5.png', dpi=300, bbox_inches='tight')

