#include <stdio.h>

int* linear_search( int * arr, const int value, const int size);

int main(){
    int arr[10] = {1,2,5,6,7,10,20,30,40,20};
    int size = sizeof(arr) / sizeof(*arr);
    int *ret = linear_search(arr, 5, size);

    printf("%p \n", ret);
    printf("%d \n", *ret);
    

    return 0;
}

int* linear_search(int * arr, const int value, const int size){
    for(int i = 0; i < size; i++){
        if(value == *(arr+i)) return (arr+i);
    }

    return NULL;

}







