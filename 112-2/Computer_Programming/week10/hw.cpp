#include <stdlib.h>
#include <stdio.h>

typedef void (*f)();

int sum = 0;
int num = 0;

void printMenu(){
	printf("---------Menu--------- \n");
	printf("1. Add New Number \n");
	printf("2. Print Current Sum\n");
	printf("3. Reset Sum\n");
	printf("4. Exit\n");
	return ;
}

void addNumber(){
	printf("Enter a number: ");
	scanf("%d", &num);
	printf("Add %d to sum \n", num);
	sum += num;
}

void printSum(){
	printf("Current sum: %d \n", sum);
}

void resetSum(){
	printf("Reset sum to 0 \n");
	sum = 0;
}

void exitProgram(){
	printf("Exit program! \n");
	exit(0);
}

int main(){
	int choice;
	f func[4] = {&addNumber, &printSum, &resetSum, &exitProgram};
	printMenu();
	while(scanf("%d", &choice) != EOF){
		if(choice < 1 || choice > 4)
			printf("Error: Invalid choice! \n");
		else
			func[choice-1]();
		printMenu();
	}
	return 0;
}

