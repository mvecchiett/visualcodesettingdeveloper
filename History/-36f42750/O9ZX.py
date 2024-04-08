with open("datos.txt", "r") as tf:
    lines = tf.read().split(',')
    
for line in lines:
    print(line)

