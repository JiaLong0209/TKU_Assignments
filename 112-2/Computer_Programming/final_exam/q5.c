#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 10

void generate_array_values(int *arr);
int* largest(int *arr);
void print_arr(int *arr);


int main(){
	int i;
    int arr[SIZE];
    srand(time(NULL));
	generate_array_values(arr);
	
    print_arr(arr);
    int *largest_ptr = largest(arr);
    printf("Address of largest_num : %p\n", largest_ptr);
    printf("Value of largest_num : %d\n", *largest_ptr);

    return 0;
}

void generate_array_values(int arr[]){
	int i;
    for(i = 0; i < SIZE; i++){
        arr[i] = (rand() % 25) + 1;
    }
}

int* largest(int *arr){
    int * largest_num = &arr[0];
	int i;
	for (i = 0; i < SIZE; i++){
        largest_num = arr[i] > *largest_num ? &arr[i] : largest_num;
	}
	return largest_num;
	
}

void print_arr(int *arr){
    int i;
    for(i = 0; i < SIZE; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}
