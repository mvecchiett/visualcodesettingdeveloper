####Ejemplo, imprime una Lista de todas las ocurrencias:
#### ejemplo findall
import re

str = "The rain in Spain"
x = re.findall("ai", str)
print(x)
#### y porque no contar la cantidad de elementos de la lista
print(len(x))


###Contraejemplo
str = "The rain in Spain"
x = re.findall("kk", str)
print(x)
#### y porque no contar la cantidad de elementos de la lista
print(len(x))

#### ejemplo search
str = "The rain in Spain"
x = re.search("Portugal", str)
print(x)
### esto no funciona.. osea, la longitud solo sirve si sabes a priori si tiene elementos : print(len(x))
print ( x is None) ### ojo no podes usar igual
if x is None:
    print("x es None")
### aca esta preguntando si x tiene el tipo none, con la funcion isinstance
print((x, isinstance(x, type(None)))) 