#include <stdio.h>
#include <math.h>

#define N_POINTS 100

void generate_data(double *t, double *y, double k, double a) {
    for (int i = 0; i < N_POINTS; ++i) {
        t[i] = -3.0 + i * (6.0 / (N_POINTS - 1));
        y[i] = k * exp(-a * t[i] * t[i]);
    }
}

int main() {
    double t[N_POINTS];
    double y[N_POINTS];
    double k = 1.0;
    double a = 0.5;

    generate_data(t, y, k, a);

    FILE *file = fopen("data.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    for (int i = 0; i < N_POINTS; ++i) {
        fprintf(file, "%lf %lf\n", t[i], y[i]);
    }

    fclose(file);

    return 0;
}

