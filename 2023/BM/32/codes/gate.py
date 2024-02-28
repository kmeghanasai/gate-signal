import matplotlib.pyplot as plt

# Read data from data.dat
data = []
with open('data.dat', 'r') as file:
        for line in file:
                    omega_0, Z_magnitude = map(float, line.split())
                            data.append((omega_0, Z_magnitude))

                            # Separate data into omega_0 and Z_magnitude
                            omega_0_values, Z_magnitude_values = zip(*data)

                            # Plot the values
                            plt.plot(omega_0_values, Z_magnitude_values, label=r'$|\mathbf{Z}| = 10^3 \left(\frac{\sqrt{100 + \omega_0^2}}{\omega_0}\right)$')

                            # Highlight the point at omega_0 = 10 in a different color
                            highlight_omega_0 = 10
                            highlight_Z_magnitude = Z_magnitude_values[omega_0_values.index(highlight_omega_0)]
                            plt.scatter(highlight_omega_0, highlight_Z_magnitude, color='red', label=f'Highlight at $\omega_0 = {highlight_omega_0}$')

                            # Add labels and legend
                            plt.xlabel(r'$\omega_0$')
                            plt.ylabel(r'$|\mathbf{Z}|$')
                            plt.legend()

                            # Show the plot
                            plt.grid(True)
                            plt.show()
