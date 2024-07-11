"""
Metodo index()... STRING
H O L A
0 1 2 3

¡   H   O   L   A       M   U   N   D   O   !
0   1   2   3   4   5   6   7   8   9   10  11

¡   H   O   L   A       M   U   N   D   O   !
0  -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1

Metodo index()
1-Conocer el indice de un caracter

mi_texto = "hola"
mi_texto.index("0")

2-Conocer que caracter hay en un indice

mi_texto[3]

"""


mi_texto = "Esta es una prueba"
resultado = mi_texto[0] #E
resultado2= mi_texto[9] #n
resultado3= mi_texto[-4] #u
print(resultado)
print(resultado2)
print(resultado3)

resultado = mi_texto.index("prueba")
print(resultado)

resultado = mi_texto.index("a",5,11)
print(resultado)

resultado = mi_texto.rindex("a") #Busca con el indice al reves
print(resultado)