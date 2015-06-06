__author__ = 'guilhermefelitti'

vetor =[]
x = 1
while x <= 10:
    n = int(input("Digite um número: "))
    vetor.append(n)
    x = x + 1
x = 9
while x >= 0:
    print(vetor[x])
    x -= 1