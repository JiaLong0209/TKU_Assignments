#include <stdio.h>
#define ROW 2
#define COL 3

int mul(int A[2][3], int B[3][2]){
    int i, j, k;
    int ret[2][2];
    
    
    
    for(i = 0; i < ROW; i++){
        for(j = 0; j < COL; j++){
        	int sum = 0;
			for(k = 0; k < COL; k++){
        		sum += A[i][k] * B[k][j];
			}
			ret[i][j] = sum;	
        }
    }
    
    printf("Result: \n");
    for(i = 0; i < ROW; i++){
        for(j = 0; j < ROW; j++){
            printf("%d " , ret[i][j]);
        }
        printf("\n" , ret[i][j]);
    }
    printf("\n\n");
    
}

int main(){
    int A[2][3] = {{1,2,3},{4,5,6}};
    int B[3][2] = {{7,8}, {9,10}, {11,12}};
    mul(A,B);


    return 0;
}
