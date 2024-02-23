#include <stdio.h>

int main() {
    FILE *fp;
    int n;
    
    fp = fopen("data32.txt", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    
    for (n = 0; n <= 10; n++) {
        int y = 0;
        for (int k = 0; k <= n; k++) {
            y += k;
        }
        fprintf(fp, "%d  %d\n",n , y);
    }
    
    fclose(fp);
    
    return 0;
}

