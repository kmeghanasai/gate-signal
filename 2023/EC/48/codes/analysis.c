#include <stdio.h>

// Function to compute y(n)
double compute_y(int n) {
    if (n == 0)
        return 1.0;
    else if (n == 1)
        return -1.0;
    else if (n == 2)
        return -0.5;
    else if (n == 3)
        return 2.5;
    else if (n == 5)
        return -1.0;
    else
        return 0.0;
}

int main() {
    // Open the file for writing
    FILE *file = fopen("analysis.dat", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Compute and store y(n) values for n from 0 to 8
    for (int n = 0; n <= 8; n++) {
        double yn = compute_y(n);
        fprintf(file, "%d %lf\n", n, yn);
    }

    // Close the file
    fclose(file);

    return 0;
}

