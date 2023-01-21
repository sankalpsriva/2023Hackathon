from tkinter import * 
from helper import rgbToColor
import random, constants
import numbers


root = Tk() 

root.geometry(constants.screensize)
root.title(constants.title)
root.config(bg = rgbToColor(constants.rgb)) 

button = Button(root)
button.place(anchor=NW, width=10, height=700)



root.mainloop()






