#include "mylib.h"
#include <stdio.h>
#include <math.h>
void linspace(float start, float stop, float step, float* x_values, float* y_values, int num_values, float(*func)(float)){
for(int i = 0; i<num_values; ++i){
 x_values[i] = start + i * step;
 y_values[i] = func(x_values[i]);
}}
