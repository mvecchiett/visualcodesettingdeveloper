# Asignar con frombytes() una cadena de bytes a 'array1' 
array1 = array.array('b')
cadena = b'Arrays Python'
array1.frombytes(cadena)
array1  #  array('b', [65, 114, 114, 97, 121, 115, 32, 80, 121,
        #              116, 104, 111, 110])

# Escribir el contenido de 'array1' a un archivo
cadena = b'Arrays Python'
array1 = array.array('b', cadena)
archivo = open('datos.txt', 'wb')
array1.tofile(archivo)
archivo.close

# Leer y añadir a 'array1' los 6 primeros bytes del archivo anterior
array1 = array.array('b')
archivo = open('datos.txt', 'rb')
array1.fromfile(archivo, 6)
array1  # array('b', [65, 114, 114, 97, 121, 115])

# Convertir a bytes los valores leídos con anterioridad
cadena = array1.tobytes()
cadena  # b'Arrays'

# Convertir bytes a cadena de texto
cadena = cadena.decode()
cadena  # 'Arrays'

# Intentar añadir elementos de una lista a un array que
# contiene elementos. Cuando se produce un error de tipo
# el array mantiene sus datos originales.
lista1 = [0, 1, 3.31, 3.5, 1.9, 0, False]
array1 = array.array('b', [9, 10, 11])
try:
    array1.fromlist(lista1)
except:
    print('Error al intentar agregar lista1')
finally:
    print(array1)