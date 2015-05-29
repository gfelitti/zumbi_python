__author__ = 'guilhermefelitti'
a = int(input("O primeiro lado do triângulo: "))
b = int(input("O segundo lado do triângulo : "))
c = int(input("A base do triângulo: "))
if a > b + c or b > a + c or c > a + b:
    print("Um triângulo não pode ter um lado maior que a soma dos outros dois lados")
elif a == b == c:
    print("Seu triângulo é equilátero")
elif a == b and b != c:
    print("Seu triângulo é isósceles")
elif a == 0 or b == 0 or c ==0:
    print("Não dá para fazer um triângulo com lado zero. Tente de novo")
else:
    print("Seu triângulo é escaleno")
