####Ejemplo, imprime una Lista de todas las ocurrencias:
#### ejemplo findall
import re

str = "The rain in Spain"
x = re.findall("ai", str)
print(x)
print(x.len())