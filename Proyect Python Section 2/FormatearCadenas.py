#Existen dos tipos de formatear cadenas
#1-Funcion format
#print("Mi auto es {} y de matricula{}", format(color_auto,matricula))

#2-Cadenas literales
#Se añade una f para formatear
#print(f"Mi auto es {color_auto} y matricula {matricula})

x = 10
y = 5

print("Mis numeros son " + str(x) + " y " + str(y))
#Esta es de la manera antigua, formateando los int a str debido a que no se puede concatenar un str y un int sin hacer un casting

print("Mis numeros son {} y {} es igual a {}".format(x,y, x+y))
#Esta es de la manera format
#Tambien podemos añadir una suma
#Pero no es la manera mas elegible, hay otras opciones

color = "rojo"
matricula = 45675

print(f"El color de tu coche es {color} y su matricula es {matricula}")
#Esta manera es mas limpia y mas comoda a la hora de leer, es legible



