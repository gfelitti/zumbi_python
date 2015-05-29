__author__ = 'guilhermefelitti'
horas = int(input("Quantas horas você trabalha por mês: "))
salhora= float(input("Quanto você ganha por hora: "))
saltotal = salhora*horas

print("Seu salário bruto todo mês é de %.2f reais. Agora vem os descontos:" %saltotal)

ir = saltotal*0.11
inss = saltotal*0.08
sindicato = saltotal*0.05
desconto = ir + sindicato + inss

print("IR = %.2f" %ir)
print("INSS = %.2f" %inss)
print("Sindicato = %.2f" %sindicato)
print("Salário líquido: %.2f" %(saltotal - desconto))
