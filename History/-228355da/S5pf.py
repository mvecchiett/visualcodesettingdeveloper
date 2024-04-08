#coding: utf-8 -*.

class Reversa:
    """
    Iterador para recorrer una secuencia de atrás para adelante.
    """
def __init__(self, datos):
    self.datos = datos
    self.indice = len(datos)

def __iter__(self):
    return self

def __next__(self):
    if self.indice == 0:
        raise StopIteration()
    self.indice = self.indice - 1
    return self.datos[self.indice]


for elemento in Reversa([1,2,3,4]):
    print(elemento)

    