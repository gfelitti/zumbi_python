__author__ = 'guilhermefelitti'
import random
lista = []
for k in range(10):
    lista.append(random.randint(1,100))
    lista.sort()


print(min(lista))
print(max(lista))
print()
print(lista[0])
print(lista[9])