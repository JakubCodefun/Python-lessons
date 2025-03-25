import tkinter as tk
import random

# Listy słów do generowania zdań
characters = ["Superbohater", "Robot", "Kosmita", "Detektyw", "Czarodziej"]
actions = ["walczy z", "ucieka przed", "szuka", "ściga", "ratuje świat przed"]
places = ["w dżungli", "na księżycu", "w podwodnym mieście", "w zamku", "w labiryncie"]
villains = ["złym czarnoksiężnikiem", "gigantycznym potworem", "armią robotów", "tajemniczym ninja", "geniuszem zła"]
twists = ["ale niespodziewanie traci swoje moce!", "ale nagle pojawia się jego tajemniczy sprzymierzeniec!", 
          "ale portal do innego wymiaru nagle się otwiera!", "ale złoczyńca okazuje się być jego bratem!", 
          "ale sytuacja wymyka się spod kontroli i wszyscy muszą uciekać!"]

colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#FFFF33", "#33FFFF", "#FF9933"]  # Kolory tła
text_colors = ["black", "white", "red", "blue", "green", "purple"]  # Kolory tekstu

# Funkcja losująca zdanie i zmieniająca kolor tła
def generate_sentence():
    hero = entry.get().strip()  
    if not hero:  
        hero = random.choice(characters)
    
    sentence = f"{hero} {random.choice(actions)} {random.choice(villains)} {random.choice(places)}, {random.choice(twists)}"
    label.config(text=sentence)
    
    # Losowa zmiana koloru tła
    root.config(bg=random.choice(colors)) #bg - kolor tla

# Funkcja zmieniająca kolor tekstu
def change_text_color():
    label.config(fg=random.choice(text_colors)) # kolor tekstu

# Tworzenie okna
root = tk.Tk()
root.title("Komiksowy Generator Zdania")
root.geometry("550x350")  

# Siatka - ustawienie kolumn - wysrodkowanie
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Pole do wpisania bohatera
entry_label = tk.Label(root, text="Wpisz własnego bohatera:", font=("Arial", 12))
entry_label.grid(row=0, column=0, columnspan=2, pady=(10, 2))

entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.grid(row=1, column=0, columnspan=2, pady=5)

# Przycisk do generowania
button = tk.Button(root, text="Losuj zdanie", command=generate_sentence, font=("Arial", 12))
button.grid(row=2, column=0, padx=10, pady=10)

# Przycisk do zmiany koloru tekstu
color_button = tk.Button(root, text="Zmień kolor tekstu", command=change_text_color, font=("Arial", 12))
color_button.grid(row=2, column=1, padx=10, pady=10)

# Etykieta na tekst
label = tk.Label(root, text="Kliknij, by wygenerować zdanie!", font=("Arial", 14), wraplength=500, justify="center")
label.grid(row=3, column=0, columnspan=2, pady=20)

# Uruchomienie aplikacji
root.mainloop()
