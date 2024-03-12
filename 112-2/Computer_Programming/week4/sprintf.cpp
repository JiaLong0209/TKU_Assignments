#include <stdio.h>

int main(){

	int a = 1034;
	double d = 23423.523;
	char str[20];

	sprintf(str, "%d", a);
	for(int i = 0; i < 10; i++){
		printf("%c", str[i]);
	}
	puts(" ");

	sprintf(str, "%lf", d);
	for(int i = 0; i < 10; i++){
		printf("%c", str[i]);
	}
	puts(" ");

}


