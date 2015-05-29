__author__ = 'guilhermefelitti'
print("Digite abaixo a altura e a largura da parede a ser pintada:")
altura = float(input("Altura: "))
largura = float(input("Largura: "))
area = altura*largura
litros = area/3
print("Você precisará de %.2f litros para pintar os %.2f metros quadrados da sua parede" %(litros, area))
latas = litros/18
preco = 80

if latas <= 1:
    print("Você precisará de uma lata e gastará %.2f" %preco)
elif latas > 1:
    print("Você precisará de")