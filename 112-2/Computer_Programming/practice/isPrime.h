#include <stdio.h>

bool isPrime(int n){
	bool flag = true;
	for (int i = 2; i < n; i++){
		if( !(n % i) ){
		 	flag = false;
		}
	}

	return flag;
}




