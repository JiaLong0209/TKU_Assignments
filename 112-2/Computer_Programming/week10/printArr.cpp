#include<stdio.h>

void printArr(int arr[], int size){
	for(int i = 0; i < size; i ++) printf("%d ", arr[i]);
	printf("\n");
}

int main(){
	int n = 5;
	int a[5] = {1,2,3,4,5};
	printArr(a, n);
	return 0;
}
