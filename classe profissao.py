# coding=UTF-8
class CV:
    def __init__(self, nome, idade, cargo, empregador):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.empregador =  empregador

    def apresentacao(self):
        print("Meu nome é %s, tenho %i anos e trabalho como %s na empresa %s" %(self.nome, self.idade, self.cargo, self.empregador))

    def pretensao(self, quero, proposta):
        self.quero = quero
        self.proposta = proposta
        if self.quero > self.proposta:
            print("Então não queremos contratá-lo.")
        else:
            print("Bem-vindo!")

print
guilherme = CV("Guilherme Felitti", 32,"jornalista", "Editora Globo")
guilherme.apresentacao()
guilherme.pretensao(8000,6000)

print
ellen = CV("Ellen Rocha", 28, "animadora", "FQ")
ellen.apresentacao()
ellen.pretensao(5000,6000)

a = str(input("Digite seu nome:"))
b = int(input("Digite sua idade: "))
c = str(input("Digite sua profissão: "))
d = str(input("Digite seu empregados: "))

novo_usuario = CV(a,b,c,d)
novo_usuario.apresentacao()
