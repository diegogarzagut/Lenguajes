import numpy as np
class memoryST(object):
    def __init__(self): 
        self.memory=[]

    def addSy(self, symbol_m):
        countTMP=0
        countTMP1=None
        temp=0
        for i in self.memory:
            if i[0]==symbol_m.var:
                countTMP=countTMP+1
                countTMP1=temp
                print(f"Se repitió: {i[0]}")
            temp=temp+1
        if countTMP==0:
            stmp=[]
            stmp.append(symbol_m.var)
            stmp.append(symbol_m.val)
            stmp.append(symbol_m.vtype)
            stmp.append(symbol_m.dim)
            stmp.append(symbol_m.dimB)
            stmp.append(symbol_m.numdim)  
            stmp.append(symbol_m.M) 
            stmp.append(symbol_m.M1) 
            stmp.append(symbol_m.M2)
            self.memory.append(stmp)
            print (np.array(self.memory))
        else:
            self.memory[countTMP1][1]=symbol_m.val
            print (np.array(self.memory))
    
    def getSymType(self,vari):
        countTMP=0
        temp=0
        for i in self.memory:
            if i[0]==vari:
                countTMP=countTMP+1
                #print(f"Encontré: {i[0]}")
            temp=temp+1
        if countTMP==0:
            if isinstance(vari,int):
                return "int"
            if isinstance(vari,float):
                return "fl"
        else:
            return "isvar" #self.memory[temp-countTMP][2]
    
    def getSymVal(self,vari1):
        countTMP=0
        countTMP1=0
        temp=0
        for i in self.memory:
            if i[0]==vari1:
                countTMP=countTMP+1
                countTMP1=temp
                #print(f"Encontré: {i[0]}")
            temp=temp+1
        if countTMP!=0:
            return self.memory[countTMP1][1]
    
    def updateVal(self,vari1,value1):
        countTMP=0
        countTMP1=0
        temp=0
        for i in self.memory:
            if i[0]==vari1:
                countTMP=countTMP+1
                countTMP1=temp
                #Encontro la variable
            temp=temp+1
        if countTMP!=0:
            self.memory[countTMP1][1]=value1
    
    def varExists(self,vari2):
        countTMP=0
        temp=0
        for i in self.memory:
            if i[0]==vari2:
                countTMP=countTMP+1
                #Encontro la variable
            temp=temp+1
        if countTMP!=0:
            return True
        else:
            return False
            
    def listMTable(self):
        print (np.array(self.memory))

    


class Symbol_m:
    def __init__(self,var,val,vtype,dim,dimB,numdim,M,M1,M2):
        self.var = var 
        self.val = val 
        self.vtype = vtype 
        self.dim = dim 
        self.dimB = dimB 
        self.numdim=numdim 
        self.M=M  
        self.M1=M1  
        self.M2=M2 

    def getType(self):
        return self.vtype

    def isDim(self):
        if self.dim==True:
            return True
        else:
            return False

    def getDimB(self):
        return self.dimB
    
    