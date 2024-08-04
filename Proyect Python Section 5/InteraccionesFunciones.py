from random import *

#LISTA INICIAL
palitos = ['-','--','---','----']



#MEZCLAR PALITOS
def mezclar(lista):
    shuffle(lista)
    return lista

#PEDIRLE INTENTO
def probar_suerte():
    intento = ''
    
    while intento not in ['1','2','3','4']:
        intento = input("Elije un numero del 1 al 4: ")
    
    return int(intento)

#COMPROBAR INTENTO

def chequear_intento(lista,intento):
    if lista[intento - 1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")
    
    print(f"Te ha tocado {lista[intento-1]}")
    
   
palitos_mezclado = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclado,seleccion)