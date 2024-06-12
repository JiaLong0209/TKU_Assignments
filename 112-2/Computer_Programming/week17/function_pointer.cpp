#include <stdio.h>

// Define some functions to use
int add(int a, int b) {
    return a + b;
}

double subtract(int a, int b) {
    return a - b;
}

int main() {
    // Declare function pointers
    int (*func1)(int, int) = &add;
    double (*func2)(int, int) = &subtract;

    // Print the size of the function pointers
    printf("Size of function pointer func1: %zu bytes\n", sizeof(func1));
    printf("Size of function pointer func2: %zu bytes\n", sizeof(func2));

    printf("Size of int: %zu bytes\n", sizeof(int));
    printf("Size of double: %zu bytes\n", sizeof(double));
    printf("Size of int pointer: %zu bytes\n", sizeof(int*));

    return 0;
}
