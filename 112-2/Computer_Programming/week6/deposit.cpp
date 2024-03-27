#include <stdio.h>

int f(double p, double r, int n){
	return n >= 1 ? f(p*(1+r), r, n-1) : p;
}

int main(){
	double principal,rate,year,amount;
	// printf("Enter p, r, n: ");
	// scanf("%lf %lf %lf",&principal, &rate, &year);
	// amount = f(principal, rate, int(year));
	for(int i = 1; i <= 10; i++){
		amount = f(1000, 0.05, i);
		printf("%d. %lf \n", i, amount);
	}
	return 0;
}


