"""
MV Marzo 2022
Ejercicio 7
A partir del ejercicio 5 cree un programa que vaya agregando
en un diccionario las compras realizadas.
"""

valor = input("Para iniciar ingrese 'i', para finalizar ingrese 'f': ")
compra = {}
total = 0
el_id = 0
while valor == 'i':
    producto, cantidad, precio = input("Ingrese el nombre la cantidad de producto en kg y el precio separado por espacio: ").split()
    total = total + int(cantidad)*int(precio)
    el_id = el_id + 1
    compra[str(el_id)] = (producto, cantidad, precio)
     
    valor = input("Para agregar otro producto ingrese 'i', para finalizar ingrese cualquier otro caracter: ")

print(compra)
for x, y in compra.items():
    print("Producto : ", y[0], " cantidad ", y[1], " precio: ", y[2])

print("El costo total es de: ", total)
