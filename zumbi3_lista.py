__author__ = 'guilhermefelitti'
notas = [7.5, 4, 6.5, 10, 3]
soma = 0
x = 0
while x <5:
    soma = x + notas[x]
    x = x + 1

print("Média: %5.2f" %(soma/x))
