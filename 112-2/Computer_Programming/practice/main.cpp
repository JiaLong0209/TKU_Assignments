#include "./include.h"

void Test_sqaure();
void Test_mode_enum();

int main(){
	Test_mode_enum();
	return 0;
}


void Test_mode_enum(){
	Mode m = Mode::hard;
	printf("Mode = %d \n", m);

	switch (m){
		case Mode::easy:
			printf("Mode: easy \n");
		break;

		case Mode::normal:
			printf("Mode: normal \n");
		break;

		case Mode::hard:
			printf("Mode: hard \n");
		break;

	}
}

void Test_sqaure(){
	const int x = 200;
	const int square_x = square(x);
	printf("%d\n", square_x);
}

