'''
def argumentos (*args)

    for arg in args:
        print(arg)
        
    return
    
argumentos(9,5,4,2)

El args lo que hace es coger todo el grupo de elemento y trabajar con el.
En este caso lo que hace es agrupar los elementos.
'''

def suma (*args):
    return(sum(args))

resultado = suma(1,2,4,5,4)
print(resultado)