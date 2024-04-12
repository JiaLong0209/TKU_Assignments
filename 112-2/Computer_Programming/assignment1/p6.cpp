#include <stdlib.h>
#include <stdio.h>

void printMenu(){
	printf("---------Menu--------- \n");
	printf("1. Add New Number \n");
	printf("2. Print Current Sum\n");
	printf("3. Reset Sum\n");
	printf("4. Exit\n");
	return ;
}

void addNumber(int *sum, int *num){
	printf("Enter a number: ");
	scanf("%d", num);
	printf("Add %d to sum \n", *num);
	*sum += *num;
}

void printSum(int *sum){
	printf("Current sum: %d \n", *sum);
}

void resetSum(int *sum){
	printf("Reset sum to 0 \n");
	*sum = 0;
}

void exitProgram(){
	printf("Exit program! \n");
	exit(0);
}

int main(){
	int choice, n, sum = 0; 
	printMenu();
	while(scanf("%d", &choice) != EOF){
		switch(choice){
			case 1: addNumber(&sum, &n); break;
			case 2: printSum(&sum); break;
			case 3: resetSum(&sum); break;
			case 4: exitProgram(); break;
			default: printf("Error: Invalid choice! \n"); break;
		}
		printMenu();
	}
	return 0;
}

