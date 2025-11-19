class Foo:
    def __init__(self, name:str):
        self.name=name

frutas:list[str]=["banana", "uva"]
coisas:list[Foo]=[Foo("Maria"), Foo("Joana")]

frutas.append("maça")
frutas.pop(1)

frutas.insert(1,"pera")

#n=int(input())
#bixa=list(range(n+1))

tam=len(frutas)

#for x in range(n):
  #  print(x)

bixa2:list[int]=[1,2,3,4,5,6,7,8,9,10]
#print(5 in bixa2)
#x=9
###
# encontrado = False
#for elemento in bixa2:
 #   if elemento == x:
  #      encontrado = True
   #     break
    #print(encontrado)
#par=[x for x in bixa2 if x%2==0]
#quadrado=[x*x for x in bixa2]
#print(quadrado)

x=7
for x in bixa2:
    bixa2.remove(x)
print(bixa2)