__author__ = 'guilhermefelitti'
nome = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

while nome == senha:
    print("Nome e senha não podem ser iguais")
    nome = str(input("Digite seu nome de usuário: "))
    senha = input("Digite sua senha: ")
