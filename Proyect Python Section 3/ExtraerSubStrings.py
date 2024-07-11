"""
Extraer porciones de texto. Fragmentar

mi_variable = "Esta palabra sera extraida"
mi_variable[5:12] - palabra
mi variable[5:12:2] - plbr

"""

texto = "ABCDEFGHIJLMNOPQRSTUVWXYZ"
fragmento = texto[2] #C 
fragmento = texto[2:5] 
#Quiero que extraigas los caracteres desde el indice 2 hasta ,pero no incluyendo, el indice 5
fragmento = texto[2:] #CDEFGHIJLMNOPQRSTUVWXYZ
fragmento = texto[:2] #AB
fragmento = texto[2:10:2] #CEGI Va saltando de dos en dos entre el caracter 2 y el 10 (pero no cogiendo el caracter 10)
fragmento = texto[::-1] #ZYXWVUTSRQPONMLJIHGFEDCBA lo fragmenta pero al reves
print(fragmento)
