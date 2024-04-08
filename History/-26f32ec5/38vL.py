import sqlite3
from peewee import *

from tkinter.messagebox import showerror
from tkinter import END
from datetime import datetime
import re


# create a peewee database instance -- our models will use this database to
# persist information
db = SqliteDatabase("gestorusuariosv2")

# model definitions -- the standard "pattern" is to define a base model class
# that specifies which database to use.  then, any subclasses will automatically
# use the correct storage.
class BaseModel(Model):
    class Meta:
        database = db 
# the user model specifies its fields (or columns) declaratively, like django
class User(BaseModel):
    usuario_id = AutoField(unique=True)
    username   = CharField(unique=True)
    nombre     = CharField() 
    apellido   = CharField()
    password   = CharField()
    email      = CharField()
    join_date  = DateTimeField()


db.connect()
db.create_tables([usuarios])

# ##############################################
# MODELO
# ##############################################
class Abmc(): 
    def __init__(self,):
        pass



    def alta(self, nombre,apellido,sexo,email,username,password,tree, nombre_entry,apellido_entry,sexo_entry,email_entry,username_entry,password_entry  ):

    
        if (nombre and apellido and sexo and email and username and password  !=('')) :
            cadena = username
            patron="^[A-Za-z. _-áéíóú]*$"  #regex para el campo username
            if (re.match(patron, cadena)):
                usuario = User()

                usuario.username    = username.get()
                usuario.nombre      = nombre.get()
                usuario.apellido    = apellido.get()
                usuario.password    = password.get()
                usuario.email       = email.get()
                usuario.join_date   = datetime.now
                usuario.save()

                self.borrar_entry(nombre_entry,apellido_entry,sexo_entry,email_entry,username_entry,password_entry)
                self.actualizar_treeview(tree)
            else:
                    showerror("error al guardar", "Por favor, ingrese los campos requeridos")

        else:
            showerror("error al guardar", "ningun campo puede permanecer vacio")

            print ("por favor complete el campo")
    
    def actualizar_treeview(self,mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)


        resultado = User.select()
        for fila in resultado:
            print(fila)
            mitreview.insert("", 0, text=fila[0], values=(fila.usuario_id,fila.username, fila.nombre, fila.apellido, fila.email) ) 

    def borrar_entry(self,nombre_entry,apellido_entry,sexo_entry,email_entry,username_entry,password_entry): 
        nombre_entry.delete(0, END)
        apellido_entry.delete(0, END)
        sexo_entry.delete(0, END)
        email_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        


    def actualizar(self, nombre,apellido,sexo,email,username,password,tree, nombre_entry,apellido_entry,sexo_entry,email_entry,username_entry,password_entry ):  
        valor = tree.selection()
        item = tree.item(valor)
        
        actualizar= User.update(nombre=nombre_entry.get(), apellido=apellido_entry.get, sexo= sexo_enty.get(), email=email_entry.get, username=username_entry.get, password = password_entry.get()).where(User.usuario_id == item['text'])
        actualizar.execute()
        
        self.borrar_entry(username)
        self.actualizar_treeview(tree)
        


    def borrar(self,tree):
        valor = tree.selection()
        item = tree.item(valor)
        
        borrar = User.get(User.usuario_id=item['text'] )
        borrar.delete_instance

        self.borrar_entry(username)
        self.actualizar_treeview(tree)

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


