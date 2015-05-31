__author__ = 'guilhermefelitti'
while True:
    print("Vamos contar quantas letras tem cada palavra?")
    print()
    s = input("Escreva qualquer palavra (quit para parar): ")
    if s == "quit":
        break
    print("Sua palavra tem %d caracteres" %len(s))