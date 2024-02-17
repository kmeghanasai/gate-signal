#include <stdio.h>
#include <math.h>
#include <complex.h> 

#define N 5 // Period of the function

double x(int n) {
    switch (n % N) {
        case 0: return 0.5;
        case 1: return 1.0;
        case 2: return 0.5;
        case 3: return 0.0;
        case 4: return 0.0;
    }
    return 0.0; // Default value (shouldn't reach here)
}

double complex a_k(int k, int size) {
    double sum_real = 0.0;
    double sum_imag = 0.0;
    int n;

    for (n = 0; n < size; n++) {
        double angle = -2 * M_PI * k * n / N;
        double xn = x(n);
        sum_real += xn * cos(angle);
        sum_imag += xn * sin(angle);
    }

    return (sum_real + sum_imag * I) / size;
}

int main() {
    int k;
    FILE *fp;

    fp = fopen("data3.txt", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    for (k = 0; k < N; k++) {
        double complex result = a_k(k, N);
        double magnitude = cabs(result); // Calculate magnitude
        fprintf(fp, "%d %lf %lf %lf\n", k, creal(result), cimag(result), magnitude); // Output real, imaginary, and magnitude parts
    }

    fclose(fp);
    
    printf("DFT coefficients calculated and written to file successfully.\n");
    return 0;
}
