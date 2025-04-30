import tkinter as tk
from tkinter import colorchooser
root = tk.Tk()
root.title("Paint")
root.geometry("600x700")

current_color = "black" 

canvas = tk.Canvas(root, bg="white", width=500, height=500)
tryb = "brush"
start_x = None
start_y = None
def set_mode(mode):
    global tryb
    tryb = mode
def start_draw(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y
def draw(event):
    global  start_x ,start_y
    size = size_slider.get()
    if(tryb == "brush"):
        x1 = event.x - size
        y1 = event.y - size
        x2 = event.x + size
        y2 = event.y + size
        canvas.create_oval(x1,y1,x2,y2, fill=current_color, outline=current_color)
    elif(tryb == "line"):
        canvas.delete("preview")
        canvas.create_line(start_x,start_y,event.x,event.y, fill=current_color,width=size,tags="preview")
    elif(tryb == "rect"):
        canvas.delete("preview")
        canvas.create_rectangle(start_x, start_y,event.x, event.y, outline=current_color,width=size, tags="preview")

def end_draw(event):
    global start_x, start_y
    size = size_slider.get()
    if(tryb == "line"):
        canvas.delete("preview")
        canvas.create_line(start_x,start_y,event.x,event.y,fill=current_color,width=size)
    elif(tryb == "rect"):
        canvas.delete("preview")
        canvas.create_rectangle(start_x,start_y,event.x, event.y,outline=current_color, width=size)
def choose_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color
def use_eraser():
    global current_color
    current_color = "white"
def change_backgroud():
    color = colorchooser.askcolor()[1]
    if color:
        canvas.config(bg=color)
def delete_all():
    canvas.delete("all")

color_button = tk.Button(root, text="Zmien kolor!", command=choose_color)
color_button.grid(column=0, row=0, padx=4, pady=4)
erase_button = tk.Button(root, text="Gumka!", command=use_eraser)
erase_button.grid(column=1, row=0, padx=4, pady=4)
size_slider = tk.Scale(root,from_=1, to=20,orient="horizontal",label="Zmien grubosc")
size_slider.grid(column=2, row=0, padx=4, pady=4)
delete_button = tk.Button(root, text="Usun wszystko", command=delete_all)
delete_button.grid(column=3, row=0, padx=4, pady=4)
line_button = tk.Button(root, text="Linia", command=lambda: set_mode("line"))
line_button.grid(column=4, row=0, padx=4, pady=4)
brush_button = tk.Button(root, text="Pedzel",command=lambda: set_mode("brush"))
brush_button.grid(column=5, row=0, padx=4, pady=4)
rect_button = tk.Button(root, text="Prostokat",command=lambda: set_mode("rect"))
rect_button.grid(column=6, row=0, padx=4, pady=4)
bg_button = tk.Button(root, text="Tło", command=change_backgroud)
bg_button.grid(row=0, column=7, padx=4, pady=4)
canvas.grid(row=2, column=0, columnspan=8)

# canvas.bind("<B1-Motion>",draw)
canvas.bind("<Button-1>", start_draw) # jak klikniemy wykona sie funkcja
canvas.bind("<B1-Motion>", draw ) # jak ruszamy myszka
canvas.bind("<ButtonRelease-1>", end_draw) # jak puscimy przycisk myszy
root.mainloop()
