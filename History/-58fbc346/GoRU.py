"""
MV Marzo 2022
Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si
son múltiplos de dos. Utilice la estructura if/else
"""
import sys

n1 = int(sys.argv[1]) % 2
n2 = int(sys.argv[2]) % 2
n3 = int(sys.argv[3]) % 2
if n1 == 0:
    print("El primer valor ingresado es par")
else:
    print("El primer valor ingresado es impar")
if n2 == 0:
    print("El primer valor ingresado es par")
else:
    print("El primer valor ingresado es impar")
if n3 == 0:
    print("El primer valor ingresado es par")
else:
    print("El primer valor ingresado es impar")
