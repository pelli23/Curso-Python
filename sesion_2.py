#Las comparanciones que tendremos son
"""
Mayor qué >
Menor qué <
Igual que ==
Mayor o igual que >=
Menor o igual que <=
Distinto de !=

igualmente podemos negar con "not" 
"""
#Un bloque If siempr recibirá una expresión booleana. debemos conocer los operadores logicos Or y And =>
#Assert indica que eso será siempre verdad
assert True == (True or True)
assert True == (True or False)
assert False == (False or False)
assert True == (True and True)
assert False == (True and False)
assert False == (False and False)

edad = 108
"""
Se ejecutara el codigo dentro del bloque if siempre que la variable edad sea mayor o igual que 18
Se usa un tab (o 4 espacios) para indicar la parte de codigo que queda dentro del bloque If
"""
if edad >= 18:
    puede_votar = True

adulto = True
responsable = True
#un If puede contener tantos Or ó And como se necesiten
if edad>=18 or (adulto and responsable):
    puede_votar = True

#Si queremos poner un bloque de codigo para en caso de que no se cumpla la condición del If
#Usaremos el bloque else
puede_votar = None
if edad>=18:
    puede_votar = True
else:
    puede_votar = False

esta_jubilado = None

#Si queremos comprobar varias condiciones para varios casos podemos usar elif
if edad<18:
    puede_votar = False
    esta_jubilado = False
elif edad>=18 and edad <65:
    puede_votar = True
    esta_jubilado = False
else:
    puede_votar = True
    esta_jubilado = True


#ejemplo negado
responsable = False
if not responsable:
    print("no es responsable")

#En caso de que queramos inicializar una variable con el valor que dependa de un if
#Podemos usar el operador ternario, para no tener que inicializar a None

puede_votar = True if edad>=18 else False

