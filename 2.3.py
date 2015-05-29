__author__ = 'guilhermefelitti'
maximo = 50
peso = 0
p = float(input("Quantos kilos de peixe Joao trouxe para casa hoje:"))
excesso = (p - 50)
multa = excesso*4

if p <= maximo:
    print("Sem multa hoje, Joao")
if p> maximo:
    print("Como você trouxe %.2f quilos a mais hoje, sua multa será de %.2f reais" %(excesso, multa))


