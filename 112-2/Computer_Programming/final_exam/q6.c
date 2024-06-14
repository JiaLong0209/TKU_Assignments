#include <stdio.h>
#define ROW 2
#define COL 3

int (*mul(int A[ROW][COL], int B[COL][ROW])) [ROW]{
    static int ret[ROW][ROW];
    for(int i = 0; i < ROW; i++){
        for(int j = 0; j < ROW; j++){
            int sum = 0;
            for(int k = 0; k < COL; k++) sum += A[i][k] * B[k][j];
            ret[i][j] = sum;
        }
    }
    return ret;
}

int main(){
    int a[ROW][COL] = {{1,2,3},{4,5,6}};
    int b[COL][ROW] = {{7,8}, {9, 10}, {11, 12}};
    int (* ret)[ROW] = mul(a, b);

    printf("Result: \n");
    for(int i = 0; i < ROW; i++){
        for(int j = 0; j < ROW; j++){
            printf("%d ", ret[i][j]);
        }
        printf("\n");
    }
    printf("\n\n");

    return 0;
}


