"""
Una lista es una secuencia ordenada de objetos 

mi_lista =[12,34,12,'david',34.5]

"""

mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
resultado = len(mi_lista) #3
resultado = mi_lista[0] #a
resultado = mi_lista[0:1] #['a']
resultado = mi_lista[1:] #['b', 'c']
resultado = mi_lista[:2] #['a', 'b']
mi_lista3 = mi_lista + mi_lista2 #['a', 'b', 'c', 'd', 'e', 'f']
mi_lista3[0] = 'alfa' #['alfa', 'b', 'c', 'd', 'e', 'f']
    #Cambia en el indice 0 la letra a por alfa
mi_lista3.append('p') #Agrega el elementos p al final de la lista 
mi_lista3.pop() #Esto elimina el ultimo elemento de la lista
mi_lista3.pop(0) #Esto elimina el elemento en el indice indicado

print(mi_lista3)
print(resultado)

lista = ['g','o','b','m','c']
lista.sort() #Sort reordena la lista
lista.reverse() #lo ordena en orden alfabetico pero al contrario
print(lista)




