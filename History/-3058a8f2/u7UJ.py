from random import *
bolcontinuar  = True
opcionesverdaderas = list1= ["S", "s", "SI" ,"si" ,"Si"]
while bolcontinuar:
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    print("Ha tirado los dados. Dado 1: ",dado1, " Dado 2: ",dado2)
    print("La suma de los dados es : ",dado1 + dado2)
    print("Tira de nuevo?")
    ingreso= (str(input().lower()))
    print(ingreso in opcionesverdaderas)
    bolcontinuar=("S" or "s" or "SI" or "si" or "Si") in ingreso

    #bolcontinuar = ("S" or "s" or "SI" or "si" or "Si") in input().lower()
