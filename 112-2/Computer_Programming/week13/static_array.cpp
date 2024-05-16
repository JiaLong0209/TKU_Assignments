#include <stdio.h>
#include <iostream>
#define size 3

void static_array(void);
void automatic_array(void);



int main(){
	static_array();
	static_array();
	automatic_array();
	automatic_array();
	return 0;
}

void static_array(void) {
	static int a[3];
	for(int i = 0; i < size; i++) a[i] += 1;
	for(auto i : a) printf("%d ", i);
	printf("\n");
	
}


void automatic_array(void) {
	int a[3] = {0};
	for(int i = 0; i < size; i++) a[i] += 1;
	for(auto i : a) std::cout << i << " ";
	printf("\n");
	
}
