class Kid:
    def __init__(self,name:str, age:int):
        self.__age=age
        self.__name=name

    def getName(self)->str:
        return self.__name
    
    def getAge(self)->int:
        return self.__age
    
    def setName(self, name:str):
        self.__name=name

    def setAge(self, age:int):
        self.__age=age

    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f"{self.__name}:{self.__age}"
    
class Pula:
    def __init__(self):
        self.espera:list[Kid]=[]
        self.la:list[Kid]=[]
        
    def arrive(self, name: str, age: int):
        self.espera.append(Kid(name, age))

    def enter(self):
        if self.espera:
            self.la.append(self.espera.pop(0))

    def __str__(self):
        return f"{self.espera} => {self.la}"

def main():
    pula=Pula()
    while True:
        line=input()
        print("$"+line)
        args=line.split()

        if args[0]=="end":
            break
        elif args[0]=="show":
            print(pula)
        elif args[0]=="arrive":
            name=args[1]
            age=int(args[2])
            pula.arrive(name,age)
        elif args[0]=="enter":
            pula.enter()
main()
        
   