#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	srand(time(NULL));
	char choices[] = "srp";
	char choice;

	do{
		int n = -1, r = rand() % 3;
		printf("Please enter s(scissor),r (rock), p(paper), q(quit): ");
		scanf(" %c", &choice); 
		printf("Computer chose: %c\n", choices[r]);

		switch(choice){
			case 's':
				n = 0;
				printf("You chose SCISSOR! \n");
				break;
			case 'r':
				n = 1;
				printf("You chose ROCK! \n");
				break;
			case 'p':
				n = 2;
				printf("You chose PAPER! \n");
				break;
			case 'q':
				printf("Quit! \n");
				return 0;
			default:
				printf("Invalid! \n");
				break;
		}

		if((r > n && !(r == 2 && n == 0)) || (r == 0 && n == 2)){
			printf("You lose! \n");
		}else if(r == n){
			printf("Same \n");
		}else if((r < n && !(r == 0 && n == 2)) || (r == 2 && n == 0)){
			printf("You win! \n");
		}

	} while(choice != 'q');
	return 0;
}

