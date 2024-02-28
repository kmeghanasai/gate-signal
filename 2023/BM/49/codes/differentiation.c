#include<stdio.h>

int u(float t,int t_0){
	if (t >= t_0){
		return 1;
	}
	else{
		return 0;	
	}
}

float y(float t){
	return t*u(t,0) + (t-2)*u(t,2) - 2*(t-1)*u(t,1);
}

float sym_dif(float x, float h){
	return (y(x+h)-y(x-h))/(2*h);

}

void main(){
	FILE *fptr;
	fptr = fopen("Differentiation.txt","w");
	//int *ptr = (int*)malloc(int(s))
	float t = -1.1;
	for(int i = 0; i <=40 ; i++){
		t = t+ (1/10.0);
		//printf("%f ,", t);
		float value1 = sym_dif(t,0.000001);
		fprintf(fptr, "%f %f\n", t, value1);
	}
	fclose(fptr);
}
