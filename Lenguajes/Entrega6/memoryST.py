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
            
    def listMTable(self):
        #max_len = len(str(max( max(i) for i in self.memory)))
        #for i in self.memory:
        #    print(", ".join([str(l).rjust(max_len) for l in i]))
        print (np.array(self.memory))

class Symbol_m:
    def __init__(self,var,val,vtype):
        self.var = var
        self.val = val
        self.vtype = vtype
    