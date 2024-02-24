import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Define the circuit parameters
R = 20
Iin = 1
C = 0.01

# Define the circuit equations
def circuit(y, t):
    Vc = y[0]
    dVc_dt = Iin - Vc/R
    return [dVc_dt/C]

# Initial condition
initial_condition = [0]

# Time points for simulation
time_points = np.arange(0, 20, 0.02e-3)

# Solve the circuit equations using odeint
solution = odeint(circuit, initial_condition, time_points)

# Extract voltage across component 1
voltage_across_c1 = solution[:, 0]

# Plot the voltage versus time
plt.plot(time_points, voltage_across_c1, label='$V_c(0^-)$')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('$V_c(0^-)$')
plt.legend()
plt.grid(True)
plt.show()

