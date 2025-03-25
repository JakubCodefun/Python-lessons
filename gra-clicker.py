import tkinter as tk

# Zmienne globalne
licznik = 0
czas_gry = 10  # Czas trwania gry w sekundach
czas_pozostaly = czas_gry
gra_trwa = False

# Funkcja aktualizująca czas
def aktualizuj_czas():
    global czas_pozostaly
    if czas_pozostaly > 0 and gra_trwa:
        czas_pozostaly -= 1
        etykieta_czas.config(text=f"Czas: {czas_pozostaly} s")
        okno.after(1000, aktualizuj_czas)
    else:
        stop()

# Funkcja rozpoczynająca nową grę
def start():
    global licznik, gra_trwa, czas_pozostaly
    licznik = 0
    gra_trwa = True
    czas_pozostaly = czas_gry
    etykieta_licznik.config(text="Kliknięcia: 0")
    etykieta_wynik.config(text="Klikaj jak najszybciej!")
    etykieta_czas.config(text=f"Czas: {czas_pozostaly} s")
    przycisk_klikaj.config(state="normal")
    okno.after(1000, aktualizuj_czas)

# Funkcja zliczająca kliknięcia
def kliknij():
    global licznik
    if gra_trwa:
        licznik += 1
        etykieta_licznik.config(text=f"Kliknięcia: {licznik}")

# Funkcja zatrzymująca grę
def stop():
    global gra_trwa
    gra_trwa = False
    przycisk_klikaj.config(state="disabled")
    etykieta_wynik.config(text=f"Koniec! Twój wynik: {licznik} kliknięć.")

# Tworzenie okna aplikacji
okno = tk.Tk()
okno.title("Clicker")

# Etykieta informująca o wyniku
etykieta_wynik = tk.Label(okno, text="Klikaj jak najszybciej!", font=("Arial", 14))
etykieta_wynik.grid(row=0, column=0, columnspan=2, pady=10)

# Etykieta licznika kliknięć
etykieta_licznik = tk.Label(okno, text="Kliknięcia: 0", font=("Arial", 14))
etykieta_licznik.grid(row=1, column=0, columnspan=2, pady=10)

# Etykieta czasu gry
etykieta_czas = tk.Label(okno, text=f"Czas: {czas_gry} s", font=("Arial", 14))
etykieta_czas.grid(row=2, column=0, columnspan=2, pady=10)

# Przycisk do klikania
przycisk_klikaj = tk.Button(okno, text="Klikaj!", font=("Arial", 14), width=15, height=3, command=kliknij, state="disabled")
przycisk_klikaj.grid(row=3, column=0, columnspan=2, pady=10)

# Przycisk "Nowa Gra"
przycisk_start = tk.Button(okno, text="Nowa Gra", font=("Arial", 12), command=start)
przycisk_start.grid(row=4, column=0, padx=5)

# Przycisk "Stop"
przycisk_stop = tk.Button(okno, text="Stop", font=("Arial", 12), command=stop)
przycisk_stop.grid(row=4, column=1, padx=5)

# Uruchomienie pętli aplikacji
okno.mainloop()

