#coding: utf-8 -*.


def peso (masa, gravedad=9.8): 
    """Fórmula del peso
    el argumento gravedad es opcional, si no lo pones toma el valor por defecto
    """
    return masa * gravedad

# Parámetros opcionales

print("Peso en la tierra:", peso (10))  
print("Peso en la luna:", peso (10, 1.63))

# Parámetros con palabras claves (o argumentos nombrados) 
print("Peso en la luna: ", peso (10, gravedad=1.63)) 
print("Peso en la luna:", peso (masa=10, gravedad=1.63)) 
print("Peso en la luna:", peso (gravedad=1.63, masa=10))


# Esta opción no es valida. Los parámetros posicionales no pueden ir después de un keyword # 
# print("Peso en la luna:", peso (masa=10, 1.63))
# SyntaxError: positional argument follows keyword argument

# Lista de parámetros

def suma_numeros(*args):
    "Suma los números pasados por parámetro"
    return sum(args)

print("6 +7 +8=", suma_numeros(*[6,7,8]))

print("6 + 7 + 8=", suma_numeros (6,7,8))
