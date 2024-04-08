from tkinter import StringVar, Tk
from tkinter import Label
from tkinter import StringVar
from tkinter import Button
from tkinter import W
from tkinter import E
from tkinter import Entry
from tkinter import ttk
import modelo

# ##############################################
# VISTA
# ##############################################
class panel ():
    def limitador(entry_text, longitud):
        if len(entry_text.get()) > 0:
           #donde esta el :longitud limitas la cantidad d caracteres
           entry_text.set(entry_text.get()[:longitud])

    def __init__(self,window):
        self.master=window
        self.master.title("Gestor de Usuarios")
        #titulo
        self.titulo = Label(
            self.master, text="ABM usuarios",
             bg="DarkOrchid3", fg="thistle1",height=1, width=60)
        self.titulo.grid(row=0, column=0, columnspan=6, padx=1, pady=1, sticky=W+E)
        self.titulo.config(bg='green')
        
        self.objeto=modelo.Abmc()
        try:
           self.objeto.conexion()
           self.objeto.crear_tabla()
        except:   
           print("error")

        #label

        self.nombre_label = Label(self.master, text="Nombre:")
        self.nombre_label.grid(row=3, column=0, sticky=W)

        self.apellido_label = Label(self.master, text="Apellido:")
        self.apellido_label.grid(row=4, column=0, sticky=W)

        self.sexo_label = Label(self.master, text="Sexo:")
        self.sexo_label.grid(row=5, column=0, sticky=W)

        self.email_label = Label(self.master, text="Email:")
        self.email_label.grid(row=6, column=0, sticky=W)

        self.username_label = Label(self.master, text="Username:")
        self.username_label.grid(row=7, column=0, sticky=W)

        self.password_label = Label(self.master, text="Password:")
        self.password_label.grid(row=8, column=0, sticky=W)

        # Defino variables para tomar valores de campos de entrada
        self.var_nombre   = StringVar()
        self.var_apellido = StringVar()     
        self.var_sexo     = StringVar()
        self.var_email    = StringVar()     
        self.var_username = StringVar()
        self.var_password = StringVar()     
 

        #entry

        self.nombre_entry = Entry(self.master,textvariable=self.var_nombre, width=25)
        self.nombre_entry.grid(row=3, column=1, padx=50)


        self.apellido_entry = Entry(self.master,textvariable=self.var_apellido, width=25)
        self.apellido_entry.grid(row=4, column=1, padx=50)
        
        self.sexo_entry = Entry(self.master,textvariable=self.var_sexo, width=10)
        self.sexo_entry.grid(row=5, column=1, padx=50)

        self.email_entry = Entry(self.master,textvariable=self.var_email, width=25)
        self.email_entry.grid(row=6, column=1, padx=50)
        
        self.username_entry = Entry(self.master,textvariable=self.var_username, width=15)
        self.username_entry.grid(row=7, column=1, padx=50)

        self.password_entry = Entry(self.master,textvariable=self.var_password, width=10)
        self.password_entry.grid(row=8, column=1, padx=50)

# --------------------------------------------------
# TREEVIEW
# --------------------------------------------------

        self.tree = ttk.Treeview(self.master)
        self.tree["columns"]=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8")
        self.tree.column("#0", width=90, minwidth=50, anchor=W)
        self.tree.column("col1", width=200, minwidth=80)
        self.tree.column("col2", width=200, minwidth=80)
        self.tree.column("col3", width=80 , minwidth=80)
        self.tree.column("col4", width=200, minwidth=80)
        self.tree.column("col5", width=100, minwidth=80)
        self.tree.column("col6", width=100, minwidth=80)
 
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Nombre")
        self.tree.heading("col2", text="Apellido")
        self.tree.heading("col3", text="Sexo")
        self.tree.heading("col4", text="Email")
        self.tree.heading("col5", text="Username")
        self.tree.heading("col6", text="Password")


        self.tree.grid(row=10, column=0, columnspan=6)


        self.alta_g= Button(self.master, text="Guardar", command=lambda:self.objeto.alta ( 
        self.var_nombre.get(), self.var_apellido.get(), self.var_sexo.get(), self.var_email.get(), self.var_username.get(),self.var_password.get(), self.tree,
        self.nombre_entry, self.apellido_entry, self.sexo_entry,self.email_entry,self.username_entry,self.password_entry ))
  
        self.alta_g.grid(row=4, column=4)
 
        self.boton_borrar=Button(self.master, text="Borrar", command=lambda:self.objeto.borrar (self.tree))
        self.boton_borrar.grid(row=5, column=4)

        self.boton_borrar=Button(self.master, 
        text="Actualizar/Mostar", 
        command=lambda:self.objeto.actualizar(
        self.var_nombre.get(), self.var_apellido.get(), self.var_sexo.get(), self.var_email.get(), self.var_username.get(),self.var_password.get(), self.tree,
        self.nombre_entry, self.apellido_entry, self.sexo_entry,self.email_entry,self.username_entry,self.password_entry))
        self.boton_borrar.grid(row=6, column=4)





