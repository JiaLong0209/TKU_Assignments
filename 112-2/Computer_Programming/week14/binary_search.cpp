#include <stdio.h>
#define N 11


int b_search(int arr[], int key, int index = N/2, int left = 0, int right = N){
	return arr[index] == key ? index : arr[index] < key ? b_search(arr, key, (left+right)/2, index, right) : b_search(arr, key, (left+right)/2, left, index);
}
int main(){
	int arr[N] = {1,2,5,6,10,20,35,100,350,1000,1100};
	for(int i = 0; i < N; i++){
		printf("%d\n", b_search(arr, arr[i]));
	}
	return 0;
}


