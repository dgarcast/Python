lista = ["a","b","c","d"]

for dinosaurio in lista:
    numero_letra = lista.index(dinosaurio) + 1
    print(f"Letras: {numero_letra} : {dinosaurio}")
    
    
    
lista = ['pablo','laura','fede','luis','julia']

for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print("Nombre que no comienza con L")

  
    
numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)


palabra = 'python es genial'

for letra in palabra:
    print(letra)
    
for letra in 'python':
    print(letra)


for obj in [[1,2],[3,4],[5,6]]:
    print(obj)
    
for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)
       
       
dic = {'clave1' : 'a', 'clave2' : 'b', 'clave3' : 'c'}

for item in dic:
    print(item)
    
for item in dic.items():
    print(item)

for item in dic.values():
    print(item)
    
for a,b in dic.items():
    print(a,b)