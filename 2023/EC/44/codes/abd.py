import numpy as np
import matplotlib.pyplot as plt

# Define the function i_c(t)
def i_c(t):
    return -np.exp(-2*t) * (np.cos(4*np.sqrt(6)*t) + (18.8/(4*np.sqrt(6))) * np.sin(4*np.sqrt(6)*t))

# Generate time values
time_values = np.linspace(0, 5, 1000)  # Adjust the range and number of points as needed

# Calculate i_c(t) values for each time point
i_c_values = i_c(time_values)

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(time_values, i_c_values, label=r'$i_c(t) = -e^{-2t} \left(\cos(4\sqrt{6}t) + \frac{18.8}{4\sqrt{6}}\sin(4\sqrt{6}t)\right)$')
plt.xlabel('Time (s)')
plt.ylabel(r'$i_c(t)$')
plt.legend()
plt.grid(True)
plt.show()

