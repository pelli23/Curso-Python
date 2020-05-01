#Tipo Int
entero = 10
#La función type nos devuelve el tipo de dato
print(type(entero))

#Tipo Float
decimal = 10.5
print(type(decimal))

#Tipo Bool
boolean = True #False
print(type(boolean))

#Tipo String
texto = "Tipo String"
print(type(texto))

#Tipo None. Similar a null en otros lenguajes
tipo_none = None
print(type(tipo_none))

#Operaciones 

a = 10
b = 3
c = a + b
print(c)
c = a - b
print(c)
c = a * b
print(c)
c = a / b
print(c)
c = a ** b
print(c)
c+=1 # c = c + 1
print(c)
c-=1 # c = c - 1
print(c)
c*=10 # c = c * 10
print(c)
c/=10 # c = c / 10
print(c)

a = 10
b = 3
a,b = b,a #Permuta
print("a: ",a)
print("b: ",b)

#Cambio de tipo de dato

a = "10"
print(type(int(a)))
print(type(float(a)))
a = 10
print(type(str(a)))
a = "True"
print(type(bool(a)))