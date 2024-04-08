def leer():
    with open("datos.txt", "r") as tf:
        lineas = tf.read().split(',')
    return lineas

mensajes = leer()
print(mensajes(0))

