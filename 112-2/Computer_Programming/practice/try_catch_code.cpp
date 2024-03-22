
#include <stdio.h>
#include <setjmp.h>

int main(void)
{
    do {
        jmp_buf ex_buf__;
        switch (setjmp(ex_buf__)) {
        case 0:
            while (1) {
            longjmp(ex_buf__, 2);
            printf("Hello World\n");
            break;
        case 1:
            printf("Something wrong\n");
            break;
        case 2:
            printf("More thing wrong\n");
            break;
        case 3:
            printf("Yet another thing wrong\n");
            break;
            }
        default:{
            printf("Clean resources\n");
            break;
            }
        }
    } while (0);

    return 0;
}

