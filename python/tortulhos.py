total = 0
numero = 1

while ( numero > 0 ):
    numero= int(input ( "numero de tortulhos obtidos "))
    if numero > 0:
        total = total + numero
    
    if total > 999999999:
        print "acaba o ciclo"
        total = 0 
    if total < 999999999:
        print "continua o ciclo"
  
    
print total        