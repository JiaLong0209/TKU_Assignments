#include <stdio.h>
#include <stdlib.h>
#include <time.h>


void generate_array_values(int *arr, int size){
    for(int i = 0; i < size; i++){
        *(arr + i) = rand() % (55 - 11 + 1) + 11;
    }
}

int *max_min(int *arr, int size){
    static int mm[2] = {arr[0], arr[1]};
    for(int i = 0; i < size; i++){
        mm[0] = arr[i] > mm[0] ? arr[i] : mm[0];
        mm[1] = arr[i] < mm[1] ? arr[i] : mm[1];
    }
    return mm;
}

int main(){
    int arr[15];
    int size = sizeof(arr) / sizeof(arr[0]);
    srand(time(NULL));
    generate_array_values(arr, size);
    int * ptr = max_min(arr, size);
    printf("max: %d, min:%d \n", ptr[0], ptr[1]);
    return 0;
}
