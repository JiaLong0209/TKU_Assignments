
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h> // rand()

#define SIZE 10

void print_maltiplication_table();
bool is_negative(int a, int b);
int add_two_integer(int a, int b);
int generate_random_number(int min, int max);
int factorial(int n);

/*  Why 0! = 1: 
        If we set n=1, then 1! = 1 * (1-1)!, or 1! = 1 * 0!.
        Since 1! is equal to 1, the equation becomes 1 = 1 * 0!.
        To solve for 0!, you would divide both sides by 1, resulting in 0! = 1. 
*/

int factorial(int n){
    return n < 2 ? 1 : n * factorial(n - 1) ;
}

void generate_array(int array[], int size = 10, int start = 1 , int end = 50){
    for (int i = 0; i < size; i++){
        array[i] = generate_random_number(start, end);
    }
}

void print_array(int array[], int size = 10){
    for(int i = 0; i < size; i++){
        printf("%d ", array[i]);
    }
}

void pass_by_value (int number){
    number = number * 10;
    printf("%d \n",  number);
    return;
}

void pass_by_address (int* number){
    *number = *number * 10;
    printf("%d \n",  *number);
    return;
}
void pass_by_value_address_test(){
    int number = 1;
    int n = 5;

    
    printf("pass_by_value: \n");
    for (int i =0; i < n; i++){
        pass_by_value(number);
    }

    printf("\npass_by_address: \n");
    for (int i =0; i < n; i++){
        pass_by_address(&number);
    }
}


void generate_array_with_pointer(int* array, int size){
    for (int i = 1; i <= size; i++){
        *(array+i) = i;
    }
}

void print_array_with_pointer(int* array, int size){
    for (int i = 1; i <= size; i++){
        printf("%d", *(array + i));
    }
}


void array_test(){
    int array[SIZE];
    generate_array(array, SIZE, 1, 50);
    print_array(array, SIZE);
}

void pointer_test (){
    int number = 5;
    int *number_ptr = &number;

    printf("number_ptr: %p \n", number_ptr);
    printf("Address of number_ptr: %p \n", &number_ptr);
    printf("number_ptr: %p \n", *&number_ptr);
    printf("number_ptr: %p \n", &*number_ptr);
    printf("%d \n", *number_ptr);

}

int main(){
    srand(0);

    int array[SIZE];
    pointer_test();
    // generate_array_with_pointer(array, SIZE);
    // print_array_with_pointer(array, SIZE);

    // for (int i=1; i <= SIZE; i++){
        // printf("%d \t", factorial(i));
        // printf("%d ", generate_random_number(10, 20));
    // }

    return 0;
}

int generate_random_number(int min, int max){
    return min + (rand() % (max - min + 1));
}

int add_two_integer(int a, int b){
    // static use the memory continuously
    static int index = 1; 
    index ++;
    printf("%d\n", index);
    return a + b;
}

bool is_negative(int a, int b){
    int diff = a - b;
    if(diff < 0){
        printf("Negative \n", diff);
    }else if (diff > 0){
        printf("Positive \n", diff);
    }else{
        printf("0 \n", diff);
    }
    return diff;
}

void print_maltiplication_table(){
    int row, col = 0; 
    for(row = 2; row < 10; row++){
        for(col = 1; col < 10; col++){
            if(row * col == 25){
                printf("\t");
                break;
            }
            else{
                printf("%d \t", row * col);
            }

        }
        printf("\n");
    }
    return;
}


/*

Naming Convention:

function: min with lowercase, use camelCase or snake_case
class: min with Uppercase


&&: Conjunction
||: Disjunction

01
11

*/

