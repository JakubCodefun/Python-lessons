# Aplikacja Paint - program do rysowania z komentarzami dla uczniów

# Importujemy potrzebne biblioteki
import tkinter as tk  # Główna biblioteka do tworzenia okienek
from tkinter import colorchooser, simpledialog  # Do wyboru kolorów i wpisywania tekstu

# Tworzymy główne okienko aplikacji
root = tk.Tk()
root.title("Paint")  # Tytuł okienka
root.geometry("1920x1080")  # Rozmiar okienka (bardzo duży - prawie cały ekran)

# ZMIENNE GLOBALNE - przechowują ważne informacje o programie
current_color = "black"  # Aktualny kolor rysowania (zaczynamy od czarnego)

# Tworzymy obszar do rysowania (płótno)
canvas = tk.Canvas(root, bg="white", width=1920, height=720)  # Białe tło, duży rozmiar

# Zmienne kontrolujące tryb rysowania
mode = "brush"  # Aktualny tryb: "brush", "line", "rect", "oval", "triangle", "text"
start_x = None  # Pozycja X gdzie zaczęliśmy rysować
start_y = None  # Pozycja Y gdzie zaczęliśmy rysować
drawn_objects = []  # Lista wszystkich narysowanych objektów (do funkcji cofnij)

# FUNKCJA: Zmiana trybu rysowania
def set_mode(option_mode):
    """
    Zmienia tryb rysowania (pędzel, linia, prostokąt, koło itp.)
    option_mode - nowy tryb do ustawienia
    """
    global mode  # Używamy globalnej zmiennej
    mode = option_mode

# FUNKCJA: Rozpoczęcie rysowania
def start_draw(event):
    """
    Wywoływana gdy klikniemy lewym przyciskiem myszy
    Zapamiętuje pozycję gdzie zaczęliśmy rysować
    event - informacje o kliknięciu (pozycja myszy)
    """
    global start_x, start_y  # Używamy globalnych zmiennych
    start_x = event.x  # Pozycja X myszy
    start_y = event.y  # Pozycja Y myszy

# FUNKCJA: Rysowanie podczas ruchu myszy
def draw(event):
    """
    Wywoływana gdy ruszamy myszą z wciśniętym przyciskiem
    Rysuje w zależności od wybranego trybu
    event - aktualna pozycja myszy
    """
    global start_x, start_y  # Używamy globalnych zmiennych
    size = size_slider.get()  # Pobieramy aktualną grubość z suwaka
    
    # TRYB PĘDZLA - rysuje małe kółka tam gdzie poruszamy myszą
    if mode == "brush":
        # Obliczamy pozycje kółka (środek w pozycji myszy)
        x1 = event.x - size  # Lewa strona kółka
        y1 = event.y - size  # Górna strona kółka
        x2 = event.x + size  # Prawa strona kółka
        y2 = event.y + size  # Dolna strona kółka
        # Rysujemy wypełnione kółko
        obj = canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color)
        drawn_objects.append(obj)  # Dodajemy do listy (żeby móc cofnąć)
    
    # TRYB LINII - pokazuje podgląd linii podczas rysowania
    elif mode == "line":
        canvas.delete("preview")  # Usuwamy poprzedni podgląd
        # Rysujemy linię od punktu startowego do aktualnej pozycji myszy
        canvas.create_line(start_x, start_y, event.x, event.y, 
                          fill=current_color, width=size, tags="preview")
    
    # TRYB PROSTOKĄTA - pokazuje podgląd prostokąta
    elif mode == "rect":
        canvas.delete("preview")  # Usuwamy poprzedni podgląd
        # Rysujemy prostokąt od punktu startowego do aktualnej pozycji
        canvas.create_rectangle(start_x, start_y, event.x, event.y, 
                               outline=current_color, width=size, tags="preview")
    
    # TRYB KOŁA/OWALU - pokazuje podgląd koła
    elif mode == "oval":
        canvas.delete("preview")  # Usuwamy poprzedni podgląd
        # Rysujemy owal od punktu startowego do aktualnej pozycji
        canvas.create_oval(start_x, start_y, event.x, event.y, 
                          outline=current_color, width=size, tags="preview")
    
    # TRYB TRÓJKĄTA - pokazuje podgląd trójkąta
    elif mode == "triangle":
        canvas.delete("preview")  # Usuwamy poprzedni podgląd
        # Obliczamy pozycje wierzchołków trójkąta
        x1 = start_x  # Lewy dolny wierzchołek
        y1 = start_y  # Górny wierzchołek
        x2 = event.x  # Prawy dolny wierzchołek
        y2 = event.y  # Dolna linia
        x3 = (x1 + x2) / 2  # Środek górnego wierzchołka
        # Rysujemy trójkąt używając trzech punktów
        canvas.create_polygon(x3, y1, x1, y2, x2, y2, 
                             outline=current_color, fill="", width=size, tags="preview")

