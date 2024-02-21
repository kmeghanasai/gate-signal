#include <stdio.h>
#include <math.h>

int main() {
    FILE *file = fopen("1.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    
    #define n 1000
    #define step 0.01 

    double t, x_t;

    double u(double t) {
        return t >= 0 ? 1.0 : 0.0;
    }

    for (int i = 0; i < n; i++) {
        t = i * step;
        x_t = (-1 + (1.0/2.0)*exp(-t) + (1.0/2.0)*exp(t)) * u(t);
        fprintf(file, "%lf\t%lf\n", t, x_t);
    }        

return 0;
}
