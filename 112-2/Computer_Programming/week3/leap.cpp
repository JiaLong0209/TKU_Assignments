#include <stdio.h>
#include <stdbool.h>
#define i int
#define f double
#define m main
#define r return
#define p printf
#define s scanf
#define e else
#define b bool

i m(){
	i y;
	b l;
	p("Enter years: ");
	s("%d", &y);
	l = (y % 4 == 0 && y % 100 != 0) || (y % 400 == 0);
	if(l) p("%d is leap \n", y);
	e p("%d is not leap \n", y);
	r 0;
}

