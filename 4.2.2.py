__author__ = 'guilhermefelitti'
import random
lista = []
lista_par = []
lista_impar = []

for i in range(20):
    lista.append(random.randint(1,100))

k = 0
while k <=19:
    if lista[k]%2 == 0:
        lista_par.append(lista[k])
    else:
        lista_impar.append(lista[k])
    k = k+1

print(lista)
print(lista_par)
print(lista_impar)