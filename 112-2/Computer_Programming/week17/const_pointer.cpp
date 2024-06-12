#include <stdio.h>

int main() {
    // Declare a const int
    const int value = 42;

    // Declare a const pointer to a const int
    const int * const a = &value;

    // Declare a const pointer to a const pointer to a const int
    const int * const * const ptr = &a;

    // Output the value using the pointers
    printf("Value: %d\n", **ptr);

    return 0;
}
