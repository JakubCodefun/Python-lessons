import tkinter as tk
import random

# Funkcja do wyboru przez komputer
def komputer_wybiera():
    return random.choice(["kamień", "papier", "nożyczki"])

# Funkcja, która ocenia wynik gry
def ocena_wyniku(gracz, komputer):
    if gracz == komputer:
        return "Remis!"
    elif (gracz == "kamień" and komputer == "nożyczki") or \
         (gracz == "papier" and komputer == "kamień") or \
         (gracz == "nożyczki" and komputer == "papier"):
        return "Wygrałeś!"
    else:
        return "Przegrałeś!"

# Funkcja do kliknięcia przycisku przez gracza
def wybierz(opcja):
    global gracz_punkty, komputer_punkty
    
    komputer_opcja = komputer_wybiera()
    wynik = ocena_wyniku(opcja, komputer_opcja)
    
    if wynik == "Wygrałeś!":
        gracz_punkty += 1
    elif wynik == "Przegrałeś!":
        komputer_punkty += 1

    wynik_label.config(text=f"Twój wybór: {opcja}\nWybór komputera: {komputer_opcja}\n{wynik}")
    punkty_label.config(text=f"Twoje punkty: {gracz_punkty} | Punkty komputera: {komputer_punkty}")

# Tworzenie okna głównego
root = tk.Tk()
root.title("Papier, Kamień, Nożyczki")

# Zmienna punktów
gracz_punkty = 0
komputer_punkty = 0

# Nagłówek
naglowek = tk.Label(root, text="Wybierz: Kamień, Papier, Nożyczki", font=("Arial", 16))
naglowek.grid(row=0, column=0, columnspan=3, pady=10)

# Etykieta wynikowa
wynik_label = tk.Label(root, text="Wynik: ", font=("Arial", 14))
wynik_label.grid(row=1, column=0, columnspan=3, pady=10)

# Etykieta punktów
punkty_label = tk.Label(root, text="Twoje punkty: 0 | Punkty komputera: 0", font=("Arial", 14))
punkty_label.grid(row=2, column=0, columnspan=3, pady=10)

# Przycisk do wyboru kamienia
kamien_button = tk.Button(root, text="Kamień", font=("Arial", 14), command=lambda: wybierz("kamień"))
kamien_button.grid(row=3, column=0, padx=10)

# Przycisk do wyboru papieru
papier_button = tk.Button(root, text="Papier", font=("Arial", 14), command=lambda: wybierz("papier"))
papier_button.grid(row=3, column=1, padx=10)

# Przycisk do wyboru nożyczek
nozyczki_button = tk.Button(root, text="Nożyczki", font=("Arial", 14), command=lambda: wybierz("nożyczki"))
nozyczki_button.grid(row=3, column=2, padx=10)

# Uruchomienie aplikacji
root.mainloop()
