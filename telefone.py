__author__ = 'guilhermefelitti'
m = int(input("Minutos falados: "))
if m < 200:
    preco = 0.2
elif m <= 400:
    preco = 0.18
elif m <= 800:
    preco = 0.15
else:
    preco = 0.08

print("Conta telefônica será de R$ %.2f" %(m*preco))