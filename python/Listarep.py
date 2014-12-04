## Defenir a lista ##

lista=[8,10,10,15,8,7]
listarep=[]

## Pecorrer a lista e dizer o repetido e os que se repetem mais que uma vez ##

for i in range (0 , len(lista)):
          elemento=lista[i]
          if (lista.count(elemento)>1 and listarep.count(elemento)==0):
                    listarep.append(elemento)

## Texto Os repetidos e os que se repetem mais do que uma vez ##

print lista
print listarep
                    