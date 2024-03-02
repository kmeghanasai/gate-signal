import matplotlib.pyplot as plt
import numpy as np

# Read data from the .dat file with space as the delimiter, skip lines starting with 'Values'
data = np.loadtxt('values_v.dat', delimiter=' ', comments='Values')

# Extracting values for t and V_o(t)
t_values = data[:, 0]
V_o_values = data[:, 1]

# Plot the graph for V_o(t)
plt.plot(t_values, V_o_values, label='$V_o(t) = 0.5 + (0.21)/2 \\sin(300t)$')
plt.xlabel('$t$')
plt.ylabel('$V_o(t)$')
plt.grid(True)
plt.legend()
plt.savefig('plot_modified.png')
# Show the combined plot
plt.show()

