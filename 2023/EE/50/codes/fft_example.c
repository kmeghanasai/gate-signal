#include <stdio.h>
#include <fftw3.h>
#include <math.h>

#define N 5 // Period of the function

// Define the input signal x(n)
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

int main() {
    fftw_complex *in, *out;
    fftw_plan plan;

    // Allocate memory for input and output arrays
    in = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
    out = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);

    // Prepare input data
    for (int i = 0; i < N; ++i) {
        in[i][0] = x(i); // Real part
        in[i][1] = 0.0; // Imaginary part (zero for this signal)
    }

    // Create FFT plan
    plan = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);

    // Execute FFT
    fftw_execute(plan);

    // Output Fourier coefficients (normalized) to file
    FILE *fp = fopen("data4.txt", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    fprintf(fp, "k Real Imaginary Magnitude\n");
    for (int i = 0; i < N; ++i) {
        double magnitude = sqrt(out[i][0] * out[i][0] + out[i][1] * out[i][1]) / N;
        fprintf(fp, "%d %lf %lf %lf\n", i, out[i][0] / N, out[i][1] / N, magnitude);
    }

    fclose(fp);

    // Free memory and cleanup
    fftw_destroy_plan(plan);
    fftw_free(in);
    fftw_free(out);

    return 0;
}
