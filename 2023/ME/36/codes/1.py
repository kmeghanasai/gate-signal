import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Load data
data = np.loadtxt('1.dat')

# Extract time and x(t) values
t = data[:, 0]
x_t = data[:, 1]

# Plot
plt.plot(t, x_t)
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.grid(True)
plt.savefig('../figs/plot1.png')
plt.show()

