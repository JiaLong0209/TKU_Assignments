#include <stdarg.h>
#include <stdio.h>
#include <time.h>

#ifdef __GNUC__
    __attribute__((format(printf, 1, 2)))
#endif

void PrintErrorMsg(const char* fmt, ...)
{
	time_t     now; 
	char       buffer[20];
	va_list    args;

    va_start(args, fmt);
    time(&now);
    strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", gmtime(&now));
    fprintf(stderr, "[%s] ", buffer); // print time
    vfprintf(stderr, fmt, args); // print %d, %f...
    fputc('\n', stderr);
    va_end(args);
}


int main(){
	int a = 3, b = 10;
	PrintErrorMsg("%d %d", a, b);
}
