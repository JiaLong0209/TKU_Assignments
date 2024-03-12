#include <stdio.h>

int main(){
	int grade,  total, counter;
	grade = total = counter = 0;


	while(counter < 3){
		scanf("%d", &grade);
		printf("Total: %d\n", total += grade);
		counter ++;
		printf("Counter: %d\n\n", counter);
	}

	printf("%lf \n", (double) total / counter);
	return 0;

}




