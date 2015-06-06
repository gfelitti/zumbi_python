__author__ = 'guilhermefelitti'
notas = []
soma = 0
x = 1
while x<=4:
    n = float(input("Digite a nota:"))
    notas.append(n)
    soma += n
    x = x + 1
print("Notas:", notas)
print("A media é %5.2f" %(soma/4))
