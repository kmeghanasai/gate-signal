#include <stdio.h>
#include <math.h>
#include<stdlib.h>

#define R1 2.2  
#define R2 2.2  
#define L 7  
#define OMEGA (100 * M_PI) 
void calculate_Y_in(double C, double *Y_in) {
    double E=pow(R1,2) + pow((L * OMEGA),2);
    double F=pow(R2,2) +(1/pow((OMEGA * C),2));
    double a = R1/E;
    double b = R2/F;
    double c = (L * OMEGA)/E;
    double D= (1/(OMEGA * C))/F;
    *Y_in = sqrt (pow(a+b,2)+pow(D-c,2));
}

int main() {
    double C_values[1000]; 
    double Y_in[1000];
    int i;
    for (i = 0; i < 1000; i++) {
        C_values[i] = 0 + i * (2 - 0.1) / 999.0;
    }
FILE *outputFile = fopen("y_data.txt", "w"); 

    if (outputFile) {
        for (i = 0; i < 1000; i++) {
        calculate_Y_in(C_values[i], &Y_in[i]);
            fprintf(outputFile, "%lf %lf\n", Y_in[i], C_values[i]);
        }

        fclose(outputFile);
    } else {
        printf("Error: Failed to open output file\n");
        return 1;
    }
    
    return 0;
}

