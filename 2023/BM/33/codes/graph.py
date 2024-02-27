import numpy as np
import matplotlib.pyplot as plt

# Load data from values.dat
data = np.loadtxt('values.dat')
f = data[:, 0]
Xf = data[:, 1]

# Plot for values.dat and save
plt.figure(figsize=(8, 6))
plt.plot(f, Xf)
plt.xlabel('f')
plt.ylabel('X(f)')
plt.grid(True)
plt.savefig('f1.png')  # Save the plot
plt.close()  # Close the current figure

# Load data from values1.dat
data = np.loadtxt('values1.dat')
f = data[:, 0]
Xsf = data[:, 1]

# Plot for values1.dat and save
plt.figure(figsize=(8, 6))
plt.plot(f, Xsf)
plt.xlabel('f')
plt.ylabel('Xs(f)')
plt.grid(True)
plt.savefig('f2.png')  # Save the plot
plt.close()  # Close the current figure

