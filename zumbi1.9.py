__author__ = 'guilhermefelitti'
d = int(input("Quantos dias de aluguel:"))
m = float(input("Qual foi a media de km diaria:"))
total = m*d
preco = d*60 + total*15/100
print("Voce rodou um total de %.2f quilometros" %total)
print("A conta toda deu R$ %.2f" %preco)