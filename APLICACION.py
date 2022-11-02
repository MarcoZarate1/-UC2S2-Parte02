# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:22:45 2022

@author: Alumno
"""
from tkinter import *
from tkinter.ttk import *

menu="""
 Datos Persona
 1)Listar Persona
 2)Agregar Persona
 3)Salir
"""
root = Tk()
root.title("login")
root.geometry("300x150")
root.resizable(width=False, height=False)
root.config(bg="aqua")




usuario=Label(root, text="Ingrese nombre de usuario: ")
usuario.pack()



usuario1=StringVar()
usu=Entry(root, width=30, textvariable=usuario1)
usu.pack()

contraseña=Label(root,text="contraseña: ")
contraseña.pack()

contra=StringVar()
contra1=Entry(root, width=30, textvariable=contra, show="*")
contra1.pack()



with open("login.txt") as file_object:
    us = file_object.read()

with open("clave.txt") as file_object:
     pas = file_object.read()
    
    
def ingresar():
    if usuario1.get()== us  and contra.get()== pas:
        root.title("Correcto")
        print(menu)
            
    else:
        root.title("Incorrecto, ingrese nuevamente")
        
        
        
bt=Button(root, text="Entrar", command=ingresar)
bt.pack(side=BOTTOM)


root.mainloop()

