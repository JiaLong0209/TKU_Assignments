#include <stdio.h>

void printDiamond(int n){
	int mid = n/2;
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < n; j++){
			switch((int)(i <= mid)){
				case 1:
					if(j < (mid - i) || j > (mid + i)){
						printf(" ");
					}else {
						printf("*");
					}
				break;

				case 0:
					if(j < (i - mid) || j > (n + mid - i - 1)){
						printf(" ");
					}else {
						printf("*");
					}
				break;
			}
		}

		printf("\n");
	}
}

int main(){
	int n = 5;
	printDiamond(n);
	return 0;
}
