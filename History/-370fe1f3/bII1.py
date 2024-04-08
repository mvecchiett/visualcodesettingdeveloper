from tkinter import *
    
splash_root = Tk()  
    
splash_root.geometry("200x200") 
  
splash_label = Label(splash_root,text="Bienvenido al sistema de gestión de usuarios",font=18) 
splash_label.pack() 
  
def main():   
    
    splash_root.destroy() 
  
    
    root = Tk()  
        
    
    root.geometry("400x400")  
  
splash_root.after(3000,main) 
  
mainloop()

