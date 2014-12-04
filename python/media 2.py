#pedir notas
teste = int(input(" teste "))

trabalho = int(input(" trabalho "))

av = int(input(" av "))

#calcular a media

media = 0.6*teste + 0.3*trabalho + 0.1*av
print media

if teste <=8 or media<9.5:
    teste = int(input("teste de rec"))
    media = 0.6*teste + 0.3*trabalho + 0.1*av

print media

#decisao de passou ou reprovou

if media <=9.5:
    print "chumbou na epoca normal"
    
    # exame
    exame = int(input("exame"))
    
    if exame <9.5:
        print "chumbou no exame"
    else:
        print "passou no exame"
    
else:
    print "passou na epoca normal"

      