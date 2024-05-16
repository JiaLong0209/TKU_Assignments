#include "./functions.h"
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

void exe(int* arr, int n, int times){
	for(int i = times; i; i--){
		printf("\n-----------------Round %d-----------------\n", times-i+1);
		randomArray(arr, n);
		printArray(arr, n);
		bubbleSort(arr, n);
		printArray(arr, n);
		double median = Median(arr, n);
		printf("\nThe median of array: %.2lf \n", median);
		double mean = Mean(arr, n);
		printf("\nThe mean of array: %.2lf \n", mean);

	}
}

int main(){
	srand(time(NULL));
	int n = 20;
	static int arr[20];
	exe(arr, n, 10);
	return 0;
}

