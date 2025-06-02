import tkinter as tk
from tkinter import colorchooser
from tkinter import messagebox

root = tk.Tk()
root.title("Zmiana koloru")
root.geometry("350x350")

def wybierzKolorTla():
    kolor = colorchooser.askcolor()[1]
    if kolor:
        root.config(bg=kolor)
        etykieta.config(bg=kolor)
    
def wybierzKolorTekstu():
    kolor = colorchooser.askcolor()[1]
    if kolor:
        etykieta.config(fg=kolor)


def zmienRozmiar(rozmiar):
    etykieta.config(font=("Arial", rozmiar))

def reset():
    # root.config(bg="SystemButtonFace")
    powiadomienie()
   
    etykieta.config(fg="black", font=("Arial", 14))

def wpisz():
    nowy_tekst = entry.get()
    etykieta.config(text=nowy_tekst)

def powiadomienie():
    messagebox.showinfo("Wazne info!!!!!!!", "Milego dzionka!")

etykieta = tk.Label(root, text="Witaj! Kliknij przyciski!", font=("Arial", 14))
etykieta.pack(pady=20)

entry = tk.Entry(root)
entry.pack(pady=5)

przycisk_entry = tk.Button(root, text="Wpisz tekst", command=wpisz)
przycisk_entry.pack(pady=5)
przycisk_tlo = tk.Button(root, text="Zmien kolor tla!", command=wybierzKolorTla)
przycisk_tlo.pack(pady=5)

przycisk_tekst = tk.Button(root, text="Zmien kolor tekstu!", command=wybierzKolorTekstu)
przycisk_tekst.pack(pady=5)

przycisk_zmniejsz = tk.Button(root, text="Zmniejsz tekst!", command= lambda: zmienRozmiar(7))
przycisk_zmniejsz.pack(pady=5)

przycisk_zwieksz = tk.Button(root, text="Zwieksz tekst!" , command= lambda: zmienRozmiar(30))
przycisk_zwieksz.pack(pady=5)

przycisk_reset = tk.Button(root, text="Resetuj!", command=reset)
przycisk_reset.pack(pady=5)


root.mainloop()


