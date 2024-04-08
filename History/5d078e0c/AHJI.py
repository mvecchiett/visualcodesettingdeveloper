from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter.messagebox import *
import sqlite3
from datetime import date
from datetime import time
import re
import random as rd


# Interfaz
root = Tk()
root.geometry("700x580")
root.resizable(width=False, height=False)
root.title("MyAgenda")

##################################################################
# Modelo
##################################################################


def conexion_sql():
    base = sqlite3.connect("base_prueba1.db")
    return base


def crear_tabla(base):
    cursor = base.cursor()
    sql = "CREATE TABLE datos(id integer,nombre text,apellido text,dni integer,edad integer,telefono integer, turno text, fecha text, hora text, PRIMARY KEY(id AUTOINCREMENT))"
    try:
        cursor.execute(sql)
        base.commit()
        titulo = "Crear Registro"
        mensaje = "La tabla en la base de datos se creo con exito!"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Crear Registro"
        mensaje = "La tabla ya esta creada"
        messagebox.showerror(titulo, mensaje)


def borrar_tabla(base):
    cursor = base.cursor()
    sql = "DROP TABLE datos"
    try:
        cursor.execute(sql)
        base.commit()
        titulo = "Borrar Registro"
        mensaje = "La tabla de la base de datos se borro con exito!"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Borrar Registro"
        mensaje = "No existe ninguna tabla"
        messagebox.showerror(titulo, mensaje)


# Conexion
base = conexion_sql()

# Contadores
mi_id = None
turno = ""


def turnos():
    global turno
    letras = "abcdefghijklmnñopqrstuvxyzABCDEFGHIJKLMNÑOPQRSTUVXYZ"
    numeros = "0123456789"
    var = f"{letras}{numeros}"
    turno = "".join(rd.sample(var, 5))
    print("en funcion:", turno)
    return turno


def editar_datos(tree):

    global mi_id

    nombre = StringVar()
    apellido = StringVar()
    dni = IntVar()
    edad = IntVar()
    telefono = IntVar()
    fecha = StringVar()
    hora = StringVar()

    mi_id = tree.item(tree.selection())["text"]
    nombre = tree.item(tree.selection())["values"][0]
    apellido = tree.item(tree.selection())["values"][1]
    dni = tree.item(tree.selection())["values"][2]
    edad = tree.item(tree.selection())["values"][3]
    telefono = tree.item(tree.selection())["values"][4]
    fecha = tree.item(tree.selection())["values"][6]
    hora = tree.item(tree.selection())["values"][7]

    habilitar_campos()
    habilitar_campos_turnos()

    entry_nombre.insert(0, nombre)
    entry_apellido.insert(0, apellido)
    entry_dni.insert(0, dni)
    entry_edad.insert(0, edad)
    entry_telefono.insert(0, telefono)
    entry_hora.insert(0, hora)
    var_dia.set("0"),
    var_mes.set("0")

    return mi_id


# datos
var_nombre = StringVar()
var_apellido = StringVar()
var_dni = IntVar()
var_edad = IntVar()
var_telefono = IntVar()
var_dia = StringVar()
var_mes = StringVar()
var_hora = StringVar()


def borrar(tree):
    valor = tree.selection()
    print(valor)
    item = tree.item(valor)
    print(item)
    print(item["text"])
    mi_id = item["text"]

    cursor = base.cursor()
    info = (mi_id,)
    sql = "DELETE FROM datos WHERE id = ?;"
    try:
        cursor.execute(sql, info)
        base.commit()
        tree.delete(valor)
    except:
        titulo = "Borrar Datos"
        mensaje = "No se a podido borrar este elemento"
        messagebox.showerror(titulo, mensaje)


def actualizar_treeview(tree):
    records = tree.get_children()
    for element in records:
        tree.delete(element)

    cursor = base.cursor()
    sql = "SELECT * FROM datos ORDER BY id ASC"
    cursor.execute(sql)
    lista_datos = cursor.fetchall()
    for x in lista_datos:
        tree.insert(
            "",
            "end",
            text=x[0],
            values=(x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]),
        )


