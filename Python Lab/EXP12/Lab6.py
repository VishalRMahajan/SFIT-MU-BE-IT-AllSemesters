from tkinter.filedialog import askopenfile
from tkinter import *
top = Tk()
top.geometry("100x100")
def show():
   filename = askopenfile()
   print(filename)
Openfile = Label(top, text = "Openfile:").place(x = 10, y = 50)  
B = Button(top, text ="Click", command = show)
B.place(x=75,y=50)
top.mainloop()
