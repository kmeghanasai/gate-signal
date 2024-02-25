import numpy as np
import matplotlib.pyplot as plt

# Define the function X(f)
def X(f):
    return np.sqrt(np.pi) * np.exp(-np.pi**2 * f**2)

# Generate f values
f_values = np.linspace(-1, 1, 1000)

# Calculate corresponding X(f) values
X_values = X(f_values)

# Plot the graph
plt.plot(f_values, X_values, label=r'$\sqrt{\pi}e^{-\pi^2f^2}$')
plt.xlabel('$f$')
plt.ylabel('$X(f)$')
plt.legend()
plt.grid(True)
plt.savefig('graph1.png')
plt.show()

