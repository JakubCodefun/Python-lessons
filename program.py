import tkinter as tk

root = tk.Tk()
root.title("Paint")
root.geometry("600x700")

def draw(event):
    size = 5

    x1 = event.x - size
    y1 = event.y - size
    x2 = event.x + size
    y2 = event.y + size
    canvas.create_oval(x1,y1,x2,y2, fill="black", outline="black")

canvas = tk.Canvas(root,bg="white",width=500,height=500)
canvas.pack(pady=20)
root.mainloop()