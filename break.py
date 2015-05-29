__author__ = 'guilhermefelitti'
soma = 0
while True:
    x = int(input("Digite seu número (e 0 para soma): "))
    if x == 0:
        break
    soma = soma + x
print("soma: %d" %soma)