# Campos de entrada
def habilitar_campos():

    var_nombre.set(""),
    var_apellido.set(""),
    var_dni.set(""),
    var_edad.set(""),
    var_telefono.set(""),
    var_dia.set(""),
    var_mes.set(""),
    var_hora.set("")

    entry_nombre.config(state="normal")
    entry_apellido.config(state="normal")
    entry_dni.config(state="normal")
    entry_edad.config(state="normal")
    entry_telefono.config(state="normal")

    b_guardar.config(state="normal")
    b_cancelar.config(state="normal")
    b_agendar.config(state="normal")


def desabilitar_campos():
    var_nombre.set(""),
    var_apellido.set(""),
    var_dni.set(""),
    var_edad.set(""),
    var_telefono.set(""),

    entry_nombre.config(state="disabled")
    entry_apellido.config(state="disabled")
    entry_dni.config(state="disabled")
    entry_edad.config(state="disabled")
    entry_telefono.config(state="disabled")

    b_guardar.config(state="disabled")
    b_cancelar.config(state="disabled")
    b_agendar.config(state="disabled")


def cancelar():
    var_nombre.set(""),
    var_apellido.set(""),
    var_dni.set(""),
    var_edad.set(""),
    var_telefono.set(""),
    var_dia.set(""),
    var_mes.set(""),
    var_hora.set(""),

    entry_nombre.config(state="disabled")
    entry_apellido.config(state="disabled")
    entry_dni.config(state="disabled")
    entry_edad.config(state="disabled")
    entry_telefono.config(state="disabled")
    entry_dia.config(state="disabled")
    entry_mes.config(state="disabled")
    entry_hora.config(state="disabled")

    b_guardar.config(state="disabled")
    b_cancelar.config(state="disabled")
    b_agendar.config(state="disabled")


def desabilitar_campos_turnos():
    entry_dia.config(state="disabled")
    entry_mes.config(state="disabled")
    entry_hora.config(state="disabled")


def habilitar_campos_turnos():
    entry_dia.config(state="normal")
    entry_mes.config(state="normal")
    entry_hora.config(state="normal")


def alta_sql(base, nombre, apellido, dni, edad, telefono, dia, mes, hora, tree):
    global mi_id
    cadena = nombre
    patron = "[A-Za-záéíóú]*$"
    turnos()

    dia = int(dia)
    mes = int(mes)

    # fechas
    if dia > 0:
        año = 2022
        f = date(año, mes, dia).isoformat()
        h = time.fromisoformat(hora)
        print("salio")
        print("date", f)
        print(h)
    else:
        f = 0000
        h = 0000

    if mi_id == None:
        if re.match(patron, cadena):
            f = str(f)
            h = str(h)
            dni = int(dni)
            edad = int(edad)
            telefono = int(telefono)
            info = (nombre, apellido, dni, edad, telefono, turno, f, h)
            cursor = base.cursor()
            sql = "INSERT INTO datos(nombre, apellido, dni, edad, telefono, turno, fecha, hora) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            try:
                cursor.execute(sql, info)
                base.commit()
                actualizar_treeview(tree)
                titulo = "Alta de Datos"
                mensaje = "Datos guardados con exito!"
                messagebox.showinfo(titulo, mensaje)
                desabilitar_campos()
                desabilitar_campos_turnos()
            except:
                titulo = "Alta de Datos"
                mensaje = "No se a podido guardar este registro"
                messagebox.showerror(titulo, mensaje)
        else:
            titulo = "Alta de Datos"
            mensaje = "Error en los datos. Inserte datos correctamente"
            messagebox.showerror(titulo, mensaje)
    else:
        print("editar")
        f = str(f)
        h = str(h)
        cursor = base.cursor()
        info = (nombre, apellido, dni, edad, telefono, f, h, mi_id)
        sql = "UPDATE datos SET nombre=?, apellido=?, dni=?, edad=?, telefono=?, fecha=?, hora=? WHERE id=?;"
        try:
            cursor.execute(sql, info)
            base.commit()
            actualizar_treeview(tree)
            titulo = "Modificacion de Datos"
            mensaje = "Datos modificados con exito!"
            messagebox.showinfo(titulo, mensaje)
            desabilitar_campos()
            desabilitar_campos_turnos()
        except:
            titulo = "Editar Datos"
            mensaje = "No se a podido editar este registro"
            messagebox.showerror(titulo, mensaje)


