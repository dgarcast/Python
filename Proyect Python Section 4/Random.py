from random import *

aleatorio = randint(1,50)
print(aleatorio) #Da como resultado numeros aleatorios

aleatorio = round(uniform(1,5),1)
print(aleatorio)

aleatorio = random()
print(aleatorio) #Esto da siempre un 0. algo aleatorio

colores = ["verde","amarillo","rojo","azul"]

aleatorio = choice(colores)
print(aleatorio)

numero = list(range(5,50,5))

shuffle(numero)

print(numero) #Mezcla los numeros que hemos creado en una lista