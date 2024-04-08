import sqlite3
from peewee import *

db = SqliteDatabase("gestorusuariosv2.db")

class BaseModel(Model):
    class Meta:
        database = db

class Usuario(BaseModel):
    #usuario_id = AutoField(unique=True)
    username   = CharField(unique=True)
    nombre     = CharField() 
    apellido   = CharField()
    password   = CharField()
    email      = CharField()
        
db.connect()
db.create_tables([Usuario])


class Abmc:
    def __init__(
        self,
    ): pass
        
    def alta(self, nombre,apellido,email,username,password, mitreeview):
        usuario=Usuario()
        usuario.nombre=nombre.get()
        usuario.apellido=apellido.get()
        usuario.email=email.get()
        usuario.username=username.get()
        usuario.password=password.get()
     
        usuario.save()

        self.actualizar_treeview(mitreeview)


    def actualizar_treeview(self, mitreeview):
        # limpieza de tabla
        records = mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)
        # Consiguiendo datos
        # no tengo idea porque no anda el select. error no such column t1.usuario_id en peewee.py linea 3177
        for fila in Usuario.select():
           # print (fila.id)
           # print (fila.nombre)
           # print(fila.apellido)
           # print(fila.email)
           # print( fila.username)
           # print ( fila.password)
            mitreeview.insert("", 0, text=fila.id, values=(fila.nombre, fila.apellido, fila.email, fila.username, fila.password))

    def baja(self, mitreeview):
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        borrar=Usuario.get(Usuario.id==valor_id["text"])
        borrar.delete_instance()
        self.actualizar_treeview(mitreeview)

    def modificar(self,nombre,apellido,email,username,password, mitreeview):
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        actualizar=Usuario.update(nombre=nombre.get(), apellido=apellido.get(), email=email.get(), password=password.get()).where(Usuario.id==valor_id["text"])
        actualizar.execute()
        self.actualizar_treeview(mitreeview)
