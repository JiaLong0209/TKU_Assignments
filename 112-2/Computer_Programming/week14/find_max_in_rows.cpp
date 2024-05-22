#include <stdlib.h>
#include <stdio.h>

#define N 3

void findMaxInRows(int arr[N][N]){
	for(int i = 0; i < N; i++){
		int max = arr[i][0];
		for(int j = 0; j < N; j++) max = arr[i][j] > max ? arr[i][j] : max;
		printf("The max in %d row: %d \n", i+1, max);
	}
}

int main(){
	int arr[3][3] = {{1,3,2},{5,4,6},{7,8,9}};
	findMaxInRows(arr);
	return 0;
}

