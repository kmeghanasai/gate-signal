#include <stdio.h>
#include <math.h>

int main() {
    FILE *file;
    file = fopen("output_data.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Print headers
    fprintf(file, "t     y(t)\n");

    // Given values
    double y_t;        // Value of y(n)

    // Generate values for t to cover the range from 0 to 3 (inclusive) with a step of 0.5
    for (double t = 0; t <= 3; t += 0.5) {
        // Calculate y(n)
        y_t =4*exp(-2 * t);

        // Write to file
        fprintf(file, "%.1lf %lf\n", t, y_t);
    }

    fclose(file);

    return 0;
}
