h = int(input( "altura "))
c = raw_input ( "m ou f ")

if c.upper() == 'm':
    pesoIdeal = (72.7*h)-58
else:
    pesoIdeal = (62.1*h)-44.7

print "pesoideal" , pesoIdeal , "kg"


