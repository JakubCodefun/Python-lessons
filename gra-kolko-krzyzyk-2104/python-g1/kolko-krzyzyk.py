import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Gra kolko i krzyzyk")
root.geometry("300x350")

aktualny_gracz = "X"

def zrob_ruch(przycisk):
    global aktualny_gracz
    if przycisk["text"] == "":
        przycisk["text"] = aktualny_gracz

        if sprawdz_wygrana():
            messagebox.showinfo("Wygrał:", aktualny_gracz)
        elif czy_remis():
                
        else:
            if aktualny_gracz == "X":
                aktualny_gracz = "O"
            elif aktualny_gracz == "O":
                aktualny_gracz = "X"
def czy_remis():
    if(button1["text"] != "" and button2["text"] != "" and button3["text"] != "" and button4["text"] != "" and button5["text"] != "" 
       and button6["text"] != "" and button7["text"] != "" and button8["text"] != "" and button9["text"] != ""):
        return True
    else:
        return False
def sprawdz_wygrana():
    #sprawdzanie wierszy
    if(button1["text"] == button2["text"]== button3["text"] != ""):
        return True
    elif(button4["text"] == button5["text"]== button6["text"] != ""):
        return True
    elif(button7["text"] == button8["text"]== button9["text"] != ""):
        return True
    #sprawdzanie kolumn
    elif(button1["text"] == button4["text"]== button7["text"] != ""):
        return True
    elif(button2["text"] == button5["text"]== button8["text"] != ""):
        return True
    elif(button3["text"] == button6["text"]== button9["text"] != ""):
        return True
    #sprawdzenie na ukos
    elif(button1["text"] == button5["text"]== button9["text"] != ""):
        return True
    elif(button3["text"] == button5["text"]== button9["text"] != ""):
        return True
title = tk.Label(root, text="Kółko i krzyżyk", font=("Arial", 16))
title.grid(row=0, column=0,columnspan=3)

button1 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command= lambda:  zrob_ruch(button1))
button1.grid(row=1,column=0)
button2 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command= lambda:  zrob_ruch(button2))
button2.grid(row=1,column=1)
button3 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command= lambda:  zrob_ruch(button3))
button3.grid(row=1,column=2)
button4 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command= lambda:  zrob_ruch(button4))
button4.grid(row=2,column=0)
button5 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command= lambda:  zrob_ruch(button5))
button5.grid(row=2,column=1)
button6 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command= lambda:  zrob_ruch(button6))
button6.grid(row=2,column=2)
button7 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command= lambda:  zrob_ruch(button7))
button7.grid(row=3,column=0)
button8 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command= lambda:  zrob_ruch(button8))
button8.grid(row=3,column=1)
button9 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command= lambda:  zrob_ruch(button9))
button9.grid(row=3,column=2)


root.mainloop()