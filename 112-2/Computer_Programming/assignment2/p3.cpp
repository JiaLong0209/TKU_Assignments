#include <stdio.h>

int main(){
	char color;
	printf("Enter the color of traffic light (R,G,Y): ");
	scanf("%c", &color);

	switch(color){
		case 'r':
		case 'R':
			printf("Stop\n");
		break;

		case 'y':
		case 'Y':
			printf("Slow\n");
		break;

		case 'g':
		case 'G':
			printf("Go\n");
		break;

		default:
			printf("Error: Invalid input!\n");
		break;
	}

	return 0;
}



