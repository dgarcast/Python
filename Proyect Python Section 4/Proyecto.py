""" 
El programa le va a preguntar al usuario su nombre
nombre = input()
El usuario debe pensar un nombre del 1 al 100 y tiene 8 intentos para adivinarlo
en cada intento el usuario dira un numero
+Si el numero es menor a 1 o superior a 100 dira que ha elegido un numero que no es permitido
+Si el numero es menor, su ruspuesta es correcta y a elegido un numero menor
+Si el numero es mayor, su ruspuesta es correcta y a elegido un numero mayor
+Y acerto, se le dira que ha ganado y cuantos intento le ha llevado

Si no ha acertado en los 8 primero intentos, se le volvera a dar un numero aleatorio y volverlo a intentar
"""
print("---- BIENVENIDO AL JUEGO DEL AÑO ----")
usuario = input("Introduzca su nombre: ")

print(f"Hola {usuario}. Tienes que adivinar un numero del 1 al 50.\n Tendras 8 intentos. \n ¡¡¡ SUERTE !!!")

preparado = input("¿ESTAS PREPARADO PORRA?: (S/N): ").lower()

if preparado == 's':

    from random import *

    aleatorio = randint(1,51)
    print(aleatorio)

    intentos = 0

    while intentos <= 8:
        print(f"Intentos: {intentos}")
        numeroAleatorio = int(input("¿Que numero crees que ha salido?: "))
        if numeroAleatorio < aleatorio:
            print("Respuesta incorrecta. Tu numero es menor. Intentalo de nuevo")
            intentos += 1
        elif numeroAleatorio > aleatorio:
            print("Respuesta incorrecta. Tu numero es mayor. Intentalo de nuevo")
            intentos +=1
        elif numeroAleatorio == aleatorio:
            print(f"Has ganado. Lo has conseguido en '{intentos}' intentos ")
            break

    else:
        print(f"¡¡¡¡¡ HAS PERDIDO. Has agotado todo tus intentos !!!!!! El numero secreto era: {aleatorio} \n Intentalo de nuevo")

else:
    print("INTENTELO DE NUEVO!!")  
        
