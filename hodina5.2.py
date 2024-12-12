import tkinter as tk
from random import randint

root = tk.Tk()
root.title("Preteky lopticiek")

platno = tk.Canvas(width=400, height=600, bg="lightblue")
platno.pack()

lopticky = []

def Start():
    Nakresli_lopticky()
    Hra()

def Nakresli_lopticky():
    posun = 10
    for i in range(10):
        lopticka = platno.create_oval(posun, 10, 20 + posun, 30, fill="red")
        lopticky.append(lopticka)
        posun += 30

def Hra():
    for lopticka in lopticky:
        platno.move(lopticka, 0, 10)
        
    platno.after(100, Hra)

randint(1,10)

Start()
