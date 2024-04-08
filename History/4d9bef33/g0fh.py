from tkinter import StringVar
from tkinter import IntVar
from tkinter import Frame
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import Radiobutton
from modelo import Abmc
from tkinter import ttk
#from tktemas import temas


class Ventanita:
    def __init__(self, window):
        self.root = window
        
        self.vnombre = StringVar()
        self.vapellido = StringVar()
        self.vemail = StringVar()
        self.vusername = StringVar()
        self.vpassword = StringVar()

        self.a = IntVar()
        self.opcion = StringVar()
        self.f = Frame(self.root)
        self.tree = ttk.Treeview(self.f)
        self.objeto_base = Abmc()
        # Frame
        self.root.title("Gestor de Usuarios")
        self.f.config(width=2020, height=2020)
        self.f.grid(row=20, column=0, columnspan=4)

        # Etiquetas
        self.superior = Label(
            self.root, text="Complete sus datos", bg="green", fg="white", width=40
        )
        self.nombre = Label(self.root, text="Nombre")
        self.apellido = Label(self.root, text="Apellido")
        self.email = Label(self.root, text="email")
        self.username = Label(self.root, text="Username")
        self.password = Label(self.root, text="Password")

        self.registros = Label(
            self.root, text="Lista de usuarios existentes (solo si la lista aparece con datos)", bg="grey", width=40)
        
        #self.temas = Label(
        #    self.root,
        #    text="Temas",
        #    bg="black",
        #    fg="red",
        #    height=1,
        #    width=40,
        #)

        self.superior.grid(
            row=0, column=0, columnspan=4, padx=1, pady=1, sticky="w" + "e"
        )
        
        self.nombre.grid(row=1, column=0, sticky="w")
        self.apellido.grid(row=2, column=0, sticky="w")
        self.email.grid(row=3, column=0, sticky="w")
        self.username.grid(row=4, column=0, sticky="w")
        self.password.grid(row=5, column=0, sticky="w")

        self.registros.grid(
            row=7, column=0, columnspan=4, padx=1, pady=1, sticky="w" + "e"
        )
        #self.temas.grid(
        #    column=0, row=20, columnspan=4, padx=1, pady=1, sticky="w" + "e"
        #)

        # Entradas
        self.Ent1 = Entry(self.root, textvariable=self.vnombre)
        self.Ent1.grid(row=1, column=1)
        self.Ent2 = Entry(self.root, textvariable=self.vapellido)
        self.Ent2.grid(row=2, column=1)
        self.Ent3 = Entry(self.root, textvariable=self.vemail)
        self.Ent3.grid(row=3, column=1)
        self.Ent4 = Entry(self.root, textvariable=self.vusername)
        self.Ent4.grid(row=4, column=1)                        
        self.Ent5 = Entry(self.root, textvariable=self.vpassword)
        self.Ent5.grid(row=5, column=1)   
        # Frame Unidad 4
        #self.frame_rojoizq = Frame(self.root, width="200", height="80", bg="red")
        #self.frame_negro = Frame(self.root, width="80", height="80", bg="black")
        #self.frame_rojoder = Frame(self.root, width="200", height="80", bg="red")

        #self.frame_rojoizq.grid(column=0, row=21)
        #self.frame_negro.grid(column=1, row=21)
        #self.frame_rojoder.grid(column=2, row=21)

        # Botones
        self.boton_alta = Button(self.root, text="Alta", command=lambda: self.alta())
        self.boton_alta.grid(row=8, column=0)

        self.boton_editar = Button(
            self.root, text="Actualizar", command=lambda: self.modificar()
        )
        self.boton_editar.grid(row=8, column=1)

        self.boton_borrar = Button(
            self.root, text="Borrar", command=lambda: self.borrar()
        )
        self.boton_borrar.grid(row=8, column=2)
        
        """
        self.boton_tema1 = Radiobutton(
            self.frame_negro,
            text="Tema 1",
            variable=self.opcion,
            value="01",
            fg="red",
            bg="black",
            command=lambda: temas.tema1(self, self.root),
        )
        self.boton_tema1.grid(column=2, row=21)

        self.boton_tema2 = Radiobutton(
            self.frame_negro,
            text="Tema 2",
            variable=self.opcion,
            value="02",
            fg="red",
            bg="black",
            command=lambda: temas.tema2(self, self.root),
        )
        self.boton_tema2.grid(column=2, row=22)

        self.boton_tema3 = Radiobutton(
            self.frame_negro,
            text="Tema 3",
            variable=self.opcion,
            value="03",
            fg="red",
            bg="black",
            command=lambda: temas.tema3(self, self.root),
        )
        self.boton_tema3.grid(column=2, row=23)
        """

        # Tree
        self.tree["columns"] = ("col1", "col2", "col3", "col4", "col5")
        self.tree.column("#0", width=90, minwidth=50, anchor="w")
        self.tree.column("col1", width=200, minwidth=80)
        self.tree.column("col2", width=200, minwidth=80)
        self.tree.column("col3", width=200, minwidth=80)
        self.tree.column("col4", width=200, minwidth=80)
        self.tree.column("col5", width=200, minwidth=80)


        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Nombre")
        self.tree.heading("col2", text="Apellido")
        self.tree.heading("col3", text="Email")
        self.tree.heading("col4", text="Username")
        self.tree.heading("col5", text="Password")
        self.tree.grid(row=15, column=0, columnspan=6)

    def alta(
        self,
    ):
        self.objeto_base.alta(self.vnombre, self.vapellido, self.vemail, self.vusername, self.vpassword, self.tree)

    def borrar(
        self,
    ):
        self.objeto_base.baja(self.tree)

    def modificar(
        self,
    ):
        self.objeto_base.modificar(self.vnombre, self.vapellido, self.vemail, self.vusername, self.vpassword, self.tree)
    
    def actualizar(
        self,
    ):
        self.objeto_base.actualizar_treeview(self.tree)

    def OnSelected(event):
        print("seleccione")
        """"
        curItem = self.tree.focus()
        contents =(self.tree.item(curItem))
        selecteditem = contents['values']
        memusuario_id = selecteditem[0]
        btn_alta.config(state=DISABLED)
        btn_consulta.config(state=DISABLED)
        btn_guardar.config(state=NORMAL)
        btn_borrar.config(state=DISABLED)
        """