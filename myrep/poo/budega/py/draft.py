class Person:
    def __init__(self, nome:str):
        self.nome=nome
    def __str__(self):
        return self.nome

class Mark:
    def __init__(self,n_caixas:int):
        self.espera:list[Person]=[]
        self.caixas:list[Person|None]=[]
        for _ in range(n_caixas):
            self.caixas.append(None)

    def arrive(self, pessoa:Person):
        self.espera.append(pessoa)

    def call(self,index:int):
        if index<0 or index>=len(self.caixas):
            print("fail: index invalido")
            return
        if self.caixas[index] is not None:
            print("fail: caixa ocupado") 
            return
        if len(self.espera)==0:
            print("fail: sem clientes")
            return
    
        self.caixas[index]=self.espera[0]
        del self.espera[0]
    
    def finish(self,index:int)->Person|None:
        if index<0 or index>=len(self.caixas):
            print("fail: caixa inexistente")
            return None
        if self.caixas[index] is None:
            print("fail: caixa vazio")
            return None
        
        aux=self.caixas[index]
        self.caixas[index]=None
        return aux

    def __str__(self):
        cadeiras=", ".join([str(x) if x else "-----" for x in self.caixas])
        espera=", ".join([str(x) for x in self.espera])
        return f"Caixas: [{cadeiras}]\nEspera: [{espera}]"

def main():
    mark=Mark(2)
    while True:
        line=input()
        print("$"+line)
        args=line.split()
        
        if args[0]=="end":
            break
        elif args[0]=="show":
            print (mark)
        elif args[0]=="init":
            mark=Mark(int(args[1]))
        elif args[0]=="arrive":
            mark.arrive(str(args[1]))
        elif args[0]=="call":
            mark.call(int(args[1]))
        elif args[0]=="finish":
            mark.finish(int(args[1]))
    
main()