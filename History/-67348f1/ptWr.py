### split function
### exactamente igual que en vb

import re
str = "The rain in Spain"
x = re.split("\s", str)
print(x)
### vamos a hacer una cosa oscura
b = re.split(" ", str)
print(b)