a = 10
b = 25
c = 66

x = int(input("Digite um número: "))

if (x ==a or x==b or x ==c):
    print("Está contido")
else:
    print("Não está")

if (x in [a,b,c]):
    print("Está contido")
else:
    print("Não está")

cores = ["amarelo", "verde", "cinza", "vermelho", "azul"]
while True:
    cor = input("Digite uma cor. Zero para sair: ")
    if cor =="0":
        break
    if cor in cores:
        print("Acertou")
    else:
        print("Não está contida")