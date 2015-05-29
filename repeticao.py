__author__ = 'guilhermefelitti'
numero = int(input("Digite um número negativo: "))
x = 0
while x <= numero:
    if x % 2 != 0:
        print(x)
    x = x + 1