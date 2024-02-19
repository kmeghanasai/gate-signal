import numpy as np
import matplotlib.pyplot as plt

# Load data from file
data = np.loadtxt('data.txt')
w_values = data[:, 0]
p_values = data[:, 1]
a_values = data[:, 2]
t_values = data[:, 3]
x_values = data[:, 4]
y_values = data[:, 5]

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# Plot the first graph
ax1.plot(w_values, a_values)
ax1.set_xlabel('$\omega$')
ax1.set_ylabel('Amplitude of $\\frac{1}{H(j\omega)}$ ')
ax1.grid(True)
ax1.set_xticks(np.arange(min(w_values), max(w_values) + 1, 1))
ax1.scatter(np.pi, np.interp(np.pi, w_values, a_values), color='red', marker='o', label=r'$\omega = \pi$')
ax1.legend()

# Plot the second graph
ax2.plot(w_values, p_values)
ax2.set_xlabel('$\omega$')
ax2.set_ylabel('Phase of $\\frac{1}{H(j\omega)}$')
ax2.grid(True)
ax2.set_xticks(np.arange(min(w_values), max(w_values) + 1, 1))
ax2.scatter(np.pi, np.interp(np.pi, w_values, p_values), color='red', marker='o', label=r'$\omega = \pi$')
ax2.legend()


# Adjust layout
plt.tight_layout()

# Save the first combined figure
save_path_combined1 = '../figs/fig1.png'  # Adjust based on the directory structure
plt.savefig(save_path_combined1)

# Create a new figure for the third graph
plt.figure()

# Plot the third graph individually
plt.plot(t_values, y_values, label='$y(t) = \sin(\pi t)$')
plt.plot(t_values, x_values, label='$x(t) = \sin(\pi t - \\frac{\pi}{2})$')
plt.grid(True)
plt.xticks(np.arange(min(t_values), max(t_values) + 1, 1))
plt.legend()

# Save the second combined figure
save_path_combined2 = '../figs/fig2.png'  # Adjust based on the directory structure
plt.savefig(save_path_combined2)

# Display the plots
plt.show()

