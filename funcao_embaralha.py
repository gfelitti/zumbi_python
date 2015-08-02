__author__ = 'guilhermefelitti'
chat = True

def embaralha(x):
    import random
    lista = list(x)
    random.shuffle(lista)
    return "".join(lista)

while chat == True:
    print(embaralha(input("Digite qualquer palavra:")))


