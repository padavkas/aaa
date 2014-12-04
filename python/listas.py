listanumeros=[]
listanumeros.append(3)
listanumeros.append(7)
listanumeros.append(1)
listanumeros.append(6)
listanumeros.append(8)
listanumeros.append(5)
listanumeros.append(7)
listanumeros.append(0)
listanumeros.append(2)
listanumeros.append(3)
listanumeros.append(4)
listanumeros.append(1)
listanumeros.append(5)
listanumeros.append(7)
print listanumeros
listanumeros.sort()
print listanumeros
listanumeros.reverse()
print listanumeros
print listanumeros.count(8)
print listanumeros.count(7)
print listanumeros.count(6)
print listanumeros.count(5)
print listanumeros.count(4)
print listanumeros.count(3)
print listanumeros.count(2)
print listanumeros.count(1)
print listanumeros.count(0)
print len(listanumeros)
print listanumeros.index (2)
print listanumeros [2]
soma = 0 
for i in range (0,14):
          soma += listanumeros[i]
print soma
          
