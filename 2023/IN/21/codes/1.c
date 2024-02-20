#include <stdio.h>
#include <math.h>

#define NUM_POINTS 1000
#define FILENAME "data.txt"

int main() {
    FILE *fp;
    fp = fopen(FILENAME, "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    double w_values[NUM_POINTS];
    double a_values[NUM_POINTS];
    double p_values[NUM_POINTS];
    double t_values[NUM_POINTS];
    double x_values[NUM_POINTS];
    double y_values[NUM_POINTS];
    for (int i = 0; i < 125; i++) {
        w_values[i] = i * 50.0 / (NUM_POINTS - 1);
        p_values[i] = (2*atan(w_values[i]/M_PI) - M_PI)/M_PI*180;
        a_values[i] = 1;
        t_values[i] = i * 50.0 / (NUM_POINTS - 1);
        x_values[i] = sin(M_PI*t_values[i]-M_PI/2);
        y_values[i] = sin(M_PI*t_values[i]);
        fprintf(fp, "%.6f %.6f %.6f %.6f %.6f %.6f\n", w_values[i], p_values[i], a_values[i], t_values[i], x_values[i], y_values[i]);
    }

    fclose(fp);
    return 0;
}
