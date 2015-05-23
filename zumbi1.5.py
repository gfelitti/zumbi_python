__author__ = 'guilhermefelitti'
p = float(input("Preco do produto:"))
d = float(input("Desconto (em porcentagem):"))
desconto = p * d/100
novo = p - desconto
print("O DESCONTÃO SERA DE R$", desconto)
print("O PRODUTO COM DESCONTÃO SAIRA POR R$", novo)