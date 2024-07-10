mi_numero = 1
print(mi_numero)

#Type te da la informacion del tipo de variable que es
print(type(mi_numero))

#El mas sirve para concatenar dos string pero en este caso
#son dos integer por lo que al concatenarlo, se suma las dos variables
mi_numero = 1 + 5
print(mi_numero + mi_numero)
print(type(mi_numero))

#Esto es una clase float, no integer
mi_numero= 5.9
print(type(mi_numero))

mi_numero= 5 + 7.6
print(type(mi_numero))

#Todo lo que ingresemos por un input se transforma en un STRING
edad = input("Dime tu edad: ")
print("Tu edad es: " + edad)
print(type(edad))

#Para solucionar esto, habria que hacer una conversion de tipos.
