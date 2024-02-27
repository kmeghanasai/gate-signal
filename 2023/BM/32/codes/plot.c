#include <stdio.h>
#include <math.h>

// Function to calculate V_C(t) and V_R(t)
void calculate_voltages(double time, double *v_c, double *v_r) {
    // Given values
    double R = 1000;  // Resistor value in ohms
    double C = 100e-6;  // Capacitor value in farads
    double omega_0 = 1;  // Angular frequency in rad/s (you can change this to the actual value)

    // Voltage source function
    double v_source = 100 * cos(omega_0 * time);

    // Voltage across capacitor (V_C(t))
    *v_c = v_source * (1 - exp(-time / (R * C)));

    // Voltage across resistor (V_R(t))
    *v_r = v_source * exp(-time / (R * C));
}

int main() {
    FILE *file = fopen("plot.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Time values
    double time_values[1000];
    for (int i = 0; i < 1000; ++i) {
        time_values[i] = i * 0.005; // Assuming 5 seconds with 1000 points
    }

    // Calculate voltages and write to file
    for (int i = 0; i < 1000; ++i) {
        double v_c, v_r;
        calculate_voltages(time_values[i], &v_c, &v_r);
        fprintf(file, "%lf %lf %lf\n", time_values[i], v_c, v_r);
    }

    fclose(file);

    return 0;
}
