#idade = int(input("Digite sua idade: "))
#if idade <= 0 or idade >140:
    #print("Impossível, chapa")
#elif idade <18:
    #print("Você ainda é uma criança")
#elif idade > 60:
    #print("Parabéns, idoso. Vamos jogar gamão?")
#else:
    #print("ótimo. Vai trabalhar")

#loop = True
#while loop == True:

    #numero = int(input("Tente adivinhar o número entre 1 e 99:"))
    #if numero is not 32:
        #print("Errou, cabeça")
        #print()
        #print("Tente de novo")
    #else:
        #print("Acertou!")
        #break

num1 = int(input("Digite um número: "))

if num1>10:
    #print("O número é maior que 10")
    if num1<=15:
        print("O número é mais que 10 e menos que 15")
    else:
        if num1 <=50:
            print("É maior ou igual que 50")
        else:
            print("Maior que 50")
else:
    if num1>5:
        print("O número é maior que 5 e menor que 10")
        if num1==7:
            print("O número é 7")
    else:
        print("O valor é menor que 5")
