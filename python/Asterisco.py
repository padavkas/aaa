## Linha vertical ##

for i in range (0 , 5):
          print "*"

print

## Linha reta * 5 ##          

for i in range ( 0 , 5):
          print "*" * 5
print

## piramide ##

estrelas = ""
for i in range ( 0 , 5):
          estrelas += "*"
          print estrelas
print

## Reverse do anterior ##
for i in range (0,5):
          estrelas=""
          espacos=""

for k in range (0,5 - i):
          espacos +=" + "

for x in range ( 0 , i ):
          estrelas += ""

## Arvore de Natal ##

for x in range ( 0 , 5 ):
          espaco+=" "
          for y in range (0,5*x+1):
          estrelas += "*"
          print espacos , estrelas         