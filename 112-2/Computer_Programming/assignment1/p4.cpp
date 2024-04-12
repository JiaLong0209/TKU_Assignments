#include <stdio.h>

double SI(double p , double r, double t){
	return (p*r*t) / 100;
}

int main(){
	double p,r,t;
	printf("Enter the number of P(Pricipal), R(Rate) and T(Time): ");
	scanf("%lf %lf %lf", &p, &r, &t);
	if(p < 0 || r < 0 || t < 0){
		printf("Fatal: All of the number must be positive! \n");
		return -1; 
	}else{
		printf("The simple interest is: %lf \n", SI(p, r, t));
	}
	return 0;
}



