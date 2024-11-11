'''
def suma(**kwargs)
    #AlgunCodigo

suma(1,2,3)

Podemos escribir tantos argumentos ocmo queramos y tambien podemos darle un nombre a los argumentos
pudiendo acceder a ellos dentro de la funcion atravez de un diccionario y obtener su item completo o solamente su clave o solamente su valor 
'''


def suma(**kwargs):
    
    total = 0
    
    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
    return total
    
print(suma(x=4, y=3, z=1))

def prueba(num1, num2, *args, **kwargs):
    
    print(f'el primer valor es {num1}')
    print(f'el segundo valor es {num2}')
    
    for arg in args:
        print(f'arg = {arg}')
    
    
    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')
        
args = [100,200,300,400,500]
kwargs = {'x':'uno','y':'dos','z':'tres'}
    
prueba(15,50, *args, **kwargs)