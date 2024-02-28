#include<stdio.h>
#include<stdlib.h>
int u(float t,int t_0){
	if(t>=t_0){
		return 1;
	}
	else{
		return 0;
	}
}
/*void append(*ptr, len, add){
	ptr = (int *)realloc(ptr, sizeof(int)*(len+1));
	*(ptr+len) = add;*/

float f(float t){
	if(t>=0 && t<=1){
		return 1;
	}
	else{
		return 0;
	}


}

float trap_integration(float a,float b,long int n){
	printf("a, b =%f %f \n", a,b);
	printf("f(a), f(b) = %f %f \n", f(a), f(b));
	float h = (b-a)/(n);
	float result = f(a) + f(b);
	for (int i = 1; i<n; i++){ 
		result += 2*(f(a+i*h));
	}
	printf("result_before_multi = %f" , result);
	result = result * (h/2);
	printf("result = %f\n\n",result);
	return result;
}


void main(){
	FILE *fptr;
	fptr = fopen("Values.txt","w");
	//int *ptr = (int*)malloc(int(s))
	float t = -1.1;
	for(int i = 0; i <=40 ; i++){
		t = t+ (1/10.0);
		//printf("%f ,", t);
		float value1 = trap_integration(t-1,t,100000);
		float value2 = t*u(t,0) + (t-2)*u(t,2) -2*(t-1)*u(t,1);
		fprintf(fptr, "%f %f %f\n", t, value1, value2);
	}
	fclose(fptr);
}
