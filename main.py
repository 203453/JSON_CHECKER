import os
from tkinter import *
from tkinter import filedialog, messagebox
from automatas import alumnos, docentes, vehiculos
# from automatas import alumnos
import json

root = Tk()
root.title('JSON CHECKER')
root.geometry("300x150")
root.configure(background="#555555")

#Funciones
def openJson():
    global x, dirLabel, valBtn;
    
    try:
        dirLabel
    except NameError:
        dirLabel = None
    else:
        dirLabel.destroy()

    try:
        valBtn
    except NameError:
        valBtn = None
    else:
        valBtn.destroy()

    
    root.filename = filedialog.askopenfilename(initialdir="automatas/", title="Select a JSON", filetypes=(("JSON files", "*.json"),("All files", "*.*")))
    ruta = root.filename
    pathname, exten = os.path.splitext(ruta)
    nameF = pathname.split('/')
    dirLabel = Label(root, text=(nameF[-1] + ".json"), bg="#555555", fg="#FFFFFF", font='Arial 8 bold', wraplength=120)
    dirLabel.place(x=170, y=10)
    #Boton para validar
    valBtn = Button(root, text="Validar",bg="#4AB5EB", command=validar)
    valBtn.place(x=90, y=45, width=68)
    try:
        f = open(str(ruta))
    except FileNotFoundError:
        messagebox.showinfo(message="Archivo no cargado", title="Error")
        dirLabel.destroy()
        valBtn.destroy()
    else:
        try:
            x = json.load(f)
        except ValueError:
            messagebox.showinfo(message="El JSON es invalido", title="Error")
            dirLabel.destroy()
            valBtn.destroy()
        else:
            x = json.dumps(x)
            x = str(x)
            x = x.lower()
            x = x.replace(" ", "")

def validar():
    global msg, valLabel;

    try:
        msg
    except NameError:
        msg = None
    else:
        msg.destroy()

    try:
        valLabel
    except NameError:
        valLabel = None
    else:
        valLabel.destroy()

    msg = Label(root)
        
    valLabel = Label(root, text='', bg="#555555", fg="#FFA444")
    valLabel.place(x=170, y=45)
    
    if(list.get(ANCHOR) == "Alumnos"):
        valLabel.config(text="Plantilla alumnos", font='Arial 10 bold')
        alumnos
        if alumnos.accepts_input(x.lower()):
            msg = Label(root, text="VALIDO", bg="#555555", fg="#98FF62", font='Arial 25 bold', justify='center')
            msg.place(x=90, y=85)
        else:
            msg = Label(root, text="INVALIDO", bg="#555555", fg="#FF6E62", font='Arial 25 bold', justify='center')
            msg.place(x=90, y=85)

    if(list.get(ANCHOR) == "Docentes"):
        valLabel.config(text="Plantilla docentes", font='Arial 10 bold')
        docentes
        if docentes.accepts_input(x.lower()):
            msg = Label(root, text="VALIDO", bg="#555555", fg="#98FF62", font='Arial 25 bold', justify='center')
            msg.place(x=90, y=85)
        else:
            msg = Label(root, text="INVALIDO", bg="#555555", fg="#FF6E62", font='Arial 25 bold', justify='center')
            msg.place(x=90, y=85)

    if(list.get(ANCHOR) == "Vehiculos"):
        valLabel.config(text="Plantilla vehiculos", font='Arial 10 bold')
        if vehiculos.accepts_input(x.lower()):
            msg = Label(root, text="VALIDO", bg="#555555", fg="#98FF62", font='Arial 25 bold', justify='center')
            msg.place(x=90, y=85)
        else:
            msg = Label(root, text="INVALIDO", bg="#555555", fg="#FF6E62", font='Arial 25 bold', justify='center')
            msg.place(x=90, y=85) 


#Boton para abrir JSON
openBtn = Button(root, text="Abrir JSON",bg="#FFE254", command=openJson).place(x=90, y=10)


#Listbox automatas
list = Listbox(root, bg="#EAEAEA")
list.place(x=10, y=10, width=65, height=60)

list.insert(END, "Alumnos")
list.insert(END, "Docentes")
list.insert(END, "Vehiculos")

root.mainloop()


