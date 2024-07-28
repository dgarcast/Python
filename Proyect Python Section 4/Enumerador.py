
lista = ['a','b','c']

indice = 0

for item in lista:
    print(indice,item)
    indice += 1

for item in enumerate(lista):
    print(item)

for indice, item in enumerate(lista):
    print(indice,item)

for indi, item in enumerate(range(18,24)):
    print(indi,item)

mis_tuples = list(enumerate(lista))
print(mis_tuples[1][0])
    