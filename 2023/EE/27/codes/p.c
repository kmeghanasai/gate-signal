#include<stdio.h>
#include<math.h>

double values(int n){
        return pow(2.7182,2*n) * (n >= 0);
}

int main() {
    FILE *file = fopen("data31.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    for (int n = -5; n <= 4; n++) {
            fprintf(file, "%d     %f \n", n, values(n));
    }
    
    fclose(file); 
    return 0;
}

