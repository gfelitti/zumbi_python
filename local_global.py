__author__ = 'guilhermefelitti'
a = 9

def muda_e_imprime():
    global a
    a = 7
    print("a dentro da função: %d" %a)

print("a antes da função: %d" %a)
muda_e_imprime()
print("a depois da função: %d" %a)
