import sqlite3
from peewee import *

db = SqliteDatabase("gestorusuariosv2.db")

class BaseModel(Model):
    class Meta:
        database = db

class Usuario(BaseModel):
    usuario_id = AutoField(unique=True)
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
        
    def alta(self, nombre,apellido,sexo,email,username,password, mitreeview):
        Usuario=Usuario()
        Usuario.nombre=nombre.get()
        Usuario.apellido=apellido.get()
        Usuario.sexo=sexo.get()
        Usuario.email=email.get()
        Usuario.username=username.get()
        Usuario.password=password.get()
     
        Usuario.save()

        self.actualizar_treeview(mitreeview)


    def actualizar_treeview(self, mitreeview):
        # limpieza de tabla
        records = mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)
        # Consiguiendo datos
        for fila in Usuario.select():
            mitreeview.insert("", 0, text=fila.id, values=(fila.nombre, fila.apellido, fila.sexo, fila.email, fila.username))

    def baja(self, mitreeview):
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        borrar=Usuario.get(Usuario.id==valor_id["text"])
        borrar.delete_instance()
        self.actualizar_treeview(mitreeview)

    def modificar(self,nombre,apellido,sexo,email,username,password, mitreeview):
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        actualizar=Usuario.update(nombre=nombre.get(), apellido=apellido.get(), sexo=sexo.get(), email=email.get(), password=password.get()).where(Usuario.id==valor_id["text"])
        actualizar.execute()
        self.actualizar_treeview(mitreeview)
