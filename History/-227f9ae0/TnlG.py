
from tkinter import Tk
from tkinter import Label
from tkinter import StringVarmvcmodelolin
from tkinter import Button
from tkinter import W
from tkinter import E
from tkinter import Entry
from tkinter import ttk
import mvcmodelo

# ##############################################
# VISTA
# ##############################################
class panel ():
    def __init__(self,window):
        self.master=window
        self.master.title("Gestor de Usuarios")
        #titulo
        self.titulo = Label(
            self.master, text="ABM usuarios",
             bg="DarkOrchid3", fg="thistle1",height=1, width=60)
        self.titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)
        self.titulo.config(bg='green')

        self.objeto=mvcmodelo.Abmc()
        try:
           self.objeto.conexion()
           self.objeto.crear_tabla()
        except:   
           print("error")

        #label
        self.titulo_label = Label(self.master, text="Titulo:")
        self.titulo_label.grid(row=3, column=0, sticky=W)
        self.autor_label= Label(self.master, text="Autor:")Ges
        self.autor_label.grid(row=4, column=0, sticky=W)
        self.ubicacion_label= Label(self.master, text="Ubicacion:")
        self.ubicacion_label.grid(row=5, column=0, sticky=W)
        # Defino variables para tomar valores de campos de entrada
        self.var_titulo,self. var_autor,self.var_ubi = StringVar(),StringVar(),StringVar()

#entry
        self.titulo_entry = Entry(self.master,textvariable=self.var_titulo, width=25)
        self.titulo_entry.grid(row=3, column=1, padx=50)
        self.autor_entry = Entry(self.master,textvariable=self.var_autor, width=25)
        self.autor_entry.grid(row=4, column=1, padx=50)
        self.ubicacion_entry = Entry(self.master,textvariable=self.var_ubi, width=25)
        self.ubicacion_entry.grid(row=5, column=1, padx=50)


# --------------------------------------------------
# TREEVIEW
# --------------------------------------------------

        self.tree = ttk.Treeview(self.master)
        self.tree["columns"]=("col1", "col2", "col3")
        self.tree.column("#0", width=90, minwidth=50, anchor=W)
        self.tree.column("col1", width=200, minwidth=80)
        self.tree.column("col2", width=200, minwidth=80)
        self.tree.column("col3", width=200, minwidth=80)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Titulo")
        self.tree.heading("col2", text="Autor")
        self.tree.heading("col3", text="Ubicacion")
        self.tree.grid(row=10, column=0, columnspan=4)


        self.alta_g= Button(self.master, text="Guardar", command=lambda:self.objeto.alta (
        self.var_titulo.get(),self.var_autor.get(),self.var_ubi.get(),
        self.tree,self.titulo_entry, self.autor_entry,  self.ubicacion_entry))
        self.alta_g.grid(row=7, column=0,)
 
        self.boton_borrar=Button(self.master, text="Borrar", command=lambda:self.objeto.borrar (self.tree))
        self.boton_borrar.grid(row=7, column=1)

        self.boton_borrar=Button(self.master, 
        text="Actualizar/Mostar", 
        command=lambda:self.objeto.actualizar(
        self.var_titulo.get(),self.var_autor.get(),self.var_ubi.get(),self.tree,
        self.titulo_entry, self.autor_entry, self.ubicacion_entry))
        self.boton_borrar.grid(row=7, column=2)





