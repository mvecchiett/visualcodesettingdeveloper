#************************************ IMPORTACIONES (REFERENCIAS ************************************ 
from tkinter import*
import sqlite3
import tkinter.ttk as ttk   
import tkinter.messagebox as tkMessageBox
#************************************ Tk OPCIONES PRINCIPALES ********************************  **** 
#https://visualtk.com/
root = Tk()
mensajes=leermensajes()
root.title(mensajes[0])
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 800
height = 700
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

Frametitulo = Frame(root, width=800, height=50, bd=8, relief="raise")
Frametitulo.pack(side=TOP)
# Frame del abm
Frameabm = Frame(root, width=800, height=350, bd=8, relief="raise")
Frameabm.pack(side=TOP)
#Frame del treeview
frameconsulta = Frame(root, width=800, height=350, bd=8, relief="raise")
frameconsulta.pack(side=TOP)

Forms = Frame(Frameabm, width=800, height=50)
Forms.pack(side=TOP)

Buttons = Frame(Frameabm, width=800, height=100, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)
RadioGroup = Frame(Forms)


root.mainloop()