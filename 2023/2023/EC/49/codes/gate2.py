import numpy as np
import matplotlib.pyplot as plt

# Function to create a triangular pulse with linear increase and decrease
def linear_triangular_pulse(omega, width):
    pulse = np.zeros_like(omega)
    
    # Linear increase from -12w to -10w
    pulse[(-12 <= omega) & (omega <= -10)] = (omega[(-12 <= omega) & (omega <= -10)] + 12) / 4
    
    # Linear decrease from -10w to -8w
    pulse[(-10 <= omega) & (omega <= -8)] = 0.5 - (omega[(-10 <= omega) & (omega <= -8)] + 10) / 4
    
    # Zero from -8w to 8w
    pulse[(-8 <= omega) & (omega <= 8)] = 0
    
    # Linear increase from 8w to 10w
    pulse[(8 <= omega) & (omega <= 10)] =  (omega[(8 <= omega) & (omega <= 10)] - 8)/4
    
    # Linear decrease from 10w to 12w
    pulse[(10 <= omega) & (omega <= 12)] = 0.5 - (omega[(10 <= omega) & (omega <= 12)] - 10)/4
    
    return pulse

# Values for omega
omega_values = np.linspace(-12, 12, 1000)

# Compute corresponding values for the linear triangular pulse
y_values = linear_triangular_pulse(omega_values, 2)

# Set the figure size
fig, ax = plt.subplots(figsize=(6, 2))  # Adjust the dimensions (width, height) as needed

# Plot the linear triangular pulse
ax.plot(omega_values, y_values, label=r'', color='black')
ax.plot([10, -10], [0.5, 0.5], 'k--')

# Draw a dotted line connecting the left peak to the x-axis at 10 omega
ax.plot([10, 10], [0.5, 0], 'k--')

# Darken the y=0 and x=0 lines
ax.axhline(0, color='black', linewidth=1.5)
ax.axvline(0, color='black', linewidth=1.5)

ax.set_title('')
ax.set_xlabel(r'')
ax.set_ylabel(r'')

# Hide the baseline by setting it to white
ax.axhline(0, color='white', linewidth=1)

ax.set_xticks([-12, -10, -8, 0, 8, 10, 12])
ax.set_xticklabels(['-12ω', '', '-8ω', '', '8ω', '10ω', '12ω'])
ax.set_yticks([0, 0.5])
ax.set_yticklabels(['0', 'ω/2'])

# Insert arrows for x and y-axes
ax.arrow(15, 0, 0.5, 0, head_width=0.05, head_length=0.1, fc='black', ec='black', shape='full')
ax.text(14, -0.05, r'$\omega$', fontsize=12)

ax.arrow(0, 0.5, 0, 0.2, head_width=0.05, head_length=0.1, fc='black', ec='black', shape='full')
ax.text(0.3, 0.7, r'$H(\omega)$', fontsize=12)

ax.text(0.3, 0.55, r'$ω/2$', fontsize=12)
# Legend

ax.legend()

# Remove outer box
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.grid(False)

# Save the figure
plt.savefig('plot3.png', dpi=300, bbox_inches='tight')



