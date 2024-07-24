""" 
Crear un programa que le diga al usuario que ingrese un texto
ingrese tambien 3 letras a su eleccion
hacemos 5 tipos de analisis
cuantas veces apareces cada letra (almacenar las letras en una lista y contar los substring (pasamos el textoa minuscula))
cuantas palabras hay en total  (metodo de string que hace transformarlo en lista y leer todo)
primera y utlima letra
palabras en orden inverso
aparece la parte python? podemos usar booleanos"""

texto = input("Ingresar el texto que te apetezca: ")

letras = []
letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la primera letra: ").lower())

print("\n")

print("CANTIDAD DE LETRAS")
cantidadLetras = texto.count(letras[0])
cantidadLetras2 = texto.count(letras[1])
cantidadLetras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida '{cantidadLetras}'")
print(f"Hemos encontrado la letra '{letras[1]}' repetida '{cantidadLetras2}'")
print(f"Hemos encontrado la letra '{letras[2]}' repetida '{cantidadLetras3}'")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras de tu texto")

print("\n")
print("LETRAS DE INICIO Y DE FIN")
letras_inicio = texto[0]
letras_final = texto[-1]
print(f"La letra de incio es {letras_inicio} y la letra final es {letras_final}")

print("\n")
print("TEXTO INVERTIDO")

textoInvertido = texto.split()
textoInvertido.reverse()
invertido = ' '.join(textoInvertido)
print(f"Texto al reves: {invertido}")


print("\n")
print("BUSCANDO LA PALABRA PYTHON")

buscador = 'python' in texto
dic = {True: "si", False:"no"}
print(f"Esta la palabra python: {dic[buscador]}")
















