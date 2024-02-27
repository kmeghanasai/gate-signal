#include <stdio.h>
#include <math.h>

// Function to calculate |Z|
double calculate_Z_magnitude(double omega_0) {
    return 1e3 * (sqrt(100 + pow(omega_0, 2)) / omega_0);
}

int main() {
    // Open the file for writing
    FILE *file = fopen("data.dat", "w");
    
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Generate values for omega_0 from 1 to 25
    for (double omega_0 = 1.0; omega_0 <= 25.0; omega_0 += 0.01) {
        // Calculate corresponding |Z| values
        double Z_magnitude = calculate_Z_magnitude(omega_0);
        
        // Print values to the file
        fprintf(file, "%.2f %.4f\n", omega_0, Z_magnitude);
    }

    // Close the file
    fclose(file);

    return 0;
}