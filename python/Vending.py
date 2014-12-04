dinheiro = int(input("Dinheiro inserido "))
custo = int(input("Custo do Produto "))

troco = dinheiro - custo

moedas50 = troco / 50

troco = troco % 50

moedas20 = troco / 20

troco = troco % 20

moedas10 = troco / 10

troco = troco % 10

moedas5 = troco / 5

troco = troco % 5

moedas2 = troco / 2

troco = troco % 2

moedas1 = troco / 1

troco = troco % 1

print "Moedas de 50 cent recebidas " , moedas50
print "Moedas de 20 cent recebidas " , moedas20
print "Moedas de 10 cent recebidas " , moedas10
print "Moedas de 5 cent recebidas " , moedas5
print "Moedas de 2 cent recebidas " , moedas2
print "moedas de 1 cent recebidas " , moedas1

