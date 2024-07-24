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

letras = []
letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")
cantidaLetras = texto.count(letras[0])
cantidaLetras2 = texto.count(letras[1])
cantidaLetras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida '{cantidaLetras}' veces ")
print(f"Hemos encontrado la letra '{letras[1]}' repetida '{cantidaLetras2}' veces ")
print(f"Hemos encontrado la letra '{letras[2]}' repetida '{cantidaLetras3}' veces ")

#Uno no es lo que es por lo que escribe, sino por lo que es leido
print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto ")

print("\n")
print("LETRAS DE INICIO Y DE FIN")
letras_inicio=texto[0]
letras_final = texto[-1]
print(f"La letra inicial es {letras_inicio} y la letra final es {letras_final}")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
invertido = ' '.join(palabras)
print(f"Texto al reves : {invertido}")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")

buscarPython = 'python' in texto
dic = {True:"si", False:"no"}
print(f"La palabra python se encuentra:  {dic[buscarPython]} se encuentra en el texto " )

