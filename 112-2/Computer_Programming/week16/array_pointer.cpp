#include <stdio.h>


void const_type_const_pointer();

int main(){

    const_type_const_pointer();

    return 0;
}


void const_type_const_pointer(){
    int x = 10;
    int y = 20;

    int * const ptr = &x;
    /*const int *ptr = &x;*/

    *ptr = 11;
    /*ptr = &y;*/
    

    printf("%d \n", *ptr);
}








