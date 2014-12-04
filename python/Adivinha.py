import random

print "##### adivinha o numero #####"
numero_adivinha = random.randint(0,9)
#print "numero a adivinhar", numero_adivinha

for a in range(1 , 10):
    x = int(input("insira o numero: "))
    #print "numero escolhido" , x
    if x==numero_adivinha:
        print "!!!parabens acertou!!!!"
        break