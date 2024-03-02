#include <stdio.h>
#include <math.h>

#define NUM_POINTS 1000
#define PI 3.14159265

int main() {
    FILE *file1, *file2, *file3;
    file1 = fopen("Vx_data.txt", "w");
    file2 = fopen("Vy_data.txt", "w");
    file3 = fopen("Vo_data.txt", "w");

    if (file1 == NULL || file2 == NULL || file3 == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    double t, Vx, Vy, Vo;
    for (int i = 0; i < NUM_POINTS; i++) {
        t = 2 * PI * i / NUM_POINTS;
        Vx = 2 * sqrt(2) * sin(t - PI/4);
        Vy = 4.6 * sin(t + PI/2);
        Vo = 4.6 - 4.6 * sqrt(2) * cos(2 * t);
        fprintf(file1, "%lf %lf\n", t, Vx);
        fprintf(file2, "%lf %lf\n", t, Vy);
        fprintf(file3, "%lf %lf\n", t, Vo);
    }

    fclose(file1);
    fclose(file2);
    fclose(file3);

    return 0;
}



