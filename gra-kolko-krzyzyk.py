# Gra w Kółko i Krzyżyk - wersja z komentarzami dla uczniów

# Importujemy potrzebne biblioteki
import tkinter as tk  # Biblioteka do tworzenia okienek i przycisków
from tkinter import messagebox  # Do wyświetlania okienek z komunikatami
import random  # Do losowego wyboru ruchu komputera

# Tworzymy główne okienko gry
root = tk.Tk()
root.title("Kółko i krzyżyk")  # Tytuł okienka
root.geometry("294x340")  # Rozmiar okienka (szerokość x wysokość)

# ZMIENNE GLOBALNE - przechowują ważne informacje o grze
obecny_gracz = "X"  # Który gracz ma teraz ruch (zaczynamy od X)
tryb_gry = ""  # Czy gramy przeciwko komputerowi czy innemu graczowi
znak_gracza = "X"  # Znak człowieka (zawsze X)
znak_komputera = "O"  # Znak komputera (zawsze O)
kolor_domyslny = "lightgray"  # Szary kolor pustych przycisków
gra_trwa = True  # Czy gra się jeszcze toczy (blokuje ruchy po końcu gry)
statystyki = {"X": 0, "O": 0, "Remis": 0}  # Ile razy wygrał X, O lub był remis

# FUNKCJA: Wybór trybu gry
def wybierz_tryb():
    """Pyta gracza, czy chce grać przeciwko komputerowi czy innemu człowiekowi"""
    global tryb_gry  # Używamy globalnej zmiennej
    # Pokazujemy okienko z pytaniem
    wybor = messagebox.askquestion("Wybór trybu", "Czy chcesz grać przeciwko komputerowi?")
    if wybor == "yes":  # Jeśli gracz kliknął "Tak"
        tryb_gry = "komputer"
    else:  # Jeśli gracz kliknął "Nie"
        tryb_gry = "gracz"

# FUNKCJA: Aktualizacja wyświetlania kolejki
def zaktualizuj_kolej(): 
    """Pokazuje na ekranie, czyja jest teraz kolej"""
    label_kolej.config(text=f"Kolej gracza: {obecny_gracz}")

# FUNKCJA: Aktualizacja wyświetlania statystyk
def zaktualizuj_statystyki():
    """Pokazuje na ekranie aktualny wynik (ile razy kto wygrał)"""
    label_statystyki.config(
        text=f"X: {statystyki['X']}   O: {statystyki['O']}   Remisy: {statystyki['Remis']}"
    )

# FUNKCJA: Wykonanie ruchu gracza
def zrob_ruch(przycisk):
    """
    Główna funkcja gry - wykonuje ruch gdy gracz kliknie przycisk
    przycisk - który przycisk został kliknięty
    """
    global obecny_gracz, gra_trwa  # Używamy globalnych zmiennych
    
    # Sprawdzamy, czy można wykonać ruch
    if not gra_trwa or przycisk["text"] != "":  # Jeśli gra skończona lub pole zajęte
        return  # Nie robimy nic i wychodzimy z funkcji

    # Wstawiamy znak gracza (X lub O) w kliknięte pole
    przycisk["text"] = obecny_gracz
    
    # Sprawdzamy, czy ktoś wygrał
    if sprawdz_wygrana():
        # Pokazujemy komunikat o wygranej
        messagebox.showinfo("Koniec gry", f"Gracz {obecny_gracz} wygrał!")
        # Dodajemy punkt do statystyk
        statystyki[obecny_gracz] += 1
        zaktualizuj_statystyki()
        gra_trwa = False  # Kończymy grę
    
    # Sprawdzamy, czy jest remis (wszystkie pola zajęte, nikt nie wygrał)
    elif czy_remis():
        messagebox.showinfo("Koniec gry", "Remis")
        statystyki["Remis"] += 1  # Dodajemy punkt za remis
        zaktualizuj_statystyki()
        gra_trwa = False  # Kończymy grę
    
    # Jeśli gra trwa dalej
    else:
        # Zmieniamy gracza na przeciwnego
        obecny_gracz = "O" if obecny_gracz == "X" else "X"
        zaktualizuj_kolej()  # Odświeżamy wyświetlanie kolejki
        
        # Jeśli teraz kolej komputera, wykonujemy jego ruch
        if tryb_gry == "komputer" and obecny_gracz == znak_komputera:
            # Czekamy pół sekundy żeby ruch wyglądał naturalniej
            root.after(500, ruch_komputera)

