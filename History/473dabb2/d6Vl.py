#coding: utf-8 -*.
"""
    Jugando con string
"""
print("Hola Mundo!")        # Con comillas dobles
print('Hola Mundo!')        # Con comillas simples
print("""Hola 
        Mundo!""")    # Con triple comillas dobles
print('''Hola 
        Mundo!''')    # Con triple comillas simples
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

a_string[5:9] # Devuelve Mundo
print(a_string[5:9])
# Longitud del string
print(len(a_string)) # Devuelve 11

"""
    Los strings son inmutables. Esto quiere decir que no se pueden modificar. Lo que
    sí se puede hacer es construir un nuevo string a partir de uno o más strings o hacer una
    copia del mismo. En caso de querer modificar un string se levantará una excepción del
    tipo TypeError. Veamos algunos ejemplos:
"""
"""
    a_string = ‘Hola Mundo!’
    a_string[6] = ‘o’ # Dará un error de tipo TypeError
    new_string = a_string + ‘?’ # Genera el string Hola Mundo!?
    new_string = a_string[:6] +’o’ + a_string[7:] # Genera el string Hola Mondo!
"""

"""
Strings con contenido dinámico
"""

"""
name = "Agustín"
"Hola %s" % name # Resultado: Hola Agustín
"El número es %d" % 5 # Resultado: El número es 5
"El número es %02d" % 5 # Resultado: El número es 005
"El decimal es %f" % 6.5 # Resultado: El número es 6.500000
"El decimal es %.2f" % 6.5 # Resultado: El número es 6.50
"Hola %(name)s" % {'name': name} # Resultado: Hola Agustín
"""


"""
    4
Entonces, ¿Cuando tendremos que codificar los strings?
Los strings habrá que codificarlos (pasar de unicode a un byte array con una
codificación determinada) o decodificarlos (pasar de un byte array con una codificación
determinada a unicode) en dos momentos. Cuando ingresa un string desde afuera
(desde un archivo, un web service, etc.), si el mismo no es unicode, habrá que
decodificarlo a unicode. Y cuando necesitemos extraer datos de nuestro sistema,
cuando los datos los necesitemos en cierta codificación, los tendremos que codificar con
dicha codificación. Veamos un ejemplo de cómo codificar y decodificar los strings.

a_string = ’Otoño’

# Codifico el string a utf-8
coding_string = a_string.encode('utf-8') # Respuesta: b'Oto\xc3\xb1o'

# Decodifico el byte array en utf-8
coding_string.decode('utf-8') # Respuesta: 'Otoño'

"""

