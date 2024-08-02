"""  
Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros),
y devuelva el resultado de dicha cuenta.
"""

lista_numeros = [2,4,8,24,54,21,3,11,56,55]

def cantidad_pares(lista_numeros):
    
    pares = 0
    
    for numeros in lista_numeros:
        if numeros%2==0:
            pares = pares + 1
        else:
            pass
    return pares

resultado = cantidad_pares(lista_numeros)
print(resultado)