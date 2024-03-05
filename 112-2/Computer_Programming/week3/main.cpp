#include <stdio.h>
#include "../week2/hello.h"

int main(){
	int score = 59;
	printf("%d\n", (--score)++);
	printf("%d\n", (++score)--);
	if(score >= 60){
		hello();
	}
	return 0;
}



