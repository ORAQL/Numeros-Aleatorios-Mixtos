from cProfile import label
from cgitb import text
from msvcrt import kbhit
from textwrap import fill
from this import d
from tkinter import *
import tkinter
from turtle import right, width
from tkinter import ttk
import pandas as pd
import os

raiz=Tk()

raiz.title("Generacion de números aleatorios multiplicativo")

pestanas = ttk.Notebook()

pestanas.pack()

frame=Frame(pestanas)

frame.pack()

semilla = StringVar()
multiplo= StringVar()
sumando = StringVar()
modulo = StringVar()

Label(frame, text="Semilla", padx=50).grid(row=0, column=1)
Entry(frame, textvariable=semilla).grid(row=1, column=1)
Label(frame, text="Variable Multiplicativa", padx=50).grid(row=0, column=2)
Entry(frame, textvariable=multiplo).grid(row=1, column=2)
Label(frame, text="Variable Aditiva", padx=50).grid(row=0, column=4)
Entry(frame, textvariable=sumando).grid(row=1, column=4)
Label(frame, text="Modulo", padx=50).grid(row=0, column=5)
Entry(frame, textvariable=modulo).grid(row=1, column=5)


def GenerarNumerosMixta():

    x = int(semilla.get())
    ai = int(multiplo.get())
    c = int(sumando.get())
    m = int(modulo.get())

    if()

    h = [x]  
    j = [ai] 
    k = [c] 
    l = [m] 
    w = [0]

    for b in range(1, m+1):

        a = ((ai*x) + c)
        x = a%m

        h.append(x)
        j.append(a)
        k.append(" ")
        l.append(" ")
        w.append(x/m)


    d = {'X':h, 'A':j, 'C':k, 'M':l, 'Numeros aleatorios':w}

    df = pd.DataFrame(data=d)
    df.to_excel('numeros.xlsx')
    os.startfile("numeros.xlsx")
    
    

    
botonGenerar=Button(frame, text="Generar", command=lambda:GenerarNumerosMixta()).grid(row = 4, column=3)

Checkbutton(frame, text="Validar Datos").grid(row=3, column=2)
Checkbutton(frame, text="No Validar Datos").grid(row=3, column=4)

frame3=Frame(pestanas)

frame3.pack()

semilla2 = StringVar()
multiplo2= StringVar()
modulo2 = StringVar()

Label(frame3, text="Semilla", padx=50).grid(row=0, column=1)
Entry(frame3, textvariable=semilla2).grid(row=1, column=1)
Label(frame3, text="Variable Multiplicativa", padx=50).grid(row=0, column=2)
Entry(frame3, textvariable=multiplo2).grid(row=1, column=2)
Label(frame3, text="Modulo", padx=50).grid(row=0, column=4)
Entry(frame3, textvariable=modulo2).grid(row=1, column=4)

def GenerarNumerosMultiplicativa():

    x2 = int(semilla2.get())
    ai2 = int(multiplo2.get())
    m2 = int(modulo2.get())

    h = [x2]  
    j = [ai2] 
    l = [m2] 
    w = [0]

    for b in range(1, m2+1):

        a = ((ai2*x2))
        x2 = a%m2

        h.append(x2)
        j.append(a)
        l.append(" ")
        w.append(x2/m2)


    d = {'X':h, 'A':j, 'M':l, 'Numeros aleatorios':w}

    df = pd.DataFrame(data=d)
    df.to_excel('numeros.xlsx')
    os.startfile("numeros.xlsx")
    

botonGenerar=Button(frame3, text="Generar", command=lambda:GenerarNumerosMultiplicativa()).grid(row= 4 , column=3)

Checkbutton(frame3, text="Validar Datos").grid(row=3, column=2)
Checkbutton(frame3, text="No Validar Datos").grid(row=3, column=4)

pestanas.add(frame, text="Formula Congruencial Mixta")
pestanas.add(frame3, text="Formula Congruencial Multiplicativa")

raiz.mainloop()
