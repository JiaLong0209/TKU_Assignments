#include <stdio.h>
#include <time.h>
#include <stdlib.h>

void bubbleSort(int* m, int n);
void printArray(int* m, int n);
void randomArray(int *m, int n);
void round(int* m, int n, int times);


int main(){
	int n = 10;
	srand(time(NULL));
	static int m[10];
	round(m, n, 10);
	return 0;
}

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

void printArray(int* m, int n){
	for(int i = 0; i < n; i++) printf("%3d ", m[i]);
	printf("\n");
}

void randomArray(int *m, int n){
	for(int i = 0; i < n; i++) m[i] = (rand() % 100) + 1;
}


void round(int*m ,int n, int times){
	
	for(int i = 0; i < times; i++){
		printf("\n----------Round %d-----------\n", i+1);
		randomArray(m, n);
		printArray(m, n);
		bubbleSort(m, n);
		printArray(m, n);
	}
}
