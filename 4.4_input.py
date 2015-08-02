__author__ = 'guilhermefelitti'
texto = str(input("Digite aqui quatro palavras seguidas: ")

lista = []

texto = texto.lower()
quebra = texto.split(" ")
palavras = list(quebra)
index = ["p","y","t","h","o","n",]

for i in range(len(palavras)):
    if palavras[i].startswith(tuple(index)) or palavras[i].endswith(tuple(index)):
        lista.append(palavras[i])

print(palavras)
print(len(palavras))
print(lista)
print(len(lista))