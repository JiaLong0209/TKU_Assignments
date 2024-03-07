#include <stdio.h>
#include "../week2/hello.h"

extern void pass();
extern void hello();

void pass(int score){
	static int totalPass = 0;
	if(score >= 60){
		totalPass += 1;
		printf("Pass! \n");
	}else{
		printf("Failed! \n");
	}
	printf("Total pass: %d \n \n", totalPass);

}


int main(){
	int scores[] = {30,60,70,5,100};
	hello();
	for(int i = 0; i < 5; i++){
		printf("Score: %d\n", scores[i]);
		pass(scores[i]);
	}

	return 0;
}

