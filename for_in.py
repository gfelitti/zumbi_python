import time

lista = ["amor", "coco", "vomito", "velhinha"]

for c in range(100,200,14):
    print(c)

lista = [i for i in range(100,367,8)]
print("Essa lista tem", len(lista), "números")
print(sum(lista))

lista1 = list(range(0,100,2))
print("Essa lista tem", len(lista1), "números")
print(sum(lista1))

media = [(x+(x-1)) / 2 for x in lista1]
print(media)

for i in range (78):
    if i>= 75:
        print("Chegou!")
        break
    print(i)
print("Terminou em 75")