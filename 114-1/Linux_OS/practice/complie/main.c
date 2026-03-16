// https://www.youtube.com/watch?v=XJC5WB2Bwrc&list=PL69RK6z-MTN8vKHTakRam5ojSz1yYdCDK&index=13
//
/*
  gcc main.c -o main -save-temps

    pre-processor -> main.i ->
    compiler -> main.o ->
    assembler -> main.s ->
    linker -> main ->

*/

#include <stdio.h>
#include <stdbool.h>



extern int is_prime(int n);

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

  int n = 100;

  if (n < 2) {
    printf("Number of prime numbers between 0 and %d is: 0 \n", n);
  }

  int count = 0;
  for (int i = 2; i <= n; i++){
    if (is_prime(i)){
      count++;
    }
  }

  printf("Number of prime numbers between 0 and %d is: %d \n", n,  count);

#ifdef _WIN32
    printf("Windows \n");

#elif __linux__
    printf("Linux \n");

#elif __APPLE__
    printf("APPLE \n");

#else 
    printf("unknown \n");

#endif

  return 0;


}
