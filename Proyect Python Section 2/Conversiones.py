#El proceso de convertir un tipo de dato a otro se llama CASTING
#y existen dos tipos de datos, IMPLICITAS y EXPLICITAS

#IMPLICITAS: Python convierte el tipo de datos en otro tipo de datos automaticamente.
#En este proceso, el usuario no debe hacer nada.

#EXPLICITAS: Phyton necesita que el usuario haga algo para convertir un tipo de dato en otro

#mi_valor = 1
#otro_valor = string(mi_valor)
#print(otro_valor)

num1 = 30
num2 = 40.5
print(type(num1)) #integer
print(type(num2)) #float

num1 = num1 + num2
print(type(num1)) #float
print(type(num2)) #float
#num1 deja de ser un integer porque la suma es con num2 que es un float
#por lo que se convierte en un tipo float de forma implicita

num1 = 5.8
print(num1)
print(type(num1))

#Asi se hace una conversion de tipo float a tipo integer, es una conversion explicita
#num1 es de tipo float y hacemos un casting explicito para convertirlo en integer, truncando el valor.
#elimina completamente el decimal.

num2 = int(num1)
print(num2) #5
print(type(num2)) #integer

edad = input("Dime tu edad: ") #el valor edad es un string
edad = int(edad) #hacemos un casting y pasamos edad a un integer
nueva_edad= 1 + edad
print(nueva_edad)
print(type(nueva_edad))
print("Tu nueva edad es: " + nueva_edad) #Esto es un error debido a que  no se puede concatenar un string
                                        #con un integer, porque el + no sabe si concatenar o sumar, porque son dos datos distintos
