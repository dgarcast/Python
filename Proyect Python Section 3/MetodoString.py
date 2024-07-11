"""
Metodos String

- upper() - pasar a mayusculas
- lower() - pasar a minuscula
- split() - separalo en partes(lista)
- join() - unir items usando separador
- find() - encontrar un sub-strings
- replace() - reemplazar un substring

"""

texto = "Este es el texto de Federico"


resultado = texto.upper() #Aumenta todos los caracteres a mayusculas
resultado = texto[2].upper() #T
resultado = texto.lower() #Disminye todas los caracteres a minusculas
resultado = texto.split() #Separa los elementos y los convierte en una lista
                          #['Este', 'es', 'el', 'texto', 'de', 'Federico']
resultado = texto.split("t") #['Es', 'e es el ', 'ex', 'o de Federico']
resultado = texto.find("s") #1
#con find si no encuentra un caracter devuelve un -1, index devuelve un error
resultado = texto.replace("Federico","David") #Reemplaza federico por david

print(resultado)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e) #Une las letras a b c d y une las palabras

