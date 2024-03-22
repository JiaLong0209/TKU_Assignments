#include <stdio.h>
// Include the above library.
//
#include "try_catch.h"

int main(void)
{
    TRY
        THROW(2);
        printf("Hello World\n");
    CATCH(1)
        printf("Something wrong\n");
    CATCH(2)
        printf("More thing wrong\n");
    CATCH(3)
        printf("Yet another thing wrong\n");
    FINALLY
        printf("Clean resources\n");
	ETRY

    return 0;
}

