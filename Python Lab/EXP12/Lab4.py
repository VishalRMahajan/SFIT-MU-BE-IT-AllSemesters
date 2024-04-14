from tkinter.simpledialog import askinteger
from tkinter.simpledialog import askfloat
from tkinter.simpledialog import askstring
from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("100x100")
#For integer
def show():
   num = askinteger("Input", "Input an Integer")
   print(num)
Integer  = Label(top, text = "Integer:").place(x = 5,y = 50)
B = Button(top, text ="Click", command = show)
B.place(x=50,y=50)
#For float
def show1():
   num = askfloat("Input", "Input a floating point number")
   print(num)
Float  = Label(top, text = "Float:").place(x = 5,y = 80)   
B = Button(top, text ="Click", command = show1)
B.place(x=50,y=80)
#For string
def show2():
   name = askstring("Input", "Enter your name")
   print(name)
Name  = Label(top, text = "Name:").place(x = 5,y = 120)	
B = Button(top, text ="Click", command = show2)
B.place(x=50,y=120)
top.mainloop()
