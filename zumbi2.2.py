__author__ = 'guilhermefelitti'
ano = int(input("Qual ano você quer saber se é bissexto:"))
if ano % 4 == 0 and (ano % 100 != 0 or a % 400 != 0):
    print("Sim, é bissexto")
else:
    print("Não é bissexto")