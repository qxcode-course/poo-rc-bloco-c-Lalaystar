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
        if args[0]=="show":
            print (mark)
        if args[0]=="arrive":
            mark.arrive(str(args[1]))
    
main()