#include <stdio.h>


int square(int *a){
	*a = *a * *a;
	return *a;
}


int main(){
	int var = 10;
	int *varPtr = &var;
	int **varPtrPtr = &varPtr;
	int ***varPtrPtrPtr = &varPtrPtr;
	int ****varPtrPtrPtrPtr = &varPtrPtrPtr;

	square(&var);

	// var
	printf("Value: %d \n", var);
	printf("Address of var: %p \n", &var);
	printf("Size: %lu \n", sizeof(var));
	printf("\n");


	// varPtr
	printf("Value of var: %d \n", *varPtr);
	printf("Value of varPtr: %p \n", varPtr);
	printf("Value of varPtr: %p \n", &*&*&*varPtr);
	printf("Address of varPtr: %p \n", &varPtr);
	printf("Size varPtr: %lu \n", sizeof(varPtr));
	printf("\n");


	// varPtrPtr
	printf("Value of var: %d \n", **varPtrPtr);
	printf("Value of varPtr: %p \n", *varPtrPtr);
	printf("Value of varPtrPtr: %p \n", varPtrPtr);
	printf("Address of varPtrPtr: %p \n", &varPtrPtr);
	printf("\n");


	// varPtrPtrPtr
	printf("Value of var: %d \n", ***varPtrPtrPtr);
	printf("Value of varPtr: %p \n", **varPtrPtrPtr);
	printf("Value of varPtrPtr: %p \n", *varPtrPtrPtr);
	printf("Value of varPtrPtrPtr: %p \n", varPtrPtrPtr);
	printf("Address of varPtrPtrPtr: %p \n", &varPtrPtrPtr);
	printf("\n");


	// varPtrPtrPtrPtr
	printf("Value of var: %d \n", **&*&**&*&*&**&*&*&*&*varPtrPtrPtrPtr);
	printf("Value of var: %d \n", ****varPtrPtrPtrPtr);
	printf("Value of varPtr: %p \n", ***varPtrPtrPtrPtr);
	printf("Value of varPtrPtr: %p \n", **varPtrPtrPtrPtr);
	printf("Value of varPtrPtrPtr: %p \n", *varPtrPtrPtrPtr);
	printf("Value of varPtrPtrPtrPtr: %p \n", varPtrPtrPtrPtr);
	printf("Address of varPtrPtrPtrPtr: %p \n", &varPtrPtrPtrPtr);
	printf("\n");


	return 0;
}

