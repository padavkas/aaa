## Arvore de Natal ##

for x in range ( 0 , 5 ):
          estrelas=""
          espacos=""
          for y in range (0,5-1*x):
                    espacos+=" "
          for k in range(0,2*x+1):
                    estrelas+="*"
          print espacos , estrelas  