__author__ = 'guilhermefelitti'
dia, mes, ano = input("Coloque qualquer data no formato DD/MM/AAAA: ").split("/")
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
         "agosto", "setembro", "outubro", "novembro", "dezembro"]

print("A data que você colocou é", dia, "de", meses[int(mes) - 1], "de", ano)