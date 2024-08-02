""" 
Crea una función (todos_positivos) que reciba una lista de números como parámetro,
y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo. 
Crea una lista llamada lista_numeros con valores positivos y negativos.

No invoques la función, solo es necesario definirla.
"""

lista_numeros = [1,2,3,-4,-2,-4,-1]

def todos_positivos(lista_numeros):
    for lista in lista_numeros:
        if lista <0:
            return False
        else:
            pass
    return True
    

resultado = todos_positivos(lista_numeros)
print(resultado)

