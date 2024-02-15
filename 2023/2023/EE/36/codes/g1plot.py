import numpy as np
import matplotlib.pyplot as plt

# Generate some data for demonstration
omega = np.linspace(0.1, 10, 100)  # Angular frequency values from 0.1 to 10 rad/s
phase_deg = -60 * np.ones_like(omega)  # Constant phase of -60 degrees

# Calculate the slope of the line passing through (0, 0) and (1, -60)
slope = -60 / 1

# Generate phase data for the line passing through (0, 0) and (1, -60)
line_phase_deg = slope * omega

# Plotting
plt.figure()
plt.plot([0, 1], [0, -60], 'r-')  # Plot the line passing through (0, 0) and (1, -60) in red dashed line
plt.plot(omega, phase_deg)
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Phase (degrees)')
plt.ylim(-90, 0)  # Set y-axis limit to -90 to 0 degrees
plt.xlim(0, 3)  # Set x-axis limit from 0 to 10 rad/s
plt.xticks([1])  # Set x-axis ticks to only include 1
plt.yticks([-60, 0])  # Set y-axis ticks to -60 and 0
plt.grid(True)

# Move x-axis to the top
ax = plt.gca()
ax.xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')

plt.show()

