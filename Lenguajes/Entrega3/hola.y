%{
	#include <stdio.h>
	#include <stdlib.h>
	#include <string.h>
	void yyerror (char *s);
%}

%union
{
	char *string;
}

%start S
%token <string> HOLA QUE TAL COMA

%type <integer> S X Y

%%

S	:	X QUE TAL		{printf("\nCORRECTO");}
		;

X	:	HOLA Y			{;}
		|			{;}
		;

Y	:	COMA HOLA Y		{;}
		|			{;}
		;

%%

void yyerror (char *s) 
{
	printf("%s\n", s);
}
int main(void)
{
	return yyparse();
}