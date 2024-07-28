"""  
Operadores Logicos

y = and
o = or
no = not
"""

mi_bool = 4 < 5 < 6
print(mi_bool)

mi_bool = 4 < 5 and 5 > 6
print(mi_bool) #Falso porque no se cumple las dos condiciones

mi_bool = 4 < 5 and 5 == 2+3
print(mi_bool) #True

mi_bool = (55 == 55) and ('perro' == 'perro')
print(mi_bool)

mi_bool = 1 == 10 or 3 == 3
print(mi_bool)

texto = "Esta frase es breve"
mi_bool = ('frase' in texto) or ('breve' in texto)
print(mi_bool)

mi_bool = not 'a' == 'a'
print(mi_bool) #False porque devuelve el contrario por el not

mi_bool = not 'a' != 'a'
print(mi_bool) #True porque devuelve el contrario por el not


