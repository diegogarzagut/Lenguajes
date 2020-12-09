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
global memArreglos
memArreglos=[None]*1000
global pBases
pBases=[0]
global dimsize1
dimsize1=[]
global dimsize2
dimsize2=[]
global dimsize3
dimsize3=[]
global M
M=1
global M1
M1=1
global M2
M2=1
global pM
pM=[]
global pM1
pM1=[]
global pM2
pM2=[]
global numDim
numDim=[]

		
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
	'LBRKT',
	'RBRKT',
	'DIR',
	'GDIRV',
	'sumMat',
	'mulMat',
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
t_LBRKT    = r'\['
t_RBRKT    = r'\]'

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
def t_sumMat(t):
	r'sumMat'
	t.type = 'sumMat'
	return t
def t_mulMat(t):
	r'mulMat'
	t.type = 'mulMat'
	return t
def t_CALL(t):
	r'call'
	t.type = 'CALL'
	return t
def t_DIR(t):
	r'dir'
	t.type = 'DIR'
	return t 
def t_GDIRV1(t):
	r'gdirv'
	t.type = 'GDIRV'
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
		elif opscode=="SAM":
			dirid1=cuadruplo[1] 
			dirid2=cuadruplo[2]
			c3=cuadruplo[3]
			tmp321=None
			if c3[0]=='T':
				tmp=c3
				tmp1=int(tmp[1:])
				tmp321=tmp1
			c3=memArreglos[int(dirid1)]+memArreglos[int(dirid2)]
			avTmps1[tmp321]=c3
			PC=PC+1
		elif opscode=="SAM1":
			c1=cuadruplo[1] # valor
			c2=cuadruplo[2] # memArrelgos index
			if len(c1)>1:
				if c1[0]=='T':
					tmp=c1
					tmp1=int(tmp[1:])
					c1=avTmps1[tmp1]
			sdest=str(c2)
			if len(sdest)>1:
				if sdest[0]=='T':
					tmp=c2
					tmp1=int(tmp[1:])
					c2=avTmps1[tmp1]
			memArreglos[int(c2)]=c1
			PC=PC+1
		elif opscode=="DIR":
			print("DIR")
			dirTmp=cuadruplo[2]
			valueTmp=cuadruplo[3]
			tmpq1=globalMem.getSymType(cuadruplo[3])
			tmpq2=globalMem.getSymType(cuadruplo[2])
			if len(str(dirTmp))>1:
				if dirTmp[0]=='T':
					tmp=dirTmp
					tmp1=int(tmp[1:])
					dirTmp=avTmps1[tmp1]
			if len(str(valueTmp))>1:
				if valueTmp[0]=='T':
					tmp=valueTmp
					tmp1=int(tmp[1:])
					valueTmp=avTmps1[tmp1]
			if tmpq1=="isvar":
				valueTmp=globalMem.getSymVal(cuadruplo[3])
			if tmpq2=="isvar":
				dirTmp=globalMem.getSymVal(cuadruplo[2])
			memArreglos[int(dirTmp)]=valueTmp
			PC=PC+1
		elif opscode=="GDIRV":
			dirTmp=cuadruplo[1]
			tmpq2=globalMem.getSymType(cuadruplo[2])
			if len(str(dirTmp))>1:
				if dirTmp[0]=='T':
					tmp=dirTmp
					tmp1=int(tmp[1:])
					dirTmp=avTmps1[tmp1]
			if tmpq2=="isvar":
				tmptmp=memArreglos[int(dirTmp)]
				globalMem.updateVal(cuadruplo[2],tmptmp)
			PC=PC+1
		elif opscode=="PRINT":#globalMem.listMTable()
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
				symMT=memoryST.Symbol_m(dest,value1,"int",False,None,None,None,None,None,None,None,None)
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
	print("\n--- MemArreglos ---")
	tempo=0
	for x in memArreglos:
		if x!=None:
			print(f'MA[{tempo}] = {x}')
		tempo=tempo+1
		

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
		   | ID COLON LBRKT ARR1 RBRKT
		   | DIR LBRKT DIR1
		   | GDIRV LBRKT GDIRV1
		   | sumMat sm1
	       |
	'''
	global numDim; global pM; global pM1; global pM2; global pBases; global st; global avTmps1; global globalMem; global auxID; global auxT; global sym; global pOps; global avTmpsCount; global avTmps; global contCuadruplos; global pDirVal; global pDirValCont; global PC
	if (p[1]=="dir"): #p[0]=p[2]
		print("dir")
	if (len(p)==6):
		auxID=p[1]
		print(pBases)
		symM=memoryST.Symbol_m(auxID,None,"int",True,pBases.pop(0),numDim.pop(0),pM.pop(0),pM1.pop(0),pM2.pop(0),dimsize1.pop(0),dimsize2.pop(0),dimsize3.pop(0),) 
		globalMem.addSy(symM)
	if (len(p)==5):
		auxID = p[1]
		#sym=symboltable.Symbol(auxID,auxT)
		#st.put(sym)
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
			symM=memoryST.Symbol_m(auxID,op1,auxT,False,None,None,None,None,None,None,None,None)
			if globalMem.varExists(auxID):
				globalMem.addSy(symM)
			else:
				globalMem.updateVal(auxID,op1)
		contCuadruplos=contCuadruplos+1
	if (len(p)==4 and p[1]=="read"):
		print(f'READ {p[3]}')
		auxT="int"
		symM=memoryST.Symbol_m(p[3],1,auxT,False,None,None,None,None,None,None,None,None)
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
	if (len(p)==3 and p[1]=="print"):
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

def p_GDIRV1(p):
	'''
	GDIRV1 : ID COMA ID COMA IDCTE RBRKT
	       | ID COMA ID COMA IDCTE COMA IDCTE RBRKT
		   | ID COMA ID COMA IDCTE COMA IDCTE COMA IDCTE RBRKT  
	'''	
	global contCuadruplos; global cuadruplos; global numDim; global pM; global pM1; global pM2; global pBases; global dimsize1; global dimsize2; global dimsize3; global M; global M1; global M2
	if len(p)==7:
		idtmp1=globalMem.getSymIndx(p[3])
		s1=p[5]
		base=globalMem.memory[idtmp1][4] #if isinstance(p[3],str):#s1=globalMem.getSymVal(p[3])
		cTmp1=[]
		cTmp1.append("+")
		cTmp1.append(s1)
		cTmp1.append(base)
		cTmp1.append("T"+str(avTmpsCount))
		cuadruplos.append(cTmp1)
		avTmps.append("T"+str(avTmpsCount)) 
		pOps.insert(0,avTmps[-1])
		contCuadruplos=contCuadruplos+1 #if isinstance(p[5],str):#s2=globalMem.getSymVal(p[5])
		cTmp2=[]
		cTmp2.append("=")
		cTmp2.append(pOps.pop(0))
		cTmp2.append(p[1])
		cTmp2.append(None)
		cuadruplos.append(cTmp2)
		print(cuadruplos[-1])
		contCuadruplos=contCuadruplos+1
	if len(p)==9:
		idtmp1=globalMem.getSymIndx(p[3])
		s1=p[5]
		s2=p[7]
		m1=globalMem.memory[idtmp1][7]
		base=globalMem.memory[idtmp1][4] #if isinstance(p[3],str):#s1=globalMem.getSymVal(p[3])
		cTmp1=[]
		cTmp1.append("*")
		cTmp1.append(s1)
		cTmp1.append(m1)
		cTmp1.append("T"+str(avTmpsCount))
		cuadruplos.append(cTmp1)
		avTmps.append("T"+str(avTmpsCount)) 
		pOps.insert(0,avTmps[-1])
		contCuadruplos=contCuadruplos+1 #if isinstance(p[5],str):#s2=globalMem.getSymVal(p[5])
		cTmp2=[]
		cTmp2.append("+")
		cTmp2.append(s2)
		cTmp2.append(pOps.pop(0))
		cTmp2.append("T"+str(avTmpsCount))
		cuadruplos.append(cTmp2)
		avTmps.append("T"+str(avTmpsCount)) 
		pOps.insert(0,avTmps[-1])
		contCuadruplos=contCuadruplos+1 # +base
		cTmp3=[]
		cTmp3.append("+")
		cTmp3.append(pOps.pop(0))
		cTmp3.append(base)
		cTmp3.append("T"+str(avTmpsCount))
		cuadruplos.append(cTmp3)
		avTmps.append("T"+str(avTmpsCount)) 
		pOps.insert(0,avTmps[-1])
		contCuadruplos=contCuadruplos+1
		cTmp4=[]
		cTmp4.append("GDIRV")
		cTmp4.append(pOps.pop(0)) # direc memarreglos
		cTmp4.append(p[1]) # variable
		cTmp4.append(None)
		cuadruplos.append(cTmp4)
		print(cuadruplos[-1])
		contCuadruplos=contCuadruplos+1

def p_sm1(p):
	'''
	sm1 : ID ID ID
	'''	
	global contCuadruplos; global cuadruplos; global numDim; global pM; global pM1; global pM2; global pBases; global dimsize1; global dimsize2; global dimsize3; global M; global M1; global M2
	idtmp1=globalMem.getSymIndx(p[1])
	idtmp2=globalMem.getSymIndx(p[2])
	idtmp3=globalMem.getSymIndx(p[3])
	d1id1=globalMem.memory[idtmp1][9]
	d1id2=globalMem.memory[idtmp2][9]
	d2id1=globalMem.memory[idtmp1][10]
	d2id2=globalMem.memory[idtmp2][10]
	d3id1=globalMem.memory[idtmp1][11]
	d3id2=globalMem.memory[idtmp2][11]
	numDimid1=globalMem.memory[idtmp1][5]
	base1=globalMem.memory[idtmp1][4]
	base2=globalMem.memory[idtmp2][4]
	base3=globalMem.memory[idtmp3][4]
	m1id1=globalMem.memory[idtmp1][7]
	m1id2=globalMem.memory[idtmp2][7]
	m1id3=globalMem.memory[idtmp3][7]
	m2id1=globalMem.memory[idtmp1][8]
	m2id2=globalMem.memory[idtmp2][8]
	m2id3=globalMem.memory[idtmp3][8]
	iint=0
	jint=0
	muld1id1d2id1=d1id1*d2id1
	if (d1id1==d1id2 and d2id1==d2id2 and d3id1==d3id2):
		if (numDimid1==1):
			while (iint<d1id1):
				dirid1=base1+iint
				dirid2=base2+iint
				vid1=memArreglos[dirid1]
				vid2=memArreglos[dirid2]
				cTmp1=[]
				cTmp1.append("+")
				cTmp1.append(vid1)
				cTmp1.append(vid2)
				cTmp1.append("T"+str(avTmpsCount))
				cuadruplos.append(cTmp1)
				avTmps.append("T"+str(avTmpsCount)) 
				pOps.insert(0,avTmps[-1])
				contCuadruplos=contCuadruplos+1
				dirid3=base3+iint
				cTmp2=[]
				cTmp2.append("SAM")
				cTmp2.append(pOps.pop(0))
				cTmp2.append(dirid3)
				cTmp2.append(None)
				cuadruplos.append(cTmp2) #avTmps.append("T"+str(avTmpsCount))  #pOps.insert(0,avTmps[-1])
				contCuadruplos=contCuadruplos+1
				iint=iint+1
		if (numDimid1==2):
			while (iint<d1id1):
				while (jint<d2id1):
					dirid1=base1+iint*m1id1+jint
					dirid2=base2+iint*m1id2+jint #vid1=memArreglos[dirid1] #vid2=memArreglos[dirid2]
					cTmp1=[]
					cTmp1.append("SAM")
					cTmp1.append(dirid1)
					cTmp1.append(dirid2)
					cTmp1.append("T"+str(avTmpsCount))
					cuadruplos.append(cTmp1)
					avTmps.append("T"+str(avTmpsCount)) 
					pOps.insert(0,avTmps[-1])
					contCuadruplos=contCuadruplos+1
					dirid3=base3+iint*m1id3+jint
					cTmp2=[]
					cTmp2.append("SAM1")
					cTmp2.append(pOps.pop(0))
					cTmp2.append(dirid3)
					cTmp2.append(None)
					cuadruplos.append(cTmp2) #avTmps.append("T"+str(avTmpsCount))  #pOps.insert(0,avTmps[-1])
					contCuadruplos=contCuadruplos+1
					jint=jint+1
				jint=0
				iint=iint+1
		#if (numDimid1==3):

def p_DIR1(p):
	'''
	DIR1 : ID COMA IDCTE RBRKT EQUAL IDCTE
	     | ID COMA IDCTE COMA IDCTE RBRKT EQUAL IDCTE
		 | ID COMA IDCTE COMA IDCTE COMA IDCTE RBRKT EQUAL IDCTE
	'''	
	global contCuadruplos; global cuadruplos; global numDim; global pM; global pM1; global pM2; global pBases; global dimsize1; global dimsize2; global dimsize3; global M; global M1; global M2
	if len(p)==7:
		print(p[1])
		idtmp1=globalMem.getSymIndx(p[1])
		s1=p[3]
		base=globalMem.memory[idtmp1][4] #if isinstance(p[3],str):#s1=globalMem.getSymVal(p[3])
		cTmp1=[]
		cTmp1.append("+")
		cTmp1.append(s1)
		cTmp1.append(base)
		cTmp1.append("T"+str(avTmpsCount))
		cuadruplos.append(cTmp1)
		avTmps.append("T"+str(avTmpsCount)) 
		pOps.insert(0,avTmps[-1])
		contCuadruplos=contCuadruplos+1 #if isinstance(p[5],str):#s2=globalMem.getSymVal(p[5])
		valor=p[6]
		cTmp2=[]
		cTmp2.append("DIR")
		cTmp2.append(p[1])
		cTmp2.append(pOps.pop(0))
		cTmp2.append(valor)
		cuadruplos.append(cTmp2)
		print(cuadruplos[-1])
		contCuadruplos=contCuadruplos+1
	if len(p)==9:
		print(p[1])
		idtmp1=globalMem.getSymIndx(p[1])
		s1=p[3]
		s2=p[5]
		m1=globalMem.memory[idtmp1][7]
		base=globalMem.memory[idtmp1][4] #if isinstance(p[3],str):#s1=globalMem.getSymVal(p[3])
		cTmp1=[]
		cTmp1.append("*")
		cTmp1.append(s1)
		cTmp1.append(m1)
		cTmp1.append("T"+str(avTmpsCount))
		cuadruplos.append(cTmp1)
		avTmps.append("T"+str(avTmpsCount)) 
		pOps.insert(0,avTmps[-1])
		contCuadruplos=contCuadruplos+1 #if isinstance(p[5],str):#s2=globalMem.getSymVal(p[5])
		cTmp2=[]
		cTmp2.append("+")
		cTmp2.append(s2)
		cTmp2.append(pOps.pop(0))
		cTmp2.append("T"+str(avTmpsCount))
		cuadruplos.append(cTmp2)
		avTmps.append("T"+str(avTmpsCount)) 
		pOps.insert(0,avTmps[-1])
		contCuadruplos=contCuadruplos+1 # +base
		cTmp3=[]
		cTmp3.append("+")
		cTmp3.append(pOps.pop(0))
		cTmp3.append(base)
		cTmp3.append("T"+str(avTmpsCount))
		cuadruplos.append(cTmp3)
		avTmps.append("T"+str(avTmpsCount)) 
		pOps.insert(0,avTmps[-1])
		contCuadruplos=contCuadruplos+1
		valor=p[8] #if isinstance(p[8],str): #valor=globalMem.getSymVal(p[8]) #dirT=s1*m1+s2+base #print(dirT) #memArreglos[int(dirT)]=valor #print(f'{p[1]}[{s1}][{s2}]={valor}\tMemoria Global[{int(dirT)}]')
		cTmp4=[]
		cTmp4.append("DIR")
		cTmp4.append(p[1])
		cTmp4.append(pOps.pop(0))
		cTmp4.append(valor)
		cuadruplos.append(cTmp4)
		print(cuadruplos[-1])
		contCuadruplos=contCuadruplos+1
	if len(p)==11:
		print(p[1])
		idtmp1=globalMem.getSymIndx(p[1])
		s1=p[3]
		s2=p[5]
		s3=p[7]
		if isinstance(p[3],str):
			s1=globalMem.getSymVal(p[3])
		if isinstance(p[5],str):
			s2=globalMem.getSymVal(p[5])
		if isinstance(p[7],str):
			s3=globalMem.getSymVal(p[7])
		m1=globalMem.memory[idtmp1][7]
		m2=globalMem.memory[idtmp1][8]
		base=globalMem.memory[idtmp1][4]
		valor=p[10]
		if isinstance(p[10],str):
			valor=globalMem.getSymVal(p[10])
		dirT=s1*m1+s2*m2+s3+base
		print(dirT)#memArreglos[int(dirT)]=valor
		print(f'{p[1]}[{s1}][{s2}][{s3}]={valor}\tMemoria Global[{int(dirT)}]')
		print(idtmp1)
		cTmp1=[]
		cTmp1.append("DIR")
		cTmp1.append(p[1])
		cTmp1.append(int(dirT))
		cTmp1.append(valor)
		cuadruplos.append(cTmp1)
		print(cuadruplos[-1])
		contCuadruplos=contCuadruplos+1

def p_ARR1(p):
	'''
	ARR1 : CTE_INT
	     | IDCTE COMA IDCTE
		 | CTE_INT COMA CTE_INT COMA CTE_INT
	'''	
	global numDim; global pM; global pM1; global pM2; global pBases; global dimsize1; global dimsize2; global dimsize3; global M; global M1; global M2
	if len(p)==2:
		numDim.append(1)
		dimsize1.append(p[1])
		dimsize2.append(None)
		dimsize3.append(None)
		M=p[1]
		pM.append(M)
		pM1.append(None)
		pM2.append(None)
		base=0
		for x in pBases:
			base=base+x
		base=base+M
		pBases.append(base)
	elif len(p)==4:
		s1=p[1]
		s2=p[3]
		tmpq1=globalMem.getSymType(p[1])
		tmpq2=globalMem.getSymType(p[3])
		if tmpq1=="isvar":
			s1=globalMem.getSymVal(p[1])
		if tmpq2=="isvar":
			s2=globalMem.getSymVal(p[3])
		numDim.append(2)
		dimsize1.append(s1)
		dimsize2.append(s2)
		dimsize3.append(None)
		M=s1*s2
		M1=M/s1 #dimsize1
		pM.append(M)
		pM1.append(M1)
		pM2.append(None)
		base=0
		for x in pBases:
			base=base+x
		base=base+M
		pBases.append(base)
	elif len(p)==6:
		numDim.append(3)
		dimsize1.append(p[1])
		dimsize2.append(p[3])
		dimsize3.append(p[5])
		M=p[1]*p[3]*p[5]
		M1=M/p[1]
		M2=M1/p[3]
		pM.append(M)
		pM1.append(M1)
		pM2.append(M2)
		base=0
		for x in pBases:
			base=base+x
		base=base+M
		pBases.append(base)
		


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
	BR : BR SEMICOLON ESTATUTO 
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