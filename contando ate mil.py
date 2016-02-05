import random
lista = range(1,1001)
lista2 =[ ]
lista3 =[ ]
lista4 =[ ]
lista5 =[ ]
lista6 =[ ]
lista7 =[ ]
lista8 =[ ]
lista9 =[ ]

for i in lista:
    if i%2 ==0:
        lista2.append(i)

for i in lista:
    if i%3 ==0:
        lista3.append(i)

for i in lista:
    if i%4 ==0:
        lista4.append(i)

for i in lista:
    if i%5 ==0:
        lista5.append(i)

for i in lista:
    if i%6 ==0:
        lista6.append(i)

for i in lista:
    if i%7 ==0:
        lista7.append(i)

for i in lista:
    if i%8 ==0:
        lista8.append(i)

for i in lista:
    if i%9 ==0:
        lista9.append(i)

print("2 -", len(lista2), 500*2)
print("3 -", len(lista3), 333*3)
print("4 -", len(lista4), 250*4)
print("5 -", len(lista5), 200*5)
print("6 -", len(lista6), 166*6)
print("7 -", len(lista7), 142*7)
print("8 -", len(lista8), 125*8)
print("9 -", len(lista9), 111*9)

print(lista[-1])