__author__ = 'guilhermefelitti'
a = int(input("Número 1:"))
b = int(input("Número 2:"))
c = int(input("Número 3:"))
if a >= b and a >= c:
    print("O maior é o %d" %a)
elif b >= c:
    print("O maior é o %d" %b)
else:
    print("O maior é o %d" %c)
