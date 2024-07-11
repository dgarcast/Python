#Crear un programa que pregunte su nombre

#Deberia empezar pregunta nombre y ventas usando un input

print("--------COMISIONES---------")

nombre = input("Cual es tu nombre?: ")
ventas = input("Cual es la cantidad de la venta: ")

ventas = float(ventas)

operacion_ventas = (ventas*13)/100

#print(round(operacion_ventas,2))
comisiones = round(operacion_ventas,2)
comisiones = int(comisiones)

print(f"Tu nombre es {nombre} y tus comisiones por ventas son {comisiones} €")

