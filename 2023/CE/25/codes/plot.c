#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define p 5
#define q 2
#define L 0.08

float* linspace(float x1, float x2, int n) {
    float *x = (float*) calloc(n, sizeof(float));

    float step = (x2 - x1) / (float)(n - 1);

    for (int i = 0; i < n; i++) {
        x[i] = x1 + ((float)i * step);
    }

    return x;
}

float f(float x){
    return (p*(pow(x,4))+q*pow(x,5));
} 

float a_n(int N, float x){
    float A=0;
    for(int i=1; i<N+1; i++){
        A += (2*q*pow(L,5))*pow((-1),i)*(((1/(i*M_PI))-(2/pow((i*M_PI),3))+(120/(pow((i*M_PI),5)))))*sin(M_PI*i*x/L);
    }
    return A;
}

float b_n(int N, float x){
    float B=0;
    for(int i=1; i<N+1; i++){
        B += (float)(2*p*pow(L,4))*(pow(-1, i))*((4/(pow((i*M_PI), 2)))-(24/(pow((i*M_PI), 4))))*cos(M_PI*i*x/L);
    }
    return B;
}

int main(){
    FILE *ptr= fopen("data.dat", "w");
    float *x=linspace(-L,L,10000);
    for(int i=0; i<10000; i++){
        fprintf(ptr, "%f\t%f\t%f\n", x[i], f(x[i]), (p*pow(L,4)/5.0) + a_n(1000, x[i])+b_n(1000, x[i]));
    }
    
}