#pedir notas

teste = int(input(" teste "))

trabalho = int(input(" trabalho "))

av = int(input(" av "))

#calcular a media

media = 0.6*teste + 0.3*trabalho + 0.1*av

print media

#decisao de passou ou reprovou

if media <=9:
    print "chumbou"
else:
    print "passou"