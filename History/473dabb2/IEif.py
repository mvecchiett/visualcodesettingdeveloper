#coding: utf-8 -*.

print("Hola Mundo!")        # Con comillas dobles
print('Hola Mundo!')        # Con comillas simples
print("""Hola Mundo!""")    # Con triple comillas dobles
print('''Hola Mundo!''')    # Con triple comillas simples
## porque imprime lo mismo? seguramente porque no estan escapeadas, y para que?


a_string = 'Hola Mundo!'
print(a_string)
# Acceso a caracteres del string.
a_string[0] # Devuleve H
print(a_string[0])
a_string[-1] # Devuelve !
print(a_string[-1])
# Slicing de un string
a_string[:4] # Devuelve Hola
print(a_string[:4])