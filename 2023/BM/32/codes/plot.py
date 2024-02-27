import matplotlib.pyplot as plt

# Read data from plot.dat file
data = []
with open("plot.dat", "r") as file:
        for line in file:
                    time, v_c, v_r = map(float, line.split())
                            data.append((time, v_c, v_r))

                            # Extracting values
                            time_values, voltage_across_capacitor, voltage_across_resistor = zip(*data)

                            # Plotting
                            plt.figure(figsize=(10, 6))
                            plt.plot(time_values, voltage_across_capacitor, label='$V_C(t)$')
                            plt.plot(time_values, voltage_across_resistor, label='$V_R(t)$')
                            plt.xlabel('Time (s)')
                            plt.ylabel('Voltage (V)')
                            plt.legend()
                            plt.grid(True)
                            plt.show()
