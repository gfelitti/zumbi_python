__author__ = 'guilhermefelitti'

def fatorial(n):
    f = 1
    while n > 0:
        f = f*n
        n = n-1
    return f

print(fatorial(10))