def es_primo(numero):
    """_
    ¿Cuantas veces se ejecuta el bloque de código que está dentro del ciclo for al llamar a la función es_primo(13)?

    """
    resultado = True

    for divisor in range(2, numero):
        print ("cuante")

        if (numero % divisor) == 0:

            resultado = False

            break

    return resultado 



print(es_primo(13))