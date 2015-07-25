__author__ = 'guilhermefelitti'
x = 0
PA = 80000
PB = 200000

while PA <= PB:
    PA = PA + PA*0.03
    PB = PB + PB*0.015
    x = x+1

print("Demorou %5.2f anos para a A passar a B" %x)