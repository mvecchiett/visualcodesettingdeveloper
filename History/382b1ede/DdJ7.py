from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        for i in range(times):
            yield 'Hello, %s' % name

if __name__ == '__main__':
    # Crear una aplicación SOAP
    soap_app = Application([HelloWorldService],
                           tns='spyne.examples.hello.soap',
                           in_protocol=Soap11(validator='lxml'),
                           out_protocol=Soap11())

    # Montar la aplicación en un servidor WSGI
    wsgi_app = WsgiApplication(soap_app)

    # Crear un servidor HTTP para manejar la aplicación
    server = make_server('0.0.0.0', 8000, wsgi_app)

    print("Servidor SOAP iniciado en http://0.0.0.0:8000/")
    
    # Iniciar el servidor
    server.serve_forever()
