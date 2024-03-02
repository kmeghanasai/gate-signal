import numpy as np
import matplotlib.pyplot as plt

# Generate values for t from 0 to 2*pi with small steps
t = np.linspace(0, 2*np.pi, 10000)

# Compute the values of cos(2t)
cos_2t = np.cos(2*t)

# Plotting the graph
plt.figure(figsize=(8, 6))
plt.plot(t, cos_2t, label=r'$\cos(2t)$', color='blue')
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.grid(True)
plt.legend()
plt.savefig('gate.png')
plt.show()

