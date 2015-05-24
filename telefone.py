__author__ = 'guilhermefelitti'
m = int(input("Minutos falados: "))
if m < 200:
    preco = 0.2
else:
    if m <= 400:
        preco = 0.18
    else:
        preco = 0.15

valor = m*preco

print("Conta telefônica será de R$ %.2f" %valor)