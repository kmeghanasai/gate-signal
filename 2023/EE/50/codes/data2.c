#include <stdio.h>

int main() {
    // Period of x_p(n)
    int period = 5;
    // Number of cycles to generate
    int num_cycles = 2;
    // Values of x_p(n)
    double x_p_values[] = {0.5, 1, 0.5, 0, 0};

    // Open file for writing
    FILE *file = fopen("data2.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write the values to the file for num_cycles
    for (int cycle = 0; cycle < num_cycles; cycle++) {
        for (int i = 0; i < period; ++i) {
            fprintf(file, "%.1f\n", x_p_values[i]);
        }
    }

    // Close the file
    fclose(file);

    return 0;
}
