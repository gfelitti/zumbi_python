__author__ = 'guilhermefelitti'
import csv

comprador = []
compradorunico = []

f = csv.reader(open("DB.csv"))

for row in f:
    comprador.append(row[3])
for empresa in comprador:
    if empresa not in compradorunico:
        compradorunico.append(empresa)

print(comprador)
print(len(comprador))
print(compradorunico)
print(len(compradorunico))
print(compradorunico[13])