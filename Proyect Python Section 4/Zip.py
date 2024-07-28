""" 
nombres = ['Juan','Pablo','Ana']
edades = [25,42,33]

zip(nombres,edades)

>>[('Juan',25),('Pablo',42),('Ana',33)]

"""

nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]
ciudades = ['lima','madrid','mexico','nueva york']

combinados = list(zip(nombres,edades,ciudades))
print(combinados)

for nombre,edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} y vive en {ciudad}")



