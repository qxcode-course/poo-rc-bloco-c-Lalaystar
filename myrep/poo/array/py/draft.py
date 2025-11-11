class Foo:
    def __init__(self, name:str):
        self.name=name

frutas:list[str]=["banana", "uva"]
coisas:list[Foo]=[Foo("Maria"), Foo("Joana")]

p=input()
for x in frutas:
    frutas.append(p)
    print(x)
