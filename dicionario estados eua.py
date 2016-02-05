estados = {
"São Paulo": "SP",
"Rio Grande do Norte": "RN",
"Espírito Santo": "ES",
"Sergipe": "SE",
"Pará": "PA",
"Amazonas": "AM"
}

cidades ={
    "SP": "São Paulo",
    "ES": "Vitória",
    "SE": "Aracaju",
    "PA": "Belém"
}

cidades["AM"] = "Manaus"
cidades["RN"] = "Natal"

print("-"*10)
print("O estado do Sergipe tem:", cidades["SE"])
print("O estado do Amazonas tem:", cidades["AM"])

print("-"*10)
print("A abreviação de Rio Grande do Norte é", estados["Rio Grande do Norte"])
print("A abreviação do Pará é", estados["Pará"])

print("-"*10)
print("Belém tem:", cidades[estados["Pará"]])
print("Espírito Santo tem", cidades[estados["Espírito Santo"]])

print("-"*10)
for estados, abreviacao in estados.items():
    print("%s é abreviado como %s" %(estados, abreviacao))

print("-"*10)
for abreviacao, cidades in cidades.items():
    print("%s tem a cidade %s" %(abreviacao,cidades))


#estados = estados.get("Paraná")
#if not estados:
    #print("Desculpe, sem Paraná")