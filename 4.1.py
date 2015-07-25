__author__ = 'guilhermefelitti'
nota = float(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("Notas entre 0 e 10, animal!")
    nota = float(input("Digite uma nota: "))
