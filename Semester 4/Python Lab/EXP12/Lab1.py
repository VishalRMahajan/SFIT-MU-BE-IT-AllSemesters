from tkinter import * 

r = Tk() 

redbutton = Button(r, text = "Red", fg = "red", width=30,  height=5, activebackground="yellow") 
redbutton.pack( side = LEFT) 

greenbutton = Button(r, text = "Black", fg = "black", width=30,  height=5, activeforeground="purple") 
greenbutton.pack( side = RIGHT ) 

bluebutton = Button(r, text = "Blue", fg = "blue", width=30, height=5, bg="pink") 
bluebutton.pack( side = TOP ) 

blackbutton = Button(r, text = "Green", fg = "green", width=30, height=5) 
blackbutton.pack( side = BOTTOM)

r.mainloop()