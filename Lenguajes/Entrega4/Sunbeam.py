#Proyecto Lenguajes y traductores
import ply.lex as lex
import ply.yacc as yacc
import sys

reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
	'dwhile' : 'DWHILE',
	'for' : 'FOR',
	'until' : 'UNTIL',
	'function' : 'FUNCTION',
	'int' : 'INT',
	'fl' : 'FL',
	'and': 'AND',
	'or' :'OR'
 }

tokens = [
	'MAIN',
	'BEGIN',
	'END',
	'ID',
	'NUMBER', 
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
	'COLON',
	'SEMICOLON',
	'EQUAL',
	'PIPE',
	'GT',
	'LT',
	'ET',
	'CTE_INT',
	'CTE_FL',
	'CHAR',
	'COMA'

] + list(reserved.values())

t_ignore  = r' '
t_ignore  = ' \t'
t_ignore_COMMENT = r'\#.*'

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_COMA    = r'\,'

def t_MAIN(t):
	r'main'
	t.type = 'MAIN'
	print(t.type)
	return t
def t_BEGIN(t):
	r'begin'
	t.type = 'BEGIN'
	print("BEGIN")
	return t
def t_END(t):
	r'end'
	t.type = 'END'
	print("END")
	return t
def t_LPAREN(t):
	r'\('
	t.type = 'LPAREN'
	print("LPAREN")
	return t

def t_RPAREN(t):
	r'\)'
	t.type = 'RPAREN'
	print("RPAREN")
	return t

def t_PIPE(t):
	r'\|'
	t.type = 'PIPE'
	print("PIPE")
	return t

def t_COLON(t):
	r'\:'
	t.type = 'COLON'
	print("COLON")
	return t

def t_SEMICOLON(t):
	r'\;'
	t.type = 'SEMICOLON'
	print("SEMICOLON")
	return t

def t_EQUAL(t):
	r'\='
	t.type = 'EQUAL'
	print("EQUAL")
	return t

def t_GT(t):
	r'\>'
	t.type = 'GT'
	print("GT")
	return t

def t_LT(t):
	r'\<'
	t.type = 'LT'
	print("LT")
	return t

def t_ET(t):
	r'\=='
	t.type = 'ET'
	print("ET")
	return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    print(t.type)
    return t
def t_CTE_INT(t):
	r'\d+'
	t.value = int(t.value)
	print(t.type)
	return t
def t_CTE_FL(t):
	r'\d+\.\d+'  
	t.value = float(t.value)
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
	print("Illegal characters!")
	t.lexer.skip(1)

lexer = lex.lex(optimize=1)

def p_S(p):
	'''
	S : main
	'''
	print("\tCORRECTO")

def p_main(p):
	'''
	main : MAIN LPAREN RPAREN vars MODULO main1
	'''
def p_main1(p):
	'''
	main1 : BLOQUE
	      | BLOQUE main1
	'''
def p_vars(p):
	'''
	vars  : dec1 ID EQUAL vars1 SEMICOLON vars
	      | 
	'''
def p_dec1(p):
	'''
	dec1  : TIPO COLON 
	      | 
	'''

def p_vars1(p):	
	'''
	vars1 : F
		  | F COMA ID EQUAL vars1
	'''
	
def p_MODULO(p):
	'''
	MODULO : FUNCTION ID LPAREN RPAREN vars BLOQUE END MODULO
	       | 
	'''

def p_BLOQUE(p):
	'''
	BLOQUE : BEGIN ESTATUTO BR END
		   | 
	'''
def p_BR(p):
	'''
	BR :     SEMICOLON ESTATUTO BR
	        | 
	'''

def p_ESTATUTO(p):
	'''
	ESTATUTO : vars
	         | IF LPAREN L RPAREN THEN ESTATUTO IF1
			 | WHILE LPAREN L RPAREN ESTATUTO END
			 | DWHILE ESTATUTO DW1 UNTIL ESTATUTO END
			 | FOR LPAREN vars PIPE L PIPE vars RPAREN ESTATUTO END
		 	 | BLOQUE
			 | 
	'''
def p_IF1(p):
	'''
	IF1 : ELSE ESTATUTO
		| 
	'''
def p_DW1(p):
	'''
	DW1 : SEMICOLON ESTATUTO DW1
	    | 
	'''
def p_X(p):
	'''
	X : MAIN
	  | BEGIN
	  | END
	'''

def p_F(p):
	'''
	F : IDCTE
	  | LPAREN E RPAREN
	'''

def p_E(p):
	'''
	E : T
	  | T PLUS E
	  | T MINUS E
	'''
def p_T(p):
	'''
	T : F 
	  | F TIMES T
	  | F DIVIDE T
	'''

def p_IDCTE(p):
	'''
	IDCTE : ID
		  | CTE_INT
		  | CTE_FL
	'''

def p_TIPO(p):
	'''
	TIPO : INT
		 | FL
		 | CHAR
	'''

def p_L(p):
	'''
	L : ID OPRL ID
	  | LPAREN D RPAREN
	'''

def p_D(p):
	'''
	D : L
	  | L D1
	'''
def p_D1(p):
	'''
	D1 : OR L
	   | AND L
	   | 
	'''

def p_OPRL(p):
	'''
	OPRL : GT
		 | LT
		 | ET
	'''

def p_error(p):
	print(f"Syntax error at {p.value!r}")

parser = yacc.yacc()

while True:
	try:
		s = input('sunbeam > ')
	except EOFError:

		break
	parser.parse(s)
