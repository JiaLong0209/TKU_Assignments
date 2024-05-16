#include <stdio.h>
#include <stdlib.h>

void bubbleSort(int* m, int n){
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n-i-1; j++){
			if(m[j] > m[j+1]){
				m[j] ^= m[j+1];
				m[j+1] ^= m[j];
				m[j] ^= m[j+1];
			}
		}
	}
}

void randomArray(int *arr, int n){
	for(int i = 0; i < n; i++) arr[i] = (rand() % 100) + 1;
}

void printArray(int *arr, int n){
	for(int i = 0; i < n; i++) printf("%3d ", arr[i]);
	printf("\n");
}

double Median(int *arr, int n){
	return n&1 ? arr[n/2] : (double)(arr[n/2-1] + arr[n/2]) / 2; }


double Mean(int *arr, int n){
	int sum = 0;
	for(int i = n; i ; i--){
		sum += arr[i];
	}
	return (double) sum / n;
}
