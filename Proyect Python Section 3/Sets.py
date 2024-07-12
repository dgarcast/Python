""" 
Los sets son una coleccion de elementos como una lista pero con una particularidad

set(1,2,3,4,5,6)
set{1,2,3,4,5,6}

Los sets solo admite elementos unicos, a los elementos duplicados los descarta autoamticamente Python

Los elementos del sets no estan ordenados en indices, no se puede indexar

Los elementos son inmutables, no se puede añadir lista ni diccionarios

"""

mi_set = set([1,2,3,4,5]) #esto es un set

print(type(mi_set))
print(mi_set)

otro_set = {1,2,3} #Otra manera de mostrar los set
print(type(otro_set))
print(otro_set)

#Los set no se pueden modificar

mi_set = set([1,2,3,4,5,5])
print(mi_set) #Elimina las repeticiones

#No se puede poner listas o diccionarios dentro de los set

mi_set = set([1,2,3,4,(1,2,3),5,5,5,6,7])
#Admiten tuples porque los taples tambien son inmutables como los sets
print(mi_set)

print(len(mi_set)) #8elementos de largo

print(2 in mi_set) #Se puede buscar dentro pero devuelve un TRUE FALSE

#UNION DE SETS
s1 = {1,2,3}
s2 = {3,5,6}
s3 = s1.union(s2)
print(s3) #{1, 2, 3, 5, 6} sin repetir elementos

#AGREGAR ELEMENTOS EN UN SET
s1={1,2,3}
s1.add(4)
print(s1)

#ELIMINAR ELEMENTOS EN UN SET
s1={1,2,3}
s1.remove(2)
print(s1)

s1.discard(6) #Metodo descartar, no da error porque es diferente a eliminar, al no haber un dato para descartar, el programa sigue sin dar error.

s1.pop() #Elimina elementos aleatorios, puede ser buena opcion para un sorteo
print(s1)

s1.clear() #Vacia todo el set



