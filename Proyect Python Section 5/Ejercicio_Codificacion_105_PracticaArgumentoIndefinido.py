'''
Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

La función debe devolver el siguiente mensaje:

"{nombre}, la suma de tus números es {suma_numeros}"
'''

def numeros_persona (nombre, *args):
    
    suma=0
    nomb=''
    for nombre, sumatorio in args:
        suma += sumatorio
        nomb = nombre
    return nomb, suma

nombre, suma = numeros_persona('David',1,3,4,5,6,7)

print(f'{nombre} y la suma de tus numeros es {suma}')