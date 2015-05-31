__author__ = 'guilhermefelitti'
number = 25
running = True

while running:
    guess = int(input("Digite o numero: "))

    if guess == number:
        print("Acertou. Parabens!")
        running = False
    elif guess < number:
        print("Mais para cima")
    else:
        print("Mais para baixo")

else:
    print("O jogo termina aqui")