#include <stdio.h>
#include <stdlib.h> // srand()
#include <time.h> // time()



void genArr(int *arr, int size);
void bubbleSort(int *arr, int size);
void swap(int *a, int *b);
void printArr(int *arr, int size);

int main(){
    srand(time(NULL));
    int arr[10];
    int size = sizeof(arr) / sizeof(*arr);
    genArr(arr, size);
    printArr(arr, size);
    bubbleSort(arr, size);
    printArr(arr, size);

    return 0;
}

void genArr(int *arr, int size){
    for(int i = 0; i < size; i++){
        *(arr + i) = rand() % 100;
    }
}

void bubbleSort(int *arr, int size){
    for(int i = 0; i < size; i++){
        for(int j = 0; j < size - i - 1; j++){
            if(*(arr + j) > *(arr + j+1)){
                swap((arr + j), (arr + j+1));
            }
        }
    }
}

void swap(int *a, int *b){
    *a ^= *b;
    *b ^= *a;
    *a ^= *b;
}

void printArr(int *arr, int size){
    for(int i = 0; i < size; i++){
        printf("%d ", *(arr + i));
    }
    printf("\n");
}


