import sqlite3
from peewee import *

db = SqliteDatabase("gestorusuariosv2.db")

class BaseModel(Model):
    class Meta:
        database = db

class Usuario(BaseModel):
    titulo = CharField(unique=True)
    descripcion = CharField()

db.connect()
db.create_tables([Usuario])


class Abmc:
    def __init__(
        self,
    ): pass
        
    def alta(self, titulo, descripcion, mitreeview):
        Usuario=Usuario()
        Usuario.titulo=titulo.get()
        Usuario.descripcion=descripcion.get()
        Usuario.save()

        self.actualizar_treeview(mitreeview)


    def actualizar_treeview(self, mitreeview):
        # limpieza de tabla
        records = mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)
        # Consiguiendo datos
        for fila in Usuario.select():
            mitreeview.insert("", 0, text=fila.id, values=(fila.titulo, fila.descripcion))

    def baja(self, mitreeview):
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        borrar=Usuario.get(Usuario.id==valor_id["text"])
        borrar.delete_instance()
        self.actualizar_treeview(mitreeview)

    def modificar(self, titulo, descripcion, mitreeview):
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        actualizar=Usuario.update(titulo=titulo.get(), descripcion=descripcion.get()).where(Usuario.id==valor_id["text"])
        actualizar.execute()
        self.actualizar_treeview(mitreeview)
