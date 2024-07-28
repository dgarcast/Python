"""  
Las leyes de un país establecen que un adulto puede conducir si tiene licencia para hacerlo, y para optar por una licencia para conducir, debe de tener 18 años o más.

Crea una estructura condicional para verificar si una persona de 16 años sin licencia puede conducir, y muestra el resultado que corresponda en pantalla:

"Puedes conducir"

"No puedes conducir aún. Debes tener 18 años y contar con una licencia"

"No puedes conducir. Necesitas contar con una licencia"

Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones.

"""

edad = int(input("Introduzca tu edad: "))

if edad >= 18:
    print("Puedes conducir")
if edad < 18:
    print("No puedes conducir aun. Debes tener 18 años y contar con una licencia")
elif edad >= 16 and edad < 18:
    print("No puedes conducir. Necesitas contar con una licencia")