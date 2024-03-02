#include <stdio.h>

// Function to generate Fibonacci sequence with recurrence and write to file with indices
void fibonacci(int n, int firstTerm, int secondTerm, FILE *file) {
    int i, nextTerm;
    fprintf(file, "Index, Value\n");
    
    fprintf(file, "1, %d\n", firstTerm);
    fprintf(file, "2, %d\n", secondTerm);

    for (i = 3; i <= n; ++i) {
        nextTerm = firstTerm + secondTerm;
        fprintf(file, "%d, %d\n", i, nextTerm);
        firstTerm = secondTerm;
        secondTerm = nextTerm;
    }
}

int main() {
    // Initial terms
    int firstTerm = 4, secondTerm = 5;

    // Open file for writing
    FILE *file = fopen("data.txt", "w");
    if (file == NULL) {
        printf("Error opening file for writing.");
        return 1; // Exit with an error code
    }

    // Generate and write the first 8 terms of the Fibonacci sequence with indices
    fibonacci(8, firstTerm, secondTerm, file);

    // Close the file
    fclose(file);

    printf("Fibonacci sequence with indices has been written to data.txt.\n");

    return 0;
}
