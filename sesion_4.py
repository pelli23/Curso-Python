#Definimos el dictado de forma literal
empresa = {"Nombre":"Andres Holdings Inc","Incorporated":"Delaware","Face_value": 0.10,"os":10000}

#Tambien podemos definirlo mediante funcion dict y pasar como panametros con nombre -a modo de key- cada valor
empresa_2 = dict(Nombre="Andres Holdings Inc",Incorporated="Delaware",Face_value=0.10,os=10000)

assert empresa == empresa_2

hijas = [{"Nombre":"Andres (Cayman) Ltd","Incorporated":"Cayman Islands","Face_value": 0.005,"os":1440000}]

#Podemos acceder a los valores pasando la clave entre corchetes, podemos añadir nuevas keys
empresa["hijas"] = hijas



lista = [["nombre","Apple Inc"],["incorporated","Delaware"]]

#Podemos crear un dictado a partir de una lista de listas
empresa_dict = dict(lista)


claves = ["Nombre","Incorporated"]

valores = ["Facebook Inc","Delaware"]

lista_2 = [[claves[0],valores[0]],[claves[1],valores[1]]]
#Tambien podemos crear un dictado si tenemos una lista de claves y otra de valores usando zip
empresa_dict =dict(zip(claves,valores))

#Podemos eliminar una clave usando la sentencia del
del empresa_dict["Incorporated"]
print(empresa_dict)

#Obtener claves como lista o tupla
claves = list(empresa.keys()) #  tuple(empresa.keys()) 


#Obtener valores como lista
valores = list(empresa.values())

#Obtener items como lista, veremos su utilidad cuando veamos bucles
items = list(empresa.items())
