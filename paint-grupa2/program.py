import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title("Paint")
root.geometry("600x700")

current_color = "black"
def draw(event):
    size = 5

    x1 = event.x - size
    y1 = event.y - size
    x2 = event.x + size
    y2 = event.y + size
    canvas.create_oval(x1,y1,x2,y2, fill=current_color, outline=current_color)
def choose_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color
def use_eraser():
    global current_color
    current_color = "white"

canvas = tk.Canvas(root,bg="white",width=500,height=500)
canvas.pack(pady=20)

canvas.bind("<B1-Motion>",draw)
color_button = tk.Button(root, text="Wybierz kolor!", command=choose_color )
color_button.pack()
eraser_button = tk.Button(root, text="Gumka", command=use_eraser )
eraser_button.pack()
size_slider = tk.Scale(root,from_=1,to=30)
size_slider.pack()
root.mainloop()