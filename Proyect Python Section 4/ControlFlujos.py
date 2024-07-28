""" 
IF = si ocurre tal cosa
ELIF = Es una mezcla y significa si no ocurre tal cosa, ocurre otra
else =  Sino

"""

if 10 > 9:
    print("Es correcto")

if True:
    print("Es correcto")

if 5 == 2:
    print("Es correcto") #No imprime nada pq no es correcto y no lee esta linea
else:
    print("No es correcto") #Lee esta linea porque es incorrecto
    
mascota = 'perro'

if mascota == 'gato':
    print("Tienes un gato")
elif mascota == 'perro':
    print("Tienes un perro")
elif mascota == 'pez':
    print("Tienes un pez")
else:
    print("No se que animal tienes")
    
    
edad = 16
calificacion = 9

if edad < 18:
    print("Menor de edad")
    if calificacion >= 7:
        print("Esta aprobado")
    else:
        print("Suspenso")
else:
    print('Eres adulto')