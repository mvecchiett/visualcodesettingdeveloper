#coding: utf-8 -*.
from random import *
"""
Cada vez que ejecutamos el programa, éste elegirá dos números 
aleatorios entre el 1 y el 6. El programa deberá imprimirlos en 
pantalla, imprimir su suma y preguntarle al usuario si quiere 
tirar los dados otra vez.
"""
bolcontinuar  = True
opcionesverdaderas = list1= ["S", "s", "SI" ,"si" ,"Si"]
while bolcontinuar:
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    print("Ha tirado los dados. Dado 1: ",dado1, " Dado 2: ",dado2)
    print("La suma de los dados es : ",dado1 + dado2)
    print("Tira de nuevo?")
    ingreso= (str(input().lower()))
    bolcontinuar=ingreso in opcionesverdaderas

    