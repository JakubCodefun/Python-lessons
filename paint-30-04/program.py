import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title("Paint")
root.geometry("600x700")

current_color = "black"
drawing_mode = "brush"
start_x = None
start_y = None
def set_mode(mode):
    global drawing_mode
    drawing_mode = mode
def start_draw(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y
def draw(event):
    global start_x, start_y
    size = size_slider.get()
    if(drawing_mode == "brush"):
        x1 = event.x - size
        y1 = event.y - size
        x2 = event.x + size
        y2 = event.y + size
        canvas.create_oval(x1,y1,x2,y2, fill=current_color, outline=current_color)
    elif(drawing_mode== "line"):
        canvas.delete("preview")
        canvas.create_line(start_x,start_y, event.x, event.y,fill=current_color, width=size, tags="preview")
        
    elif(drawing_mode== "rectangle"):
        canvas.delete("preview")
        canvas.create_rectangle(start_x,start_y, event.x, event.y,outline=current_color, width=size, tags="preview")
def change_backgroud():
    color = colorchooser.askcolor()[1]
    if color:
        canvas.config(bg=color)
def end_draw(event):
    global start_x, start_y
    size = size_slider.get()
    if(drawing_mode=="line"):
        canvas.delete("preview")
        canvas.create_line(start_x,start_y, event.x, event.y,fill=current_color, width=size)
    elif(drawing_mode == "rect"):
        canvas.delete("preview")
        canvas.create_rectangle(start_x,start_y, event.x, event.y,outline=current_color, width=size)
def choose_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color
def use_eraser():
    global current_color
    current_color = "white"
def clear():
    canvas.delete("all")

canvas = tk.Canvas(root,bg="white",width=500,height=500)
canvas.grid(row=2, column=0,padx=10,pady=10,columnspan=7)

# canvas.bind("<B1-Motion>",draw)

canvas.bind("<Button-1>", start_draw) # wykonaj na klikniecie przycisku 1 myszki
canvas.bind("<B1-Motion>", draw) #gdy przytrzymamy przycisk 1 myszki
canvas.bind("<ButtonRelease-1>", end_draw) #gdy puscimy przycisk 1 myszki
color_button = tk.Button(root, text="Wybierz kolor!", command=choose_color )
color_button.grid(row=1, column=0)
eraser_button = tk.Button(root, text="Gumka", command=use_eraser )
eraser_button.grid(row=1, column=1)
size_slider = tk.Scale(root,from_=1,to=30, orient="horizontal", label="Grubosc pedzla")
size_slider.grid(row=1, column=2)
delete_button = tk.Button(root,text="Usun wszystko",command=clear)
delete_button.grid(row=1, column=3)
brush_button = tk.Button(root, text="Pędzel", command=lambda: set_mode("brush"))
brush_button.grid(row=1, column=4)
line_button = tk.Button(root, text="Linia", command=lambda: set_mode("line"))
line_button.grid(row=1, column=5)
rec_button = tk.Button(root, text="Prostokat", command=lambda: set_mode("rectangle"))
rec_button.grid(row=1, column=6)
bg_button = tk.Button(root, text="tło", command=change_backgroud)
bg_button.grid(row=1, column=7)
root.mainloop()
