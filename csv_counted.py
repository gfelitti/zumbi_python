__author__ = 'guilhermefelitti'
import csv

i = []

f = csv.reader(open("counted.csv", "r", encoding="utf-8"), delimiter =";")
for row in f:
    i.append(row[1])

print(i)