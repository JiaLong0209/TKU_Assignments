#include <stdio.h>
#include "./isPrime.h"

int main(){
	int n = 6;
	int max = 100000;
	while(n <= max){

		bool find = false;
		printf("-----------------------\n");
		printf("n = %d \n", n);

		for(int i = 2; i <= n/2; i++){
			int b = n - i;
			printf("%d %d\n",i, b);

			if(isPrime(i) && isPrime(b)){
				find = true;
				printf("find: %d, %d! \n", i, b);
				break;
			}
		}

		if(!find){
			break;
		}else{
			n += 2;
		}

	}
	return 0;
}