# FUNKCJA: Zakończenie rysowania
def end_draw(event):
    """
    Wywoływana gdy puszczamy przycisk myszy
    Kończy rysowanie figury i zapisuje ją na stałe
    event - pozycja gdzie zakończyliśmy rysowanie
    """
    global start_x, start_y  # Używamy globalnych zmiennych
    size = size_slider.get()  # Pobieramy grubość
    
    # ZAKOŃCZENIE RYSOWANIA LINII
    if mode == "line":
        canvas.delete("preview")  # Usuwamy podgląd
        # Rysujemy ostateczną linię
        obj = canvas.create_line(start_x, start_y, event.x, event.y, 
                                fill=current_color, width=size)
        drawn_objects.append(obj)  # Dodajemy do listy objektów
        print(drawn_objects)  # Wypisujemy listę (do debugowania)
    
    # ZAKOŃCZENIE RYSOWANIA PROSTOKĄTA
    elif mode == "rect":
        canvas.delete("preview")  # Usuwamy podgląd
        # Rysujemy ostateczny prostokąt
        obj = canvas.create_rectangle(start_x, start_y, event.x, event.y, 
                                     outline=current_color, width=size)
        drawn_objects.append(obj)  # Dodajemy do listy
        print(drawn_objects)
    
    # ZAKOŃCZENIE RYSOWANIA KOŁA
    elif mode == "oval":
        canvas.delete("preview")  # Usuwamy podgląd
        # Rysujemy ostateczne koło
        obj = canvas.create_oval(start_x, start_y, event.x, event.y, 
                                outline=current_color, width=size)
        drawn_objects.append(obj)  # Dodajemy do listy
        print(drawn_objects)
    
    # ZAKOŃCZENIE RYSOWANIA TRÓJKĄTA
    elif mode == "triangle":
        canvas.delete("preview")  # Usuwamy podgląd
        # Obliczamy pozycje wierzchołków (tak samo jak w podglądzie)
        x1 = start_x
        y1 = start_y
        x2 = event.x
        y2 = event.y
        x3 = (x1 + x2) / 2
        # Rysujemy ostateczny trójkąt
        obj = canvas.create_polygon(x3, y1, x1, y2, x2, y2, 
                                   outline=current_color, fill="", width=size)
        drawn_objects.append(obj)  # Dodajemy do listy
        print(drawn_objects)
    
    # TRYB TEKSTU - wyświetla okienko do wpisania tekstu
    elif mode == "text":
        # Pytamy użytkownika o tekst do wpisania
        text_input = simpledialog.askstring("Tekst", "Wpisz tekst:")
        if text_input:  # Jeśli użytkownik wpisał jakiś tekst
            # Umieszczamy tekst w miejscu kliknięcia
            canvas.create_text(event.x, event.y, text=text_input, 
                              fill=current_color, font=("Arial", size))

# FUNKCJA: Wybór koloru
def choose_color():
    """Otwiera okienko wyboru koloru i zmienia aktualny kolor"""
    global current_color  # Używamy globalnej zmiennej
    color = colorchooser.askcolor()[1]  # Otwieramy okienko wyboru koloru
    if color:  # Jeśli użytkownik wybrał kolor (nie anulował)
        current_color = color  # Zmieniamy aktualny kolor

# FUNKCJA: Gumka
def use_eraser():
    """Zmienia kolor na biały (kolor tła) - działa jak gumka"""
    global current_color
    current_color = "white"  # Biały kolor = gumka

# FUNKCJA: Zmiana tła
def change_backgroud():
    """Pozwala zmienić kolor tła płótna"""
    color = colorchooser.askcolor()[1]  # Wybieramy kolor
    if color:  # Jeśli użytkownik wybrał kolor
        canvas.config(bg=color)  # Zmieniamy tło płótna

# FUNKCJA: Usuń wszystko
def delete_all():
    """Czyści całe płótno - usuwa wszystkie rysunki"""
    canvas.delete("all")  # Usuwa wszystkie objekty z płótna

# FUNKCJA: Cofnij ostatni ruch
def undo():
    """Usuwa ostatnio narysowany objekt"""
    if drawn_objects:  # Jeśli lista nie jest pusta
        last_object = drawn_objects.pop()  # Bierzemy ostatni objekt z listy
        canvas.delete(last_object)  # Usuwamy go z płótna
        print(drawn_objects)  # Wypisujemy aktualną listę

