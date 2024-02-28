import numpy as np
from scipy.fft import ifft

# Define X(e^jω) and H(e^jω) functions
def X(w):
    return 1 - np.exp(-1j * w) + 2 * np.exp(-3j * w)

def H(w):
    return 1 - 0.5 * np.exp(-2j * w)

# Perform convolution in frequency domain
n_values = np.arange(0, 9)  # n from 0 to 8
omega_values = 2 * np.pi * np.fft.fftfreq(len(n_values), d=1)  # Frequencies
X_values = X(omega_values)
H_values = H(omega_values)
Y_values = X_values * H_values

# Perform IDFT to obtain y(n)
y_values = np.real(ifft(Y_values))

# Correcting y(n) values where they should be zero
y_values[np.abs(y_values) < 1e-10] = 0

# Save results to file
with open("convolution.dat", "w") as file:
    file.write("n\ty(n)\n")
    for n, y in zip(n_values, y_values):
        file.write(f"{n}\t{y}\n")

