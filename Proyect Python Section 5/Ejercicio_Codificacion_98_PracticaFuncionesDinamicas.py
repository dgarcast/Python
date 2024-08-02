""" 
Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros)
siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.
"""

lista_numeros = [1,3,56,43,2,45,11]

def suma_menores(lista_numeros):
    
    suma = 0
    for num in lista_numeros:
        if num > 0 and num < 1000:
            suma += num
        
    return suma


resultado = suma_menores(lista_numeros)
print(resultado)