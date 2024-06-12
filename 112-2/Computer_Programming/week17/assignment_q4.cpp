// Question 4
// Write a function in C that takes two pointers to integers and returns the pointer to the larger integer.
#include <stdio.h>

/*int* large_number(int a, int b){*/
/*    return a > b ? &a : &b;*/
/*}*/

int* large_number(int *a, int *b){
    return *a > *b ? a : b;
}


void swap(int *a, int *b){
    *a ^= *b;
    *b ^= *a;
    *a ^= *b;
}


int main(){
    int a = 10;
    int b = 20;
    /*int* large = large_number(&a, &b);*/
    printf("a: %d \n", a);
    printf("b: %d \n", b);
    swap(&a, &b);

    printf("a: %d \n", a);
    printf("b: %d \n", b);


    /*printf("large: %p \n", large);*/
    /*printf("large: %d \n", *large);*/
}

