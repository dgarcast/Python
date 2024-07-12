"""
 
mi_dic = {'c1':'valor1','c2':'valor2','c2':'valor2'}


"""

diccionario = {'c1':'valor1','c2':'valor2','c2':'valor2'}
print(type(diccionario)) #dict
print(diccionario)

resultado = diccionario['c1'] #Para buscar el valor de un indice 
print(resultado) #valor1

cliente = {'nombre':'Juan','apellido':'Fuentes','peso':88,'talla':1.76}
consulta = cliente['apellido']
print(consulta) #Fuente

dic = {'c1':55, 'c2':[10,20,30],'c3':{'s1':100,'s2':200}}

print(dic['c2'][1]) #Imprime lo que haya en el diccionario en el indice 2 y con el otro colchete lo que hay en el indice de la lista
print(dic['c3']['s2']) #Esto busca dentro del diccionario dentro de otro diccionario

dic = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic['c2'][1].upper()) #E

dic = {1:'a',2:'b'}
print(dic)
dic[3] = 'c' #Añade un nuevo valor al diccionario
print(dic)

dic[2] = 'B' #Esto lo que hace es sobrescribir
print(dic)

print(dic.keys()) #Esto imprime los indices ... dict_keys([1, 2, 3])
print(dic.values()) #Esto imprime los valores ... dict_values(['a', 'B', 'c'])
print(dic.items()) #Se ve todos los elementos del diccionario

