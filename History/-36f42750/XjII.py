def leer():
    with open("datos.txt", "r") as tf:
        lineas = tf.read().split(',')
    return lineas

mensajes = leer()
for line in mensajes:
    print(line)
print(mensajes[0]])

