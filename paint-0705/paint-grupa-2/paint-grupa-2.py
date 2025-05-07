import tkinter as tk
from tkinter import colorchooser
root = tk.Tk()
root.title("Paint")
root.geometry("1920x1080")

current_color = "black" 

canvas = tk.Canvas(root, bg="white", width=1920, height=720)
mode = "brush"
start_x = None
start_y = None
drawn_objects = []

def set_mode(option_mode):
    global mode
    mode = option_mode
def start_draw(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y
def draw(event):
    global  start_x ,start_y
    size = size_slider.get()
    if(mode == "brush"):
        x1 = event.x - size
        y1 = event.y - size
        x2 = event.x + size
        y2 = event.y + size
        canvas.create_oval(x1,y1,x2,y2, fill=current_color, outline=current_color)
    elif(mode == "line"):
        canvas.delete("preview")
        canvas.create_line(start_x,start_y,event.x,event.y, fill=current_color,width=size,tags="preview")
    elif(mode == "rect"):
        canvas.delete("preview")
        canvas.create_rectangle(start_x, start_y,event.x, event.y, outline=current_color,width=size, tags="preview")
    elif(mode == "oval"):
        canvas.delete("preview")
        canvas.create_oval(start_x, start_y, event.x, event.y, outline=current_color, width=size, tags="preview")
    elif(mode == "triangle"):
        canvas.delete("preview")
        x1 = start_x
        y1 = start_y
        x2 = event.x
        y2 = event.y
        x3 = (x1 + x2) / 2
        canvas.create_polygon(x3,y1,x1,y2,x2,y2, outline=current_color,fill="", width=size, tags="preview")

def end_draw(event):
    global start_x, start_y
    size = size_slider.get()
    if(mode == "line"):
        canvas.delete("preview")
        obj = canvas.create_line(start_x,start_y,event.x,event.y,fill=current_color,width=size)
        drawn_objects.append(obj)
        print(drawn_objects)
    elif(mode == "rect"):
        canvas.delete("preview")
        obj = canvas.create_rectangle(start_x,start_y,event.x, event.y,outline=current_color, width=size)
        drawn_objects.append(obj)
        print(drawn_objects)
    elif(mode == "oval"):
        canvas.delete("preview")
        obj = canvas.create_oval(start_x, start_y, event.x, event.y, outline=current_color, width=size)
        drawn_objects.append(obj)
        print(drawn_objects)
    elif(mode == "triangle"):
        canvas.delete("preview")
        x1 = start_x
        y1 = start_y
        x2 = event.x
        y2 = event.y
        x3 = (x1 + x2) / 2
        obj = canvas.create_polygon(x3,y1,x1,y2,x2,y2, outline=current_color,fill="", width=size)
        drawn_objects.append(obj)
        print(drawn_objects)
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
def undo():
    if drawn_objects:
        last_object = drawn_objects.pop()
        canvas.delete(last_object)
        print(drawn_objects)
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
oval_button = tk.Button(root, text="Kolo",command=lambda: set_mode("oval"))
oval_button.grid(column=8, row=0, padx=4, pady=4)
triangle_button = tk.Button(root, text="Trojkat",command=lambda: set_mode("triangle"))
triangle_button.grid(column=9, row=0, padx=4, pady=4)
canvas.grid(row=2, column=0, columnspan=12)


canvas.bind("<Button-1>", start_draw) # jak klikniemy wykona sie funkcja
canvas.bind("<B1-Motion>", draw ) # jak ruszamy myszka
canvas.bind("<ButtonRelease-1>", end_draw) # jak puscimy przycisk myszy
root.mainloop()