from cProfile import label
from cgitb import text
from textwrap import fill
from tkinter import *
import tkinter
from turtle import right, width
from tkinter import ttk

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
Label(frame, text="Variable Aditiva", padx=50).grid(row=0, column=3)
Entry(frame, textvariable=sumando).grid(row=1, column=3)
Label(frame, text="Modulo", padx=50).grid(row=0, column=4)
Entry(frame, textvariable=modulo).grid(row=1, column=4)

def GenerarNumerosMixta():

    x = int(semilla.get())
    ai = int(multiplo.get())
    c = int(sumando.get())
    m = int(modulo.get())

    if()
    
    raiz2=Tk()

    raiz2.title("Numeros generados")

    frame2=Frame(raiz2)

    frame2.pack()

    Label(frame2, text="X", padx=50).grid(row=0, column=1)
    Label(frame2, text="A", padx=50).grid(row=0, column=2)
    Label(frame2, text="C", padx=50).grid(row=0, column=3)
    Label(frame2, text="M", padx=50).grid(row=0, column=4)
    Label(frame2, text=x, padx=50).grid(row=1, column=1)
    Label(frame2, text=ai, padx=50).grid(row=1, column=2)
    Label(frame2, text=c, padx=50).grid(row=1, column=3)
    Label(frame2, text=m, padx=50).grid(row=1, column=4)

    for b in range(1, m+1):

        Label(frame2, text=b, padx=50).grid(row=b+1, column=0)
        

        a = ((ai*x) + c)
        x = a%m

        Label(frame2, text=x, padx=50).grid(row=b+1, column=1)
        Label(frame2, text=a, padx=50).grid(row=b+1, column=2)
    
botonGenerar=Button(frame, text="Generar", command=lambda:GenerarNumerosMixta()).grid(row = 3, column=2)

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


    raiz2=Tk()

    raiz2.title("Numeros generados")

    frame2=Frame(raiz2)

    frame2.pack()

    Label(frame2, text="X", padx=50).grid(row=0, column=1)
    Label(frame2, text="A", padx=50).grid(row=0, column=2)
    Label(frame2, text="M", padx=50).grid(row=0, column=4)
    Label(frame2, text=x2, padx=50).grid(row=1, column=1)
    Label(frame2, text=ai2, padx=50).grid(row=1, column=2)
    Label(frame2, text=m2, padx=50).grid(row=1, column=4)

    for b in range(1, m2+1):

        Label(frame2, text=b, padx=50).grid(row=b+1, column=0)
        

        a = ((ai2*x2))
        x2 = a%m2

        Label(frame2, text=x2, padx=50).grid(row=b+1, column=1)
        Label(frame2, text=a, padx=50).grid(row=b+1, column=2)
    

botonGenerar=Button(frame3, text="Generar", command=lambda:GenerarNumerosMultiplicativa()).grid(row= 3 , column=2)

pestanas.add(frame, text="Formula Congruencial Mixta")
pestanas.add(frame3, text="Formula Congruencial Multiplicativa")

raiz.mainloop()




