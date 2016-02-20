import datetime
class Pessoa():
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
    def idade(self):
        delta = datetime.date.today() - self.nascimento
        return int(delta.days/365)
    def __str__(self):
        return "%s, %d anos" %(self.nome, self.idade())

masanori = Pessoa("Fernando Masanori", datetime.date(1980, 9,1))
felitti = Pessoa("Guilherme Felitti", datetime.date(1983,3,25))

print(masanori.idade())
print(masanori)
print(felitti.idade())
print(felitti)