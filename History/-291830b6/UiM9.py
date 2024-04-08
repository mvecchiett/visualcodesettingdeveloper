import vista
from tkinter import Tk

class Controller:

    def __init__(self,master_w):
       self.master=master_w
       self.objeto_mvcvista=vista.panel(self.master)


if __name__=="__main__":
    master = Tk()
    gestorusuarios_app=Controller(master)
    # como se muestra no entendi aca, quien llama a quien
    #gestorusuarios_app.objeto_mvcvista.ac
    master.mainloop()