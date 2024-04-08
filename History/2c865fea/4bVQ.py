# Consulta en este ejemplo, como sabe la clase chinos, mapear  el metodo comer_arroz de persona
# porque no se puede debuquear este programa? 

class Personas:
    def comer_arroz(self,):
        self.accion()

class Chinos(Personas):
    def accion(self,):
        print("los chinos comen arroz con palillos")


x=Chinos()
x.comer_arroz()