__author__ = 'guilhermefelitti'
print("Vamos contar quantas letras tem cada palavra?")
print()
while True:
    s = input("Escreva qualquer palavra (quit para parar): ")
    if s == "quit":
        break
    print("Sua palavra tem %d letras" %len(s))
    print()