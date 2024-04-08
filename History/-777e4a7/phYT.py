# Importamos tkinter
from tkinter  import *
from tkinter  import messagebox
from tkinter  import ttk
# Importamos motor DB
import sqlite3

from cProfile import label
from cgitb    import text   
from optparse import Values



# Desarrollo interfaz gráfica
main = Tk()
main.title("Ojala funcione de una")
main.geometry("800x600")


def crear_base():
    conexion = sqlite3.connect("bd1.db")
    return conexion


def crear_tabla():
    conexion = crear_base()
    micursor = conexion.cursor()
    sqltabla = """CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY AUTOINCREMENT,
            cuilcuit TEXT NOT NULL,
            razonsocial TEXT NOT NULL,
            direccion TEXT NOT NULL,
            telefono TEXT NOT NULL,
            mail TEXT NOT NULL)"""
    micursor.execute(sqltabla)
    conexion.commit()


# crear_base()


'''
def conexion_base_datos():
    mi_conexion = sqlite3.connect("base_datos.db")
    mi_cursor = mi_conexion.cursor()

    try:
        mi_cursor.execute(
            """
            CREATE TABLE cliente_tabla (
                
                CUIL_CUIT VARCHAR(50),
                RAZON_SOCIAL VARCHAR(50),
                DIRECCION VARCHAR(50),
                TELEFONO VARCHAR(50),
                MAIL VARCHAR(50)
            )     
        
        """
        )
        messagebox.showinfo("CONEXION", "Base de Datos Creada con Exito")
    except:
        messagebox.showinfo("CONEXION", "Conexión exitosa con la BD")
'''

'''
def eliminar_base_datos():
    mi_conexion = sqlite3.connect("base_datos.db")
    mi_cursor = mi_conexion.cursor()
    if messagebox.askyesno(
        message="Cuidado!!, Realmente desea eliminar la BD?", title="ADVERTENCIA"
    ):
        mi_cursor.execute("DROP TABLE cliente_tabla")
    else:
        pass


def salir_aplicacion():
    valor_dialogo = messagebox.askquestion("Salir," "Desea Salir?")
    if valor_dialogo == "yes":
        main.destroy()


def limpiar_campos():
    # id_cliente.set("")
    cuil_cuit.set("")
    razon_social.set("")
    direccion.set("")
    telefono.set("")
    mail.set("")


def mensaje_aplicacion():
    acerca = """
    Aplicación CRUD
    Versión 1.0
    Tecnología Py Tk    
    """
'''

#################### Métodos CRUD ####################


def alta(cuilcuit, razonsocial, direccion, telefono, mail):
    conexion = crear_base()
    micursor = conexion.cursor()
    data = (cuilcuit, razonsocial, direccion, telefono, mail)
    sqlinsertar = "INSERT INTO clientes(cuilcuit, razonsocial, direccion, telefono, mail) VALUES(?, ?, ?, ?, ?)"
    micursor.execute(sqlinsertar, data)
    conexion.commit()
    conexion.close()
    print("alta")


conexion = crear_base()
crear_tabla

"""
def crear():
    mi_conexion = sqlite3.connect("base_datos.db")
    mi_cursor = mi_conexion.cursor()
    try:

        cc_cli = cuil_cuit.get()
        rs_cli = razon_social.get()
        d_cli = direccion.get()
        t_cli = telefono.get()
        m_cli = mail.get()

        mi_cursor.execute(
            "INSERT INTO cliente_tabla VALUES ( ?, ?, ?, ?, ?)",
            (
                cc_cli,
                rs_cli,
                d_cli,
                t_cli,
                m_cli,
            ),
        )
        print("entra")
        mi_conexion.commit()
    except:
        messagebox.showwarning("OJO", "ACÁ ESTÁ EL ERROR")
        pass
    limpiar_campos()
    mostrar()

"""

