from tkinter import*
import sqlite3
import tkinter.ttk as ttk   
import tkinter.messagebox as tkMessageBox
root = Tk()

root.title("hola")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 700
height = 750
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)
Top = Frame(root, width=700, height=50, bd=8, relief="raise")
Top.pack(side=TOP)


Left = Frame(root, width=700, height=350, bd=8, relief="raise")
Left.pack(side=TOP)

Right = Frame(root, width=700, height=350, bd=8, relief="raise")
Right.pack(side=BOTTOM)


root.mainloop()