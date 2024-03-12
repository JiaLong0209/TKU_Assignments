#include <stdio.h>

int fac(int n){
	return n > 0 ? fac(n-1) * n : 1;
}

int main() {
	for(int i = 1; i <= 20; i++){
		printf("fac(%d) = %d \n",i , fac(i));
	}
}

