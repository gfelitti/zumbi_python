__author__ = 'guilhermefelitti'
__author__ = 'guilhermefelitti'
import random
lista = []
k = 1

while len(lista) < 15:
    x = random.randint(1,100)
    if x not in lista:
        lista.append(x)

lista.sort()
print(lista)