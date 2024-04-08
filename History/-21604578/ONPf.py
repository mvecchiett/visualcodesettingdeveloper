# Diccionario de parámetros 
def imprimir_ticket (*args, **kwargs): 

    "Imprime el ticket de una compra"
    print("Detalle Ticket")

    for item, precio in kwargs.items(): 
        print(item, ":", precio)


d= dict(item = "culo")