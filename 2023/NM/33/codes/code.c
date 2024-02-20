#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define GRAVITY 9.81

int main() {
    // Given wave parameters
    double wave_height = 3.5; // in meters
    double wave_period = 9.0; // in seconds

    // Calculate wavelength
    double wavelength = (GRAVITY * pow(wave_period, 2)) / (2 * M_PI);

    // Calculate wave steepness
    double wave_steepness = wave_height / wavelength;

    // Open the file for writing
    FILE *output_file = fopen("output.dat", "w");
    
    // Check if the file opened successfully
    if (output_file == NULL) {
        perror("Error opening file");
        return EXIT_FAILURE;
    }

    // Print the numerical answer to the file
    fprintf(output_file, "%.3f\n", wave_steepness);

    // Close the file
    fclose(output_file);

    return 0;
}

