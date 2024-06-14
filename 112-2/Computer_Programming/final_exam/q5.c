#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 5

void generate_array_values(int arr[]){
    for(int i = 0; i < SIZE; i++){
        arr[i] = rand() % (25 + 1 - 1) + 1;
    }
}

int* largest(int *arr){
    int num = arr[0];
    int *max = &num;
    for(int i = 0; i < SIZE; i++){
        max = arr[i] > num ? &arr[i] : max;
    }
    printf("%p \n", max);
    return max;
}

void print_arr(int *arr){
    for(int i = 0; i < SIZE; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main(){
    int arr[15];
    srand(time(NULL));

    generate_array_values(arr);
    print_arr(arr);
    int * ptr = largest(arr);
    printf("%p \n", ptr);
    printf("%d \n", *ptr);
    


    return 0;
}
