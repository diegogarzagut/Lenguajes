import numpy as np
class memoryST(object):
    def __init__(self): 
        self.memory=[]

    def addSy(self, symbol_m):
        countTMP=0
        temp=0
        for i in self.memory:
            if i[0]==symbol_m.var:
                countTMP=countTMP+1
                print(f"Se repitió: {i[0]}")
            temp=temp+1
        if countTMP==0:
            stmp=[]
            stmp.append(symbol_m.var)
            stmp.append(symbol_m.val)
            stmp.append(symbol_m.vtype)
            self.memory.append(stmp)
            print (np.array(self.memory))
        else:
            self.memory[temp-countTMP][1]=symbol_m.val
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
                #print(f"Encontré: {i[0]}")
            temp=temp+1
        if countTMP!=0:
            self.memory[countTMP1][1]=value1
            
    def listMTable(self):
        print (np.array(self.memory))

    


class Symbol_m:
    def __init__(self,var,val,vtype):
        self.var = var
        self.val = val
        self.vtype = vtype

    def getType(self):
        return self.vtype
    