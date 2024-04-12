#include <stdio.h>

int fun(){
	static int a = 0;
	a += 1;
	return a;
}

int main(){

	printf("%d\n", fun());
	printf("%d\n", fun());
	return 0;
}








