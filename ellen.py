__author__ = 'guilhermefelitti'

chat = True

while chat:
    fala = str(input("Fale alguma coisa, Ellen (ou tchau para sair): "))
    if fala == "Gigi":
        print ("Guilherme: Oi")
        print()
    elif fala == "Ce me ama?":
        print ("Guilherme: Amo")
        print()
    elif fala == "Ama muito?":
        print ("Guilherme: Muito")
        print()
    elif fala == "tchau":
        print("Guilherme: Tchau, gatinha!")
        chat = False
    else:
        print ("Coisinha linda, fala de novo")
        print()

