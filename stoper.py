import tkinter as tk

# Zmienne globalne
czas = 0
dziala = False
okrazenia = []

# Funkcja aktualizująca stoper
def aktualizuj_stoper():
    global czas
    if dziala:
        czas += 1
        etykieta_czas.config(text=f"{czas} s")
        okno.after(1000, aktualizuj_stoper)  # Aktualizacja co 1 sekundę

# Funkcja startująca stoper
def start():
    global dziala
    if not dziala:
        dziala = True
        aktualizuj_stoper()

# Funkcja zatrzymująca stoper
def stop():
    global dziala
    dziala = False

# Funkcja resetująca stoper
def reset():
    global czas, dziala, okrazenia
    dziala = False
    czas = 0
    okrazenia = []
    etykieta_czas.config(text="0 s")
    lista_okrazen.config(text="Okrążenia:")

# Funkcja aktualizująca wyświetlaną listę okrążeń
def aktualizuj_liste_okrazen():
    tekst = "Okrążenia:\n"
    numer = 1
    for czas in okrazenia:
        tekst += f"{numer}. {czas} s\n"
        numer += 1
    lista_okrazen.config(text=tekst)

# Funkcja dodająca okrążenie
def dodaj_okrazenie():
    if dziala:
        okrazenia.append(czas)
        aktualizuj_liste_okrazen()

# Tworzenie głównego okna aplikacji
okno = tk.Tk()
okno.title("Stoper")

# Etykieta wyświetlająca czas
etykieta_czas = tk.Label(okno, text="0 s", font=("Arial", 20))
etykieta_czas.grid(row=0, column=0, columnspan=4, pady=10)

# Przycisk "Start"
przycisk_start = tk.Button(okno, text="Start", command=start, font=("Arial", 12))
przycisk_start.grid(row=1, column=0, padx=5)

# Przycisk "Stop"
przycisk_stop = tk.Button(okno, text="Stop", command=stop, font=("Arial", 12))
przycisk_stop.grid(row=1, column=1, padx=5)

# Przycisk "Reset"
przycisk_reset = tk.Button(okno, text="Reset", command=reset, font=("Arial", 12))
przycisk_reset.grid(row=1, column=2, padx=5)

# Przycisk "Dodaj okrążenie"
przycisk_okrazenie = tk.Button(okno, text="Dodaj okrążenie", command=dodaj_okrazenie, font=("Arial", 12))
przycisk_okrazenie.grid(row=1, column=3, padx=5)

# Etykieta do wyświetlania okrążeń
lista_okrazen = tk.Label(okno, text="Okrążenia:", font=("Arial", 12))
lista_okrazen.grid(row=2, column=0, columnspan=4, pady=10)

# Uruchomienie głównej pętli aplikacji
okno.mainloop()

