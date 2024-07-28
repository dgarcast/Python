""" 
While --- Mientra la condicion se cumpla....

while una_condicion:
    #un_codigo
else:
    #otro_codigo
    
"""


monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas = monedas - 1
else:
    print("No tengo mas dinero")

respuesta = 's'

while respuesta == 's':
    respuesta = input("Quieres seguir? (s/n) ")
else:
    print("Gracias")


while respuesta == 's':
    pass #Un while nunca puede estar vacio, pues ponemos pass para reservar el while vacio si queremos usarlo en el futuro
print("hola")

nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == 'r':
        break #Interrumpe la condicion
    print(letra)
    

nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == 'r':
        continue 
    print(letra)

