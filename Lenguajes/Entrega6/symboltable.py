class SymbolTable(object):
    def __init__(self): 
        self.symbols = {}

    def put(self, symbol):
        if self.symbols.__contains__(symbol.nombre):
            return False
        else:
            self.symbols[symbol.nombre]= symbol.tipo
            return True
        
    def listSTable(self):
        for x,y in self.symbols.items():
            print(f'{x} \t {y}')
    
    def getLastKey(self):
        keys=[]
        if (bool(self.symbols)):
            for x in self.symbols.keys():
                keys.append(str(x))
            tmp1=keys[-1]
            return tmp1


class Symbol:
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
    