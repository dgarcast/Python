""" 
- Inmutables: Una vez que ha sido construido el string no se puede cambiar su contenido interno. Para cambiar su contenido debes almacenarla en una variable
            pero su contenido del string es inmutable

- Concatenable: Puede ser concatenable con un +
- Multilineales: con tres comillas se puede hacer saltos de lineas dentro de los string sin necesidad de poner /n
- Verificar si contiene: 
    mi_texto = "hola mundo"
    print("hola" in mi_texto) - true or false
- Calcular su longitud.

"""
nombre = "Carina"
#nombre[0] = "K" #Esto es un error, debido a que el contenido del string es inmutable
nombre = "Karina" #Ahora si se cambia porque creamos una nueva variable con el string que queremos
print(nombre)

n1 = "Kari"
n2 = "na"
print(n1 + n2) #Esto es una concatenacion de dos string
print(n1 * 10) #Esto repite la variable diez veces

poema = """Mil pequeños peces blancos 
como si hirviera
el color del agua"""
print(poema) #Asi hacemos saltos de lineas en un string

print("agua" in poema) #Imprime si agua existe en poema. TRUE
print("Sol" in poema) #FALSE
print("Sol" not in poema) #TRUE

print(len(poema)) #Asi sabemos el largo de un string
