#include <stdio.h>
#include <math.h>

#define PI 3.14159265359

int main() {
    FILE *file = fopen("data.txt", "w");

    if (file == NULL) {
        fprintf(stderr, "Error opening file for writing.\n");
        return 1;
    }

    // Generate and save data
    for (double t = 0.0; t <= 2 * PI; t += 0.01) {
        double x_t = 39.24 * sin(5 * t + PI / 2);
        fprintf(file, "%f\t%f\n", t, x_t);
    }

    fclose(file);
    return 0;
}

