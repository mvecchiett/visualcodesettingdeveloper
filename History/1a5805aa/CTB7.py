#coding: utf-8 ...
def maximo_2(a, b):
    "Devuelve el máximo entre a y b"

    maximo = a if b > a: maximo = b

    return maximo

def maximo_3 (a, b, c):
    "Devuelve el máximo entre a, by c" 
    return maximo_2(a, maximo_2(b, c))

print(maximo_2(2, 5))

print(maximo_3(6, 1, 5))

