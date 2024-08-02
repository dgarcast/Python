precios_cafe = [('capuchino',1.5),('espresso',1.2),('Mocha',1.9)]

for cafe, precio in precios_cafe:
    print(cafe)

for cafe, precio in precios_cafe:
    print(precio)
    
for elementos in precios_cafe:
    print(elementos)
    
print("-------------------------------------------------")
    
def cafe_mas_caro(lista_precio):
    
    precio_mayor = 0
    cafe_mas_caro = ''
    
    for cafe,precio in lista_precio:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    
    return (cafe_mas_caro,precio_mayor)

print(cafe_mas_caro(precios_cafe))
