####Ejemplo, imprime una Lista de todas las ocurrencias:

import re

str = "The rain in Spain"
x = re.findall("ai", str)
print(x)
print(x.__len__)