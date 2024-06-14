#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void generate_array_values(int *arr);
int * max_min(int *arr, int size);

int main(){
	int i;
    int arr[15];
    srand(time(NULL));
	generate_array_values(arr);
    int *max_min_ptr = max_min(arr, 15);
    printf("Maximum: %d \nMinimum: %d", max_min_ptr[0], max_min_ptr[1]);
    return 0;
}

void generate_array_values(int *arr){
    int size = sizeof(arr) / sizeof(arr[0]);
//    int size = 15;
	int i;
    for(i = 0; i < size; i++){
        *(arr+i) = (rand() % (55-11+1)) + 11;
    }
    
}

int * max_min(int *arr, int size){
	int max_min_arr[2] = {arr[0], arr[0]};  // {max, min}
	int i;
	for (i = 0; i < size; i++){
		max_min_arr[0] = arr[i] > max_min_arr[0] ? arr[i] : max_min_arr[0]; 
		max_min_arr[1] = arr[i] < max_min_arr[1] ? arr[i] : max_min_arr[1]; 
	}
	return max_min_arr;
	
}
