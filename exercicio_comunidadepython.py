texto = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."
texto = texto.lower()

import string

for c in string.punctuation:
    texto = texto.replace(c, "")
texto = texto.split()

lista =[]
lista1 = []
lista2 =[]
for e in texto:
    if e[0] in "python":
        lista.append(e)

for e in texto:
    if e[-1] in "python":
        lista.append(e)

for palavra in texto:
    for letra in palavra:
        if letra in "python":
            lista1.append(palavra)
        if palavra in lista1:
            break

for palavra in lista1:
    if len(palavra) > 4:
        lista2.append(palavra)

print("A lista original tem", len(texto), "itens")
print("A lista que tem palavras que comecem ou terminam com python tem", len(lista), "caracteres")
print("A lista com palavras que tenham letras de python tem", len(lista1), "itens")
print("Por fim, a lista acima reduzida a palavras com mais de 4 caracteres tem", len(lista2), "itens")

print(lista1)
print(lista2)

