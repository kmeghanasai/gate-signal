import numpy as np
import matplotlib.pyplot as plt

# Define the time range
t = np.linspace(-5, 5, 400)

# Define the Dirac delta function approximation (a very narrow Gaussian)
def delta(t, sigma=0.01):
    return np.exp(-t**2 / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))

# Define the function h(t)
def h(t):
    return 5 * np.exp(t) + 3 * delta(t)

# Calculate the values of h(t)
h_values = h(t)

# Plot the function
plt.figure(figsize=(8, 6))
plt.plot(t, h_values, label=r'$h(t) = 5e^t + 3\delta(t)$')
plt.title('Plot of $h(t) = 5e^t + 3\delta(t)$')
plt.xlabel('t')
plt.ylabel('h(t)')
plt.grid(True)
plt.legend()
plt.savefig("../figs/plot.png")
 
