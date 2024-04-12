#include <stdio.h>

int main(){
	double a,b;
	char op;
	printf("Enter two numbers: ");
	scanf("%lf %lf", &a, &b);
	printf("Enter an operation (+,-,*,/): ");
	scanf(" %c", &op);
		
	if(op == '+'){
		printf("Result: %lf \n", a+b);
	}else if(op == '-'){
		printf("Result: %lf \n", a-b);
	}else if(op == '*'){
		printf("Result: %lf \n", a*b);
	}else if(op == '/'){
		if(b == 0){
			printf("Error: cannot division by zero\n");
		}else{
			printf("Result: %lf \n", a/b);
		}
	}

	return 0;
}	







