'''
Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros. 
Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valor intermedio.

'''

def devolver_distintos(a,b,c):
    
    suma = a+b+c
    lista = [a,b,c]
    
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]
    
print(devolver_distintos(20,15,7))


def letras_unicas(palabra):
    
    mi_set = set()
    
    for letra in palabra:
        mi_set.add(letra)
        
    mi_lista = list(mi_set)
    mi_lista.sort()
    
    return mi_lista

print(letras_unicas("entretenido"))


def ceros_vecinos(*args):
    
    contador = 0
    
    for num in args:
        if args[contador] == 0 and args[contador + 1] == 0:
            return True
        else: 
            contador += 1
    
    return False

print(ceros_vecinos(1,3,3,4,5,3,7,8,6,5,4,3,2,0,0))

def contar_primos(numero):
    
    primos=[2]
    iteracion = 3
    
    if numero < 2:
        return 0
    
    while iteracion <= numero:
        
        for n in range(3,iteracion,2):
            
            if iteracion % n == 0:
                iteracion +=2
                break
            else:
                primos.append(iteracion)
                iteracion += 2

    print(primos)
    return len(primos)

print(contar_primos(50))

