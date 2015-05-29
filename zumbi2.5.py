__author__ = 'guilhermefelitti'
a = int(input("Número 1:"))
b = int(input("Número 2:"))
c = int(input("Número 3:"))
if a >= b and a >= c and b >= c:
    print("O maior é o %d e o menor é o %d" %(a, c))
elif a >= b and a >= c and c >= c:
    print("O maior é o %d e o menor é %d" %(a, b))
elif b >= a and b >= c and a >= c:
    print("O maior é o %d e o menor é %d" %(b, c))
elif c >= a:
    print("O maior é o %d e o menor é %d" %(b, a))
elif c >= a and c >= b and b >= a:
    print("O maior é o %d e o menor é %d" %(c, a))
else:
    print("O maior é o %d e o menor é %d" %(c, b))
