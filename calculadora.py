__author__ = 'guilhermefelitti'
def soma(x, y):
   return x + y

def sub(x, y):
   return x - y

def multi(x, y):
   return x * y

def divisao(x, y):
   return x / y

print("Selecione a operacao:")
print("1.Soma")
print("2.Subtracao")
print("3.Multiplicacao")
print("4.Divisao")

choice = input("Escolha 1, 2, 3 ou 4:")

num1 = int(input("Primeiro numero: "))
num2 = int(input("Segundo numero: "))

if choice == '1':
   print(num1,"mais",num2,"=", soma(num1,num2))

elif choice == '2':
   print(num1,"menos",num2,"=", sub(num1,num2))

elif choice == '3':
   print(num1,"vezes",num2,"=", multi(num1,num2))

elif choice == '4':
   print(num1,"dividido por",num2,"=", divisao(num1,num2))
else:
   print("Escolha numeros corretos")