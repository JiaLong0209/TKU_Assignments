#include <stdio.h>
typedef double (*f)(double, double);

double add(double a, double b){ return a+b; }
double minus(double a, double b){ return a-b; }
double multiply(double a, double b){ return a*b; }
double devide(double a, double b){ return a/b; }

int main(){
	double a,b;
	char op;

	printf("Input two num and an operator: ex. 10 * 20\n");
	
	scanf("%lf %c %lf", &a, &op, &b);
	double result = 0;

	switch (op) {
		case '+':
			result = add(a,b);
		break;
		case '-':
			result = minus(a,b);
		break;
		case '*':
			result = multiply(a,b);
		break;
		case '/':
			result = devide(a,b);
		break;
		default:
			printf("Invalid operator!\n");
		break;
	}
	printf("Result: %lf \n", result);

	return 0;
}



