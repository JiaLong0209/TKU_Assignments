#include <stdio.h>
#define ROW 2
#define COL 3

void gen_array(int array[][COL]);
void print_array(int array[][COL]);
void transpose_array(int array[][COL], int temp_array[][ROW]);
void print_transposed_array(int array[][ROW]);

int main(){
	int arr[ROW][COL];
	int trans_arr[COL][ROW];
	gen_array(arr);
	print_array(arr);
	transpose_array(arr, trans_arr);
	print_transposed_array(trans_arr);

}

void gen_array(int array[][COL]){

	for(int i = 0 ; i < ROW; i++){
		for(int j = 0; j < COL; j++){
			array[i][j] = j +1 + i * 3;
		}
	}
}


void print_array(int array[][COL]){

	for(int i = 0 ; i < ROW; i++){
		for(int j = 0; j < COL; j++){
			printf("%d ", array[i][j]);
		}
		printf("\n");
	}
}

void print_transposed_array(int array[][ROW]){

	for(int i = 0 ; i < COL; i++){
		for(int j = 0; j < ROW; j++){
			printf("%d ", array[i][j]);
		}
		printf("\n");
	}

}

void transpose_array(int array[][COL], int temp_array[][ROW]){

}
