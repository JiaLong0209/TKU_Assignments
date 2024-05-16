#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int indexOf(int* arr, int n, int target, bool right);
void randomArray(int* arr, int n);
void printArray(int* arr, int n);
void exe(int* arr, int n, int times);


int main(){
	int n = 10;
	srand(time(NULL));
	static int arr[10];
	exe(arr, n, 10);
	return 0;
}

void exe(int* arr, int n, int times){
	for(int i = times;i ; i--){
		printf("\n-------------------Round %d-------------------\n", i-times+1);
		randomArray(arr, n);
		printArray(arr, n);
		indexOf(arr, n, 5, true);
	}
}

int indexOf(int* arr, int n, int target, bool right){
	for(int i=right?n-1:0; right?i>=0:i<n; i+=right?-1:1){
		if(arr[i] == target){
			printf("Found %d at index %d\n", target, i);
			return i;
		}
	}
	printf("Cannot find %d!\n", target);
	return -1;

}

void randomArray(int *arr, int n){
	for(int i = 0; i < n; i++) arr[i] = (rand() % 10) + 1;
}

void printArray(int *arr, int n){
	for(int i = 0; i < n; i++) printf("%d ", arr[i]);
	printf("\n");
}

