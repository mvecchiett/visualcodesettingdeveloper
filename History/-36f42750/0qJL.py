import array

array1 = array.append("Dato1")
array1 = array.append("Dato2")
array1 = array.append("Dato3")
array1 = array.append("Dato4")
archivo = open('datos.txt', 'wb')
array1.tofile(archivo)
archivo.close

