__author__ = 'guilhermefelitti'
import random
import operator

vetor1 = []
vetor2 = []

for i in range(10):
    vetor1.append(random.randint(1,100))
    vetor2.append(random.randint(1,100))

vetor3 = [20]*(len(vetor1)+len(vetor2))
vetor3[::2] = vetor1
vetor3[1::2] = vetor2

print(vetor1)
print(vetor2)
print(vetor3)