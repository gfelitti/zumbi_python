__author__ = 'guilhermefelitti'
import csv
contas = [linha for linha in csv.reader(open("DB.csv", "rt", encoding="utf-8"), delimiter=",")]
header = contas.pop(0)
print(header)

outfile = open("db_format.csv", "wb")
outfilewriter = csv.writer(outfile, delimiter=",")

for linha in contas:
    for letra in linha:
        if letra in "aeiou":
            outfile.write("*")
        else:
            outfile.write(letra)


outfile.close()