##################################################################
# Vista
##################################################################

crear_tabla(base)
# Menu
menubar = Menu(root)

menu_inicio = Menu(menubar, tearoff=0)
menu_inicio.add_command(label="Agregar Datos", command=lambda: habilitar_campos())
menu_inicio.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Inicio", menu=menu_inicio)

menu_config = Menu(menubar, tearoff=0)
menu_config.add_command(label="Crear base de datos", command=lambda: crear_tabla(base))
menu_config.add_command(
    label="Elimnar base de datos", command=lambda: borrar_tabla(base)
)
menubar.add_cascade(label="Configuración", menu=menu_config)

menu_ayuda = Menu(menubar, tearoff=0)
menu_ayuda.add_command(label="Manual de uso")
menubar.add_cascade(label="Ayuda", menu=menu_ayuda)

root.config(menu=menubar)


# Label´s
fuente_logo = ("Roboto Medium Italic", 15)
fuente_a = ("Roboto Medium", 10)

titulo = Label(
    root,
    text="MyAgenda",
    width=64,
    bg="#48C9B0",
    fg="white",
    font=fuente_logo,
)
titulo.grid(row=0, column=0, sticky=W, columnspan=6)

texto = Label(
    root,
    text="Datos del paciente",
    width=50,
    font=fuente_a,
    bg="#A9CCE3",
    fg="white",
)
texto.grid(row=1, column=0, columnspan=3, sticky=W)

label_nombre = Label(root, text="Nombre:")
label_nombre.config(font=("Arial", 10))
label_nombre.grid(row=2, column=0, padx=10, pady=10)

label_apellido = Label(root, text="Apellido:")
label_apellido.config(font=("Arial", 10))
label_apellido.grid(row=3, column=0, padx=10, pady=10)

label_dni = Label(root, text="DNI:")
label_dni.config(font=("Arial", 10))
label_dni.grid(row=4, column=0, padx=10, pady=10)


label_edad = Label(root, text="Edad:")
label_edad.config(font=("Arial", 10))
label_edad.grid(row=5, column=0, padx=10, pady=10)

label_telefono = Label(root, text="Numero Telefonico:")
label_telefono.config(font=("Arial", 10))
label_telefono.grid(row=6, column=0, padx=10, pady=10)

label_turno = Label(
    root,
    text="Agendar Turno",
    width=50,
    font=fuente_a,
    bg="#FAD7A0",
    fg="white",
)
label_turno.grid(row=1, column=3, columnspan=3, sticky=W)

label_dia = Label(root, text="Día")
label_dia.config(font=("Arial", 10))
label_dia.grid(row=2, column=3, padx=10, pady=10)

label_mes = Label(root, text="Mes")
label_mes.config(font=("Arial", 10))
label_mes.grid(row=3, column=3, padx=10, pady=10)

label_hora = Label(root, text="Hora")
label_hora.config(font=("Arial", 10))
label_hora.grid(row=4, column=3, padx=10, pady=10)


# Entry´s
entry_nombre = Entry(root, textvariable=var_nombre)
entry_nombre.grid(row=2, column=1)

entry_apellido = Entry(root, textvariable=var_apellido)
entry_apellido.grid(row=3, column=1)

entry_dni = Entry(root, textvariable=var_dni)
entry_dni.grid(row=4, column=1)

entry_edad = Entry(root, textvariable=var_edad)
entry_edad.grid(row=5, column=1)

