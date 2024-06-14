#include <stdio.h>

int digits(int n);

int main(){
	int i,n;
	printf("Please enter an integer: ");
    scanf("%d", &n);
    
    printf("The digits of %d is %d\n",n, digits(n));
    
	
    return 0;
}

int digits(int n){
    int t = 0;
	if(n < 0){
        n = -n;
    }
    while(n /= 10){
    	t++;
	}

    return t+1;
}

