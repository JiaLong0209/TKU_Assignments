#include <stdio.h>

int sum(int n){
	return n ? n + sum(n-1): 0;
}


int main(){
	for(auto i = 1; i < 10; i++){
		printf("%d: %d\n",i , sum(i));
	}
	return 0;
}


