#include <stdio.h>


int power(int base, int exp){
    return exp ? base * power(base, exp-1) : 1;
}

int main(){
    for(int i = 0; i < 10; i ++){
        printf("2 ^ %d = %d\n", i, power(2, i));
    }
    return 0;
}



