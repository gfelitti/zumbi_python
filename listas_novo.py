lista_indice = [0,1,2,3]
lista_nums = [100,200,300,400]
for item in lista_indice:
    lista_nums[item]+=1000
print(lista_nums)

print()

lista_nums = [100,200,300,400,500,600,700,800,900,1000]
for item in range(len(lista_nums)):
    lista_nums[item]+=1000
print(lista_nums)

print()

lista_nums = [100,200,300,400]
for idx, item in enumerate(lista_nums):
    lista_nums[idx]+=1000
print(lista_nums)
