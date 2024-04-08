
from configparser import MAX_INTERPOLATION_DEPTH
import sqlite3
from tkinter.messagebox import showerror
from tkinter import END
import re
from typing import TypeVar




# ##############################################
# MODELO
# ##############################################
class Abmc(): 
    def __init__(self,):pass


    def conexion(self,):
        con = sqlite3.connect("mistock_2.db")
        return con

    def crear_tabla(self,):
        con = self.conexion()
        cursor = con.cursor()
        sql = """CREATE TABLE clasificacion
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo varchar(20) NOT NULL,
                autor varchar(20)NOT NULL,
                ubicacion varchar(20)NOT NULL)
                
        """
        cursor.execute(sql)
        con.commit()

#try:
#    conexion()
#    crear_tabla()
#except:
#    print("Hay un error")


    def alta(self,titulo,autor,ubicacion,tree,titulo_entry, autor_entry,  ubicacion_entry):
    
        if (titulo and autor and ubicacion  !=('')) :
            cadena = autor
            patron="^[A-Za-z. _-áéíóú]*$"  #regex para el campo cadena
            if (re.match(patron, cadena)):
                print (titulo,autor,ubicacion)
                con=self.conexion()
                cursor=con.cursor()
                data=(titulo,autor,ubicacion)
                sql="INSERT INTO clasificacion (titulo,autor,ubicacion) VALUES(?,?,?)"
                cursor.execute(sql, data)
                con.commit()
                print("Estoy en alta todo ok")
                self.borrar_entry(titulo_entry, autor_entry,  ubicacion_entry)
                self.actualizar_treeview(tree)
            else:
                    showerror("error al guardar",
                "el autor no puede contener un numero")

        else:
            showerror("error al guardar",
            "ningun campo puede permanecer vacio")

            print ("por favor complete el campo")
    
    def actualizar_treeview(self,mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)

        sql = "SELECT * FROM clasificacion ORDER BY id ASC"
        con=self.conexion()
        cursor=con.cursor()
        datos=cursor.execute(sql)

        resultado = datos.fetchall()
        for fila in resultado:
            print(fila)
            mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))   

    def borrar_entry(self,titulo_entry, autor_entry,  ubicacion_entry): 
        titulo_entry.delete(0, END)
        autor_entry.delete(0, END)
        ubicacion_entry.delete(0, END)


    def actualizar(self,titulo,autor,ubicacion,tree,titulo_entry, autor_entry,  ubicacion_entry):  
        valor = tree.selection()
        item = tree.item(valor)
    
        print(item['text'])
        mi_id = item['text']
        con=self.conexion()
        cursor=con.cursor()
        print(type(  mi_id ))
        if mi_id!="":
            data=(titulo,autor,ubicacion,mi_id,)
            sql= "UPDATE clasificacion SET (titulo,autor,ubicacion)=(?,?,?) WHERE id=?;"
    
        
        cursor.execute(sql,data)
        con.commit()
        self.borrar_entry(titulo_entry, autor_entry,  ubicacion_entry)
        self.actualizar_treeview(tree)
        

        


    def borrar(self,tree):
        valor = tree.selection()
        print(valor)  
        item = tree.item(valor)
        print(item)    
        print(item['text'])
        mi_id = item['text']

        con=self.conexion()
        cursor=con.cursor()
        data = (mi_id,)
        sql = "DELETE FROM clasificacion WHERE id = ?;"
        cursor.execute(sql, data)
        con.commit()
        tree.delete(valor)



