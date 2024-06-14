#include <stdio.h>


int fib(int n){
    int arr[n];
    for(int i = 0; i <= n ; i++){
        if(i <= 1) arr[i] = i;
        else arr[i] = arr[i-1] + arr[i-2];
    }
    return arr[n-1];
}

int main(){
    for(int i = 0; i < 10; i++){
        printf("fib(%d) = %d \n", i, fib(i+1));
    }
    return 0;
}




