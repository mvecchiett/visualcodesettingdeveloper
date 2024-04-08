import array
cadena = 'Arrays Python'
array1 = array.array('b', cadena)
archivo = open('datos.txt', 'wb')
array1.tofile(archivo)
archivo.close

