#include <stdio.h>
#include <math.h>

// Define the function x(t) with a fundamental period of 100 seconds
double x(double t) {
    return sin(2 * M_PI * t / 100);
}

// Define the function y(t) = x(4t)
double y(double t) {
    return x(4 * t);
}

int main() {
    FILE *file;
    file = fopen("output_data.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Print headers
    fprintf(file, "t  x(t)   y(t)\n");

    // Given values
    double t, x_t, y_t;

    // Generate values for t from 0 to 100 with a step of 0.1
    for (t = 0; t <= 100; t += 4) {
        // Calculate x(t)
        x_t = x(t);

        // Calculate y(t) = x(4t)
        y_t = y(t);

        // Write to file
        fprintf(file, "%.2lf  %.6lf %.6lf\n", t, x_t, y_t);
    }

    fclose(file);

    return 0;
}
