#a = int(input("Digite um número: "))
#print("Seu número é par" if a%2==0 else "Seu número é ímpar")

#b = int(input("Digite um número: "))
#if b%2 ==0:
    #print("Seu número é par")
#else:
    #print("Seu número é ímpar")

#for i in range(18):
    #print(i)

#from datetime import date
#x = 0
#print("while")
#while(x<10):
    #print(x)
    #x+=1
#else:
    #print(date.today())
#print("fim")

import random

lista = []


#for c in "guilherme":
    #lista.append(c)
    #random.shuffle(lista)
a = "guilherme"
x=0
troca =""
while x < len(a):
    if a[x] in "aeiou":
        troca = troca + "*"
    else:
        troca = troca + a[x]
    x+=1
    
print(troca)