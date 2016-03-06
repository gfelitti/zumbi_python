arq = open("grandeC.rtf", "r")
texto = arq.read()
texto = texto.lower()
saida = open("grandeC_pont.txt", "w")
#import string
texto = texto.strip()

for linha in texto:
    for letra in linha:
        if letra in ",.;-()%$?!'~`^:":
            saida.write(letra)
        else:
            saida.write("")

arq.close()