entry_telefono = Entry(root, textvariable=var_telefono)
entry_telefono.grid(row=6, column=1)

entry_dia = Entry(root, textvariable=var_dia)
entry_dia.grid(row=2, column=4)

entry_mes = Entry(root, textvariable=var_mes)
entry_mes.grid(row=3, column=4)

entry_hora = Entry(root, textvariable=var_hora)
entry_hora.grid(row=4, column=4)


# Tree View
tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8")
tree.column("#0", width=40, minwidth=40, anchor=W)
tree.column("col1", width=80, minwidth=80)
tree.column("col2", width=80, minwidth=80)
tree.column("col3", width=80, minwidth=80)
tree.column("col4", width=80, minwidth=80)
tree.column("col5", width=80, minwidth=80)
tree.column("col6", width=80, minwidth=80)
tree.column("col7", width=80, minwidth=80)
tree.column("col8", width=80, minwidth=80)
tree.heading("#0", text="ID")
tree.heading("col1", text="Nombre")
tree.heading("col2", text="Apellido")
tree.heading("col3", text="DNI")
tree.heading("col4", text="Edad")
tree.heading("col5", text="Telefono")
tree.heading("col6", text="Turno")
tree.heading("col7", text="Fecha")
tree.heading("col8", text="Hora")

tree.grid(row=8, column=0, columnspan=6, sticky=W)


# Scroll Tree
scroll_tree = Scrollbar(root, orient="vertical", command=tree.yview)
scroll_tree.grid(row=8, column=4, sticky="nse")
scroll_tree.config(command=tree.yview)
tree.configure(yscrollcommand=scroll_tree.set)


# Button´s
b_guardar = Button(
    root,
    text="Guardar",
    command=lambda: alta_sql(
        base,
        var_nombre.get(),
        var_apellido.get(),
        var_dni.get(),
        var_edad.get(),
        var_telefono.get(),
        var_dia.get(),
        var_mes.get(),
        var_hora.get(),
        tree,
    ),
)
b_guardar.config(
    width=20,
    font=fuente_a,
    bg="#A9CCE3",
    fg="white",
    cursor="hand2",
    activebackground="#7F9EB3",
)
b_guardar.grid(row=7, column=1, pady=10)

b_modificar = Button(root, text="Modificar Datos", command=lambda: editar_datos(tree))

b_modificar.config(
    width=20,
    font=fuente_a,
    bg="#48C9B0",
    fg="white",
    cursor="hand2",
    activebackground="#46B09C",
)
b_modificar.grid(row=9, column=0, pady=10)

b_agendar = Button(
    root, text="Agendar Turno", command=lambda: habilitar_campos_turnos()
)
b_agendar.config(
    width=20,
    font=fuente_a,
    bg="#FAD7A0",
    fg="white",
    cursor="hand2",
    activebackground="#D6AC68",
)
b_agendar.grid(row=7, column=4, pady=10)

b_nuevo = Button(root, text="Nuevo", command=lambda: habilitar_campos())
b_nuevo.config(
    width=20,
    font=fuente_a,
    bg="#48C9B0",
    fg="white",
    cursor="hand2",
    activebackground="#46B09C",
)
b_nuevo.grid(row=7, column=0, pady=10)

b_cancelar = Button(root, text="Cancelar", command=lambda: cancelar())
b_cancelar.config(
    width=20,
    font=fuente_a,
    bg="#EC7063",
    fg="white",
    cursor="hand2",
    activebackground="#B76158",
)
b_cancelar.grid(row=7, column=3, pady=10)

b_eliminar = Button(root, text="Eliminar", command=lambda: borrar(tree))
b_eliminar.config(
    width=20,
    font=fuente_a,
    bg="#EC7063",
    fg="white",
    cursor="hand2",
    activebackground="#B76158",
)
b_eliminar.grid(row=9, column=1, pady=10)


desabilitar_campos()
desabilitar_campos_turnos()
actualizar_treeview(tree)


root.mainloop()
