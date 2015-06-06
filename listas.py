__author__ = 'guilhermefelitti'
notas = [6,7,5,2,9]
soma = 0
x = 0

while x< 5:
    soma = soma + notas[x]
    x = x+1
print("Media: %5.2f" %(soma/x))


vetor = []
i = 1
while i <= 5:
    n = int(input("Digite um número: "))
    vetor.append(n)
    i = i + 1
print ("Vetor lido", vetor)