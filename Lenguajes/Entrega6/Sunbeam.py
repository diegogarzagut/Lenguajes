#Proyecto Lenguajes y traductores
import sys

import numpy as np
import ply.lex as lex
import ply.yacc as yacc

import memoryST
import symboltable

global st
st = symboltable.SymbolTable()
global globalMem
globalMem = memoryST.memoryST()
global auxT
global auxID
global pOps
pOps=[]
global avTmps
avTmps=[]
global avTmps1
avTmps1=[None]*50
global avTmpsCount
avTmpsCount=0
global contadortmp
contadortmp=0
global countIDCTE
countIDCTE=0
global countF
countF=0
global opT
global cuadruplos
cuadruplos=[]
global contCuadruplos
contCuadruplos=0
global pilaSaltos
pilaSaltos=[]
global contSaltos
contSaltos=0
global pDirVal
pDirVal=[]
global pDirValCont
pDirValCont=0
global PC
PC=0
global cTmp2
cTmp2=0
global idTmp
idTmp=None
global pProcs
pProcs=[]
global pProcsCont
pProcsCont=0
global callcont
callcont=None
global pExec
pExec=[]

		
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
	'bool': 'BOOL',
	'and': 'AND',
	'or' :'OR',
	'call':'CALL'
 }
tokens = [
	'MAIN',
	'BEGIN',
	'END',
	'ID',
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
	'COMA',
	'READ',
	'PRINT',
	'LCOR',
	'RCOR',
	'MAINF'
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
def t_READ(t):
	r'read'
	t.type = 'READ'
	#print(t.type)
	return t
def t_CALL(t):
	r'call'
	t.type = 'CALL'
	return t
def t_LCOR(t):
	r'\{'
	t.type = 'LCOR'
	#print(t.type)
	return t
def t_MAINF(t):
	r'mainf'
	t.type = 'MAINF'
	#print(t.type)
	return t
def t_RCOR(t):
	r'\}'
	t.type = 'RCOR'
	#print(t.type)
	return t
def t_PRINT(t):
	r'print'
	t.type = 'PRINT'
	#print(t.type)
	return t
def t_BEGIN(t):
	r'begin'
	t.type = 'BEGIN'
	#print("BEGIN")
	global contadortmp
	#contadortmp=contadortmp+1
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
	r'\&'
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
	global callcont; global cuadruplos; global contCuadruplos; global avTmps; global avTmpsCount; global pilaSaltos; global pDirValCont; global PC; global globalMem
	print("\t\t\t\t Sintaxis Correcto")
	print("--- Tabla de simbolos ---")
	print(f'Var  Valor  Tipo')
	#st.listSTable()
	globalMem.listMTable()
	print("\n--- Avails ---")
	tempo=0
	for x in avTmps:
		print(f'T{tempo} = {x}')
		tempo=tempo+1
	
	#print(f"\nPila Dirección-Valor: ({pDirValCont})\n")
	#y=0
	#for x in pDirVal:
	#	print(f'[{y}] = {x}')
	#	y=y+1
	print(f"\nCuadruplos: ({contCuadruplos})")
	t=0
	for x in cuadruplos:
		print(f'{t}) {x}')
		t=t+1
	print("\n--- Pila de Saltos ---\n")
	for x in pilaSaltos:
		print(x)
	print(f"\nEjecución:\n")
	PC=0
	while (PC!=-1):
		cuadruplo=cuadruplos[PC]
		opscode=cuadruplos[PC][0]
		if opscode=="ENDP":
			print("ENDP")
			PC=-1
		elif opscode=="ENDPROC":
			print("ENDPROC")
			PC=pExec.pop(0)
		elif opscode=="PRINT":
			#globalMem.listMTable()
			if isinstance(cuadruplo[1],str):
				val=globalMem.getSymVal(cuadruplo[1])
				print(f'print: val={val}')
			PC=PC+1
		elif opscode=="READ":
			val= int(input(f'{cuadruplo[1]}: '))
			if globalMem.varExists(cuadruplo[1]):
				globalMem.updateVal(cuadruplo[1],val)
			PC=PC+1
		elif opscode=="CALL":
			#callcont=PC+1
			pExec.insert(0,PC+1)
			PC=cuadruplo[1]
		elif opscode=="GOTO":
			PC=cuadruplo[1]
		elif opscode=="GTF":
			value1=cuadruplo[1]
			if len(str(value1))>1:
				if value1[0]=='T':
					tmp=value1
					tmp1=int(tmp[1:])
					value1=avTmps1[tmp1]
			if value1==False:
				print(f'{cuadruplo[1]}={value1}')
				PC=cuadruplo[2]
			else:
				PC=PC+1
			print(f'{cuadruplo[1]}={value1}')
		elif opscode=="=":
			value1=cuadruplo[1]
			svalue1=str(value1)
			if len(svalue1)>1:
				if svalue1[0]=='T':
					tmp=value1
					tmp1=int(tmp[1:])
					value1=avTmps1[tmp1] #cambie
			if globalMem.getSymType(value1)=="isvar":
				value1=globalMem.getSymVal(value1)
			dest=cuadruplo[2]
			sdest=str(dest)
			if len(sdest)>1:
				if sdest[0]=='T':
					tmp=dest
					tmp1=int(tmp[1:])
					dest=avTmps1[tmp1] #cambie
			if globalMem.varExists(dest):
				globalMem.updateVal(dest,value1)
			else:
				symMT=memoryST.Symbol_m(dest,value1,"int")
				globalMem.addSy(symMT)
			print(f'{dest}={value1}')
			PC=PC+1
		elif opscode=="+":
			tmpq1=globalMem.getSymType(cuadruplo[1])
			tmpq2=globalMem.getSymType(cuadruplo[2])
			c1=cuadruplo[1]
			c2=cuadruplo[2]
			c3=cuadruplo[3]
			tmp321=None
			if (tmpq1=="int" or tmpq1=="fl") and (tmpq2=="int" or tmpq2=="fl") : #si ambos int o float
				if len(str(c3))>1:
					if c3[0]=='T':
						tmp=c3
						tmp1=int(tmp[1:])
						tmp321=tmp1
						#print(f'PRUEBA:{c3} -> tmp321: {tmp321} tmp1: {tmp1}' )
						avTmps1[tmp321]=cuadruplo[1]+cuadruplo[2] #cambie
						#print(avTmps1)
						#avTmps1.insert(0,cuadruplo[1]+cuadruplo[2])
				print(f'{cuadruplo[1]}+{cuadruplo[2]}={avTmps[tmp1]}')
			else:
				if c3[0]=='T':
						tmp=c3
						tmp1=int(tmp[1:])
						tmp321=tmp1
				if tmpq1=="isvar":
					c1=globalMem.getSymVal(cuadruplo[1])
				if tmpq2=="isvar":
					c2=globalMem.getSymVal(cuadruplo[2])
				if isinstance(c1,str):
					if len(str(c1))>1:
						if c1[0]=='T':
							tmp=c1
							tmp1=int(tmp[1:])
							c1=avTmps1[tmp1]#cambie
				if isinstance(c2,str):
					if len(str(c2))>1:
						if c2[0]=='T':
							tmp=c2
							tmp1=int(tmp[1:])
							c2=avTmps1[tmp1]#cambie
				c3=c1+c2
				avTmps1[tmp321]=c3 #cambie
				#print(f'PRUEBA:{c3} -> tmp321: {tmp321} tmp1: {tmp1}' )
				#print(avTmps1) #cambie
				print(f'{c1}+{c2}={c3}')
			PC=PC+1
		elif opscode=='-':
			tmpq1=globalMem.getSymType(cuadruplo[1])
			tmpq2=globalMem.getSymType(cuadruplo[2])
			c1=cuadruplo[1]
			c2=cuadruplo[2]
			c3=cuadruplo[3]
			tmp321=None
			if (tmpq1=="int" or tmpq1=="fl") and (tmpq2=="int" or tmpq2=="fl") : #si ambos int o float
				if len(str(c3))>1:
					if c3[0]=='T':
						tmp=c3
						tmp1=int(tmp[1:])
						tmp321=tmp1
						avTmps1[tmp321]=cuadruplo[1]-cuadruplo[2] #cambie
						#print(f'PRUEBA:{c3} -> tmp321: {tmp321} tmp1: {tmp1}' )
						#print(avTmps1) #cambie
						#avTmps1.insert(0,cuadruplo[1]-cuadruplo[2])
				print(f'{cuadruplo[1]}-{cuadruplo[2]}={avTmps[tmp1]}')
			else:
				if c3[0]=='T':
						tmp=c3
						tmp1=int(tmp[1:])
						tmp321=tmp1
				if tmpq1=="isvar":
					c1=globalMem.getSymVal(cuadruplo[1])
				if tmpq2=="isvar":
					c2=globalMem.getSymVal(cuadruplo[2])
				if isinstance(c1,str):
					if len(str(c1))>1:
						if c1[0]=='T':
							tmp=c1
							tmp1=int(tmp[1:])
							c1=avTmps1[tmp1] #cambie
				if isinstance(c2,str):
					if len(str(c2))>1:
						if c2[0]=='T':
							tmp=c2
							tmp1=int(tmp[1:])
							c2=avTmps1[tmp1] #cambie
				c3=c1-c2
				avTmps1[tmp321]=c3 #cambie
				#print(f'PRUEBA:{c3} -> tmp321: {tmp321} tmp1: {tmp1}' )
				#print(avTmps1) #cambie
				print(f'{c1}-{c2}={c3}')
			PC=PC+1
		elif opscode=='*':
			tmpq1=globalMem.getSymType(cuadruplo[1])
			tmpq2=globalMem.getSymType(cuadruplo[2])
			c1=cuadruplo[1]
			c2=cuadruplo[2]
			c3=cuadruplo[3]
			tmp321=None
			if (tmpq1=="int" or tmpq1=="fl") and (tmpq2=="int" or tmpq2=="fl") : #si ambos int o float
				if len(str(c3))>1:
					if c3[0]=='T':
						tmp=c3
						tmp1=int(tmp[1:])
						tmp321=tmp1
						avTmps1[tmp321]=cuadruplo[1]*cuadruplo[2] #cambie
						#print(f'PRUEBA:{c3} -> tmp321: {tmp321} tmp1: {tmp1}' )
						#print(avTmps1) #cambie
				print(f'{cuadruplo[1]}*{cuadruplo[2]}={avTmps[tmp1]}')
			else:
				if c3[0]=='T':
						tmp=c3
						tmp1=int(tmp[1:])
						tmp321=tmp1
				if tmpq1=="isvar":
					c1=globalMem.getSymVal(cuadruplo[1])
				if tmpq2=="isvar":
					c2=globalMem.getSymVal(cuadruplo[2])
				if isinstance(c1,str):
					if len(str(c1))>1:
						if c1[0]=='T':
							tmp=c1
							tmp1=int(tmp[1:])
							c1=avTmps1[tmp1] #cambie
				if isinstance(c2,str):
					if len(str(c2))>1:
						if c2[0]=='T':
							tmp=c2
							tmp1=int(tmp[1:])
							c2=avTmps1[tmp1] #cambie
				c3=c1*c2
				avTmps1[tmp321]=c3 #cambie
				#print(f'PRUEBA:{c3} -> tmp321: {tmp321} tmp1: {tmp1}' )
				#print(avTmps1)#cambie
				print(f'{c1}*{c2}={c3}')
			PC=PC+1
		elif opscode=='/':
			c1=cuadruplo[1]
			c2=cuadruplo[2]
			c3=cuadruplo[3]
			tmpq1=globalMem.getSymType(cuadruplo[1])
			tmpq2=globalMem.getSymType(cuadruplo[2])
			#globalMem.listMTable()
			tmp321=None
			if (tmpq1=="int" or tmpq1=="fl") and (tmpq2=="int" or tmpq2=="fl") : #si ambos int o float
				if len(str(c3))>1:
					if c3[0]=='T':
						tmp=c3
						tmp1=int(tmp[1:])
						tmp321=tmp1
						avTmps1[tmp321]=cuadruplo[1]/cuadruplo[2] #cambie
						#print(f'PRUEBA:{c3} -> tmp321: {tmp321} tmp1: {tmp1}' )
						#print(avTmps1) #cambie
				print(f'{cuadruplo[1]}/{cuadruplo[2]}={avTmps1[tmp1]}')
			else:
				if c3[0]=='T':
						tmp=c3
						tmp1=int(tmp[1:])
						tmp321=tmp1
				if tmpq1=="isvar":
					c1=globalMem.getSymVal(cuadruplo[1])
				if tmpq2=="isvar":
					c2=globalMem.getSymVal(cuadruplo[2])
				if isinstance(c1,str):
					if len(str(c1))>1:
						if c1[0]=='T':
							tmp=c1
							tmp1=int(tmp[1:])
							c1=avTmps1[tmp1] #cambie
				if isinstance(c2,str):
					if len(str(c2))>1:
						if c2[0]=='T':
							tmp=c2
							tmp1=int(tmp[1:])
							c2=avTmps1[tmp1] #cambie
				c3=c1/c2
				avTmps1[tmp321]=c3 #cambie
				#print(f'PRUEBA:{c3} -> tmp321: {tmp321} tmp1: {tmp1}' )
				#print(avTmps1)#cambie
				print(f'{c1}/{c2}={c3}')
			PC=PC+1
		elif opscode=='AND':
			tmpq1=globalMem.getSymType(cuadruplo[1])
			tmpq2=globalMem.getSymType(cuadruplo[2])
			c1=cuadruplo[1]
			c2=cuadruplo[2]
			c3=cuadruplo[3]
			tmp321=None
			if isinstance(c1,bool) and isinstance(c2,bool): #si ambos int o float
				if len(str(c3))>1:
					if c3[0]=='T':
						tmp=c3
						tmp1=int(tmp[1:])
						tmp321=tmp1
						avTmps1[tmp1]= cuadruplo[1] and cuadruplo[2] #cambie
				print(f'AND={avTmps1[tmp1]}')#cambie
			else:
				if c3[0]=='T':
						tmp=c3
						tmp1=int(tmp[1:])
						tmp321=tmp1
				if tmpq1=="isvar":
					c1=globalMem.getSymVal(cuadruplo[1])
				if tmpq2=="isvar":
					c2=globalMem.getSymVal(cuadruplo[2])
				if isinstance(c1,str):
					if len(str(c1))>1:
						if c1[0]=='T':
							tmp=c1
							tmp1=int(tmp[1:])
							c1=avTmps1[tmp1] #cambie
				if isinstance(c2,str):
					if len(str(c2))>1:
						if c2[0]=='T':
							tmp=c2
							tmp1=int(tmp[1:])
							c2=avTmps1[tmp1] #cambie
				c3=c1 and c2
				avTmps1[tmp321]=c3 #cambie
				print(f'{c1}and{c2}={c3}')
			PC=PC+1
		elif opscode=='<':
			tmpq1=globalMem.getSymType(cuadruplo[1])
			tmpq2=globalMem.getSymType(cuadruplo[2])
			c1=cuadruplo[1]
			c2=cuadruplo[2]
			c3=cuadruplo[3]
			tmp321=None
			if (tmpq1=="int" or tmpq1=="fl") and (tmpq2=="int" or tmpq2=="fl") : #si ambos int o float
				if len(str(c3))>1:
					if c3[0]=='T':
						tmp=c3
						tmp1=int(tmp[1:])
						tmp321=tmp1
					if globalMem.getSymVal(c1)<globalMem.getSymVal(c2):
						c3=True
						print(f'{cuadruplo[1]}<{cuadruplo[2]}= True')
					else:
						c3=False
						print(f'{cuadruplo[1]}<{cuadruplo[2]}= False')
					avTmps1[tmp321]=c3 #cambie
				#print(f'{cuadruplo[1]}<{cuadruplo[2]}={avTmps[tmp1]}')
			else:
				if c3[0]=='T':
						tmp=c3
						tmp1=int(tmp[1:])
						tmp321=tmp1
				if tmpq1=="isvar":
					c1=globalMem.getSymVal(cuadruplo[1])
				if tmpq2=="isvar":
					c2=globalMem.getSymVal(cuadruplo[2])
				if isinstance(c1,str):
					if len(str(c1))>1:
						if c1[0]=='T':
							tmp=c1
							tmp1=int(tmp[1:])
							c1=avTmps1[tmp1]#cambie
				if isinstance(c2,str):
					if len(str(c2))>1:
						if c2[0]=='T':
							tmp=c2
							tmp1=int(tmp[1:])
							c2=avTmps1[tmp1]#cambie
				if c1<c2:
					print(f'{cuadruplo[1]}<{cuadruplo[2]}= True')
					c3=True
				else:
					print(f'{cuadruplo[1]}<{cuadruplo[2]}= False')
					c3=False
				avTmps1[tmp321]=c3#cambie
				#print(f'{c1}<{c2}={c3}')
			PC=PC+1
		elif opscode=='>':
			tmpq1=globalMem.getSymType(cuadruplo[1])
			tmpq2=globalMem.getSymType(cuadruplo[2])
			c1=cuadruplo[1]
			c2=cuadruplo[2]
			c3=cuadruplo[3]
			tmp321=None
			if (tmpq1=="int" or tmpq1=="fl") and (tmpq2=="int" or tmpq2=="fl") : #si ambos int o float
				if len(str(c3))>1:
					if c3[0]=='T':
						tmp=c3
						tmp1=int(tmp[1:])
						tmp321=tmp1
					if globalMem.getSymVal(c1)>globalMem.getSymVal(c2):
						c3=False
						print(f'{cuadruplo[1]}>{cuadruplo[2]}= False')
					else:
						c3=True
						print(f'{cuadruplo[1]}>{cuadruplo[2]}= True')
					avTmps1[tmp321]=c3#cambie
				#print(f'{cuadruplo[1]}{cuadruplo[2]}={avTmps[tmp1]}')
			else:
				if c3[0]=='T':
						tmp=c3
						tmp1=int(tmp[1:])
						tmp321=tmp1
				if tmpq1=="isvar":
					c1=globalMem.getSymVal(cuadruplo[1])
				if tmpq2=="isvar":
					c2=globalMem.getSymVal(cuadruplo[2])
				if isinstance(c1,str):
					if len(str(c1))>1:
						if c1[0]=='T':
							tmp=c1
							tmp1=int(tmp[1:])
							c1=avTmps1[tmp1]#cambie
				if isinstance(c2,str):
					if len(str(c2))>1:
						if c2[0]=='T':
							tmp=c2
							tmp1=int(tmp[1:])
							c2=avTmps1[tmp1]#cambie
				if c1>c2:
					print(f'{cuadruplo[1]}>{cuadruplo[2]}= True')
					c3=True
				else:
					print(f'{cuadruplo[1]}>{cuadruplo[2]}= False')
					c3=False
				avTmps1[tmp321]=c3#cambie
				#print(f'{c1}<{c2}={c3}')
			PC=PC+1
		elif opscode=='&':
			tmpq1=globalMem.getSymType(cuadruplo[1])
			tmpq2=globalMem.getSymType(cuadruplo[2])
			c1=cuadruplo[1]
			c2=cuadruplo[2]
			c3=cuadruplo[3]
			tmp321=None
			if (tmpq1=="int" or tmpq1=="fl") and (tmpq2=="int" or tmpq2=="fl") : #si ambos int o float
				if len(str(c3))>1:
					if c3[0]=='T':
						tmp=c3
						tmp1=int(tmp[1:])
						tmp321=tmp1
					if globalMem.getSymVal(c1)==globalMem.getSymVal(c2):
						c3=False
						print(f'{cuadruplo[1]}&{cuadruplo[2]}= False')
					else:
						c3=True
						print(f'{cuadruplo[1]}&{cuadruplo[2]}= True')
					avTmps1[tmp321]=c3#cambie
				#print(f'{cuadruplo[1]}{cuadruplo[2]}={avTmps[tmp1]}')
			else:
				if c3[0]=='T':
						tmp=c3
						tmp1=int(tmp[1:])
						tmp321=tmp1
				if tmpq1=="isvar":
					c1=globalMem.getSymVal(cuadruplo[1])
				if tmpq2=="isvar":
					c2=globalMem.getSymVal(cuadruplo[2])
				if isinstance(c1,str):
					if len(str(c1))>1:
						if c1[0]=='T':
							tmp=c1
							tmp1=int(tmp[1:])
							c1=avTmps1[tmp1]#cambie
				if isinstance(c2,str):
					if len(str(c2))>1:
						if c2[0]=='T':
							tmp=c2
							tmp1=int(tmp[1:])
							c2=avTmps1[tmp1]#cambie
				if c1==c2:
					print(f'{cuadruplo[1]}&{cuadruplo[2]}= True')
					c3=True
				else:
					print(f'{cuadruplo[1]}&{cuadruplo[2]}= False')
					c3=False
				avTmps1[tmp321]=c3#cambie
				#print(f'{c1}<{c2}={c3}')
			PC=PC+1
	#print("\n--- Avails ---")
	#tempo=0
	#for x in avTmps:
	#	print(f'T{tempo} = {x}')
	#	tempo=tempo+1
		

def p_main(p):
	'''
	main : PC MAIN LPAREN RPAREN PC1 vars MODULO main1 PC2
	'''
def p_PC(p):
	'''
	PC : 
	'''
	global contCuadruplos; global pilaSaltos
	cTmp1=[]
	cTmp1.append("GOTO")
	cTmp1.append(None)
	cTmp1.append(None)
	cTmp1.append(None)
	cuadruplos.append(cTmp1)
	contCuadruplos=contCuadruplos+1
	pilaSaltos.append(contCuadruplos-1)

def p_PC1(p):
	'''
	PC1 : 
	'''
	global PC; global contCuadruplos; global pilaSaltos
	fin=pilaSaltos.pop()
	cuadruplos[fin][1]=contCuadruplos
	print(f'PDS PC1: {pilaSaltos}')
	
def p_PC2(p):
	'''
	PC2 : 
	'''
	global PC; global cuadruplos; global contCuadruplos
	cTmp="ENDP"
	cTmp1=[]
	cTmp1.append("ENDP")
	cTmp1.append(None)
	cTmp1.append(None)
	cTmp1.append(None)
	cuadruplos.append(cTmp1)
	contCuadruplos=contCuadruplos+1

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

def p_dec1(p):
	'''
	dec1  : TIPO COLON 
	      | 
	'''

def p_TIPO(p):
	'''
	TIPO : INT
		 | FL
		 | BOOL
	'''
	global auxT
	auxT = p[1]

def p_vars0(p):
	'''
	vars0  : ID EQUAL F SEMICOLON
		   | READ EQUAL ID
		   | PRINT ID
		   | CALLF
	       |
	'''
	global st; global avTmps1; global globalMem; global auxID; global auxT; global sym; global pOps; global avTmpsCount; global avTmps; global contCuadruplos; global pDirVal; global pDirValCont; global PC
	if (len(p)==5):
		auxID = p[1]
		sym=symboltable.Symbol(auxID,auxT)
		st.put(sym)
		op1=pOps.pop(0)
		if (p[2]=="="):
			print(f'= {op1} {p[1]}')
			cTmp1=[]
			cTmp1.append("=")
			cTmp1.append(op1)
			cTmp1.append(p[1])
			cTmp1.append(None)
			cuadruplos.append(cTmp1)
			avTmps.append(str(p[1]))
			pOps.insert(0,avTmps[-1])
			print(pOps)
			# if isinstance(op1,str):
			# 	if len(str(op1))>1:
			# 		if op1[0]=='T':
			# 			tmp=op1
			# 			tmp1=int(tmp[1:])
			# 			op1=avTmps1[tmp1]#cambie
			symM=memoryST.Symbol_m(auxID,op1,auxT)
			if globalMem.varExists(auxID):
				globalMem.addSy(symM)
			else:
				globalMem.updateVal(auxID,op1)
		contCuadruplos=contCuadruplos+1
	if (len(p)==4):
		print(f'READ {p[3]}')
		auxT="int"
		symM=memoryST.Symbol_m(p[3],None,auxT)
		globalMem.addSy(symM)
		cTmp1=[]
		cTmp1.append("READ")
		cTmp1.append(p[3])
		cTmp1.append(None)
		cTmp1.append(None)
		cuadruplos.append(cTmp1)
		contCuadruplos=contCuadruplos+1
		#avTmps.append(str(p[1]))
		#pOps.insert(0,avTmps[-1])
		print(pOps)
	if (len(p)==3):
		#val= globalMem.getSymVal(p[2])
		print(f'PRINT {p[2]}')
		cTmp1=[]
		cTmp1.append("PRINT")
		cTmp1.append(p[2])
		cTmp1.append(None)
		cTmp1.append(None)
		cuadruplos.append(cTmp1)
		contCuadruplos=contCuadruplos+1
		#avTmps.append(str(p[1]))
		#pOps.insert(0,avTmps[-1])
		#print(pOps)

def p_MODULO(p):
	'''
	MODULO : FUNCTION ID MOD1 LPAREN RPAREN vars BLOQUE END MODULO MOD2
	       | 
	'''	
	
def p_MOD1(p):
	'''
	MOD1 : 
	'''	
	global pProcs; global pProcsCont; global idTmp; global st; global globalMem; global auxID; global auxT; global sym; global pOps; global avTmpsCount; global avTmps; global contCuadruplos; global pDirVal; global pDirValCont; global PC
	pProcs.insert(0,contCuadruplos)
	#print(f'pProcs:{pProcs}')

def p_MOD2(p):
	'''
	MOD2 : 
	'''	
	global pProcs; global pProcsCont; global idTmp; global st; global globalMem; global auxID; global auxT; global sym; global pOps; global avTmpsCount; global avTmps; global contCuadruplos; global pDirVal; global pDirValCont; global PC
	#cTmp1=[]
	#cTmp1.append("CALL")
	#cTmp1.append(pProcs[0])
	#cTmp1.append(None)
	#cTmp1.append(None)
	#cuadruplos.append(cTmp1)
	#print(cuadruplos[-1])
	#contCuadruplos=contCuadruplos+1
	cTmp2=[]
	cTmp2.append("ENDPROC")
	cTmp2.append(None)
	cTmp2.append(None)
	cTmp2.append(None)
	cuadruplos.append(cTmp2)
	print(cuadruplos[-1])
	contCuadruplos=contCuadruplos+1
	cuadruplos[0][1]=contCuadruplos

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
	         | IF L THEN THEN1 ESTATUTO IF1 FINIF
			 | WHILE WHILE1 L WHILE2 ESTATUTO WHILE3 END
			 | DWHILE ESTATUTO DW1 UNTIL ESTATUTO END
			 | FOR LPAREN vars PIPE L PIPE vars RPAREN ESTATUTO END
		 	 | BLOQUE
			 |
	'''
	global pOps; global pilaSaltos; global cuadruplos; global contCuadruplos; global pDirVal; global pDirValCont; global PC

def p_THEN1(p):
	'''
	THEN1 : 
	'''
	global pOps; global pilaSaltos; global cuadruplos; global contCuadruplos; global pDirVal; global pDirValCont; global PC
	#print(f'ContCuadruplos: {contCuadruplos}')
	resultado = pOps.pop(0)
	print(pOps)
	cTmp="GTF "+str(resultado)
	cTmp1=[]
	#PRUEBA RODRIGO

	cTmp1.append("GTF")
	cTmp1.append(resultado)
	cTmp1.append(None)
	cTmp1.append(None)
	cuadruplos.append(cTmp1)
	print(cuadruplos[-1])
	contCuadruplos=contCuadruplos+1
	#regresar resultado al avail
	pilaSaltos.insert(0,contCuadruplos-1)
	print(f'PDS THEN: {pilaSaltos}')

def p_CALLF(p):
	'''
	CALLF : CALL ID 
	'''
	global pProcs; global pOps; global pilaSaltos; global cuadruplos; global contCuadruplos; global pDirVal; global pDirValCont; global PC
	if len(p)==3:
		print(f'ContCuadruplos: {contCuadruplos}')
		cTmp1=[]
		cTmp1.append("CALL")
		cTmp1.append(pProcs[0])
		cTmp1.append(None)
		cTmp1.append(None)
		cuadruplos.append(cTmp1)
		print(cuadruplos[-1])
		contCuadruplos=contCuadruplos+1

def p_IF1(p):
	'''
	IF1 : ELSE ELSE1 ESTATUTO
		| 
	'''
	global pOps; global pilaSaltos; global cuadruplos; global contCuadruplos; global pDirVal; global pDirValCont; global PC

def p_ELSE1(p):
	'''
	ELSE1 : 
	'''
	global pOps; global pilaSaltos; global cuadruplos; global contCuadruplos; global pDirVal; global pDirValCont; global PC
	print(f'PDS ELSE: {pilaSaltos}')
	cTmp="GOTO"
	cTmp1=[]
	cTmp1.append("GOTO")
	cTmp1.append(None)
	cTmp1.append(None)
	cTmp1.append(None)
	cuadruplos.append(cTmp1)
	contCuadruplos=contCuadruplos+1
	#regresar resultado al avail
	f=pilaSaltos.pop(0)
	#cuadruplos[f]=cuadruplos[f]+" "+str(contCuadruplos)
	cuadruplos[f][2]=contCuadruplos
	pilaSaltos.insert(0,contCuadruplos-1)
	print(f'PDS ELSE: {pilaSaltos}')

def p_FINIF(p):
	'''
	FINIF : 
	'''
	global pOps; global pilaSaltos; global cuadruplos; global contCuadruplos; global pDirVal; global pDirValCont; global PC
	print(f'PDS FINIF: {pilaSaltos}')
	fin=pilaSaltos.pop(0)
	#cuadruplos[fin]=cuadruplos[fin]+" "+str(contCuadruplos)
	cuadruplos[fin][1]=contCuadruplos
	print(f'PDS FINIF: {pilaSaltos}')

def p_WHILE1(p):
	'''
	WHILE1 : 
	'''
	global pOps; global pilaSaltos; global cuadruplos; global contCuadruplos; global pDirVal; global pDirValCont; global PC
	print(f'PDS WHILE1: {pilaSaltos}')
	print(f'ContCuadruplos: {contCuadruplos}')
	#pilaSaltos.insert(0,contCuadruplos)
	pilaSaltos.append(contCuadruplos)
	print(f'PDS WHILE1: {pilaSaltos}')

def p_WHILE2(p):
	'''
	WHILE2 : 
	'''
	global pOps; global contIF; global pilaSaltos; global cuadruplos; global contCuadruplos; global pDirVal; global pDirValCont; global PC
	print(f'PDS WHILE2: {pilaSaltos}')
	print(f'GTF:{contCuadruplos}')
	print(f'ContCuadruplos: {contCuadruplos}')
	ANS=pOps.pop(0)
	cTmp1=[]
	cTmp1.append("GTF")
	cTmp1.append(ANS)
	cTmp1.append(None)
	cTmp1.append(None)
	cuadruplos.append(cTmp1)
	contCuadruplos=contCuadruplos+1
	#regresar resultado al avail
	pilaSaltos.append(contCuadruplos-1)
	print(f'PDS WHILE2: {pilaSaltos}')

def p_WHILE3(p):
	'''
	WHILE3 : 
	'''
	global pOps; global contIF; global pilaSaltos; global cuadruplos; global contCuadruplos; global pDirVal; global pDirValCont; global PC
	print(f'PDS WHILE3: {pilaSaltos}')
	print(f'ContCuadruplos: {contCuadruplos}')
	dir1= pilaSaltos.pop()
	dir2= pilaSaltos.pop()
	cTmp1=[]
	cTmp1.append("GOTO")
	cTmp1.append(dir2)
	cTmp1.append(None)
	cTmp1.append(None)
	cuadruplos.append(cTmp1)
	contCuadruplos=contCuadruplos+1
	cuadruplos[dir1][2]=contCuadruplos
	print(f'PDS WHILE3: {pilaSaltos}')

def p_DW1(p):
	'''
	DW1 : SEMICOLON ESTATUTO DW1
	    | 
	'''

def p_IDCTE(p):
	'''
	IDCTE : ID
		  | CTE_INT
		  | CTE_FL
	'''
	global pOps; global st
	p[0]=p[1]
		
def p_F(p):
	'''
	F : IDCTE
	  | LPAREN E RPAREN
	'''
	if (len(p)==2):
		p[0]=p[1]
		pOps.insert(0,p[1])

def p_E(p):
	'''
	E : T
	  | E PLUS T
	  | E MINUS T
	'''
	global pOps; global st; global avTmps; global avTmpsCount; global cuadruplos; global contCuadruplos; global pilaSaltos; global pDirVal; global pDirValCont; global PC
	if (len(p)==2):
		p[0]=p[1]
		#pOps.insert(0,p[1])
	elif (len(p)==4):
		p[0]=p[1]
		if len(pOps)>1:
			op1=pOps.pop(0)
			op2=pOps.pop(0)
			if (p[2]=="+"):
				print(f'+ {op2} {op1} T{avTmpsCount}')
				cTmp="+ "+str(op2)+" "+str(op1)+" T"+str(avTmpsCount)
				cTmp1=[]
				cTmp1.append("+")
				cTmp1.append(op2)
				cTmp1.append(op1)
				cTmp1.append("T"+str(avTmpsCount))
				cuadruplos.append(cTmp1)
				avTmps.append("T"+str(avTmpsCount)) # en vez de 1, va el resultado
				pOps.insert(0,avTmps[-1]) #append(avTmps[-1]) 
				print(pOps)
			elif (p[2]=="-"):
				print(f'- {op2} {op1} T{avTmpsCount}')
				cTmp="- "+str(op2)+" "+str(op1)+" T"+str(avTmpsCount)
				cTmp1=[]
				cTmp1.append("-")
				cTmp1.append(op2)
				cTmp1.append(op1)
				cTmp1.append("T"+str(avTmpsCount))
				cuadruplos.append(cTmp1)
				avTmps.append("T"+str(avTmpsCount)) # aqui va el resultado
				pOps.insert(0,avTmps[-1]) #append(avTmps[-1]) 
				print(pOps)
			avTmpsCount=avTmpsCount+1
			contCuadruplos=contCuadruplos+1

def p_T(p):
	'''
	T : F
	  | T TIMES F
	  | T DIVIDE F
	'''
	global cTmp2; global pOps; global st; global avTmps; global avTmpsCount; global cuadruplos; global contCuadruplos; global pilaSaltos; global pDirVal; global pDirValCont; global PC
	if (len(p)==2):
		p[0]=p[1]
		#pOps.insert(0,p[1])
	elif (len(p)==4):
		p[0]=p[1]
		#print("PRUEBAS!!")
		#print(p[0])
		print(pOps)
		if len(pOps)>1:
			op1=pOps.pop(0)
			op2=pOps.pop(0)
			if (p[2]=="*"):
				print(f'* {op2} {op1} T{avTmpsCount}')
				cTmp="* "+str(op2)+" "+str(op1)+" T"+str(avTmpsCount)
				cTmp1=[]
				cTmp1.append("*")
				cTmp1.append(op2)
				cTmp1.append(op1)
				cTmp1.append("T"+str(avTmpsCount))
				cuadruplos.append(cTmp1)
				contCuadruplos=contCuadruplos+1
				avTmps.append("T"+str(avTmpsCount)) # en vez de 1, va el resultado
				pOps.insert(0,avTmps[-1]) #append(avTmps[-1]) 
				print(f'pOps:{pOps}')
			elif (p[2]=="/"):
				print(f'/ {op2} {op1} T{avTmpsCount}')
				cTmp="/ "+str(op2)+" "+str(op1)+" T"+str(avTmpsCount)
				cTmp1=[]
				cTmp1.append("/")
				cTmp1.append(op2)
				cTmp1.append(op1)
				cTmp1.append("T"+str(avTmpsCount))
				cuadruplos.append(cTmp1)
				contCuadruplos=contCuadruplos+1
				avTmps.append("T"+str(avTmpsCount)) # aqui va el resultado
				pOps.insert(0,avTmps[-1]) #append(avTmps[-1]) 
				print(f'pOps:{pOps}')
			avTmpsCount=avTmpsCount+1


def p_OPRL(p):
	'''
	OPRL : GT
		 | LT
		 | ET
	'''
	global pOps; global avTmpsCount; global avTmps;global contadortmp; global pDirVal; global pDirValCont; global PC
	#if (contadortmp>0):
	p[0]=p[1]

def p_L(p):
	'''
	L : ID OPRL ID
	  | LPAREN D RPAREN
	'''
	global pOps; global avTmpsCount; global avTmps; global opT; global cuadruplos; global contCuadruplos; global pilaSaltos; global pDirVal; global pDirValCont; global PC
	if p[1]!="(":
		opT=p[2]
		pOps.insert(0,str(p[1]))
		pOps.insert(0,str(p[3]))
		print(f'pOps:{pOps}')
		if len(pOps)>1:
			op1=pOps.pop(0)
			op2=pOps.pop(0)
			if (p[2]==">"):
				print(f'> {op2} {op1} T{avTmpsCount}')
				cTmp="> "+str(op2)+" "+str(op1)+" T"+str(avTmpsCount)
				cTmp1=[]
				cTmp1.append(">")
				cTmp1.append(op2)
				cTmp1.append(op1)
				cTmp1.append("T"+str(avTmpsCount))
				cuadruplos.append(cTmp1)
				contCuadruplos=contCuadruplos+1
				avTmps.append("T"+str(avTmpsCount)) # en vez de 1, va el resultado
				pOps.insert(0,avTmps[-1]) #append(avTmps[-1]) 
				print(f'pOps:{pOps}')
			elif (p[2]=="<"):
				print(f'< {op2} {op1} T{avTmpsCount}')
				cTmp="< "+str(op2)+" "+str(op1)+" T"+str(avTmpsCount)
				cTmp1=[]
				cTmp1.append("<")
				cTmp1.append(op2)
				cTmp1.append(op1)
				cTmp1.append("T"+str(avTmpsCount))
				cuadruplos.append(cTmp1)
				contCuadruplos=contCuadruplos+1
				avTmps.append("T"+str(avTmpsCount)) # aqui va el resultado
				pOps.insert(0,avTmps[-1]) #append(avTmps[-1]) 
				print(f'pOps:{pOps}')
			elif (p[2]=="&"):
				print(f'& {op2} {op1} T{avTmpsCount}')
				cTmp="& "+str(op2)+" "+str(op1)+" T"+str(avTmpsCount)
				cTmp1=[]
				cTmp1.append("&")
				cTmp1.append(op2)
				cTmp1.append(op1)
				cTmp1.append("T"+str(avTmpsCount))
				cuadruplos.append(cTmp1)
				contCuadruplos=contCuadruplos+1
				avTmps.append("T"+str(avTmpsCount)) # aqui va el resultado
				pOps.insert(0,avTmps[-1]) #append(avTmps[-1]) 
				print(f'pOps:{pOps}')
			avTmpsCount=avTmpsCount+1

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
	global pOps; global avTmpsCount; global avTmps; global cuadruplos; global contCuadruplos; global pilaSaltos; global pDirVal; global pDirValCont; global PC
	if (len(p)==3):
		if len(pOps)>1:
			op1=pOps.pop(0)
			op2=pOps.pop(0)
			if (p[1]=="or"):
				print(f'OR {op2} {op1} T{avTmpsCount}')
				cTmp="OR "+str(op2)+" "+str(op1)+" T"+str(avTmpsCount)
				cTmp1=[]
				cTmp1.append("OR")
				cTmp1.append(op2)
				cTmp1.append(op1)
				cTmp1.append("T"+str(avTmpsCount))
				cuadruplos.append(cTmp1)
				contCuadruplos=contCuadruplos+1
				avTmps.append("T"+str(avTmpsCount)) # en vez de 1, va el resultado
				pOps.insert(0,avTmps[-1]) #append(avTmps[-1]) 
				print(f'pOps:{pOps}')
			elif (p[1]=="and"):
				print(f'AND {op2} {op1} T{avTmpsCount}')
				cTmp="AND "+str(op2)+" "+str(op1)+" T"+str(avTmpsCount)
				cTmp1=[]
				cTmp1.append("AND")
				cTmp1.append(op2)
				cTmp1.append(op1)
				cTmp1.append("T"+str(avTmpsCount))
				cuadruplos.append(cTmp1)
				contCuadruplos=contCuadruplos+1
				avTmps.append("T"+str(avTmpsCount)) # aqui va el resultado
				pOps.insert(0,avTmps[-1]) #append(avTmps[-1]) 
				print(f'pOps:{pOps}')
			avTmpsCount=avTmpsCount+1


def p_error(p):
	print(f"Syntax error at {p.value!r}")
	global cuadruplos
	print(f"\nCuadruplos: ({contCuadruplos})")
	t=0
	for x in cuadruplos:
		print(f'{t}) {x}')
		t=t+1

parser = yacc.yacc()


while True:
	try:
		s = input('sunbeam > ')
	except EOFError:
		break
	parser.parse(s)