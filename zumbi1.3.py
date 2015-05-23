__author__ = 'guilhermefelitti'
d = int(input("Dias:"))
h = int(input("Horas:"))
m = int(input("Minutos:"))
s = int(input("Segundos:"))

total = d*8640 + h*3600 + m*60 + s
print(total)
