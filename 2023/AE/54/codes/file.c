#include <stdio.h>
#include <math.h>

#define NUM_POINTS 10000

int main() {
    FILE *file;
    file = fopen("function_data.dat", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Generate data points and write to file
    double x, result;
    double start = 1.0;
    double end = 5.0;
    double step = (end - start) / (NUM_POINTS - 1);

    for (int i = 0; i < NUM_POINTS; i++) {
        x = start + i * step;
        result = 1.0 / x - 1.0 / (x * x);
        fprintf(file, "%.2f %.6f\n", x, result);
    }

    fclose(file);
    printf("Data generated and saved to function_data.dat\n");

    return 0;
}


