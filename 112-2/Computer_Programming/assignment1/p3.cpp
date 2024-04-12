#include <stdio.h>
#include <time.h>
#include <stdlib.h>

void error(int *num){
	printf("Error: number must be between 1 ~ 100\n");
	(*num)--;
}

int main(){
	srand(time(0));
	int target = (rand() % 100) + 1;
	int guess, times = 0;
	// printf("%d \n", target);

	do{

		times++;
		printf("------------------------------\n");
		printf("Number of guesses: %d \n", times);	

		if(times > 5){
			printf("You loss ! \n");
			printf("The correct answer is: %d \n", target);
			return 0;
		}

		printf("Guess the number (1 ~ 100): ");	
		scanf("%d", &guess);
		
		if(guess > 100 || guess < 1)
			error(&times);
		else if(guess == target)
			goto WIN;
		else if (guess < target)
			printf("Too low \n");
		else
			printf("Too high \n");
		
		
	}while(target != guess);

	WIN:
		printf("You win! \n");

	return 0;
}