# FUNKCJA: Ruch komputera
def ruch_komputera():
    """Komputer wybiera losowe wolne pole i wykonuje ruch"""
    # Lista wszystkich przycisków na planszy
    wszystkie_przyciski = [button1, button2, button3, button4, button5, 
                          button6, button7, button8, button9]
    
    # Znajdźmy wszystkie wolne pola (bez X ani O)
    wolne_przyciski = []
    for przycisk in wszystkie_przyciski:
        if przycisk["text"] == "":  # Jeśli pole puste
            wolne_przyciski.append(przycisk)  # Dodajemy do listy wolnych
    
    # Jeśli są wolne pola
    if wolne_przyciski:
        # Wybieramy losowo jedno z wolnych pól
        ruch = random.choice(wolne_przyciski)
        # Wykonujemy ruch komputera
        zrob_ruch(ruch)

# FUNKCJA: Sprawdzenie remisu
def czy_remis():
    """Sprawdza, czy wszystkie pola są zajęte (remis)"""
    # Jeśli wszystkie 9 pól ma jakiś znak (nie są puste)
    if (button1["text"] != "" and button2["text"] != "" and button3["text"] != "" and 
        button4["text"] != "" and button5["text"] != "" and button6["text"] != "" and 
        button7["text"] != "" and button8["text"] != "" and button9["text"] != ""):
        return True  # To jest remis
    else:
        return False  # Jeszcze nie remis

# FUNKCJA: Reset gry
def reset_gry():
    """Rozpoczyna nową grę - czyści planszę i resetuje wszystko"""
    global obecny_gracz, gra_trwa  # Używamy globalnych zmiennych
    
    gra_trwa = True  # Włączamy możliwość gry
    # Lista wszystkich przycisków
    wszystkie_przyciski = [button1, button2, button3, button4, button5,
                          button6, button7, button8, button9]
    obecny_gracz = "X"  # Zaczynamy od gracza X
    
    # Czyścimy wszystkie przyciski
    for przycisk in wszystkie_przyciski:
        przycisk.config(text="", bg=kolor_domyslny)  # Usuwamy tekst i przywracamy szary kolor
    
    # Odświeżamy wyświetlanie
    label_kolej.config(text=f"Tura gracza: {obecny_gracz}")
    zaktualizuj_statystyki()

# FUNKCJA: Sprawdzenie wygranej
def sprawdz_wygrana():
    """
    Sprawdza wszystkie możliwe kombinacje wygrywające:
    - 3 wiersze poziome
    - 3 kolumny pionowe  
    - 2 przekątne
    """
    
    # SPRAWDZAMY WIERSZE (poziomo)
    # Pierwszy wiersz: pola 1-2-3
    if button1["text"] == button2["text"] == button3["text"] != "":
        # Zaznaczamy wygrywające pola na zielono
        button1.config(bg="lightgreen")
        button2.config(bg="lightgreen")
        button3.config(bg="lightgreen")
        return True
    
    # Drugi wiersz: pola 4-5-6
    elif button4["text"] == button5["text"] == button6["text"] != "":
        button4.config(bg="lightgreen")
        button5.config(bg="lightgreen")
        button6.config(bg="lightgreen")
        return True
    
    # Trzeci wiersz: pola 7-8-9
    elif button7["text"] == button8["text"] == button9["text"] != "":
        button7.config(bg="lightgreen")
        button8.config(bg="lightgreen")
        button9.config(bg="lightgreen")
        return True
    
    # SPRAWDZAMY KOLUMNY (pionowo)
    # Pierwsza kolumna: pola 1-4-7
    elif button1["text"] == button4["text"] == button7["text"] != "":
        button1.config(bg="lightgreen")
        button4.config(bg="lightgreen")
        button7.config(bg="lightgreen")
        return True
    
    # Druga kolumna: pola 2-5-8
    elif button2["text"] == button5["text"] == button8["text"] != "":
        button2.config(bg="lightgreen")
        button5.config(bg="lightgreen")
        button8.config(bg="lightgreen")
        return True
    
    # Trzecia kolumna: pola 3-6-9
    elif button3["text"] == button6["text"] == button9["text"] != "":
        button3.config(bg="lightgreen")
        button6.config(bg="lightgreen")
        button9.config(bg="lightgreen")
        return True
    
    # SPRAWDZAMY PRZEKĄTNE
    # Przekątna z lewego górnego do prawego dolnego: pola 1-5-9
    elif button1["text"] == button5["text"] == button9["text"] != "":
        button1.config(bg="lightgreen")
        button5.config(bg="lightgreen")
        button9.config(bg="lightgreen")
        return True
    
    # Przekątna z prawego górnego do lewego dolnego: pola 3-5-7
    elif button3["text"] == button5["text"] == button7["text"] != "":
        button3.config(bg="lightgreen")
        button5.config(bg="lightgreen")
        button7.config(bg="lightgreen")
        return True
    
    # Jeśli żadna kombinacja nie wygrała
    return False