# ZMIENNE I FUNKCJE DO CIĄGŁEGO COFANIA (przytrzymanie przycisku)
active_undo = False  # Czy aktualnie cofamy ciągle

def continous_undo():
    """Wykonuje cofanie w pętli dopóki przycisk jest wciśnięty"""
    undo()  # Cofnij jeden element
    if active_undo:  # Jeśli nadal cofamy
        root.after(100, continous_undo)  # Za 100ms wywołaj ponownie

def undo_press():
    """Wywoływana gdy wciśniemy przycisk cofnij"""
    global active_undo
    active_undo = True  # Włączamy tryb ciągłego cofania
    continous_undo()  # Rozpoczynamy cofanie

def undo_release():
    """Wywoływana gdy puszczamy przycisk cofnij"""
    global active_undo
    active_undo = False  # Wyłączamy tryb ciągłego cofania

# ===== TWORZENIE INTERFEJSU UŻYTKOWNIKA =====
# Wszystkie przyciski umieszczamy w pierwszym rzędzie (row=0)

# Przycisk wyboru koloru
color_button = tk.Button(root, text="Zmien kolor!", command=choose_color)
color_button.grid(column=0, row=0, padx=4, pady=4)

# Przycisk gumki
erase_button = tk.Button(root, text="Gumka!", command=use_eraser)
erase_button.grid(column=1, row=0, padx=4, pady=4)

# Suwak do zmiany grubości/rozmiaru
size_slider = tk.Scale(root, from_=1, to=20, orient="horizontal", label="Zmien grubosc")
size_slider.grid(column=2, row=0, padx=4, pady=4)

# Przycisk usuwania wszystkiego
delete_button = tk.Button(root, text="Usun wszystko", command=delete_all)
delete_button.grid(column=3, row=0, padx=4, pady=4)

# Przycisk trybu linii
line_button = tk.Button(root, text="Linia", command=lambda: set_mode("line"))
line_button.grid(column=4, row=0, padx=4, pady=4)

# Przycisk trybu pędzla
brush_button = tk.Button(root, text="Pedzel", command=lambda: set_mode("brush"))
brush_button.grid(column=5, row=0, padx=4, pady=4)

# Przycisk trybu prostokąta
rect_button = tk.Button(root, text="Prostokat", command=lambda: set_mode("rect"))
rect_button.grid(column=6, row=0, padx=4, pady=4)

# Przycisk zmiany tła
bg_button = tk.Button(root, text="Tło", command=change_backgroud)
bg_button.grid(row=0, column=7, padx=4, pady=4)

# Przycisk trybu koła
oval_button = tk.Button(root, text="Kolo", command=lambda: set_mode("oval"))
oval_button.grid(column=8, row=0, padx=4, pady=4)

# Przycisk trybu trójkąta
triangle_button = tk.Button(root, text="Trojkat", command=lambda: set_mode("triangle"))
triangle_button.grid(column=9, row=0, padx=4, pady=4)

# Przycisk cofania
undo_button = tk.Button(root, text="Cofnij", command=undo)
undo_button.grid(column=10, row=0, padx=4, pady=4)

# Przycisk trybu tekstu
text_button = tk.Button(root, text="Tekst", command=lambda: set_mode("text"))
text_button.grid(column=11, row=0, padx=4, pady=4)

# Umieszczamy płótno pod przyciskami (rząd 2, rozciąga się przez wszystkie kolumny)
canvas.grid(row=2, column=0, columnspan=12)

# ===== PODŁĄCZANIE WYDARZEŃ MYSZY =====
# Łączymy ruchy myszy z funkcjami rysowania

canvas.bind("<Button-1>", start_draw)        # Kliknięcie lewym przyciskiem = start rysowania
canvas.bind("<B1-Motion>", draw)             # Ruch myszy z wciśniętym przyciskiem = rysowanie
canvas.bind("<ButtonRelease-1>", end_draw)  # Puszczenie przycisku = koniec rysowania

# Specjalne wydarzenia dla przycisku cofnij (żeby działało ciągłe cofanie)
undo_button.bind("<ButtonPress-1>", lambda e: undo_press())      # Wciśnięcie przycisku
undo_button.bind("<ButtonRelease-1>", lambda e: undo_release())  # Puszczenie przycisku

# ===== START PROGRAMU =====
root.mainloop()  # Uruchamiamy główną pętlę programu
