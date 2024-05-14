#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 10

int main(){
	srand( time(NULL));

	int n = SIZE;
	char arr[SIZE][SIZE];

	for(int i = 0; i < n; i++){
		for(int  j = 0; j < n; j++){
			arr[i][j] = '.';
		}
	}

	while(n){
		int x = rand() % SIZE;
		int y = rand() % SIZE;
		if(arr[x][y] != '*'){
			arr[x][y] = '*';
			n--;
		}
	}


	for(int i = 0; i < SIZE; i++){
		for(int  j = 0; j < SIZE; j++){
			printf("%c ", arr[i][j]);
		}
		printf("\n");
	}
	return 0;
}

