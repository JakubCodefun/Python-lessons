import tkinter as tk
import random

# Funkcja rozpoczynająca nową grę
def rozpocznij_nowa_gre():
    global wylosowana_liczba, proby
    wylosowana_liczba = random.randint(1, 100)  # Losujemy liczbę od 1 do 100
    proby = 0
    wynik.config(text="Zgadnij liczbę od 1 do 100")
    pole_wejscia.delete(0, tk.END)
    przycisk_sprawdz.grid(row=2, column=0)  # Przywracamy przycisk "Sprawdź" na miejsce

# Funkcja obsługująca sprawdzenie liczby
def sprawdz_liczbe():
    global proby
    liczba = pole_wejscia.get()
    if liczba.isdigit():
        liczba = int(liczba)
        proby += 1
        if liczba < wylosowana_liczba:
            wynik.config(text="Za mało!")
        elif liczba > wylosowana_liczba:
            wynik.config(text="Za dużo!")
        else:
            wynik.config(text=f"Brawo! Zgadłeś w {proby} próbach!")
            przycisk_sprawdz.grid_forget()  # Usuwamy przycisk "Sprawdź"
    else:
        wynik.config(text="Wpisz liczbę!")

# Tworzenie głównego okna aplikacji
okno = tk.Tk()
okno.title("Zgadnij Liczbę")

# Etykieta z wynikiem
wynik = tk.Label(okno, text="Zgadnij liczbę od 1 do 100", font=("Arial", 14))
wynik.grid(row=0, column=0, columnspan=2, pady=10)

# Pole wejściowe
pole_wejscia = tk.Entry(okno, width=20, font=("Arial", 14))
pole_wejscia.grid(row=1, column=0, columnspan=2, pady=10)

# Przycisk "Sprawdź"
przycisk_sprawdz = tk.Button(okno, text="Sprawdź", command=sprawdz_liczbe, font=("Arial", 12))
przycisk_sprawdz.grid(row=2, column=0)

# Przycisk "Nowa Gra"
przycisk_nowa_gra = tk.Button(okno, text="Nowa Gra", command=rozpocznij_nowa_gre, font=("Arial", 12))
przycisk_nowa_gra.grid(row=2, column=1)

# Rozpoczęcie nowej gry
rozpocznij_nowa_gre()

# Uruchomienie głównej pętli aplikacji
okno.mainloop()
