__author__ = 'guilhermefelitti'
#arquivo = open("mensagem.txt", "w")
#for linha in range(1,101):
    #arquivo.write("%d\n" % linha)
#arquivo.close()

#arquivo = open("numeros.txt", "r")
#for linha in arquivo.readlines():
    #print(linha.rstrip())
#arquivo.close()

texto = open("mensagem.txt")
saida = open("cripto.txt", "w")
for linha in texto.readlines():
    for letra in linha:
        if letra in "aeiou":
            saida.write("*")
        else:
            saida.write(letra)

texto.close()
saida.close()