# Mostar as notas dos alunos e media / usando ciclos
notaaluno = [0,0,0,0,0]

for numero in range ( 0 , 5 ):
    notaaluno[numero] = int(input( "nota do aluno: "))

somanotas=0
maiornota=0

for numero in range ( 0 , 5 ):
    somanotas += notaaluno[numero]
    if notaaluno[numero]>maiornota:
        maiornota=notaaluno[numero]
        

media = somanotas /5 
print somanotas / 5 



    

    