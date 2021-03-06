#Proyecto Lenguajes y traductores
import ply.lex as lex
import ply.yacc as yacc
import sys
import symboltable

global st
st = symboltable.SymbolTable()
global auxT
global auxID
global pOps
pOps=[]
global avTmps
avTmps=[]
global avTmpsCount
avTmpsCount=0
global contadortmp
contadortmp=0
global countIDCTE
countIDCTE=0
global countF
countF=0



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
	'CTE_FL',
	'CTE_INT',
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
	#print(t.type)
	return t
def t_BEGIN(t):
	r'begin'
	t.type = 'BEGIN'
	#print("BEGIN")
	global contadortmp
	contadortmp=contadortmp+1
	return t
def t_END(t):
	r'end'
	t.type = 'END'
	#print("END")
	return t
def t_LPAREN(t):
	r'\('
	t.type = 'LPAREN'
	#print("LPAREN")
	return t

def t_RPAREN(t):
	r'\)'
	t.type = 'RPAREN'
	#print("RPAREN")
	return t

def t_PIPE(t):
	r'\|'
	t.type = 'PIPE'
	#print("PIPE")
	return t

def t_COLON(t):
	r'\:'
	t.type = 'COLON'
	#print("COLON")
	return t

def t_SEMICOLON(t):
	r'\;'
	t.type = 'SEMICOLON'
	#print("SEMICOLON")
	return t

def t_EQUAL(t):
	r'\='
	t.type = 'EQUAL'
	#print("EQUAL")
	return t

def t_GT(t):
	r'\>'
	t.type = 'GT'
	#print("GT")
	return t

def t_LT(t):
	r'\<'
	t.type = 'LT'
	#print("LT")
	return t

def t_ET(t):
	r'\=='
	t.type = 'ET'
	#print("ET")
	return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    #print(t.type)
    return t

def t_CTE_FL(t):
	r'\d+\.\d+'  
	t.value = float(t.value)
	#print(t.type)
	return t

def t_CTE_INT(t):
	r'\d+'
	t.value = int(t.value)
	#print(t.type)
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
	print("--- Tabla de simbolos ---")
	print(f'Var\tTipo')
	st.listSTable()
	print("\t\t\t\t Sintaxis Correcto")
	print(st.symbols)
	print(pOps)

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
	vars  : dec1 vars0 vars
	      |
	'''

def p_vars0(p):
	'''
	vars0  : ID EQUAL F SEMICOLON
	       |
	'''
	global auxID
	auxID = p[1]
	global sym
	sym=symboltable.Symbol(auxID,auxT)
	st.put(sym)

def p_dec1(p):
	'''
	dec1  : TIPO COLON 
	      | 
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

def p_IDCTE(p):
	'''
	IDCTE : ID
		  | CTE_INT
		  | CTE_FL
	'''
	global pOps
	global st
	global contadortmp
	if (len(p)==2):
		p[0]=p[1]
		tmp1=p[1]                                                 
		pOps.append(str(tmp1))
		print(pOps)

def p_F(p):
	'''
	F : IDCTE
	  | LPAREN E RPAREN
	'''
	if (len(p)==2):
		p[0]==p[1]

def p_E(p):
	'''
	E : T
	  | T PLUS E
	  | T MINUS E
	'''
	global pOps
	global st
	global avTmps
	global avTmpsCount
	if (len(p)==2):
		p[0]==p[1]
	if (len(p)==4):
		if len(pOps)>1:
			op2=pOps.pop()
			op1=pOps.pop()
			if (p[2]=="+"):
				print(f'+ {op1} {op2} T{avTmpsCount}')
				avTmps.append(1) # en vez de 1, va el resultado
				pOps.append("T") #insert(0,avTmps[-1]) 
				print(pOps)
			elif (p[2]=="-"):
				print(f'- {op1} {op2} T{avTmpsCount}')
				avTmps.append("T") # aqui va el resultado
				pOps.append(avTmps[-1]) # insert(0,avTmps[-1])  
				print(pOps)
			avTmpsCount=avTmpsCount+1
			
def p_T(p):
	'''
	T : F 
	  | F TIMES T
	  | F DIVIDE T
	'''
	global pOps
	global st
	global avTmps
	global avTmpsCount
	if (len(p)==4):
		op1=pOps.pop(0)
		op2=pOps.pop(0)
		if (p[2]=="*"):
			print(f'+ {op1} {op2} T{avTmpsCount}')
			avTmps.append(1) # en vez de 1, va el resultado
			pOps.insert(0,avTmps[-1])
			print(pOps)
		elif (p[2]=="/"):
			print(f'/ {op1} {op2} T{avTmpsCount}')
			avTmps.append(1) # aqui va el resultado
			pOps.insert(0,avTmps[-1])
			print(pOps)
		avTmpsCount=avTmpsCount+1


def p_TIPO(p):
	'''
	TIPO : INT
		 | FL
	'''
	global auxT
	auxT = p[1]

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

