#************************************ IMPORTACIONES (REFERENCIAS ************************************ 
from cgitb import reset
from tkinter import*
import sqlite3
import tkinter.ttk as ttk   
import tkinter.messagebox as tkMessageBox
import re
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap

#https://docs.python.org/es/3/library/tkinter.html
mensajes = []
#************************************ FUNCION DE MENSAJES ************************************ 
def leermensajes():
    with open("datos.txt", "r") as tf:
        lineas = tf.read().split(',')
    return lineas

#************************************ Tk OPCIONES PRINCIPALES ********************************  **** 
#https://visualtk.com/
root = Tk()
mensajes=leermensajes()
root.title(mensajes[0])
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

#************************************ OTRAS FUNCIONES ************************************  
    
def Database():
    global conn, cursor
    conn = sqlite3.connect('gestorusuarios.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `usuarios` (usuario_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nombre TEXT, apellido TEXT, sexo TEXT, email TEXT, username TEXT, password TEXT)")
    
def Alta():
    if  NOMBRE.get() == "" or APELLIDO.get() == "" or SEXO.get() == "" or EMAIL.get() == "" or USERNAME.get() == "" or PASSWORD.get() == "":
        txt_resultado.config(text="Por favor, complete los campos requeridos", fg="red")
    else:
        Database()
        cursor.execute("INSERT INTO `usuarios` (nombre, apellido, sexo, email, username, password) VALUES(?, ?, ?, ?, ?, ?)", (str(NOMBRE.get()), str(APELLIDO.get()), str(SEXO.get()), str(EMAIL.get()), str(USERNAME.get()), str(PASSWORD.get())))
        tree.delete(*tree.get_children())
        cursor.execute("SELECT * FROM `usuarios` ORDER BY `apellido` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
        conn.commit()
        NOMBRE.set("")
        APELLIDO.set("")
        SEXO.set("")
        EMAIL.set("")
        USERNAME.set("")
        PASSWORD.set("")
        cursor.close()
        conn.close()
        txt_resultado.config(text="Usuario creado con éxito,", fg="green")

def Consultar():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM usuarios ORDER BY apellido ASC")
    fetch = cursor.fetchall()
    registros = len(fetch)
    if registros >0:
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
            txt_resultado.config(text="Registros leidos en la base de datos: " + str(registros) ,fg="black")
    else:
        txt_resultado.config(text="No hay registros para consultar." ,fg="black")
    cursor.close()
    conn.close()
    

def Validardatos():
    blnSalida = FALSE
    if NOMBRE.get() == "" or APELLIDO.get() == "" or SEXO.get() == "" or EMAIL.get() == "" or USERNAME.get() == "" or PASSWORD.get() == "":
        txt_resultado.config(text="Complete los datos para poder guardar.", fg="red")
    else:
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',EMAIL.get().lower):
            blnSalida=TRUE
        else:
            txt_resultado.config(text="Direccion de email incorrecto.", fg="red")

    return (blnSalida)

def Guardar():
    Database()
#    if NOMBRE.get() == "" or APELLIDO.get() == "" or SEXO.get() == "" or EMAIL.get() == "" or USERNAME.get() == "" or PASSWORD.get() == "":
    if Validardatos()==TRUE:
        tree.delete(*tree.get_children())
        cursor.execute("UPDATE `usuarios` SET `nombre` = ?, `apellido` = ?, `sexo` =?,  `email` = ?,  `username` = ?, `password` = ? WHERE `usuario_id` = ?", (str(NOMBRE.get()), str(APELLIDO.get()), str(SEXO.get()), str(EMAIL.get()), str(USERNAME.get()), str(PASSWORD.get()), int(memusuario_id)))
        conn.commit()
        cursor.execute("SELECT * FROM `usuarios` ORDER BY `apellido` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
        cursor.close()
        conn.close()
        NOMBRE.set("")
        APELLIDO.set("")
        SEXO.set("")
        EMAIL.set("")
        USERNAME.set("")
        PASSWORD.set("")
        btn_alta.config(state=NORMAL)
        btn_consulta.config(state=NORMAL)
        btn_guardar.config(state=DISABLED)
        btn_borrar.config(state=NORMAL)
        txt_resultado.config(text="Usuario modificado con éxito", fg="black")


def OnSelected(event):
    global memusuario_id;
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    memusuario_id = selecteditem[0]
    NOMBRE.set("")
    APELLIDO.set("")
    SEXO.set("")
    EMAIL.set("")
    USERNAME.set("")
    PASSWORD.set("")
    NOMBRE.set(selecteditem[1])
    APELLIDO.set(selecteditem[2])
    SEXO.set(selecteditem[3])
    EMAIL.set(selecteditem[4])
    USERNAME.set(selecteditem[5])
    PASSWORD.set(selecteditem[6])
    btn_alta.config(state=DISABLED)
    btn_consulta.config(state=DISABLED)
    btn_guardar.config(state=NORMAL)
    btn_borrar.config(state=DISABLED)

def Borrar():
    if not tree.selection():
       txt_resultado.config(text="Por favor, seleccione un registro primero,", fg="red")
    else:
        resultado = tkMessageBox.askquestion("Gestor de Usuarios", "Esta seguro de eliminar este registro?", icon="warning")
        if resultado == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `usuarios` WHERE `usuario_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
            txt_resultado.config(mensajes(7), fg="black")
            
    
def Salir():
    resultado = tkMessageBox.askquestion("Gestor de Usuarios","Desea Salir?", icon="warning")
    if resultado == 'yes':
        root.destroy()
        exit()

    

#********************************VARIABLES********************************
NOMBRE = StringVar()
APELLIDO = StringVar()
SEXO = StringVar(value="Hombre")
EMAIL = StringVar()
USERNAME = StringVar()
PASSWORD = StringVar()

#********************************PANTALLA********************************
#recuadro del titulo
Frametitulo = Frame(root, width=900, height=50, bd=8, relief="raise")
Frametitulo.pack(side=TOP)
# Frame del abm
Left = Frame(root, width=300, height=500, bd=8, relief="raise")
Left.pack(side=LEFT)
#Frame del treeview
Right = Frame(root, width=600, height=500, bd=8, relief="raise")
Right.pack(side=RIGHT)

Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)

Botones = Frame(Left, width=300, height=100, bd=8, relief="raise")
Botones.pack(side=BOTTOM)
RadioGroup = Frame(Forms)
#Hombre = Radiobutton(RadioGroup, text=mensajes(10), variable=SEXO, value=mensajes(10), font=('arial', 16)).pack(side=LEFT)
#Mujer =  Radiobutton(RadioGroup, text=mensajes(11), variable=SEXO, value=mensajes(11), font=('arial', 16)).pack(side=LEFT)
#nota aparentemente me vuelvo a chocar con la iposibilidad de generalizar la busqueda de literales
# pendiente analizar https://stackoverflow.com/questions/31087111/typeerror-list-object-is-not-callable-in-python

Hombre = Radiobutton(RadioGroup, text='Hombre', variable=SEXO, value='Hombre', font=('arial', 16)).pack(side=LEFT)
Mujer =  Radiobutton(RadioGroup, text='Mujer', variable=SEXO, value='Mujer', font=('arial', 16)).pack(side=LEFT)
   
#********************************ETIQUETAS********************************
txt_titulo = Label(Frametitulo, width=900, font=('arial', 24), text = mensajes[0])
txt_titulo.pack()
txt_nombre = Label(Forms, text='Nombre', font=('arial', 16), bd=15)
txt_nombre.grid(row=0, sticky="e")
txt_apellido = Label(Forms, text='Apellido', font=('arial', 16), bd=15)
txt_apellido.grid(row=1, sticky="e")
txt_sexo = Label(Forms, text='Sexo', font=('arial', 16), bd=15)
txt_sexo.grid(row=2, sticky="e")
txt_email = Label(Forms, text='Email', font=('arial', 16), bd=15)
txt_email.grid(row=3, sticky="e")
txt_username = Label(Forms, text='Usuario', font=('arial', 16), bd=15)
txt_username.grid(row=4, sticky="e")
txt_password = Label(Forms, text='Password', font=('arial', 16), bd=15)
txt_password.grid(row=5, sticky="e")
txt_resultado = Label(Botones)
txt_resultado.pack(side=TOP)

#********************************INGRESO DE DATOS?********************************
nombre = Entry(Forms, textvariable=NOMBRE, width=30)
nombre.grid(row=0, column=1)
apellido = Entry(Forms, textvariable=APELLIDO, width=30)
apellido.grid(row=1, column=1)
RadioGroup.grid(row=2, column=1)
email = Entry(Forms, textvariable=EMAIL, width=30)
email.grid(row=3, column=1)
nombre = Entry(Forms, textvariable=USERNAME, width=30)
nombre.grid(row=4, column=1)
password = Entry(Forms, textvariable=PASSWORD, show="*", width=30)
password.grid(row=5, column=1)

#********************************Mapeo botones con acciones ********************************
btn_alta = Button(Botones, width=10, text="Alta", command=Alta)
btn_alta.pack(side=LEFT)
btn_consulta = Button(Botones, width=10, text="Consulta", command=Consultar )
btn_consulta.pack(side=LEFT)
btn_guardar = Button(Botones, width=10, text="Guardar", command=Guardar, state=DISABLED)
btn_guardar.pack(side=LEFT)
btn_borrar = Button(Botones, width=10, text="Borrar", command=Borrar)
btn_borrar.pack(side=LEFT)
btn_salir = Button(Botones, width=10, text="Exit", command=Salir)
btn_salir.pack(side=LEFT)

#********************************LISTA DE CONSULTA********************************
scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=("usuariosID", "Nombre", "Apellido", "Sexo", "Email", "Username", "Password"), selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('usuariosID', text="usuariosID", anchor=W)
tree.heading('Nombre', text="Nombre", anchor=W)
tree.heading('Apellido', text="Apellido", anchor=W)
tree.heading('Sexo', text="Sexo", anchor=W)
tree.heading('Email', text="Email", anchor=W)
tree.heading('Username', text="Username", anchor=W)
tree.heading('Password', text="Password", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=80)
tree.column('#5', stretch=NO, minwidth=0, width=150)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.column('#7', stretch=NO, minwidth=0, width=120)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected)

#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    root.mainloop()
