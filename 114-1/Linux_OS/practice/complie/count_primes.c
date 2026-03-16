
#include <stdio.h>
#include <stdbool.h>

extern int is_prime_(int *n);

// bool is_prime(int num){ 
//   if (num < 2) return false;
//   for (int i = 2; i * i <= num; i++){
//     if (num % i == 0){
//       retun false;
//     }
//   }
//   return true;
// }


int main(int argc, char *argv[]){
  if (argc != 2) {

      printf("Usage: %s <positive_integer> \n", argv[0]);
  }

  int n = atoi(argv[1]);
  if (n < 2) {
    printf("Number of prime numbers between 0 and %d is: 0 \n", n);
  }

  int count = 0;
  for (int i = 2; i <= n; i++){
    if (is_prime(i)){
      count++;
    }
  }

  printf("Number of prime numbers between 0 and %d is: 0 \n", count);
  return 0;
}