# ===== TWORZENIE INTERFEJSU UŻYTKOWNIKA =====

# Tytuł gry u góry okienka
tytul = tk.Label(root, text="Gra - Kółko i krzyżyk", font=("Arial", 16))
tytul.grid(row=0, column=0, columnspan=3)  # Rozciąga się przez 3 kolumny

# Label pokazujący czyja jest kolej
label_kolej = tk.Label(root, text=f"Tura gracza: {obecny_gracz}", font=("Arial", 12))
label_kolej.grid(row=1, column=0, columnspan=3)

# PRZYCISKI PLANSZY - układamy je w siatkę 3x3
# Pierwszy rząd przycisków
button1 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, 
                   bg=kolor_domyslny, command=lambda: zrob_ruch(button1))
button1.grid(row=2, column=0)  # Pozycja: rząd 2, kolumna 0

button2 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, 
                   bg=kolor_domyslny, command=lambda: zrob_ruch(button2))
button2.grid(row=2, column=1)  # Pozycja: rząd 2, kolumna 1

button3 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, 
                   bg=kolor_domyslny, command=lambda: zrob_ruch(button3))
button3.grid(row=2, column=2)  # Pozycja: rząd 2, kolumna 2

# Drugi rząd przycisków
button4 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, 
                   bg=kolor_domyslny, command=lambda: zrob_ruch(button4))
button4.grid(row=3, column=0)

button5 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, 
                   bg=kolor_domyslny, command=lambda: zrob_ruch(button5))
button5.grid(row=3, column=1)

button6 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, 
                   bg=kolor_domyslny, command=lambda: zrob_ruch(button6))
button6.grid(row=3, column=2)

# Trzeci rząd przycisków
button7 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, 
                   bg=kolor_domyslny, command=lambda: zrob_ruch(button7))
button7.grid(row=4, column=0)

button8 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, 
                   bg=kolor_domyslny, command=lambda: zrob_ruch(button8))
button8.grid(row=4, column=1)

button9 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, 
                   bg=kolor_domyslny, command=lambda: zrob_ruch(button9))
button9.grid(row=4, column=2)

# Przycisk do resetowania gry
przycisk_reset = tk.Button(root, text="Resetuj grę", font=("Arial", 12), command=reset_gry)
przycisk_reset.grid(row=5, column=0, columnspan=3)

# Label pokazujący statystyki (wyniki)
label_statystyki = tk.Label(root, text=f"X: {statystyki['X']}   O: {statystyki['O']}   Remisy: {statystyki['Remis']}", 
                           font=("Arial", 10))
label_statystyki.grid(row=6, column=0, columnspan=3)

# ===== START PROGRAMU =====
wybierz_tryb()  # Na początku pytamy o tryb gry
root.mainloop()  # Uruchamiamy główną pętlę programu (okienko czeka na kliknięcia)