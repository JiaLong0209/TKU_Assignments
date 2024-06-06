// Question 4.
// Write a function in C that takes two pionters to integers and returns the pointer to the larger integer.
#include <stdio.h>

/*int* check_larger_value(int *a, int *b);*/

void change_value(int *x){
    *x = 100;
}

int main(){
    int x = 23;
    change_value(&x);
    printf("%d \n", x);

    /*int *larger_value = check_larger_value(&x, &y);*/
    /*printf("%d \n", *larger_value);*/
}

/*int* check_larger_value(int *a, int *b){*/
/*    return *a > *b ? a : b;*/
/*}*/
