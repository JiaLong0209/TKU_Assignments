// Question1: 
// Write a function in C that takes an integer pionter and increments the value points to it by 1.

#include <stdio.h>

void increment(int *num);

int main(){
    int num = 0;
    increment(&num);
    printf("%d \n", num);
    increment(&num);
    printf("%d \n", num);
    return 0;
}

void increment(int *num){
    *num += 1;
}
