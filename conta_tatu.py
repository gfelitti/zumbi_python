__author__ = 'guilhermefelitti'
from banco_tatu import Cliente
from banco_tatu import Conta

joao = Cliente("Joao da Silva", "4341993")
maria = Cliente("Maria da silva", "4372176")

print("Nome: %s. Telefone: %s."
      %(joao.nome, joao.telefone))

print("Nome: %s. Telefone: %s."
      %(maria.nome, maria.telefone))

conta1 = Conta([joao], 1, 1000)
conta2 = Conta([maria, joao], 2, 500)
conta1.resumo()
conta2.resumo()