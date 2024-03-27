#include <stdio.h>
int main(){
	for(int i = 2; i <= 9; i++) for(int j = 1; j <= 9; j++) printf("%d*%d=%d%s", i, j, i*j, j == 9 ? "\n" : " | ");
}


