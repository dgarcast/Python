"""
Son unas coleccion de elementos, son INMUTABLES

mi_tuples = 'perro','gatos','pajaros'

Los tuples ocupan menos espacio de memoria y se ejecutan mas rapdios que las listas
Al no ser posible modificadas, lo usamos en situaciones que no queramos que nuestros valores no puedan ser modificados

"""

mi_tuple = (1,2,3,4)
mi_tuple = 1,2,3,4
#Lo mas comun es verlo entre parentesis
print(type(mi_tuple))

print(mi_tuple[0]) #1
print(mi_tuple[-1]) #derecha a izquierda ... 4

#mi_tuple[0] = 5 #Esto no es posible debido que son inmutables y no se pueden modificar

mi_tuple = (1,2,(10,20),4)
print(mi_tuple[2]) #Busca en el tuple la posicion 2
print(mi_tuple[2][1]) #Busca en el tuple en la posicion 2 y dentro de la posicion

mi_tuple = list(mi_tuple) #hemos hecho un casting para pasarlo como tipo lista... ahora si se puede modificar porque no es un tuples, es una lista

#Asignar el contenido de un tuple a diferentes variables
t=(1,2,3)
x,y,z = t
print(t) #(1,2,3) al tener la misma cantidad de valores que de variables se asigna una a una... en la lista y los diccionarios tambien puede ser asi

t=(1,2,3,1)
print(len(t)) #4 elementos

print(t.count(1)) #El metodo count cuenta las cantidad de aparacion de un elemento dentro de un tuples
print(t.index(2)) #1

      


