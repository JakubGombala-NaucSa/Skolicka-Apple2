import tkinter as tk

root = tk.Tk()
root.title("Preteky lopticiek")

platno = tk.Canvas(width=400, height=600, bg="lightblue")
platno.pack()

lopticky = []

def Start():
    Nakresli_lopticky()

def Nakresli_lopticky():
    for i in range(10):
        lopticka = platno.create_oval(10 + 20*i, 10, 30 + 20*i, 30, fill="red")
        lopticky.append(lopticka)

Start()
