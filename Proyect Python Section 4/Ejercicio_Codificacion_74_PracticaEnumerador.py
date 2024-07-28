""" 
Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() los índices de cada caracter del string "Python".

Llama a la lista obtenida con el nombre de variable lista_indices .
"""

palabra = "python"

lista_indices = list(enumerate(palabra))
for indice, elemento in lista_indices:
    print(indice,elemento)