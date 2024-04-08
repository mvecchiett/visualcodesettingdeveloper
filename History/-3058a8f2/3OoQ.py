from random import *
from re import *
bolcontinuar  = True
while bolcontinuar:
    print("Ha tirado los dados. Dado 1: ",randint(1,6), " Dado 2: ",randint(1,6))
    print("Tira de nuevo?")
    bolcontinuar = ("S" or "s" or "SI" or "si" or "Si") in input().lower()
