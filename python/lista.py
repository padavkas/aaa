listanumeros=[]
listanumeros.append(8)
listanumeros.append(6)
listanumeros.append(10)
listanumeros.append(15)
listanumeros.append(8)
listanumeros.append(15)
listanumeros.append(8)

novalista=[]
for i in range (0 ,len(listanumeros)) :
          if (novalista.count (listanumeros[i])==0):
                    novalista.append(listanumeros[i])
print novalista