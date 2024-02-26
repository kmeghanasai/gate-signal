#include <stdio.h>
#include <complex.h>
#include <math.h>
int main() {
    // Given value
    double complex w4 = 16 * I;  // 16j in C is represented by I

    // Options
    double complex option_A = 2 * cexp(I * (2 * M_PI / 8));
    double complex option_B = 2 * cexp(I * (M_PI / 8));
    double complex option_C = 2 * cexp(I * (5 * M_PI / 8));
    double complex option_D = 2 * cexp(I * (9 * M_PI / 8));

    // Verifying options
    if (cabs(w4 - cpow(option_A, 4)) < 1e-10) {
        printf("(A) 2e^(j(2\u03C0/8)) is a value of w.\n");
    } else {
        printf("(A) 2e^(j(2\u03C0/8)) is not a value of w.\n");
        return 0;
    }

    if (cabs(w4 - cpow(option_B, 4)) < 1e-10) {
        printf("(B) 2e^(j(\u03C0/8)) is a value of w.\n");
    } else {
        printf("(B) 2e^(j(\u03C0/8)) is not a value of w.\n");
        return 0;
    }

    if (cabs(w4 - cpow(option_C, 4)) < 1e-10) {
        printf("(C) 2e^(j(5\u03C0/8)) is a value of w.\n");
    } else {
        printf("(C) 2e^(j(5\u03C0/8)) is not a value of w.\n");
        return 0;
        
    }

    if (cabs(w4 - cpow(option_D, 4)) < 1e-10) {
        printf("(D) 2e^(j(9\u03C0/8)) is a value of w.\n");
    } else {
        printf("(D) 2e^(j(9\u03C0/8)) is not a value of w.\n");
        return 0;
    }

    return 0;
}
