#include <stdio.h>

int main(){
	char choice;
	do{

		// scanf("Please enter r(rock), p(paper), s(scissor), q(quit) %c", &c);
		printf("Please enter r(rock), p(paper), s(scissor), q(quit): ");
		//
		// Add space before %c to consume the newline character.
		scanf(" %c", &choice); 

		switch(choice){
			case 'r':
				printf("You chose ROCK! \n");
				break;
			case 'p':
				printf("You chose PAPER! \n");
				break;
			case 's':
				printf("You chose SCISSOR! \n");
				break;
			case 'q':
				printf("Quit! \n");
				break;
			default:
				printf("Invalid! \n");
				break;
		}

	} while(choice != 'q');
	return 0;
}

