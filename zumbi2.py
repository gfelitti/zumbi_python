__author__ = 'guilhermefelitti'
m = int(input("Quantos minutos nesse mês você falou pelo celular?"))
if m < 200:
    v = 0.2
if m >= 200 and m < 400:
    v = 0.18
else:
    v = 0.15

print("Sua conta esse mês será de R$ %.2f" %(m*v))