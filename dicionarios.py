__author__ = 'guilhermefelitti'

alice = open("alice.txt")
texto = alice.read()
texto = texto.lower()
import string
for c in string.punctuation:
    texto = texto.replace(c, " ")
texto = texto.split()

dic ={}
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1

print(dic["rabbit"])
print(dic["alice"])
print(dic["get"])
alice.close()
