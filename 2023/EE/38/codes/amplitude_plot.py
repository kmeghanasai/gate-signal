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

# Given frequency and amplitude gain
given_frequency = 4  # Given frequency in rad/s
given_gain = 6       # Given amplitude gain in dB

# Find the index closest to the given frequency in the frequency array
index_given_frequency = np.argmin(np.abs(frequency - given_frequency))

# Plotting the Bode amplitude plot
plt.figure(figsize=(10, 6))  

plt.semilogx(frequency, frequency_response[0])
plt.scatter(given_frequency, given_gain, color='red', label='Given frequency and amplitude gain')  # Mark given frequency and gain
plt.annotate(f'({given_frequency}, {given_gain} dB)',
             xy=(given_frequency, given_gain),
             xytext=(given_frequency + 2, given_gain + 5),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=8)
plt.title('Bode Plot - Amplitude')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Amplitude (dB)')
plt.legend()
plt.grid(True)
plt.show()

