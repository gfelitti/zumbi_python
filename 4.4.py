__author__ = 'guilhermefelitti'
lista = []
texto = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone Our community is based on mutual respect tolerance and encouragement and we are working to help each other live up to these principles We want our community to be more diverse whoever you are and whatever your background we welcome you"
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