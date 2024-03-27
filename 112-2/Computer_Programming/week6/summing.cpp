#include<stdio.h>

int sum_even(int l,int r){
	int sum = 0;
	for(int i = l; i <= r; sum += i, i += 2); 
	return sum;
}

int main(){
	printf("%d \n", sum_even(2, 100));
	return 0;
}





