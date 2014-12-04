# mostar o maior numero
maior = 0
menor = 10000
nota = [115,17,9,27]
pmaiorn = -1
pmenorn= -1

for pos in range (0 , 4):
    if (nota[pos] > maior):
        maior = nota[pos]
        pmaiorn = pos
        
for pos in range (0 , 4):
    if (nota [pos] < menor):
        menor = nota[pos]
        pmenorn = pos

print maior        
print pmaiorn        
print menor
print pmenorn
