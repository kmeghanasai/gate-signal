import numpy as np
import matplotlib.pyplot as plt

# Define the function x(t)
def x(t):
    return np.exp(-t**2)

# Generate t values
t_values = np.linspace(-3, 3, 1000)

# Calculate corresponding x(t) values
x_values = x(t_values)

# Plot the graph
plt.plot(t_values, x_values, label=r'$e^{-t^2}$')
plt.xlabel('t')
plt.ylabel('$x(t)$')
plt.legend()
plt.grid(True)
plt.savefig('graph.png')
plt.show()

