#include <stdio.h>
int power(int base, int exp);

int main(){
	int i,n = 10;
	for(i = 0; i <= n; i++){
		printf("2 ^ %d = %d \n", i, power(2, i));
	}
	return 0;
}

int power(int base, int exp){
	return exp ? base * power(base, exp-1) : 1 ;	
}


