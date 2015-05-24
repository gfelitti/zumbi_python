__author__ = 'guilhermefelitti'
m = int(input("Quantos minutos nesse mês você falou pelo celular?"))
if m < 200:
    v = 2/10
    print("Sua conta esse mês será de R$ %.2f" %(m*v))
if m >= 200 and m < 400:
    v = 18/10
    print("Sua conta esse mês será de R$ %.2f" %(m*v))
else:
    v = 15/10
    print("Sua conta esse mês será de R$ %.2f" %(m*v))