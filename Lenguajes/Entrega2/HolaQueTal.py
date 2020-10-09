#Proyecto Lenguajes y traductores
import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = [
	'HOLA',
	'COMA',
	'QUE',
	'TAL'
]

t_ignore = r' '

def t_HOLA(t):
	r'hola'
	t.type = 'HOLA'
	print("HOLA")
	return t

def t_COMA(t):
	r','
	t.type = 'COMA'
	print(",")
	return t

def t_QUE(t):
	r'que'
	t.type = 'QUE'
	print("QUE")
	return t

def t_TAL(t):
	r'tal'
	t.type = 'TAL'
	print("TAL")
	return t

def t_error(t):
	print("Illegal characters!")
	t.lexer.skip(1)

lexer = lex.lex(optimize=1)

def p_S(p):
	'''
	S : X QUE TAL
	'''
	print("\tCORRECTO")

def p_X(p):
	'''
	X : HOLA Y
	'''

def p_Y(p):
	'''
	Y : COMA HOLA Y
	  | 
	'''
def p_error(p):
	print("\tINCORRECTO")

parser = yacc.yacc()

while True:
	try:
		s = input('')
	except EOFError:
		break
	parser.parse(s)