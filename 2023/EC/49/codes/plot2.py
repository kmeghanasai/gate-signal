import numpy as np
import matplotlib.pyplot as plt

# Frequency values
omega = np.linspace(-2, 2, 1000)

# Fourier transform of sin(omega t) / (pi t)
fourier_transform = np.where(np.abs(omega) < 1, 1, 0)

# Set a smaller figure size
fig, ax = plt.subplots(figsize=(1.5, 1.5))
ax.axvline(0, color='black', linewidth=0.5)
ax.text(0.3, 1.1, r'$X_2(\omega)$', fontsize=12)

# Plot the Fourier transform
plt.plot(omega, fourier_transform)

plt.axhline(y=0, color='black', linestyle='--', linewidth=0.8)  # X-axis
plt.axvline(x=0, color='black', linestyle='--', linewidth=0.8)  # Y-axis

# Show specific points on the x-axis
plt.xticks([-1, 0, 1], ['-ω', '0', 'ω'])
plt.yticks([0, 1], ['0', '1'])
ax.legend()

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.legend()
plt.grid(False)

# Save the figure without borders
plt.savefig('plot4.png', dpi=300, bbox_inches='tight')

