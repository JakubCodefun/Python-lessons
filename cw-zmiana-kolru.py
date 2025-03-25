import tkinter as tk
from tkinter import colorchooser

# Tworzenie głównego okna
root = tk.Tk()
root.title("Zmiana Koloru")
root.geometry("350x350")

# Funkcja do wyboru koloru tła
def wybierz_kolor_tla():
    kolor = colorchooser.askcolor()[1]  # Pobiera kolor w HEX
    if kolor:
        root.config(bg=kolor)

# Funkcja do wyboru koloru tekstu
def wybierz_kolor_tekstu():
    kolor = colorchooser.askcolor()[1]
    if kolor:
        etykieta.config(fg=kolor)


# Funkcja do zmiany rozmiaru tekstu
def zmien_rozmiar(rozmiar):
    etykieta.config(font=("Arial", rozmiar))

# Tworzenie etykiety
etykieta = tk.Label(root, text="Kliknij przycisk!", font=("Arial", 14))
etykieta.pack(pady=20)

# Przyciski do zmiany tła
przycisk_tlo = tk.Button(root, text="Wybierz kolor tła", command=wybierz_kolor_tla)
przycisk_tlo.pack()

# Przyciski do zmiany koloru tekstu
przycisk_tekst = tk.Button(root, text="Wybierz kolor tekstu", command=wybierz_kolor_tekstu)
przycisk_tekst.pack()



# Przyciski do zmiany rozmiaru tekstu
przycisk_mniejszy = tk.Button(root, text="Mniejszy tekst", command=lambda: zmien_rozmiar(10))
przycisk_mniejszy.pack()

przycisk_wiekszy = tk.Button(root, text="Większy tekst", command=lambda: zmien_rozmiar(20))
przycisk_wiekszy.pack()

# Uruchomienie pętli głównej
root.mainloop()
