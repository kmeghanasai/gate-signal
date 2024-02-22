#include <stdio.h>
#include <math.h>
#include "mylib.h"
float f(float x){
return 2 * fabs(cos(x / 2));
}
int main() {
    // Define the range and step size
    float start = -M_PI;
    float stop = M_PI;
    float step = 0.1;

    // Calculate the number of values in the range
    int num_values = (stop - start) / step + 1;

    // Allocate arrays to store the generated values
    float x_values[num_values];
    float y_values[num_values];
	float(*func)(float);
	func = f;
    // Call the linspace function
    linspace(start, stop, step, x_values, y_values, num_values, func);
    //Save data to a file
     FILE* file = fopen("output.dat", "w");

    if (file != NULL) {
        for (int i = 0; i < num_values; ++i) {
            fprintf(file, "%f %f\n", x_values[i], y_values[i]);
        }

        fclose(file);
        printf("Data saved to 'output.dat'.\n");
    } else {
        printf("Error opening file for writing.\n");
    }

    return 0;
}
