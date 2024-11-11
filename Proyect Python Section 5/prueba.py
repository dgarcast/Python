def hola (x):
    
    print("Esto es: " + x)
    
hola("Blanco")

def money (num1):
    
    resulTotal = num1 * 0.90
    return resulTotal

resultado = money(3)
print(resultado)

def cifras (lista):
    
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False

resultado = cifras ([23,54,22,35])
print(resultado)


def cifras (lista):
    
    cifrasSave = []   
     
    for n in lista:
        if n in range(100,1000):
            cifrasSave.append(n)
        else:
            pass
    return cifrasSave
resultado = cifras ([233,54,22,355])
print(resultado)


def todos_positivos (lista):
        
    lista_numeros = []
        
    for n in lista:
        if n < 0:
           return False
        else:
            pass
    return True
            
    
resultado = todos_positivos([1,2,-3,-5,7,-9])
print(resultado)

precio = 5
precio_mayor = 0
print(precio_mayor)
precio_mayor = precio

print(precio_mayor)



precios_supermecado = [('COLACAO', 2.50), ('COCACOLA',3),('SUAVIZANTE', 4.5), ('RON',15), ('PAÑALES', 8)]

def supermercado (lista_precios):
    
    precio_mayor = 0
    producto_mayor = ''
    
    for producto, precio in lista_precios:
        print(precio,producto)
        if precio > precio_mayor:
            precio_mayor = precio
            producto_mayor = producto
        else:
            pass
    return (producto_mayor, precio_mayor)




producto, precio = supermercado(precios_supermecado)
print(f" El producto se llama: {producto} y tiene un precio de: {precio}")

