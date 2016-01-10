s = "a maldicao do sofa ataca novamente"

#for c in s:
    #print(c)

#indice = 0
#while indice < len(s):
    #print(indice, s[indice])
    #indice +=1

#for k,v in enumerate(s):
    #dicio.append(k)
    #dicio.append(v)
    #print(k, v)

dicio= {}
dicio = dict(enumerate(s))
print(dicio)