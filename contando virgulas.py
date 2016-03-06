import 
arq = open("grandeC_pont.txt", "r")
texto = arq.read()

dic ={ }
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1

print(",", dic[","])
print(";", dic[";"])
#print("( é usada", dic["("], "vezes")
#print(". é usada", dic["."], "vezes")
#print(") é usada", dic[")"], "vezes")
#print(": é usada", dic[":"], "vezes")
#print("- é usada", dic["-"], "vezes")
#print("% é usada", dic["%"], "vezes")
#print("$ é usada", dic["$"], "vezes")
#print("? é usada", dic["?"], "vezes")
#print("! é usada", dic["!"], "vezes")
#print("~ é usada", dic["~"], "vezes")
#print("' é usada", dic["'"], "vezes")
#print(" é usada", dic["`"], "vezes")


arq.close()