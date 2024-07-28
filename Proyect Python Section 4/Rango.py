""" 
Rango es una funcion que permite estableces un rango de numero sin necesidad
de crear una lista
"""

for numero in range(5): #range(5) crea una lista que va del 0 al 5, pero el 5 no es inclusivo, llega hasta el 4
    print(numero)       #range no acepta float
    
for numero in range(1,5):
    print(numero)
    
lista = list(range(1,101))

print(lista)