from tkinter.colorchooser import askcolor
from tkinter import *
top = Tk()
top.geometry("100x100")
def show():
   color = askcolor()
   print(color)
Color = Label(top, text = "Color pallete:").place(x = 5,y = 50)  
B = Button(top, text ="Click", command = show)
B.place(x=100,y=50)
top.mainloop()
