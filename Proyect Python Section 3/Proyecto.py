""" 
Crear un programa que le diga al usuario que ingrese un texto
ingrese tambien 3 letras a su eleccion
hacemos 5 tipos de analisis
cuantas veces apareces cada letra (almacenar las letras en una lista y contar los substring (pasamos el textoa minuscula))
cuantas palabras hay en total  (metodo de string que hace transformarlo en lista y leer todo)
primera y utlima letra
palabras en orden inverso
aparece la parte python? podemos usar booleanos
"""

texto = input("Ingresa el texto que te apetezca: ")
letra1 = input("Ingresa la primera letra: ")
letra2 = input("Ingresa la segunda letra: ")
letra3 = input("Ingresa la tercera letra: ")

texto = texto.lower()
print(texto)

texto = list(texto)
repeticionLetras = texto
print(repeticionLetras)
print(type(texto))
