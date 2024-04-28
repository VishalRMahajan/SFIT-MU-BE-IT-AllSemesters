import tkinter as tk

def oval(event):
    canvas.create_oval(event.x, event.y, event.x+50, event.y+50, fill="green")

def rectangle(event):
    canvas.create_rectangle(event.x, event.y, event.x+50, event.y+30, fill="blue")

root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack()

canvas.bind("<Button-1>", oval)
canvas.bind("<Button-3>", rectangle)

root.mainloop()
