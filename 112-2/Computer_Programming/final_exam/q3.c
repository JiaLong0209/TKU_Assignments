#include <stdio.h>

int digits(int n){
    int t = 0;
    if(n < 0) n = -n;
    while(n /= 10) t ++; 
    return t+1;
}

int main(){
    int n;
    scanf("%d", &n);
    printf("Digits of %d is %d\n", n, digits(n));
    return 0;
}
