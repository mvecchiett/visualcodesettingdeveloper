def es_primo(numero):
    """_
    ¿Cuantas veces se ejecuta el bloque de código que está dentro del ciclo for al llamar a la función es_primo(13)?

    """
    resultado = True
    n=0
    for divisor in range(2, numero):
        n=n+1
        if (numero % divisor) == 0:

            resultado = False

            break
    print (n)

    return resultado 



print(es_primo(13))




s = 0

for n in range(1, 10):

     if n % 7 == 0:

         break;

     s += n