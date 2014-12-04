nota= -1
while ( nota  > 20 or nota < 0):
          nota = int(input("insira a nota (0 a 20)"))

if nota <10:
          print"negativa"
elif nota <17:
          print "suficiente"
elif nota:
          print "excelente"