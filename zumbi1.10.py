__author__ = 'guilhermefelitti'
media = int(input("Quantos cigarros voce fuma por dia:"))
vida = int(input("Ha quantos anos voce eh fumante:"))
total_cigarros = vida*365*media
total_tempo = total_cigarros*10
total_dias = total_tempo/1440
print("Voce ja perdeu %.2f dias de vida por fumar" %total_dias)
