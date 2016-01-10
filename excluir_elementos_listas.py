loop = True
lista = ['antonio', 'celso', 'cicero', 'damiao', 'louca do 11 andar', 'paulo', 'república', 'sandro', 'antonio']

a = input("Esse nome está na lista?: ")

while loop == True:

    if a in lista:
        print(a, "está na posição", lista.index(a), "da lista")
    else:
        print(a, "não está na lista!")
