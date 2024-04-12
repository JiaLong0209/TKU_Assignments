#include <stdio.h>
#include <stdlib.h>

int main(){
	int num, prev;
	printf("Enter a number: \n");
	scanf("%d", &num);
	prev = num;
	if(num != 1){
		printf("Error: It must start with 1 \n");
		return 0;
	}

	while(scanf("%d", &num)){
		if(num < prev || abs(prev - num) > 1 || num == 0){
			if(!num)
				printf("Stop program! \n"); 
			else
				printf("Error: Invalid value! \n");
			break;
		}
		prev = num;
	}
	return 0;
}
