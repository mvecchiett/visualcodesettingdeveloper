# Importar módulo array
import array

# Declarar lista con valores numéricos
lista1 = [1, 0, 1, 0, 1, 1, 0, 0]

# Obtener cadena con todos los tipos de arrays disponbiles
array.typecodes  # 'bBuhHiIlLqQfd'

# Declarar 'array1' de tipo 'char sin signo' con datos de 'lista1'
array1 = array.array('B', lista1)

# Declarar 'array2' de tipo 'float' con datos de 'lista1'
array2 = array.array('f', lista1)

# Declarar 'array3' de tipo 'int sin signo' con datos de 
# 'lista1' en orden inverso 
array3 = array.array('I', (elemento for elemento in lista1[::-1]))

# Declarar 'array4' de tipo 'char con signo' a partir cadena de bytes
cadena = b'Python'
array4 = array.array('b', cadena)

# Declarar 'array5' de tipo 'int con signo' con valores del 0 al 9
array5 = array.array('i', range(10))

# Obtener tipo de array y datos de 'array1'
array1  # array('B', [1, 0, 1, 0, 1, 1, 0, 0])

# Obtener tipo de array y datos de 'array2'
array2  # array('f', [1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0])

# Obtener tipo de array y datos de 'array3'
array3  # array('I', [0, 0, 1, 1, 0, 1, 0, 1])

# Obtener tipo de array y datos de 'array4'
array4  # array('b', [80, 121, 116, 104, 111, 110])

# Obtener tipo de array y datos de 'array4'
array5  # array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Obtener tipo de objeto de 'array1'
type(array1)  # array.array

# Obtener tipo de array de 'array1', 'array2' y 'array2'
array1.typecode  # 'B'
array2.typecode  # 'f'
array3.typecode  # 'I'

# Obtener tamaño (en bytes) que ocupa un elemento en los arrays
array1.itemsize  # 1
array2.itemsize  # 4
array3.itemsize  # 4