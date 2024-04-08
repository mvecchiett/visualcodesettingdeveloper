"""
MV Marzo 2022
Ejercicio 6
A partir del ejercicio 5 cree un programa que vaya agregando en una lista las compras realizadas.
"""
valor = input("Para iniciar ingrese 'i', para finalizar ingrese 'f': ")
compra = []
total = 0

while valor == 'i':
    producto, cantidad, precio = input("Ingrese el nombre la cantidad de producto en kg y el precio separado por espacio: ").split()
    total = total + int(cantidad)*int(precio)
    compra.append([producto, cantidad, precio])
    valor = input("Para agregar otro producto ingrese 'i', para finalizar ingrese cualquier otro caracter: ")

print(compra)
for x in compra:
    print("Producto : ", x[0], " cantidad ", x[1], " precio: ", x[2])
    
print("El costo total es de: ", total)
    
 
