#include <stdio.h>

int fib(int n);

int main(){
	int i,k = 10;
	for(i = 0; i <= k; i++){
		printf("fib(%d) = %d \n", i, fib(i+1));
	}
    return 0;
}

int fib(int n){
    int arr[n];
    int i;
    for(i = 0; i < n; i++){
		if(i == 0){
			arr[i] = 0;
		}else if(i == 1){
			arr[i] = 1;
		}else{
            arr[i] = arr[i-1] + arr[i-2];
        }
    }
    return arr[n-1];
}

