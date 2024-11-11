'''
Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.
'''

def cantidad_atributos(**kwargs):
    
    
    for atri, valor in kwargs.items():
        print(f'{atri} = {valor}')
    
cantidad_atributos(x='4',t='5')