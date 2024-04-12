#include <stdio.h>

// Define a function pointer type for functions that take an int argument and return an int
typedef int (*IntFunction)(int);

// Define a function that takes a function pointer as an argument and calls it with a value
int applyFunction(int value, IntFunction func) {
    return func(value);
}

int main() {
    // Define and use a lambda-like function
    IntFunction lambda = [](int x) -> int { return x * 2; }; // This line is not valid C syntax

    // Call applyFunction with the lambda-like function
    int result = applyFunction(5, lambda);

    printf("Result: %d\n", result);

    return 0;
}
