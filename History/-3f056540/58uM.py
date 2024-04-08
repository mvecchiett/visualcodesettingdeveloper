from zeep import Client

# URL del servicio SOAP
url = 'http://localhost:8000/?wsdl'

# Crear un cliente SOAP
client = Client(url)

# Llamar al método say_hello del servicio
name = input("Ingrese su nombre: ")
times = int(input("Ingrese el número de veces que desea saludar: "))

result = client.service.say_hello(name, times)

# Imprimir los resultados
for message in result:
    print(message)
