class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

tv_quarto = Televisao()
tv_sala = Televisao()

print(tv_quarto.ligada)
print(tv_quarto.canal)

tv_sala.canal = 7
tv_sala.ligada = True

print(tv_sala.canal)
print(tv_sala.ligada)