class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
    def canal_mais(self):
        self.canal += 1
    def canal_menos(self):
        self.canal -= 1

tv = Televisao()
print(tv.canal)

tv.canal_mais()
tv.canal_mais()

print(tv.canal)
tv.canal_menos()
print(tv.canal)