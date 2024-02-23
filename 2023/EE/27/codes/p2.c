#include <stdio.h>
#include <math.h>

double h(int n) {
    return 0.5;
}

int main() {
    FILE *fp;
    fp = fopen("data33.txt", "w");
    
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    
    int n;
    double g = 0.0;
    for (n = 0; n <= 20; n++) {
        g += fabs(h(n));
        fprintf(fp, "%d %lf\n", n, g);
    }
    
    fclose(fp);
    
    return 0;
}

