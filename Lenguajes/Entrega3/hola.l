%{
	#include "hola.tab.h"
%}

%%

"hola"						{printf("HOLA\n"); return HOLA;}
"que"						{printf("QUE\n"); return QUE;}
"tal"						{printf("TAL\n"); return TAL;}
","						{printf(", \n"); return COMA;}
[ \t\n]						;
.						{ECHO; yyerror("ERROR\n");}

%%

int yywrap()
{
	return 1;
}