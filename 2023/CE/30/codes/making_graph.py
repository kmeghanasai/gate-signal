import numpy as np
import matplotlib.pyplot as plt

# Load data from the .dat file
data = np.loadtxt('data4.dat')
t_values = data[:, 0]
y_values = data[:, 1]

# Plot the graph
plt.plot(t_values, y_values, label='Data from C')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)
plt.show()

