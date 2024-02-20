import subprocess
import matplotlib.pyplot as plt
import numpy as np

# Compile the C code
subprocess.run(["gcc", "file.c", "-o", "file"])

# Run the compiled C code
subprocess.run(["./file"])

# Read data from the generated file
data = np.loadtxt("function_data.dat")

# Separate x and y values
x_values = data[:, 0]
y_values = data[:, 1]

# Create a line plot
plt.plot(x_values, y_values, label="Function Data")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.legend()
plt.show()

