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

# Plot the first graph
plt.plot(w_values, a_values)
plt.xlabel('$\omega$')
plt.ylabel('Amplitude of $\\frac{1}{H(j\omega)}$ ')
plt.grid(True)

# Set x-axis ticks with an interval of 1 unit
plt.xticks(np.arange(min(w_values), max(w_values) + 1, 1))

# Mark x=pi with a point
plt.scatter(np.pi, np.interp(np.pi, w_values, a_values), color='red', marker='o', label=r'$\omega = \pi$')

# Save the first figure
save_path1 = '../figs/figure1.png'  # Adjust based on the directory structure
plt.savefig(save_path1)

# Plot the second graph
plt.figure()  # Create a new figure for the second plot

plt.plot(w_values, p_values)
plt.xlabel('$\omega$')
plt.ylabel('Phase of $\\frac{1}{H(j\omega)}$')
plt.grid(True)

# Set x-axis ticks with an interval of 1 unit
plt.xticks(np.arange(min(w_values), max(w_values) + 1, 1))

# Mark x=pi with a point
plt.scatter(np.pi, np.interp(np.pi, w_values, p_values), color='red', marker='o', label=r'$\omega = \pi$')

# Save the second figure
save_path2 = '../figs/figure2.png'  # Adjust based on the directory structure
plt.savefig(save_path2)

plt.figure()

# Plot the graph
plt.plot(t_values, y_values, label='$y(t) = \sin(\pi t)$')
plt.plot(t_values, x_values, label='$x(t) = \sin(\pi t - \\frac{\pi}{2})$')
plt.grid(True)

# Set x-axis ticks with an interval of 1 unit
plt.xticks(np.arange(min(t_values), max(t_values) + 1, 1))

# Save the figure
save_path3 = '../figs/figure3.png'  # Adjust based on the directory structure
plt.savefig(save_path3)



# Display the plots
plt.show()