"""
def mostrar():
    mi_conexion = sqlite3.connect("base_datos.db")
    mi_cursor = mi_conexion.cursor()
    registros_clientes = tree.get_children()
    for elemento in registros_clientes:
        tree.delete(elemento)

    try:
        mi_cursor.execute("SELECT * FROM cliente_tabla")
        for row in mi_cursor:
            tree.insert(
                "", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5])
            )
    except:
        pass

"""
#################### Tabla CRUD ####################
"""
tree = ttk.Treeview(
    height=10,
    columns=(
        "#0",
        "#1",
        "#2",
        "#3",
        "#4",
        "#5",
    ),
)
tree.place(x=0, y=180)
tree.column("#0", width=40)
tree.heading("#0", text="ID", anchor=CENTER)
tree.column("#1", width=150)
tree.heading("#1", text="CUIL-CUIT", anchor=CENTER)
tree.column("#2", width=150)
tree.heading("#2", text="RAZÓN SOCIAL", anchor=CENTER)
tree.column("#3", width=150)
tree.heading("#3", text="DIRECCIÓN", anchor=CENTER)
tree.column("#4", width=150)
tree.heading("#4", text="TELÉFONO", anchor=CENTER)
tree.column("#5", width=150)
tree.heading("#5", text="MAIL", anchor=CENTER)

"""
"""
def seleccionar_click(event):
    item = tree.identify("item", event.x, event.y)
    id_cliente.set(tree.item(item, "text"))
    cuil_cuit.set(tree.item(item, "values")[0])
    razon_social.set(tree.item(item, "values")[1])
    direccion.set(tree.item(item, "values")[2])
    telefono.set(tree.item(item, "values")[3])
    mail.set(tree.item(item, "values")[4])


tree.bind("<Double-1>", seleccionar_click)
"""
"""
def modificar():

    mi_conexion = sqlite3.connect("base_datos.db")
    mi_cursor = mi_conexion.cursor()
    data = razon_social, direccion, telefono, mail

    try:

        sql = (
            "UPDATE cliente_tabla SET RAZON_SOCIAL=?, DIRECCION=?, TELEFONO=?, MAIL=?"
            + "WHERE CUIL_CUIT="
            + cuil_cuit.get(),
            (data),
        )

        mi_cursor.execute(sql, data)

        mi_conexion.commit()

    except:
        messagebox.showwarning("OJO", "Error al modificar registro")

    limpiar_campos()
    mostrar()
"""
"""
def borrar():
    mi_conexion = sqlite3.connect("base_datos.db")
    mi_cursor = mi_conexion.cursor()
    try:
        if messagebox.askyesno(
            message="Está a punto de eliminar un registro", title="ADVERTENCIA"
        ):
            mi_cursor.execute("DELETE FROM cliente_tabla WHERE ID=" + id_cliente.get())
    except:
        messagebox.showwarning(
            "ADVERTENCIA", "Ocurrió un error al tratar de eliminar un registro"
        )
        pass
    limpiar_campos()
    mostrar()

"""
#################### widgets ####################

############## Menús ##############
"""
menu_bar = Menu(main)
menu_base_datos = Menu(menu_bar, tearoff=0)
menu_base_datos.add_command(label="Crear/Conectar Base de Datos", command=conexion)
menu_base_datos.add_command(label="Eliminar Base de Datos", command=eliminar_base_datos)
menu_base_datos.add_command(label="Salir", command=salir_aplicacion)
menu_bar.add_cascade(label="Inicio", menu=menu_base_datos)

menu_ayuda = Menu(menu_bar, tearoff=0)
menu_ayuda.add_command(label="Limpiar Campos", command=limpiar_campos)
menu_ayuda.add_command(label="Acerca", command=mensaje_aplicacion)
menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)

main.config(menu=menu_bar)
"""
############## Etiquetas y Entris ##############

# e1 = Entry(main, textvariable=id_cliente)


idcli = IntVar()
cccli = StringVar()
rzcli = StringVar()
dircli = StringVar()
telcli = StringVar()
mailcli = StringVar()

l1 = Label(main, text="Id Cliente")
l1.place(x=500, y=10)
l1 = IntVar()

l2 = Label(main, text="Cuil-Cuit")
l2.place(x=50, y=10)
e2 = Entry(main, textvariable=cccli, width=50)
e2.place(x=150, y=10)

l3 = Label(main, text="Razón Social")
l3.place(x=50, y=30)
e3 = Entry(main, textvariable=rzcli, width=50)
e3.place(x=150, y=30)

l4 = Label(main, text="Dirección")
l4.place(x=50, y=50)
e4 = Entry(main, textvariable=dircli, width=50)
e4.place(x=150, y=50)

l5 = Label(main, text="Teléfono")
l5.place(x=50, y=70)
e5 = Entry(main, textvariable=telcli, width=50)
e5.place(x=150, y=70)

l6 = Label(main, text="e-mail")
l6.place(x=50, y=90)
e6 = Entry(main, textvariable=mailcli, width=50)
e6.place(x=150, y=90)

############## Botones ##############


boton_alta = Button(
    main,
    text="Crear Registro",
    command=lambda: alta(
        # cccli.get, rzcli.get(), dircli.get(), telcli.get(), mailcli.get()
        # idcliente(),
        cccli.get(),
        rzcli.get(),
        dircli.get(),
        telcli.get(),
        mailcli.get(),
    ),
)
boton_alta.place(x=50, y=130)
# btn_modificar = Button(main, text="Modificar Registro", command=modificar)
# btn_modificar.place(x=150, y=130)
# btn_mostrar = Button(main, text="Mostrar Lista", command=mostrar)
# btn_mostrar.place(x=275, y=130)
# btn_borrar = Button(main, text="Eliminar Registro", command=borrar)
# btn_borrar.place(x=370, y=130)


main.mainloop()
