#login = input("Digite seu login: ")
#senha = input("Digite sua senha: ")

#print("seu login é %s e a senha digitada é %s" %(login,senha))
#num = int(input("Digite um número entre 10 e 99: "))
#tens = num // 10
#ones = num % 10
#print(num)
#print(tens)
#print(ones)

#num1 = float(input("Digite um número: "))
#num2 = float(input("Digite outro número: "))

#divisao = num1 / num2
#resto = num1 % num2
#print(num1, "dividido por", num2, "é igual a: %5.13f" %divisao)
#print("O resto da divisão entre", num1, "e", num2, "é igual a %i" %resto)

#if num1 % 2 == 0:
    #print("Seu número é PAR")
#else:
    #print("Seu número é impar")
#import math

#print(5**306)
#print(math.pi)

loop = True

#while loop == True:

    #acao = int(input("Digite 1 para sim e 2 para nao: "))
    #if(acao ==1):
        #print("Você disse que sim")
        #print("Vamos de novo")
    #elif(acao==2):
        #print("Você nao quer, animal")
        #break
    #else:
        #print("É 1 ou 2, salafráfio")


import random
loop = True
while loop == True:
    a = input("Digite qualquer tecla para um número aleatório ou e para sair: ")
    if a == "e":
        break
    else:
        print(random.randint(1,100))

print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))

import random
lista = []

for i in range(17):
    lista.append(i)
    random.shuffle(lista)

print(lista)

lista = []
for i in range(6):
    lista.append(random.randint(1,100))
lista.sort()
print(lista)