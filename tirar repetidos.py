__author__ = 'guilhermefelitti'
f1 = open('db2.csv', 'r')
f2 = open('db1.csv', 'r')
f3 = open('DB3.1.csv', 'w')

c1 = f1.read()
c2 = f2.read()

for linha in c1:
    if linha not in c2:
        c3.write(linha)

f1.close()
f2.close()
f3.close()