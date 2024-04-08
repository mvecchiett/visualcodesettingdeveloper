
import sqlite3
from tkinter.messagebox import showerror
from tkinter import END
import re




# ##############################################
# MODELO
# ##############################################
class Abmc(): 
    def __init__(self,):pass


    def conexion(self,):
        con = sqlite3.connect("gestorusuariosv2.db")
        return con

    def crear_tabla(self,):
        con = self.conexion()
        cursor = con.cursor()
        sql = "CREATE TABLE IF NOT EXISTS `usuarios` (usuario_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nombre TEXT, apellido TEXT, sexo TEXT, email TEXT, username TEXT, password TEXT)"

        cursor.execute(sql)
        con.commit()


    def alta(self, nombre,apellido,sexo,email,username,password,tree, nombre_entry,apellido_entry,sexo_entry,email_entry,username_entry,password_entry  ):
    
        if (nombre and apellido and sexo and email and username and password  !=('')) :
            cadena = username
            patron="^[A-Za-z. _-áéíóú]*$"  #regex para el campo username
            if (re.match(patron, cadena)):
                print (nombre,apellido,sexo,email, username ,  password)
                con=self.conexion()
                cursor=con.cursor()
                data=(nombre,apellido,sexo,email, username ,  password)
                sql="INSERT INTO usuarios (nombre,apellido,sexo,email, username ,  password) VALUES(?,?,?,?,?,?)"
                cursor.execute(sql, data)
                con.commit()
                print("Estoy en alta todo ok")
                self.borrar_entry(nombre_entry,apellido_entry,sexo_entry,email_entry,username_entry,password_entry)
                self.actualizar_treeview(tree)
            else:
                    showerror("error al guardar", "Por favor, ingrese los campos requeridos")

        else:
            showerror("error al guardar", "ningun campo puede permanecer vacio")

            print ("por favor complete el campo")
    
    def actualizar_treevwie(self,mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)

        sql = "SELECT * FROM usuarios ORDER BY id ASC"
        con=self.conexion()
        cursor=con.cursor()
        datos=cursor.execute(sql)

        resultado = datos.fetchall()
        for fila in resultado:
            print(fila)
            mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5]))  

    def borrar_entry(self,nombre_entry,apellido_entry,sexo_entry,email_entry,username_entry,password_entry): 
        nombre_entry.delete(0, END)
        apellido_entry.delete(0, END)
        sexo_entry.delete(0, END)
        email_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        


    def actualizar(self,nombre,apellido,sexo,email, username , password):  
        valor = tree.selection()
        item = tree.item(valor)
    
        print(item['text'])
        mi_id = item['text']

        con=self.conexion()
        cursor=con.cursor()
        data=(username,mi_id,)
        sql= "UPDATE usuarios SET (nombre,apellido,sexo,email, password)=(?,?,?,?,?) WHERE id=?;"
    
        
        cursor.execute(sql,data)
        con.commit()
        self.borrar_entry(username)
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
        sql = "DELETE FROM usuarios WHERE id = ?;"
        cursor.execute(sql, data)
        con.commit()
        tree.delete(valor)



