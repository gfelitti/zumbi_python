__author__ = 'guilhermefelitti'
arquivo = open("ola.html", "w", encoding="utf-8")
arquivo.write("""<!DOCTYPE html>
<html lang = "pt-BR">
<head>
<meta charset="utf-8")
<title>Título da página</title>
</head>
<body>
Olá!
</body>
</html>""")
arquivo.close()