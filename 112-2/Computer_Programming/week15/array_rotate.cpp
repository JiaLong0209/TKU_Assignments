#include <stdio.h>
#define SIZE 10

void gen_array(int array[]);
void print_array(const int array[]);
void rotate_array(int array[], const int position);

int main(void){
	int arr[SIZE];
	gen_array(arr);
	printf("Orignal: ");
	print_array(arr);
	printf("Rotated: \n");
	rotate_array(arr, 1);
	print_array(arr);
	rotate_array(arr, 1);
	print_array(arr);
	rotate_array(arr, 1);
	print_array(arr);
	rotate_array(arr, 1);
	print_array(arr);
	rotate_array(arr, 1);
	print_array(arr);
	rotate_array(arr, 1);
	print_array(arr);

	return 0;
}

void gen_array(int array[]){
	for(int i = 0; i < SIZE; i++){
		array[i] = i;
	}
}

void print_array(const int array[]){
	for(int i = 0; i < SIZE; i++){
		printf("%d ", array[i]);
	}
	printf("\n");
}

void rotate_array(int array[], const int position){
	int temp[SIZE];
	for(int i = 0; i < SIZE; i++){
		temp[(i+position)%SIZE] = array[i];
	}
	for(int i = 0; i < SIZE; i++){
	array[i] = temp[i];
	}
}
