from tkinter import*
import sqlite3
import tkinter.ttk as ttk   
import tkinter.messagebox as tkMessageBox
root = Tk()

root.title("hola")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 800
height = 700
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)
Top = Frame(root, width=800, height=50, bd=8, relief="raise")
Top.pack(side=TOP)

up = Frame(root, width=800, height=300, bd=8, relief="raise")
up.pack(side=TOP)
botonera = Frame(root, width=800, height=50, bd=8, relief="raise")
botonera.pack(side=TOP)

treedatos = Frame(root, width=800, height=300, bd=8, relief="raise")
treedatos.pack(side=BOTTOM)


root.mainloop()