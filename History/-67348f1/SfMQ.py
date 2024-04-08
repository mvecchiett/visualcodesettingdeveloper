### split function
### exactamente igual que en vb

import re
str = "The rain in Spain"
x = re.split("\s", str)
print(x)
### vamos a hacer una cosa oscura /funciona igual cual es la maldita diferencia... 
b = re.split(" ", str)
print(b)

print(' '.join(b))