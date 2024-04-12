#include <stdio.h>

int main(){
	int n;
	scanf("%d",&n);
	for(int i = 0; i < n; i++){
		int a,b, sum=0;
		scanf("%d %d", &a, &b);
		for(int j = a; j <= b; j++){
			if(j % 2) sum+=j;
		}
		printf("Case %d: %d\n", i+1, sum);
	}
	return 0;
}


