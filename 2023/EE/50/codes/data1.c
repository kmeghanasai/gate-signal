#include <stdio.h>

int main() {
    // Values of x(n)
    double x_values[] = {0.5, 1, 0.5, 0, 0};

    // Open file for writing
    FILE *file = fopen("data1.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write the values to the file
    for (int i = 0; i < 5; ++i) {
        fprintf(file, "%.1f\n", x_values[i]);
    }

    // Close the file
    fclose(file);

    return 0;
}
