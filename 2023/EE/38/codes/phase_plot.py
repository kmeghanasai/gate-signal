import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# System parameters
a = 2
beta = 4

# Transfer function of the lead compensator
numerator = [1, a]
denominator = [1, a * beta]
system = signal.TransferFunction(numerator, denominator)

# Frequency range for Bode plot
frequency = np.logspace(-1, 2, 1000)

# Bode plot calculation
frequency_response = signal.bode(system, frequency)

# Plotting the Bode phase plot
plt.figure(figsize=(10, 6))
plt.semilogx(frequency, frequency_response[1])
plt.title('Bode Plot - Phase')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Phase (degrees)')
plt.grid(True)
plt.show()

