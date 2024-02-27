#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define SAMPLING_RATE 600
#define SIGNAL_DURATION 1 

double X(double f) {
    if (fabs(f) <= 200 ) {
            return 1 - fabs(f) / 200;
        
    } else {
        return 0;
    }
}

int main() {
    FILE *fp1, *fp2;
    fp1 = fopen("values.dat", "w"); // Open for writing in text mode
    fp2 = fopen("values1.dat", "w"); // Open for writing in text mode

    if (fp1 == NULL || fp2 == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    int num_samples = SAMPLING_RATE * SIGNAL_DURATION;
    double delta_f = (double)SAMPLING_RATE / num_samples;
    double f;
    double magnitude = 0;

    for (int i = 0; i <= 1000; ++i) {
        f = -200 + i * delta_f;
         magnitude = X(f) ;
        fprintf(fp1, "%.2f %lf\n", f, magnitude); // Write frequency and magnitude to file1
	}
	magnitude = 0;
      for (int i = 0; i <= 1000; ++i) {
        f = -200 + i * delta_f;  
        magnitude = X(f)+X(f-600); // Use the shifted frequency for the second part
        fprintf(fp2, "%.2f %lf\n", f, magnitude); // Write frequency and magnitude to file2
        
    }

    fclose(fp1); // Close file1
    fclose(fp2); // Close file2

    return 0;
}

