import array
cadena = 'Arrays Python'
array1 = array.array( cadena)
archivo = open('datos.txt', 'wb')
array1.tofile(archivo)
archivo.close

