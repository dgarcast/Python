palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra)
    
print(lista)


lista = [letra for letra in palabra]
print(lista)

lista = [nn for nn in range(4,44)]
print(lista)
    