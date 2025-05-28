import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Kolko i krzyzyk")
root.geometry("300x350")

obecny_gracz = "X"
tryb_gry = ""
znak_gracza = "X"
znak_komputera = "O"

def wybierz_tryb():
    global tryb_gry, znak_gracza, znak_komputera
    wybor = messagebox.askquestion("Wybor trybu","Czy chcesz grac przeciwko komputerowi?")
    print(wybor)
    if(wybor == "yes"):
        tryb_gry = "komputer"
        print(tryb_gry)
    else:
        tryb_gry = "gracz"
        print(tryb_gry)

def zrob_ruch(przycisk):
    global obecny_gracz
    if przycisk["text"] == "":
        przycisk["text"] = obecny_gracz
        if sprawdz_wygrana():
            messagebox.showinfo("Koniec gry", f"Gracz {obecny_gracz} wygrał!")
        elif czy_remis():
            messagebox.showinfo("Koniec gry", "Remis")
        else:
            if(obecny_gracz == "X"):
                obecny_gracz = "O"
            else:
                obecny_gracz = "X"
            if(tryb_gry == "komputer" and obecny_gracz == znak_komputera):
                ruch_komputera()

def ruch_komputera():
    wszystkie_przyciski = [button1,button2,button3,button4,button5,button6,button7,button8,button9]
    wolne_przyciski = []
    for przycisk in wszystkie_przyciski:
        if przycisk["text"] == "":
            wolne_przyciski.append(przycisk)
    if wolne_przyciski:
        ruch = random.choice(wolne_przyciski)
        zrob_ruch(ruch)


def czy_remis():
    if (button1["text"] != "" and button2["text"] != "" and button3["text"] != "" and button4["text"] != "" and button5["text"] != ""
        and button6["text"] != "" and button7["text"] != "" and button8["text"] != "" and button9["text"] != ""):
        return True
    else:
        return False
    

def reset_gry():
    global obecny_gracz
    wszystkie_przyciski = [button1,button2,button3,button4,button5,button6,button7,button8,button9]
    obecny_gracz = "X"
    for przycisk in wszystkie_przyciski:
        przycisk.config(text="")
        
def sprawdz_wygrana():
    #wiersze
    if(button1["text"] == button2["text"] == button3["text"] != ""):
        return True
    elif(button4["text"] == button5["text"] == button6["text"] != ""):
        return True
    elif(button7["text"] == button8["text"] == button9["text"] != ""):
        return True
    
    #kolumny
    elif(button1["text"] == button4["text"] == button7["text"] != ""):
        return True
    elif(button2["text"] == button5["text"] == button8["text"] != ""):
        return True
    elif(button3["text"] == button6["text"] == button9["text"] != ""):
        return True
    #po ukosie
    elif(button1["text"] == button5["text"] == button9["text"] != ""):
        return True
    elif(button3["text"] == button5["text"] == button7["text"] != ""):
        return True
tytul = tk.Label(root, text="Gra - kółko i krzyżyk", font=("Arial", 16))
tytul.grid(row=0, column=0, columnspan=3)

button1 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command= lambda: zrob_ruch(button1))
button1.grid(row=1,column=0)
button2 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command= lambda: zrob_ruch(button2))
button2.grid(row=1,column=1)
button3 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command= lambda: zrob_ruch(button3))
button3.grid(row=1,column=2)
button4 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command= lambda: zrob_ruch(button4))
button4.grid(row=2,column=0)
button5 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command= lambda: zrob_ruch(button5))
button5.grid(row=2,column=1)
button6 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command= lambda: zrob_ruch(button6))
button6.grid(row=2,column=2)
button7 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command= lambda: zrob_ruch(button7))
button7.grid(row=3,column=0)
button8 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command= lambda: zrob_ruch(button8))
button8.grid(row=3,column=1)
button9 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command= lambda: zrob_ruch(button9))
button9.grid(row=3,column=2)

przycisk_reset = tk.Button(root, text="Resetuj gre", font=("Arial", 12), command=reset_gry)
przycisk_reset.grid(row=4, column=0, columnspan=3)
wybierz_tryb()
root.mainloop()